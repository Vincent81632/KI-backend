import torch
import torch.nn as nn
import torch.nn.functional as F



# Self-Attention
class SelfAttention(nn.Module): # Neue Klasse definieren, welche von nn.Module erbt.

    # Funktion, welche sagt, was bei einer Eingabe passiert.
    def __init__(self, embed_dim):

         # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        super().__init__()

        # Nun werden Q, K & V erstellt. Die inputs haben eine Dimension von embed_dim (4).
        self.query = nn.Linear(embed_dim, embed_dim)
        self.key   = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

    # Nun wird wie Funktion geschrieben mit den oben definierten Q, K & V. forward(): Wenn man das Modell auf Daten anwendet, wird diese Funktion automatisch aufgerufen.
    def forward(self, x):
        B, T, C = x.size() # B: Das ist die Batch-size. Also wie viele Sätze in einem Batch sind. T: Wei viele Wörter ein Satz hat. C: Wie viele Dimensionen ein Wort hat.
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        scores = torch.matmul(Q, K.transpose(-2, -1)) / (C ** 0.5) # Alles, was zwischen den hellgrünen Kästen und dem Orangen Kasten passiert.
        weights = F.softmax(scores, dim=-1)                        # Softmax (Violetter Kasten)                                         
        attended = torch.matmul(weights, V)                        # Softmax x V (türkieser Kasten) 

        # Ergebniss ausgeben.
        return attended

# Feed Forward (hat einen ganzen Eintrag dazu.)
class FeedForward(nn.Module):                           # Neue Klasse definieren, welche von nn.Module erbt.
    def __init__(self, embed_dim):                      # Sagt, wie das Modell aufgebaut ist.
        super().__init__()                              # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.fc1 = nn.Linear(embed_dim, embed_dim * 2)  # W1 & d1 (Grafik in Feed Forward) W1 hat so viele Vektore, wie der eingabe-Vektor lang ist. Jeder dieser Vektore ist doppelt so lange, wie der eingabe-Vektor.
        self.fc2 = nn.Linear(embed_dim * 2, embed_dim)  # W2 & d2 (Grafik in Feed Forward) W2 hat doppelt so viele Vektore, wie der eingabe-Vektor lang ist. Jeder dieser Vektore ist so lange, wie der eingabe-Vektor.

    def forward(self, x):                               # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        return self.fc2(F.relu(self.fc1(x)))            # Zuerst wird x mal W1 plus b1 gerrechnet. Danach werden alle Negativen Werte mit relu auf null gesetzt. Am Ende werden diese Werte mit W2 multipliziert und b2 wird dazu Addiert. Das ganze ist sehr kompakt geschrieben. Man könnte es etwas einfacher, dafür länger schreiben: def forward(self, x): x = self.fc1(x) x = F.relu(x) x = self.fc2(x) return x   Das ist etwas mehr Code, dafür etwas verständlicher.

# Ein übergeordneter Encoder-Block (kann mehrfach gestackt werden)
class EncoderBlock(nn.Module):
    def __init__(self, embed_dim):                      # Sagt, wie das Modell aufgebaut ist.
        super().__init__()                              # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.attn = SelfAttention(embed_dim)            # Die Self-Attention holen.
        self.ffn = FeedForward(embed_dim)               # Das Feed Forward Netzwerk holen.
        self.norm1 = nn.LayerNorm(embed_dim)            # Add & Norm 1 holen.
        self.norm2 = nn.LayerNorm(embed_dim)            # Add & Norm 2 holen.

    def forward(self, x):                               # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        x = self.norm1(x + self.attn(x))                # self.attn(x): x Wird durch die self-Attention geschickt. x + self.attn(x): Verhindert, dass informationen unterwegs verloren geht, oder das Netz schwer traininerbar wird. slf.norm1(): Das Ergebniss wird nach dem Add & Norm Prinzip verändert.        
        x = self.norm2(x + self.ffn(x))                 # self.ffn(x): x wird durch Feed Forward geschickt. x + self.ffn(x): Verhindert, dass informationen unterwegs verloren geht, oder das Netz schwer traininerbar wird. slf.norm2(): Das Ergebniss wird nach dem Add & Norm Prinzip verändert.
        return x                                        # Ergebniss zurückgeben.

