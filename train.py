
from model import EncoderDecoderModel
import torch
import torch.nn as nn
import firebase_admin
from firebase_admin import credentials, firestore
from torch.nn.utils.rnn import pad_sequence
import os
from firebase_admin import credentials
import json







device = torch.device("cuda" if torch.cuda.is_available() else "cpu") # Dafür sorgen, dass alles auf dem gleichen Rechengerät ist.


# Tokenizer (Hat einen ganzen Eintrag dazu.)
class SimpleTokenizer:
    def __init__(self, sätze):
        words = set(" ".join(sätze).split())                                              # " ".join(sätze): setzt alle Wörter in sätze zusammen mit Lehrzeichen dazwischen. split(): Setzt bei jedem Leerzeichen ein Komma. So werden die einzelnen Wörter abgetrennt. set([]) Wandelt die Lieste in eine Menge um. Das bedeutet: Keine doppelten Einträge, Sammlung von allen Wörtern in beispiele.
        self.word2idx = {"<pad>": 0, "<unk>": 1, "<eos>": 2, "<bos>": 3}                                          # Es wird ein Wörterbuch erstellt, um Text in Code zu übersetzen. self speichert word2idx nicht nur in der Klasse, sondern überall. Man kann auch ausserhalb der Klasse darauf zugreifen. <pad> Das sind leerzeichen, welche genutzt werden, um einen Satz mit zu Wenig Zeichen aufzufüllen. Sie werden mit 0 im Wörterbuch gespeichert. <unk> Dies sind unbekannte Wörter, also wörter, die nicht im Wörterbuch enthalten sind. Sie werden mit 1 im Wörterbuch gespeichert.
        for i, word in enumerate(sorted(words), start=4):                                 # Eine Schleife, welche durch jedes Wort im Satz geht. sorted(words): Die Wörter im Wörterbuch werden Alphabetisch sortiert. enumerate(start=2): Jedes Wort bekommt der Reihe nach eine Zahl. dabei startet das ganze bei 2, da 0 & 1 ja schon <pad> & <unk> sind.
            self.word2idx[word] = i                                                       # Das Wort, das gerade bei i ist, wird dem Wörterbuch hunzugefügt.
        self.idx2word = {idx: word for word, idx in self.word2idx.items()}                # Erstellt ein Wörterbuch, welches nicht Wort = Zahl beinhaltet, sondern Zahl = Wort. Damit man zurückübersetzen kann. self.word2idx.items(): Holt alle Paare aus self.word2idx. bsp. Hund: 2. for word, idx in: Nimmt die einzelnen Bestandteile der Paare auseinander. idx: word: Vertauscht die Reihenfolge.

        # Wörter in Zahlen übersetzen
    def encode(self, text):
        return [self.word2idx.get(word, self.word2idx["<unk>"]) for word in text.split()] # text.split(): Setzt zwischen jedes Leerzeichen ein Komma. for word in: Geht durch jedes Wort in text. self.word2idx.get(word, self.word2idx["<unk>"]): Versucht für das Wort die passende Zahl im Wörterbuch herauszusuchen. Wenn nichts gefunden wird, wird <unk> eingesetzt. Das Ganze ist eine Listenkompression, damit der Code kürzer und übersichtlicher bleibt. man könnte es auch so schreiben: tokens = [] for word in text.split(): tokens.append(word2idx.get(word, word2idx["<unk>"])) return tokens   Dies ist allerdings etwas weniger kompakt.
        
        # Zahlen in Wörter übersetzen
    def decode(self, token_ids):
        return " ".join([self.idx2word.get(token, "<unk>") for token in token_ids]) # Hier passiert genau das Selbe, wie beim encode, nur dass nun Zahlen in Wörter übersetzt werden.
        
        # Die grösse des Wörterbuches bekannt geben
    def vocab_size(self):                                                          
        return len(self.word2idx) # len(self.word2idx) Sagt, wie viele Elemente das Wörterbuch hat.
    



     


# Inputs von der firestore Datenbank holen.
cred_json = os.getenv("UEBUNGEN.JSON")
cred_dict = json.loads(cred_json)
cred = credentials.Certificate(cred_dict) # credentials.Certificate: Lädt eine Service Account Datei im JSONFormat, welche Firebase verwendet, um sich zu authentifizieren. "übungen.json": Das ist der Pfad der json Datei (Sie ist im Hauptverzeichniss des Projekts).
firebase_admin.initialize_app(cred)            # Diese Zeile initialisiert mit Hilfe der json Datei ("übungen.json") eine Verbindung zur Firestore Datenbank.
db = firestore.client()                        # Stellt eine Verbindung zur Datenbank her.



