import firebase_admin
from firebase_admin import credentials, firestore

# Initialisierung mit deinem Service-Account
cred = credentials.Certificate("übungen.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

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

# Testausgabe
daten = fetch_all_data()

muskeln = ['Gluten', 'Trapez-Muskel', 'Brust', 'Six-pack', 'Latissimus', 'Hamstrings', 'Unterarme', 'Autochthone', 'Seitliche-Bauchmuskeln', 'Quadrizeps']

übungen = daten.get("exercises", {}).values()
filtered_übungen = []

for übung in übungen:
    trainingsart = übung.get("Trainingsart")
    übung_muskeln_str = übung.get("Muskeln")
    übung_muskeln = {muskel.strip() for muskel in übung_muskeln_str.split(",")}

    if 'Cool-down' in trainingsart:
        if not übung_muskeln.isdisjoint(muskeln):
            filtered_übungen.append(übung)

filtered_übungen.sort(key=lambda ü: ü.get("Name", ""))
länge = len(filtered_übungen)

for übung in filtered_übungen:
    print(übung)
print(f"Insgesammt sind es {länge} Übungen.")





