# Der komplette Encoder (mit mehreren Blocks + Embeddings)
class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, embed_dim, max_len, num_layers=2):                     # Sagt, wie das Modell aufgebaut ist. vocab_size: Wie viele Wörter der Transformer aktuell kennt. embed_dim: Wie viele Dimensionen ein Vektor hat. max_len: Wie lange alle Sätze sind. num_Layers = 2: Wie viele Encoderblöcke eingebaut werden.
        super().__init__()                                                                # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.embedding = nn.Embedding(vocab_size, embed_dim)                              # Für jedes Wort einen Vektor mit der Dimension embed_dim.
        self.pos_embedding = nn.Embedding(max_len, embed_dim)                             # Positional embedding: torch.randn(1, max_len, embed_dim) Erstellt Positionsinformationen für einen Satz mit max_len Vektoren und einer Vektoren-Dimension von embed_dim. nn.Parameter: Sagt, dass diese informations-Parameter beim Training von der KI angepasst werden können.
        self.blocks = nn.ModuleList([EncoderBlock(embed_dim) for _ in range(num_layers)]) # EncoderBlock(embed_dim): Das ist der zuvor definierte Encoderblock. for _ in range(num_layers): Führt das ganze so viel mal aus, wie num_layers gross ist. nn.ModuleList: Das ist der Ort, wo die Encoderblöcke gespeichert werden. Das Ganze ist wieder eine List Comprehension. Ohne sie würde es so aussehen: self.blocks = nn.ModuleList()  for i in range(num_layers):  block = EncoderBlock(embed_dim)  self.blocks.append(block)

    def forward(self, x):                                                                 # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        tok_emb = self.embedding(x)  # Shape: [batch_size, seq_len, embed_dim]

        positions = torch.arange(x.size(1), device=x.device).unsqueeze(0)  # Shape: [1, seq_len]
        pos_emb = self.pos_embedding(positions)                                           # pos_embedding einbinden. :, Alle Batches also Sätze das ist genau einer. x.size(1): Wie Viele Wörter in einem Satz sind. : Alle dimensionen nehmen.         
        x = tok_emb + pos_emb                                                             # Jetzt werden die Positionsinformationen zum Vektorisierten Satz Addiert. Ein Satz mit Positionsiformationen entsteht.
        for block in self.blocks:                                                         # Durch jeden block in self.blocks gehen. 
            x = block(x)                                                                  # Nun wird x durch jeden block in self.blocks gegeben, also jeden Encoderblock.
        return x                                                                          # Ergebniss ausgeben (wird später in den Decoder eingespeist)     