def fetch_all_data():                             # Eine Funktion, welche alle Daten aus der Datenbank holen soll.
    all_data = {}                                 # Hier werden die gewonnenen Daten gespeichert.

    for col in db.collections():                  # Eine for schleife, welche durch jede Kolektion in der Datenbank geht.
        col_name = col.id                         # Den Namen der aktuellen Kollektion in col_name abspeichern.
        docs = col.stream()                       # Alle Daten aus der aktuellen Kollektion laden.
        col_entries = {}                          # Leeres Python dictionary erstellen.

        for doc in docs:                          # Eine for Schleife, welche durch alles geht, was in docs steht.
            col_entries[doc.id] = doc.to_dict()   # col_entries[doc.id] Speichert jedes Dokument mit der id des Dokuments. dox.to_dict() Wandelt das Ganze in ein dictionary um.

        all_data[col_name] = col_entries          # Die gewonnenen Daten mit ihrem Namen in all_data speichern.

    return all_data                               # all_data zurückgeben.

daten = fetch_all_data()                          # Die Funktion als daten speichern.

# Aktuell ist das Ganze ein Wörterbuch. Da der Transformer allerdings Listen braucht, wandelt man das Ganze in Sätze um und speichert es in einer Liste.
sätze = []                                                                                              # Hier werden die Sätze gespeichert.
for pair in daten.get("Inputs & Outputs", {}).values():                                                 # Das ist eine for Schleife, welche durch die Kolektion "Inputs & Outputs" geht. daten.get("Inputs & Outputs", {}) Dieser Abschnitt greift auf die Kollektion "Inputs & Outputs" zu, welche mit dieser id in daten gespeichert sind. Fals diese Kollektions-id nicht existiert, wird ein lehres dictionary {} zurückgegeben. .value() Greift auf alle Daten in der Kollektion zu.
    input_data = pair.get("input", {})                                                                  # Holt den input aus der Datenbank und wenn die id "input" nicht existiert, wird ein leeres dictionary zurückgegeben.
    output_data = pair.get("output", {})                                                                # Holt den output aus der Datenbank und wenn die id "output" nicht existiert, wird ein leeres dictionary zurückgegeben.

    input_text = " ".join(f"{key}: {value}" for key, value in input_data.items())                       # Hier wird aus dem input_data dictionary ein Fliestext. for key, value in input_data.items() Gibt alle Schlüssel-Wert paare aus dem dictionary input_data zurück, alsu zum Beispiel {"Ziel": "Muskelaufbau", "Alter": 14} f"{key}: {value}" Wandelt die Paare zu Strings um. " ".join(...) hängt alle paare zusammen und trennt sie mit leerzeichen. beispiel: input_text = "Ziel: Muskelaufbau Alter: 14"
    output_text = " ".join(
        f"{day}: {' '.join(exercises)}"
        for week_data in output_data
        for day, exercises in week_data.items()
)
   # Hier passiert im Grunde das selbe wie bei input_text, mit nur einer kleinen erweiterung. Da in output ein Tag zu mehreren Übungen gehört, muss man noch einen Zusatzschritt machen. Nämlich das: {' '.join(exercises)} Die exercises sehen nämlich ohne diese Zeile so aus: "Liegestützen", "Burpies" mit dieser Zeile sehen sie dann so aus: Liegestützen Burpies.

    sätze.append(input_text)                                                                            # den input_text bei sätze einfügen. 
    sätze.append(output_text)                                                                           # den output_text bei sätze einfügen.


# Liste aller Übungen aus der Datenbank als Fließtext
exercise_infos = []

