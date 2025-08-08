import firebase_admin
from firebase_admin import credentials, firestore

# Initialisierung mit Schlüssel
cred = credentials.Certificate("übungen.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Funktion zum Speichern beliebig vieler Übungen
def save_exercises(exercise_list):
    for exercise_data in exercise_list:
        db.collection("exercises").add(exercise_data)
        print(f"Übung '{exercise_data['Name']}' wurde gespeichert!")

# Beispiel: Liste mit mehreren Übungen
exercise_list = [
  {
  "Name": "Hampelmänner",
  "Ziele": {
    "Warm-up": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.3,
    "Waden": 0.3,
    "Schultern": 0.2,
    "Autochthone": 0.2
  }
},
{
  "Name": "Knieheben-im-Wechsel",
  "Ziele": {
    "Warm-up": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Hamstrings": 0.2,
    "Gluten": 0.2,
    "Autochthone": 0.2
  }
},
{
  "Name": "Beinkreisen-im-Stehen",
  "Ziele": {
    "Warm-up": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Gluten": 0.3,
    "Hamstrings": 0.3,
    "Quadrizeps": 0.2,
    "Autochthone": 0.2
  }
},
{
  "Name": "Langsame-Bodyweight-Squats",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.2,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.4,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Ausfallschritte",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.2,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Hamstrings": 0.3
  }
},
{
  "Name": "Wall-Sit",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.5,
    "Gluten": 0.3,
    "Waden": 0.2
  }
},
{
  "Name": "Step-ups",
  "Ziele": {
    "Muskelaufbau": 0.5,
    "Abnehmen": 0.3,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "Stufe",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.4,
    "Waden": 0.2
  }
},
{
  "Name": "Side-Steps-mit-Mini-Band",
  "Ziele": {
    "Muskelaufbau": 0.5,
    "Abnehmen": 0.3,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "Mini-Band",
  "Muskeln": {
    "Gluten": 0.5,
    "Quadrizeps": 0.3,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Glute-Bridges-mit-Band",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "Mini-Band",
  "Muskeln": {
    "Gluten": 0.6,
    "Hamstrings": 0.3,
    "Autochthone": 0.1
  }
},
{
  "Name": "Kniebeugen-statisch-halten",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.3,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.5,
    "Gluten": 0.3,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Squat-Jumps",
  "Ziele": {
    "Muskelaufbau": 0.4,
    "Abnehmen": 0.3,
    "Ausdauer": 0.3
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 5,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Waden": 0.3
  }
},
{
  "Name": "Donkey-Kicks",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Gluten": 0.6,
    "Hamstrings": 0.3,
    "Autochthone": 0.1
  }
},
{
  "Name": "Springseil-locker",
  "Ziele": {
    "Muskelaufbau": 0.1,
    "Abnehmen": 0.4,
    "Ausdauer": 0.5
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "Springseil",
  "Muskeln": {
    "Waden": 0.5,
    "Quadrizeps": 0.3,
    "Schultern": 0.2
  }
},
{
  "Name": "Springseil-etwas-schneller",
  "Ziele": {
    "Muskelaufbau": 0.1,
    "Abnehmen": 0.4,
    "Ausdauer": 0.5
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "Springseil",
  "Muskeln": {
    "Waden": 0.5,
    "Quadrizeps": 0.3,
    "Schultern": 0.2
  }
},
{
  "Name": "Tiefe-Hocke",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 2,
  "Equipment": "None",
  "Muskeln": {
    "Gluten": 0.3,
    "Hamstrings": 0.3,
    "Quadrizeps": 0.3,
    "Autochthone": 0.1
  }
},
{
  "Name": "Quadrizeps-Dehnung-links",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 1,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 1.0
  }
},
{
  "Name": "Quadrizeps-Dehnung-rechts",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 1,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 1.0
  }
},
{
  "Name": "Leichte-Skater-Schritte",
  "Ziele": {
    "Warm-up": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 2,
  "Equipment": "None",
  "Muskeln": {
    "Gluten": 0.3,
    "Quadrizeps": 0.3,
    "Hamstrings": 0.2,
    "Autochthone": 0.2
  }
},
{
  "Name": "Arm-und-Beinpendeln",
  "Ziele": {
    "Warm-up": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 1,
  "Equipment": "None",
  "Muskeln": {
    "Schultern": 0.3,
    "Quadrizeps": 0.3,
    "Gluten": 0.2,
    "Autochthone": 0.2
  }
},
{
  "Name": "Kniebeugen-mit-Band",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.2,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "Mini-Band",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.4,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Reverse-Lunges",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.2,
    "Ausdauer": 0.2
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Hamstrings": 0.3
  }
},
{
  "Name": "Wall Sit+Mini-Band-Zug-nach-außen",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "Mini-Band",
  "Muskeln": {
    "Quadrizeps": 0.5,
    "Gluten": 0.3,
    "Waden": 0.2
  }
},
{
  "Name": "Glute-Bridge-March",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Gluten": 0.6,
    "Hamstrings": 0.3,
    "Autochthone": 0.1
  }
},
{
  "Name": "Sumo-Squats-mit-kurzen-Haltepunkten",
  "Ziele": {
    "Muskelaufbau": 0.6,
    "Abnehmen": 0.3,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.4,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Bulgarian-Split Squats",
  "Ziele": {
    "Muskelaufbau": 0.7,
    "Abnehmen": 0.2,
    "Ausdauer": 0.1
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 5,
  "Equipment": "Bank",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.4,
    "Hamstrings": 0.2
  }
},
{
  "Name": "Step-Touch",
  "Ziele": {
    "Muskelaufbau": 0.3,
    "Abnehmen": 0.4,
    "Ausdauer": 0.3
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 3,
  "Equipment": "None",
  "Muskeln": {
    "Waden": 0.3,
    "Quadrizeps": 0.3,
    "Gluten": 0.3,
    "Schultern": 0.1
  }
},
{
  "Name": "Seilspringen (Intervall: 30s springen / 30s Pause)",
  "Ziele": {
    "Muskelaufbau": 0.1,
    "Abnehmen": 0.4,
    "Ausdauer": 0.5
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 4,
  "Equipment": "Springseil",
  "Muskeln": {
    "Waden": 0.5,
    "Quadrizeps": 0.3,
    "Schultern": 0.2
  }
},
{
  "Name": "Fatburner-Circuit: 30s Squat, 30s High Knees, 30s Side Lunges",
  "Ziele": {
    "Muskelaufbau": 0.3,
    "Abnehmen": 0.4,
    "Ausdauer": 0.3
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 5,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Hamstrings": 0.2,
    "Waden": 0.1
  }
},
{
  "Name": "Vorbeuge-im-Stand",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 2,
  "Equipment": "None",
  "Muskeln": {
    "Hamstrings": 0.5,
    "Autochthone": 0.3,
    "Waden": 0.2
  }
},
{
  "Name": "Tiefer-Ausfallschritt-links",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 2,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Hamstrings": 0.3
  }
},
{
  "Name": "Tiefer-Ausfallschritt-rechts",
  "Ziele": {
    "Cool-down": 1.0
  },
  "Ort": "Zuhause",
  "Schwierigkeitsgrad": 2,
  "Equipment": "None",
  "Muskeln": {
    "Quadrizeps": 0.4,
    "Gluten": 0.3,
    "Hamstrings": 0.3
  }
}
]


save_exercises(exercise_list)