# masked Self-Attention (Hat einen ganzen Eintrag zu normaler Self-Attention und dem, was bei masked Self-Attention dazukommt.)
class MaskedSelfAttention(nn.Module):                      # Neue Klasse definieren, welche von nn.Module erbt.
    def __init__(self, embed_dim):                   # Sagt, wie das Modell aufgebaut ist.   
        super().__init__()                           # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        # Nun werden Q, K & V erstellt.
        self.query = nn.Linear(embed_dim, embed_dim)
        self.key   = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

    # Nun wird wie Funktion geschrieben mit den oben definierten Q, K & V. forward(): Wenn man das Modell auf Daten anwendet, wird diese Funktion automatisch aufgerufen.
    def forward(self, x):
        B, T, C = x.size()  # B: Das ist die Batch-size. Also wie viele Sätze in einem Batch sind. T: Wei viele Wörter ein Satz hat. C: Wie viele Dimensionen ein Wort hat.
        Q = self.query(x)
        K = self.key(x)
        V = self.value(x)

        # Alles, was zwischen den hellgrünen Kästen und dem Orangen Kasten passiert. 
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (C ** 0.5)
        # Eine Maske erstellen mit der Matrix (T, T). Wenn der Satz also zum Beispiel 5 Wörter hat, hat die Matrix 5 Vektore mit je 5 Dimensionen. Jede Zahl davon ist 1.
        mask = torch.triu(torch.ones(T, T), diagonal=1).bool().to(x.device) # torch.ones(T, T) Erstellt eine Matrix nur mit einsen. torch.triu(diagonal = 1) Erstellt eine Dreiecksmatrix, Das bedeutet, dass die gesammte Matrix in der Mitte geteilt wird. diagonal = 1 das bedeutet, dass oberhalb der Trennung nur einsen sind und unterhalb der Trennung nur nullen. Das ganze kann man in der Grafik zu Masked self-Attention sehen. .bool() wandelt jede eins in True um und alles andere in False. .to(x.device): Sorgt dafür, dass mask und x auf dem selben Rechengerät ist, also CPU oder GPU. Wenn diese Dinge nicht am selben Ort sind, bekommt man einen Fehler.
        scores = scores.masked_fill(mask, float("-inf"))                    # Die bissherigen scores werden nun mit der maske bedekt. Das heisst: bei jeder Stelle in mask wo True steht, wird in scores -inf eingesetz. 
        # Softmax (Violetter Kasten)
        weights = F.softmax(scores, dim=-1) 
        # Softmax x V (türkieser Kasten) 
        attended = torch.matmul(weights, V)  

        # Ergebniss ausgeben.   
        return attended
    

# Cross-Attention Das ist die self-Attention, wo die Daten vom Encoder und die des Decoders zusammenkommen.
class CrossAttention(nn.Module):
    def __init__(self, embed_dim):
        super().__init__()
        # W_q, W_k & W_v erstellen.
        self.query = nn.Linear(embed_dim, embed_dim)
        self.key   = nn.Linear(embed_dim, embed_dim)
        self.value = nn.Linear(embed_dim, embed_dim)

    # Nun werden die vorhin definierten Gewichtsmatrixen mit dem Anfangswert multipliziert. Und hier kommt auch der Unterschied zwischen Cross-Attention und Self-Attention. Wärend bei der Self-Attention alle Gewichtsmatrixen mit x multipliziert werden, wird bei der Cross-Atteniton nur W_q mit x multipliziert. Die anderen beiden mit context. Der context ist der Output des Encoders. So bekommt der Decoder die Informationen, welche der Encoder gesammelt hat.
    def forward(self, x, context):
        Q = self.query(x)
        K = self.key(context)
        V = self.value(context)
        
        # Alles, was zwischen den hellgrünen Kästen und dem Orangen Kasten passiert. 
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (Q.size(-1) ** 0.5)

        # Softmax (Violetter Kasten)
        weights = F.softmax(scores, dim=-1)

        # Softmax x V (türkieser Kasten)
        attended = torch.matmul(weights, V)

        # Ergebniss ausgeben.
        return attended
 

# Übergeordneter Decoder Block.
class DecoderBlock(nn.Module):                                 # Neue Klasse definieren, welche von nn.Module erbt.
    def __init__(self, embed_dim):                             # Sagt, wie das Modell aufgebaut ist.
        super().__init__()                                     # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.self_attn = MaskedSelfAttention(embed_dim)        # masked self-attention holen.
        self.cross_attn = CrossAttention(embed_dim)            # cross-attention holen.
        self.ffn = FeedForward(embed_dim)                      # Feed Forward holen.
        self.norm1 = nn.LayerNorm(embed_dim)                   # Add & Norm 1 holen.
        self.norm2 = nn.LayerNorm(embed_dim)                   # Add & Norm 2 holen.
        self.norm3 = nn.LayerNorm(embed_dim)                   # Add & Norm 3 holen.

    def forward(self, x, encoder_output):                      # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        x = self.norm1(x + self.self_attn(x))                  # masked self-attention auf x anwenden und anschliesend Add & Norm 1 anwenden.
        x = self.norm2(x + self.cross_attn(x, encoder_output)) # cross-attention auf x & den encoder_output anwenden und anschliesend Add & Norm 2 anwenden.
        x = self.norm3(x + self.ffn(x))                        # feed-forward auf x anwenden und anschliessend Add & Norm 3 anwenden.
        return x                                               # Ergebniss ausgeben.