for übung in daten.get("exercises", {}).values():                                                                                                    # Eine for Schleife, welche durch die Kollektion exercises geht. Genau das selbe Prinzip, wie bei sätze.
    name = übung.get("Name", "")                                                                                                                     # Holt mit dem Schlüssel "name" den namen der aktuellen Übung. Wenn "name" nicht existiert, wird ein leerer String zurückgegeben.                                                              
    muskeln = übung.get("Muskeln", {})                                                                                                   # Hier passiert das selbe, wie bei name nur für die Muskelgruppe. 
    schwierigkeitsgrad = übung.get("Schwierigkeitsgrad")                                            
    equipment = übung.get("Equipment", "")
    trainingsart = übung.get("Ziele", {})                                                                                                  # Bis hier passiert für jeden key das Selbe.

    text = f"{name} Muskeln: {muskeln}, Equipment: {equipment}, Schwierigkeitsgrad: {schwierigkeitsgrad}, Trainingsart: {trainingsart}"   # Einen fliestext mit den gewonnenen daten erstellen.
    exercise_infos.append(text)       
    

                                                                                                       
# Gesamter Übungstext
exercise_text = " Verfügbare Übungen: " + " | ".join(exercise_infos)                                                                                # Nun fügen wir exercise_text in sätze ein, damit man das ganze tokensieren kann.                                                                    # exercise_text so verändern, dass man in sätze anfügen kann.
sätze.append(exercise_text)                                                                                                                         # exercise_text sätze anfügen.


# Nun kann man dem Tokenizer die sätze einspeisen.
tokenizer = SimpleTokenizer(sätze)
    

# Training-Daten erstellen.
train_data_src_ids = []                                                                                # Das bekommt der Encoder als Input.
train_data_tgt_input_ids = []                                                                          # Das bekommt der Decoder als Input.
train_data_tgt_output_ids = []                                                                         # Das ist das Ziel, welches der Transformer erreichen soll. Damti wird der loss berrechnet.

for pair in daten.get("Inputs & Outputs", {}).values():                                                # Hier passiert genau das gleiche, wei bei sätze.
    input_data = pair.get("input", {})                                                                 # Wie bei Sätze.
    output_data = pair.get("output", {})                                                               # Wie bei Sätze.
    
    input_text = " ".join(f"{k}: {v}" for k, v in input_data.items())                                  # Einen input_text erzeugen. Wie bie Sätze.

    full_input_text = exercise_text + input_text                                           # Den input_text mit exercise_text addieren. Das ist der Text, den der Transformer dann eingespeisst bekommt.
    
    # Ausgabe (Trainingsplan)
    output_text = ""
    for i, week_dict in enumerate(output_data):
        days_text = " ".join(
            f"{day}: {' '.join(exercises)}"
            for day, exercises in week_dict.items()
        )
        output_text += f"Woche {i+1}: {days_text}"

                                                                                                         # Hier wird ein output erstellt, also das, was der Transformer erstellen soll. Wie bei Sätze.

    # Tokenisieren
    src_ids = tokenizer.encode(full_input_text)
    src_ids.append(tokenizer.word2idx["<eos>"])                        # Den full_input_text tokensieren, also in Zahlen übersetzen, damit die KI amit arbeiten kann.
    tgt_ids = tokenizer.encode(output_text)                                                            # Den output_text tokensieren, also in Zahlen übersetzen, damit die KI amit arbeiten kann.

    # Shifted target
    tgt_input_ids = [tokenizer.word2idx["<bos>"]] + tgt_ids[:-1]                                       # Hier nimmt man tgt_ids und nimmt jedes Token, ausser das Letzte das ist nämlich das <eos> (end of sequense) Token. dann setzt man mit tokenizer.bos_token_id das <bos> (begin of sequens), welches den Anfang des Textes signalisiert.
    tgt_output_ids = tgt_ids                                                                           # tgt_ids als tgt_output_ids speichern. 

    # In die verschiedenen Trainingsdaten einfügen.
    train_data_src_ids.append(src_ids)                                                                 
    train_data_tgt_input_ids.append(tgt_input_ids)
    train_data_tgt_output_ids.append(tgt_output_ids)


