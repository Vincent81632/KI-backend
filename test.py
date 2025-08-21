from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import torch
from train import vocab_size
from train import exercise_text
from train import tokenizer
from pydantic import BaseModel
import torch.nn.functional as F
from model import EncoderDecoderModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8081"],  # Für Entwicklung okay
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TrainingsInput(BaseModel):
    ziel: str
    ort: str
    muskeln: str
    schwierigkeitsgrad: int
    zeit: int
    häufigkeit: int
    equipment: str




model = EncoderDecoderModel(vocab_size, embed_dim=128, max_len=10000, num_layers=2)  # gleiche Parameter wie beim Training
checkpoint = torch.load("checkpoint.pt")

model.load_state_dict(checkpoint["model_state_dict"])

# testen
def sample_next_token(logits, temperature=1.0):
    """Samplet den nächsten Token mit Temperatur."""
    logits = logits / temperature                                                       # Die logits durch temperature teilen.
    probabilities = F.softmax(logits, dim=-1)                                           # Softmax am Ergebniss anwenden. dim=-1: Softmax wird auf die letzte Dimension angewendet. Das ist vocab_size. Softmax berrechnet für jedes Wort darin eine Warscheinlichkeit.
    return torch.multinomial(probabilities, num_samples=1).item()                       # multinomial wält ein Wört zufällig basierend auf der dazugehörigen Warscheinlichkeit. probabilities sind die Ergebnisse. item() holt aus dem Ergebniss den Index heraus. Ist das Ergebnis z. B. tensor([2]) nimmt item() 2 daraus.

# Antwort generieren.
def generate_response(model, tokenizer, input_dict, max_len=1000, temperature=1.0):       # model: Das ist das Transformer Modell. tokenizer: Der Tokenizer. input_dict: Der Input fürs Modell. max_len=50 wie lange die Antwort maximal sein darf. temperature: Wie vorsichtig das modell die Wörter wählt. ist dieser Wert unter 1, so ist das Modell eher vorsichtig Darüber passiert genau das Gegenteil.
    model.eval()                                                                        # Versetzt das Modell in den Test-Modus.
    device = next(model.parameters()).device                                            # Herausfinden, auf welchem Rechengerät das modell aktuell ist.model.parameters() Holt alle Parameter im Modell. Next: Nimmt das erste Parameter. .device: schaut, auf welchem Rechengerät das Parameter gerade ist.

    # Eingabe vorbereiten
    input_text = " ".join(f"{k}: {v}" for k, v in input_dict.items())                   # Das selbe Prinzip wie in Sätze.
    full_input = input_text + exercise_text                                             # Addiert die Übungen auf den input_text.
    src_ids = tokenizer.encode(full_input) + [tokenizer.word2idx["<eos>"]]              # tokenizer.encode(full_input) tokensiert full_input. Hängt am Ende ein <eos> Token an.
    src_tensor = torch.tensor([src_ids], dtype=torch.long).to(device)                   # Wandelt das Ganze in einen Tensor um und gibt es auf das aktuelle Rechengerät.

    # Start des Decoders mit <bos>
    tgt_input = [tokenizer.word2idx["<bos>"]]                                           # Das ist der Decoder Input. Er ist nur ein <bos> Token, damit das Modell weiss, dass es anfangen soll, zu schreiben.

    for _ in range(max_len):                                                            # Eine for Schleife, welche so lange läuft, wie max_len gross ist.
        tgt_tensor = torch.tensor([tgt_input], dtype=torch.long).to(device)             # Macht das selbe wei bei src_tensor mit tgt_input.
        with torch.no_grad():                                                           # Das ist der Trainingsmodus. Es werden keine Gradienten berrechnet und ein loss auch nicht. Das spart Rechenleistung.
            logits = model(src_tensor, tgt_tensor)                                      # Das nächste Wort mit dem modell generieren.
        
        next_token_logits = logits[0, -1]                                               # Letztes Token des Outputs nehmen. [0, -1] 0: nimmte die erste Sequenz des batches. -1 Nimmt den Token der Sequenz.
        next_token_id = sample_next_token(next_token_logits, temperature=temperature)   # Mit sample_next_token das nächste Token herausfinen.

        if next_token_id == tokenizer.word2idx["<eos>"]:                                # Wenn das nächste Token ein eos Token ist, wird die Schleife beendet. 
            break

        tgt_input.append(next_token_id)                                                 # Dem tgt_input das nächste Token einfspeien.

    decoded_output = tokenizer.decode(tgt_input[1:])                                    # Die Ausgegebenen Tokens wieder in normale Wörter übersetzen. [1:] Das ist der ganze Satz, ohne den ersten Token. Das ist nämlich <bos>.
    return decoded_output                                                               # Ergebniss ausgeben.

# Das ist der Input, welcher das Modell bekommt.


# Trainingsplan generieren.
@app.post("/generate_plan")
def generate_plan(input: TrainingsInput):
    input_dict = input.dict()
    antwort = generate_response(model, tokenizer, input_dict, max_len=10000, temperature=0.8)
    return {"trainingsplan": antwort}