# Das gesammte Decoder Modell.
class TransformerDecoder(nn.Module):                                                        # Neue Klasse definieren, welche von nn.Module erbt.
    def __init__(self, vocab_size, embed_dim, max_len, num_layers=2):                       # Sagt, wie das Modell aufgebaut ist.
        super().__init__()                                                                  # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.embedding = nn.Embedding(vocab_size, embed_dim)                                # Embedding erstellen.
        self.pos_embedding = nn.Embedding(max_len, embed_dim)               # Positional embedding: torch.randn(1, max_len, embed_dim) Erstellt Positionsinformationen für einen Satz mit max_len Vektoren und einer Vektoren-Dimension von embed_dim. nn.Parameter: Sagt, dass diese informations-Parameter beim Training von der KI angepasst werden können.
        self.blocks = nn.ModuleList([DecoderBlock(embed_dim) for _ in range(num_layers)])   # DecoderBlock(embed_dim): Das ist der zuvor definierte Decoderblock. for _ in range(num_layers): Führt das ganze so viel mal aus, wie num_layers gross ist. nn.ModuleList: Das ist der Ort, wo die Decoderblöcke gespeichert werden. Das Ganze ist wieder eine List Comprehension. Ohne sie würde es so aussehen: self.blocks = nn.ModuleList()  for i in range(num_layers):  block = DecoderBlock(embed_dim)  self.blocks.append(block)
        self.fc_out = nn.Linear(embed_dim, vocab_size)                                      # Berrechnet, welches das nächst warscheinlichste Wort ist. embed_dim: grösse eines Vektores. vocab_size: Ist im Tokenizer definiert. Das ist die Grösse der bekannten wörter.                     

    def forward(self, x, encoder_output):                                                   # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        tok_emb = self.embedding(x) 
        positions = torch.arange(x.size(1), device=x.device).unsqueeze(0)                   # Embedding auf x anwenden und in tok_emb speichern.
        pos_emb = self.pos_embedding(positions)                                             # pos_embedding einbinden. :, Alle Batches also Sätze das ist genau einer. x.size(1): Wie Viele Wörter in einem Satz sind. : Alle dimensionen nehmen.         
        x = tok_emb + pos_emb                                                               # Die Positionsinformationen auf die Tokens addieren.
        for block in self.blocks:                                                           # Eine for Schleife, welche durch jeden block in self.blocks geht.
            x = block(x, encoder_output)                                                    # x & den encoder_output in den Decoderblock einspeisen und anschliessend in x speichern.
        logits = self.fc_out(x)                                                             # Auf x self.fx_out(x) anwenden und anschliessend in logits speichern.
        return logits                                                                       # Ergebniss ausgeben.
    

# Das gesammte Modell mit dem Encoder und dem Decoder.
class EncoderDecoderModel(nn.Module):                                                 # Neue Klasse definieren, welche von nn.Module erbt.
    def __init__(self, vocab_size, embed_dim=128, max_len=100, num_layers=2):         # Sagt, wie das Modell aufgebaut ist. embed_dim = 128: wie viele Dimension ein Token hat. max_len = 100: Wie lange jede Sequenz(Satz) sein soll. num_layers: wie viele Blöcke das Modell hat.
        super().__init__()                                                            # Wichtig, um die Elternklasse (nn.Module) richtig zu laden.
        self.encoder = TransformerEncoder(vocab_size, embed_dim, max_len, num_layers) # Den Encoder holen.
        self.decoder = TransformerDecoder(vocab_size, embed_dim, max_len, num_layers) # Den Decoder holen.

    def forward(self, src, tgt):                                                      # Funktion die sagt, was passiert, wenn das Modell angewendet wird.
        encoder_output = self.encoder(src)             # src = Nutzerprofil (Das ist der Input).
        logits = self.decoder(tgt, encoder_output)     # tgt = Bisher generierter Trainingsplan.
        return logits                                  # Finales Ergebniss ausgeben.