src_tensor = pad_sequence([torch.tensor(x, dtype=torch.long) for x in train_data_src_ids], batch_first=True, padding_value=tokenizer.word2idx["<pad>"])               # [torch.tensor(x, dtype=torch.long) for x in train_data_src_ids]: Wandelt jede Eingabesequenz in einen tensor um. Bsp: [[1,5,3], [8, 3]] => [tensor([1, 5, 3]), tensor([8, 3])]  pad_sequence(..., batch_first=True, padding_value=tokenizer.word2idx["<pad>"]): pad_sequence Füllt alle Sequenzen mit dem <pad> Token so auf, dass sie gleich lang sind. batch_first = True: Der Batch steht zuerst. Nicht die sequenz. Ergebniss: (batch, sequence). padding_value = ... Gibt an, dass mit dem <pad> Token aufgefüllt werden soll.
tgt_input_tensor = pad_sequence([torch.tensor(x, dtype=torch.long) for x in train_data_tgt_input_ids], batch_first=True, padding_value=tokenizer.word2idx["<pad>"])   # Hier passiert das selbe.
tgt_output_tensor = pad_sequence([torch.tensor(x, dtype=torch.long) for x in train_data_tgt_output_ids], batch_first=True, padding_value=tokenizer.word2idx["<pad>"]) # Hier auch.

# Mit device (Ist ganz oben definiert) alles auf das selbe Rechengerät leiten.
src_tensor = src_tensor.to(device)                           
tgt_input_tensor = tgt_input_tensor.to(device)
tgt_output_tensor = tgt_output_tensor.to(device)

vocab_size = tokenizer.vocab_size()                                       # Mit der Funktion vocab_size() herausfinden, wie viele Wörter im Vokabular sind.
embed_dim = 128                                                           # Wie viele Dimensionen ein Vektor hat.
max_len = 10000                                                             # Wie viele Tokens maximal eingebetted werden.
num_layers = 2                                                            # Wie viele EncoderDecoderModel Blöcke verwendet werden.
model = EncoderDecoderModel(vocab_size, embed_dim, max_len, num_layers)   # Das definierte Transformer-Modell holen.
model.to(device)

optimizer = torch.optim.Adam(model.parameters(), lr=0.001)    # Es wird der optimizer Adam gewählt, welcher sagt, wie Parameter angepasst werden. model.parameters(): holt alle veränderbaren parameter aus dem modell. lr = 0.01: Das ist die Learning-rate, also wie stark das Modell Were verändert. So kann das Modell schneller "lernen". Wenn dieser Wert allerdings zu hoch ist, werden die Daten zu stark verändert, was die Genauigkeit verschlechtert.
criterion = nn.CrossEntropyLoss()                             # Das ist der loss, welcher berrechnet, wie weit werg die KI vom eigentlichen Ziel entfernt war. Dieser Wert sollte immer kleiner werden, da sich die KI immer verbessert.                 

# Training
if __name__ == "__main__":
    epochs = 400                                              # Das sind die Training-epochen, welche das Modell durchläuft. Das Modell wird mit jeder Epoche etwas besser.
    for epoch in range(epochs):                               # Das ist eine For Schleife, welche sagt, was in jeder Epoche passiert.
        model.train()                                         # Hier sagt man, dass das Modell trainiert werden soll. Das ist quasi der Trainingsmodus. Es würde auch ohne gehen, aber man braucht es zum Beispiel für Dropouts etc.
        optimizer.zero_grad()                                 # Die gespeicherten Gradienten der letzten Epoche löschen, damit sich diese nicht aufsummieren. Gradienten sagen dem optimizer (in dem Fall Adam) wo der Loss war & wie stark er war. Wenn man diese nicht löscht, werden dies automatisch aufsummiert und dann wäre das gesammte Training für die Katz.
        logits = model(src_tensor, tgt_input_tensor)          # Die vorbereiteten inputs in das Modell geben.   
        logits = logits.view(-1, logits.size(-1))             # (B*T, V) Multipliziert die batch-size mit sequence-length.
        targets = tgt_output_tensor.view(-1)                  # (B*T) hier passiert das selbe. Braucht man, um den loss beerrechnen zu können.
        loss = criterion(logits, targets)                     # Der Loss ist die Differenz zwischen dem Ergebniss und dem Ziel.

        loss.backward()                                       # Der loss wird rückwärts durchs Modell berrechnet.     
        optimizer.step()                                      # Der optimizer (Adam) verändert die Werte aufgrund der Gradienten (Den Loss Informationen).
        print(f'Epoche: {epoch + 1} Loss: {loss.item():.5f}') # Jede Epoche anzeigen mit dem dazugehörigen loss, welcher auf 4 Stellen hinter dem Komma gerundet wird.

    torch.save({
        'epoch': epoch + 1,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        },"checkpoint.pt")