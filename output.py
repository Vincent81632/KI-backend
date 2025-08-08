import firebase_admin
from firebase_admin import credentials, firestore
from input import inputs


outputs = []

output = []
week = {
    "Montag": [    # Warm-up (ca. 5–7 Minuten)
    "1x 30 sec Hampelmänner",
    "1x 20 sec Knieheben-im-Wechsel",
    "1x 30 sec Beinkreisen-im-Stehen",

    # Hauptteil (ca. 52 Minuten)
    "4x 15 langsame-Bodyweight-Squats",
    "3x 15 Ausfallschritte",
    "3x 30 sec Wall-Sit",
    "3x 15 Step-ups",
    "3x 20 Side-Steps-mit-Mini-Band",
    "3x 12 Glute-Bridges-mit-Band",
    "3x 20 sec Kniebeugen-statisch-halten",
    "3x 10 Squat-Jumps",
    "3x 12 Donkey-Kicks",
    "1x 3 min Springseil-locker",
    "1x 3 min Springseil-etwas-schneller",

    # Cool-down (ca. 5 Minuten)
    "30 sec tiefe-Hocke",
    "30 sec Quadrizeps-Dehnung-links",
    "30 sec Quadrizeps-Dehnung-rechts"
    ]
}
output.append(week)

week = {
    "Montag": [    # Warm-up
    "1x 30 sec Hampelmänner",
    "1x 30 sec leichte Skater-Schritte",
    "1x 20 sec Arm- und Beinpendeln",

    # Hauptteil
    "4x 20 Kniebeugen mit Band",
    "4x 12 Reverse Lunges",
    "3x 20 sec Wall Sit + Mini-Band-Zug-nach-außen",
    "3x 15 Glute-Bridge March",
    "3x 12 Sumo Squats mit kurzen Haltepunkten",
    "3x 15 Bulgarian Split Squats",
    "3x 1 min Step Touch + Mini-Jump",
    "1x 4 min Seilspringen",
    "2x 3 min Fatburner-Circuit: 30s Squat, 30s High Knees, 30s Side Lunges",

    # Cool-down
    "30 sec Vorbeuge-im-Stand",
    "30 sec tiefer-Ausfallschritt-links",
    "30 sec tiefer-Ausfallschritt-rechts"
    ]
}
output.append(week)

week = {
    "Montag": [    # Warm-up
    "1x 30 sec Knee Pulls",
    "1x 30 sec Hampelmann-Variationen",
    "1x 20 sec Beckenheben-auf-Boden",

    # Hauptteil
    "4x 12 Jump Squats",
    "3x 15 Step-ups+Knee-Drive",
    "3x 12 Sumo Puls Squats-mit-Mini-Band",
    "3x 30 sec Isometrischer-Ausfallschritt",
    "3x 12 Glute-Bridges-mit-Gewicht",
    "3x 20 Walking-Lunges",
    "3x 30 sec Side-Squats+Toe-Tap",
    "1x 5 min Springseil-mit-Richtungswechsel",
    "2x 1 min High-Knees",

    # Cool-down
    "30 sec tiefe-Hocke-mit-Hüftöffner",
    "30 sec Quadrizeps-Dehnung-im-Liegen-links",
    "30 sec Quadrizeps-Dehnung-im-Liegen-rechts"
    ]
}
output.append(week)

week = {
    "Montag": [ # Warm-up
    "1x 30 sec Arm-und-Beinpendeln",
    "1x 20 sec Knieheben-mit-Armeinsatz",
    "1x 30 sec lockeres-auf-der-Stelle-Joggen",

    # Hauptteil
    "4x 15 Bodyweight-Squats-mit 3-sec-Haltepunkt",
    "3x 15 Ausfallschritte-nach-hinten+Armlift",
    "3x 12 Sumo-Squats-mit-Mini-Band",
    "3x 20 sec Wall-Sit+Mini-Bewegungen",
    "3x 12 Donkey-Kicks-mit Mini-Band",
    "3x 15 Step-ups+Schulterkreisen",
    "3x 20 Side-Walks-mit-Mini-Band",
    "1x 4 min Springseil-45s-on-15s-off",
    "1x 30 sec High-Knees",
    "1x 30 sec Squat-Kicks",

    # Cool-down
    "30 sec tiefer Ausfallschritt-links",
    "30 sec tiefer Ausfallschritt-rechts",
    "30 sec tiefe-Hocke-mit-Hüftmobilisation"
    ]
}
output.append(week)

week = {
    "Montag": [
         # Warm-up
    "1x 30 sec Hampelmänner",
    "1x 30 sec Hight-Knees",
    "1x 20 sec Squat-to-Stand-Dehnung",

    # Hauptteil
    "4x 20 Mini-Band-Kniebeugen",
    "3x 15 Walking Lunges",
    "3x 30 sec Sumo-Hold-mit-Mini-Band+Pulses",
    "3x 20 sec Wall-Sit+Mini-Band-Zug-außen",
    "3x 12 Glute-Bridges-mit-Band+Armhub",
    "3x 15 Step-ups-mit-Knee-Raise",
    "3x 20 sec Duck-Walk",
    "1x 4 min Seilspringen",
    "1x 45 sec Sqauts",
    "1x 45 sec Hampelmänner",
    "1x 45 sec Mountain-Climbers",
    "1x 45 sec High-Knees",
    "1x 45 sec Sqauts",
    "1x 45 sec Hampelmänner",
    "1x 45 sec Mountain-Climbers",
    "1x 45 sec High-Knees",

    # Cool-down
    "30 sec Beinpendeln",
    "30 sec Quadrizeps-Stretch-stehend-links",
    "30 sec Quadrizeps-Stretch-stehend-rechts"
    ]
}
output.append(week)

week = {
    "Montag": [
         # Warm-up
    "1x 30 sec Seilspringen-leicht",
    "1x 20 sec Arm-und-Beinkreisen",
    "1x 30 sec Mini-Squats-mit-Armhub",

    # Hauptteil
    "4x 15 Kniebeugen-mit-tiefem-Haltepunkt",
    "3x 12 Bulgarian-Split-Squats",
    "3x 30 sec Sumo-Puls-Squats-mit-Band",
    "3x 12 Glute-Bridges-einbeinig",
    "3x 15 Step-ups-mit-Tempo",
    "3x 20 Side-Steps-mit-Mini-Band",
    "1x 5 min Intervall-Seilspringen-30s-schnell-30s-Pause)",
    "2x 3 min Drill-Rotation: Lunges–Jump-Squats–Shadow-Boxing–High-Knees",

    # Cool-down
    "30 sec tiefe-Hocke-mit-Dehnung",
    "30 sec Quadrizeps-Stretch-im-Liegen-links",
    "30 sec Quadrizeps-Stretch-im-Liegen-rechts"
    ]
}
output.append(week)
outputs.append(output)

output = []

week = {
    "Montag": [
    # Warm-up
    "1x 30 sec Hampelmänner",
    "1x 20 sec Beinpendel-seitlich",
    "1x 20 sec Schulterkreisen+Armkreisen",

    # Hauptteil (Intervallzirkel, 3 Runden)
    "3x 30 sec Mountain-Climber",
    "3x 30 sec Jump-Squats",
    "3x 30 sec Glute-Bridge-Marches",
    "3x 30 sec Kettlebell-Swings",
    "3x 30 sec Superman-Heben-mit-Halten",
    "3x 30 sec High-Knees",
    "3x 30 sec Rückenstrecker-diagonal",
    "3x 30 sec Hollow-Hold",

    # Cool-down
    "30 sec tiefe-Hocke-und-Vorbeugen",
    "30 sec Rückenrolle-mit-Atemfokus",
    "30 sec Pigeon-Stretch"
    ],

    "Donnerstag": [
            # Warm-up
    "1x 30 sec Armkreisen-und-Schulterkreisen",
    "1x 20 sec lockere-Seilsprünge-oder-Hüpfen",
    "1x 30 sec diagonales-Knieheben-mit-Armzug",

    # Hauptteil (4 Runden je 6 Übungen, 30s Belastung, 15s Pause)
    "4x 30 sec Liegestütz-Variante",
    "4x 30 sec Trizeps-Dips",
    "4x 30 sec Seilspringen",
    "4x 30 sec Ruderzug-mit-Handtuch",
    "4x 30 sec Bicycle-Crunches",
    "4x 30 sec Wadenheben-schnell",

    # Cool-down
    "30 sec Armstreckung-über-Kopf",
    "30 sec Brustdehnung-an-der-Wand",
    "30 sec Lat-Stretch-in-der-Tür"
    ]
}
output.append(week)

week = {
    "Montag": [
          # Warm-up
    "1x 30 sec Hampelmänner-mit-Armzug",
    "1x 30 sec Skater-Schritte",
    "1x 20 sec Kniebeugen-mit-Armkreisen",

    # Hauptteil (3 Runden Zirkeltraining)
    "3x 30 sec Bulgarian-Split-Squats",
    "3x 30 sec Glute-Bridge-mit-Mini-Band",
    "3x 30 sec Donkey-Kicks+Pulses-rechts",
    "3x 30 sec Donkey-Kicks+Pulses-links",
    "3x 30 sec Kreuzheben-mit-Rucksack/Kettlebell",
    "3x 30 sec Unterarmstütz-mit-Beinheben",
    "3x 30 sec Side-Plank-Dips-rechts",
    "3x 30 sec Side-Plank-Dips-links",

    # Cool-down
    "30 sec tiefer-Ausfallschritt-rechts",
    "30 sec tiefer-Ausfallschritt-links",
    "30 sec Rückenrollen-am-Boden"  
    ],

    "Donnerstag": [
           # Warm-up
    "1x 30 sec lockeres-Seilspringen",
    "1x 30 sec Armkreisen+Schulteröffner",
    "1x 20 sec Rumpfkreisen-im-Stand",

    # Hauptteil (4 Runden – Intervalltraining)
    "4x 30 sec Liegestütze-langsam-mit-Haltepunkt",
    "4x 30 sec Lat-Zug-mit-Handtuch-um-Türgriff",
    "4x 30 sec Trizeps-Liegestütze",
    "4x 30 sec Wadenheben-schnell",
    "4x 30 sec Leg-Raises",
    "4x 30 sec Flutter-Kicks",

    # Cool-down
    "30 sec Brustdehnung-in-Türrahmen",
    "30 sec Trizeps-Stretch-hinter-Kopf",
    "30 sec Katzen-Kuh-Bewegung-im-Vierfüßler" 
    ]
}

output.append(week)

week = {
    "Montag": [
         # Warm-up
    "1x 30 sec Seilspringen",
    "1x 20 sec Beinpendel",
    "1x 30 sec Kniebeugen-mit-Drehung",

    # Hauptteil (3 Runden Zirkel)
    "3x 30 sec Jump Squats",
    "3x 30 sec Kreuzheben-mit-Kettlebell-oder-Rucksack",
    "3x 30 sec Superwoman-Hold+Arme-abheben",
    "3x 30 sec Sumo-Squats mit Mini-Band",
    "3x 30 sec Plank-mit-diagonalen-Beinheben",
    "3x 30 sec Glute Bridge einbeinig-rechts",
    "3x 30 sec Glute-Bridge-einbeinig-links",
    "3x 30 sec Russian-Twists",

    # Cool-down
    "30 sec tiefe-Hocke",
    "30 sec Pigeon-Stretch-rechts",
    "30 sec Pigeon-Stretch-links"
    ], 

    "Donnerstag": [
         # Warm-up
    "1x 30 sec Schulterkreisen+Hampelmänner",
    "1x 20 sec diagonales-Arm-Bein-Schwingen",
    "1x 30 sec Jumping Jacks (moderat)",

    # Hauptteil (3 Runden Intervall)
    "3x 30 sec Liegestütz-Position+Schulter-Taps",
    "3x 30 sec Ruderbewegung-mit-Handtuch",
    "3x 30 sec Trizeps-Dips",
    "3x 30 sec Jumping-Lunges",
    "3x 30 sec Crunch-to-Toe-Reach",
    "3x 30 sec Seitliches-Beinheben-rechts",
    "3x 30 sec Seitliches Beinheben-links",
    "3x 30 sec Wadenheben-schnell+oben-halten",

    # Cool-down
    "30 sec Schulterdehnung-quer-über-Brust",
    "30 sec Dehnung-seitliche-Bauchmuskeln-rechts",
    "30 sec Dehnung-seitliche-Bauchmuskeln-links"
    ]
}
output.append(week)

week = {
    "Montag": [
           # Warm-up
    "1x 30 sec Hampelmänner",
    "1x 30 sec Kniehebelauf-auf-der-Stelle",
    "1x 30 sec Ausfallschritt-mit-Rumpfdrehung",

    # Hauptteil (3 Runden Zirkeltraining)
    "3x 30 sec Seitliche-Ausfallschritte",
    "3x 30 sec Glute-Kickbacks-mit-Mini-Band",
    "3x 30 sec Wall-Sit-mit-Armheben",
    "3x 30 sec einbeinige-Deadlifts-mit-Rucksack-rechs",
    "3x 30 sec einbeinige-Deadlifts-mit-Rucksack-links",
    "3x 30 sec Bauchlage-Diagonale-Arm-Bein-Lifts",
    "3x 30 sec Plank-Jacks",
    "3x 30 sec Flutter-Kicks"

    # Cool-down
    "30 sec tief- Hocke-mit-Armstreckung",
    "30 sec Hamstring-Stretch-rechts",
    "30 sec Hamstring-Stretch-links" 
    ],

    "Donnerstag": [
            # Warm-up
    "1x 30 sec Seilspringen-leicht",
    "1x 30 sec Schulterkreisen+Rückenöffnung",
    "1x 20 sec Armkreisen-rückwärts+Vorbeugen",

    # Hauptteil (Intervall – 4 Runden)
    "4x 30 sec Liegestütze-+-Rotation",
    "4x 30 sec Tür-Rudern",
    "4x 30 sec Trizeps-Push-Backs-mit-Mini-Band",
    "4x 30 sec Wadenheben-schnell+Pause-oben",
    "4x 30 sec Klappmesser",
    "4x 30 sec Bicycle-Crunches"

    # Cool-down
    "30 sec Brustöffner-an-Wand-stehend",
    "30 sec Trizeps-Stretch-über-Kopf",
    "30 sec Katze-Kuh-im-Stand"
    ]
}
output.append(week)

week = {
    "Montag": [
            # Warm-up
    "1x 30 sec Hocksprünge-leicht",
    "1x 30 sec Hüftöffner-im-Ausfallschritt",
    "1x 30 sec Sprinter-Kicks-im-Stand",

    # Hauptteil (3 Runden – Kraft & Koordination)
    "3x 30 sec Einbeinige-Step-ups",
    "3x 30 sec Glute-Bridge-mit-diagonaler-Armführung",
    "3x 30 sec Mini-Band-Monster-Walks",
    "3x 30 sec Good-Mornings",
    "3x 30 sec Rückenlage-Dead-Bugs",
    "3x 30 sec Plank-mit-Beinheben-abwechselnd",
    "3x 30 sec Side-Leg-Lifts-rechts",
    "3x 30 sec Side-Leg-Lifts-links"

    # Cool-down
    "30 sec tiefer-Ausfallschritt+Oberkörper-Rotation",
    "30 sec Glute-Stretch-Rückenlage-rechter-Fuß-auf-Knie",
    "30 sec Glute-Stretch-Rückenlage-linker-Fuß-auf-Knie"
    ],

    "Donnerstag": [
            # Warm-up
    "1x 30 sec Jumping-Jacks+Armzug",
    "1x 30 sec Schulterkreisen-in-Standwaage",
    "1x 30 sec Brustöffner-im-Ausfallschritt-tehend",

    # Hauptteil (3 Runden Intervalltraining)
    "3x 30 sec Liegestütze-mit-kurzer-Haltepause-unten",
    "3x 30 sec Superman-Pulls-Boden-Lat-Fokus",
    "3x 30 sec Trizeps-Dips",
    "3x 30 sec Wadenheben-mit-explosivem-Tempo",
    "3x 30 sec Crunch-Pulses+Beine-oben",
    "3x 30 sec Plank-to-Elbow-Taps",
    "3x 30 sec Beinpendel-liegend",
    "3x 30 sec Hollow-Body-Hold"

    # Cool-down
    "30 sec Armstreckung-an-Türrahmen",
    "30 sec Trizeps-und-Schulterdehnung-rechts",
    "30 sec Trizeps- und Schulterdehnung-links"
    ]
}
output.append(week)

week = {
    "Montag": [
            # Warm-up
    "1x 30 sec Jumping Jacks",
    "1x 30 sec Beinrückseite aktiv dehnen im Stand",
    "1x 30 sec Ausfallschritt seitlich mit Armheben",

    # Hauptteil (3 Runden, gesteigert)
    "3x 30 sec Sprungausfallschritte (alternativ: normal)",
    "3x 30 sec Glute Bridge mit engem Widerstandsband",
    "3x 30 sec Superman-Heben mit Halten",
    "3x 30 sec Step-Back Lunges mit Kettlebell",
    "3x 30 sec Plank mit Schultertipps",
    "3x 30 sec Toe-Touches im Liegen",
    "3x 30 sec Hip Raises mit Langsamhub",
    "3x 30 sec Bauchlage – diagonales Arm-Bein-Heben"

    # Cool-down
    "30 sec tiefe Hocke mit Beinarbeit",
    "30 sec Beinrückseiten-Stretch (stehend, beidseitig)",
    "30 sec Hüftmobilisation im Vierfüßler"
    ],

    "Donnerstag": [
            # Warm-up
    "1x 30 sec Seilspringen moderat",
    "1x 30 sec Schulterkreisen rückwärts",
    "1x 30 sec Arm-Heben in Bauchlage (aktivierend)",

    # Hauptteil (3 Runden, Ausdauerlastig)
    "3x 30 sec Liegestütz-Wand-Walk (alternativ: normale)",
    "3x 30 sec Renegade Rows mit Wasserflaschen",
    "3x 30 sec Trizeps Push-ups (Knie erlaubt)",
    "3x 30 sec Wadenheben im Tempo-Wechsel",
    "3x 30 sec Sit-ups mit Twist",
    "3x 30 sec Mountain Climbers",
    "3x 30 sec Plank-Ups",
    "3x 30 sec seitliches Beinheben im Stütz"

    # Cool-down
    "30 sec Arme hinter Rücken ziehen (Schulterdehnung)",
    "30 sec diagonales Armziehen (Latissimus-Stretch)",
    "30 sec Kinderpose mit Atmung"
    ]
}
output.append(week)
outputs.append(output)

output = []

week = {
    "Montag": [   # Warm-up (6 Minuten)
    "1x 3 min Rudermaschine, moderates Tempo",
    "1x 15 Schulterkreisen + Armkreisen rückwärts",
    "1x 10 Air Squats + 10 Armheben über Kopf",

    # Hauptteil (ca. 54 Minuten)
    # Supersatz 1 – Rücken & Bizeps
    "3x 10 Latziehen (weiter Griff)",
    "3x 12 Bizeps-Curls mit EZ-Curl-Bar",
    
    # Supersatz 2 – Unterer Rücken & Trapez
    "3x 10 Good Mornings mit Langhantel",
    "3x 12 Shrugs mit Kurzhanteln",
    
    # Supersatz 3 – Schultern & Trizeps
    "3x 10 Schulterdrücken mit Kurzhanteln im Sitzen",
    "3x 12 Trizepsdrücken mit Kurzhantel über Kopf",
    
    # Supersatz 4 – Beine & Gesäß
    "3x 12 Bulgarian Split Squats mit Kurzhanteln",
    "3x 15 Beinbeuger an Maschine",
    
    # Supersatz 5 – Core & Unterarme
    "3x 12 Hanging Leg Raises an Sling-Trainer",
    "3x 30 sec Wrist-Curls mit Kurzhanteln (beidseitig)",

    # Zusatz-Satz – Waden (abschließend)
    "3x 20 Wadenheben stehend mit Kettlebell",

    # Cool-down (6 Minuten)
    "1x 30 sec Lat-Dehnung an der Wand",
    "1x 30 sec Vorbeuge mit lockeren Schultern",
    "1x 60 sec tiefer Ausfallschritt + Rotation je Seite",
    "1x 30 sec Armstrecken + Schulterdehnung",
    "1x 30 sec Waden-Stretch an der Wand"
    ]
}
output.append(week)

week = {
    "Montag": [
            # Warm-up (6 Minuten)
    "1x 2 min Rudermaschine, moderat",
    "1x 10 Schulterkreisen + 10 Rumpfrotationen",
    "1x 10 Kniebeugen mit Schulterheben (Langhantel ohne Gewicht)",

    # Hauptteil (ca. 54 Minuten)
    # Supersatz 1 – Rücken & Bizeps
    "3x 10 Rudern vorgebeugt mit Langhantel",
    "3x 12 Bizepscurls mit Kurzhanteln im Sitzen",

    # Supersatz 2 – Trapez & Unterarme
    "3x 10 Aufrechtes Rudern mit SZ-Stange",
    "3x 12 Farmers Walk mit schweren Kurzhanteln (30 sec)",

    # Supersatz 3 – Beine & Gesäß
    "3x 10 Beinpresse schwer",
    "3x 12 Kettlebell Swings",

    # Supersatz 4 – Schultern & Trizeps
    "3x 10 Seitheben mit Kurzhanteln",
    "3x 12 Trizepsdrücken am Sling-Trainer",

    # Supersatz 5 – Rückenstrecker & Waden
    "3x 12 Back Extensions (mit Gewichtsscheibe auf Brust)",
    "3x 20 Wadenheben einbeinig auf Kurzhantel",

    # Cool-down (6 Minuten)
    "1x 30 sec Dehnung unterer Rücken im Sitzen",
    "1x 30 sec Schulterdehnung quer über die Brust",
    "1x 30 sec Lat-Stretch an Sprossenwand",
    "1x 30 sec Wadendehnung (gegen Wand)",
    "1x 30 sec Oberschenkel-Rückseite im Ausfallschritt"
    ]
}
output.append(week)

week = {
    "Montag": [
            # Warm-up (6 Minuten)
    "1x 2 min Rudermaschine locker",
    "1x 10 Schulterkreisen + 10 Armkreisen vorwärts",
    "1x 10 Langhantel-Overhead Press mit leerer Stange",

    # Hauptteil (ca. 54 Minuten)
    # Supersatz 1 – Brust & Trizeps
    "3x 10 Bankdrücken mit Langhantel",
    "3x 12 Trizeps-Kickbacks mit Kurzhanteln",

    # Supersatz 2 – Gesäß & Rückenstrecker
    "3x 12 Hip Thrusts mit Langhantel",
    "3x 12 Superman-Holds auf der Bank",

    # Supersatz 3 – Schultern & Unterarme
    "3x 10 Arnold Press mit Kurzhanteln",
    "3x 20 sec Wrist Roller mit Gewicht (EZ-Curl-Stange + Seil)",

    # Supersatz 4 – Latissimus & Bizeps
    "3x 10 Latzug enger Griff",
    "3x 12 Konzentrationscurls einarmig mit Kurzhantel",

    # Supersatz 5 – Core & Waden
    "3x 15 Russian Twists mit Kettlebell",
    "3x 20 Wadenheben in der Beinpresse",

    # Cool-down (6 Minuten)
    "1x 30 sec Trizeps-Dehnung über Kopf",
    "1x 30 sec Glute-Stretch liegend",
    "1x 30 sec Bauchdehnung in Kobra-Position",
    "1x 30 sec Trapez-Dehnung seitlich",
    "1x 30 sec tiefer Lunge-Stretch mit Rotation"
    ]
}
output.append(week)

week = {
    "Montag": [
          # Warm-up (6 Min)
    "1x 2 min Rudermaschine locker",
    "1x 15 Schulterkreisen + 15 Hüftkreisen",
    "1x 10 explosive Bodyweight-Squats",

    # Hauptteil (ca. 54 Min)
    # Supersatz 1 – Latissimus & Unterarme
    "3x 12 Latzug weiter Griff",
    "3x 15 Kurzhantel-Grip Holds (30 sec)",

    # Supersatz 2 – Schultern & Autochthone
    "3x 12 Frontheben mit Kurzhanteln",
    "3x 15 Superman-Rückenheben mit Pause (3 sec oben)",

    # Supersatz 3 – Beine & Gluteus
    "3x 10 Bulgarian Split Squats mit Kurzhanteln",
    "3x 12 Hip Thrusts mit Kettlebell",

    # Supersatz 4 – Trapez & Bizeps
    "3x 12 Shrugs mit Kurzhanteln",
    "3x 10 SZ-Curls am Kabel mit Pause (2 sec unten)",

    # Supersatz 5 – Waden & Rumpfstabilität
    "3x 15 stehendes Wadenheben mit Kurzhanteln",
    "3x 30 sec Plank mit Vor-Rückwippen",

    # Cool-down (6 Min)
    "1x 30 sec Schulterdehnung quer",
    "1x 30 sec Waden Stretch an Wand",
    "1x 30 sec Rückenbeuge im Sitzen",
    "1x 30 sec Gluteus-Dehnung liegend",
    "1x 30 sec Lat-Dehnung an Sprossenwand"
    ]
}
output.append(week)

week = {
    "Montag": [
         # Warm-up (6 Min)
    "1x 2 min Rudermaschine (starkes Tempo)",
    "1x 10 Schulterkreisen + 10 Armkreisen rückwärts",
    "1x 10 Air-Squats mit Gewichtsscheibe vorn"

    # Hauptteil (ca. 54 Min)
    # Supersatz 1 – Brust & Trizeps
    "3x 10 Pec Deck Maschine langsam + explosiv",
    "3x 12 Overhead Trizepsdrücken mit Kurzhantel",

    # Supersatz 2 – Bizeps & Schultern
    "3x 10 Hammer-Curls mit Kettlebells",
    "3x 10 Schulterdrücken sitzend mit Langhantel",

    # Supersatz 3 – Gluteus & Autochthone
    "3x 10 Hip Thrusts mit Langhantel + 3 sec Hold",
    "3x 12 Rückenstrecker an Bank (mit Scheibe auf Brust)",

    # Supersatz 4 – Unterarme & Trapez
    "3x 20 sec Wrist Curls mit SZ-Stange",
    "3x 12 Langhantel Shrugs mit Slow Down Phase",

    # Supersatz 5 – Waden & Core
    "3x 20 Wadenheben einbeinig auf Step",
    "3x 30 sec Russian Twist mit Kettlebell"

    # Cool-down (6 Min)
    "1x 30 sec Brustdehnung an Wand",
    "1x 30 sec Trizeps-Dehnung hinter Kopf",
    "1x 30 sec Lendenwirbeldehnung im Liegen",
    "1x 30 sec tiefer Lung-Stretch",
    "1x 30 sec Bauchstretch (Kobra)"
    ]
}
output.append(week)

week = {
    "Montag": [
    # Warm-up (2 Minuten)
    "1x 30 sec Armkreisen mit Spannung (Mini-Band oder ohne)",
    "1x 30 sec Schulter-Shrugs mit Widerstandsband (für Trapez)",
    "1x 1 min Loaded Wrist & Elbow Mobilisation (Handgelenk + Trizeps vorbereiten)",

    # Hauptteil (10 Minuten)
    # Supersatz 1 – Körperspannung + Kontrolle
    "2x 6 Planche Push-ups (Tuck oder Full, je nach Niveau)",
    "2x 10 Elevated Pike Push-ups mit engem Griff (Trizeps-Fokus)",

    # Supersatz 2 – Kraft + statische Kontrolle
    "2x 8 Handstand Push-ups (Wand oder freistehend)",
    "2x 15 sec Isometrischer Shrug-Hold im Pike-Stütz (Trapez-Isolation)",

    # Supersatz 3 – Ausbrennen & Finish
    "2x 15 Trizeps-Kickbacks mit Band (über Kopf, explosive Streckung)",
    "2x 15 sec Wall-Plank Hold mit aktiven Schultern (Trapez statisch)",

    # Cool-down (2 Minuten)
    "1x 30 sec Trizeps-Stretch mit Arm über Kopf",
    "1x 30 sec Nacken-Dehnung (Kopf zur Seite + Arm hinter Rücken)",
    "1x 30 sec Massageball am Trizeps oder oberen Rücken"
    ]
}
output.append(week)

week = {
    "Montag": [
         # Warm-up (2 Minuten)
    "1x 30 sec Armkreisen rückwärts mit Spannung (Mini-Bands)",
    "1x 30 sec Scapula Push-ups (Aktivierung für Trapez)",
    "1x 1 min Trizeps-Mobilisation am Türrahmen (Schwungfrei!)",

    # Hauptteil (10 Minuten)
    # Supersatz 1 – Körperspannung + Kontrolle
    "2x 8 Wall-Assisted Handstand Push-ups mit Schulter-Touch (Trapez & Trizeps)",
    "2x 8 Archer Push-ups mit engem Griff (Trizeps-Dominanz)",

    # Supersatz 2 – Dynamik + statische Kraft
    "2x 6 Tiger-Bend Push-ups (vom Unterarm in den Handstandstütz drücken)",
    "2x 20 sec Wall Shrug Holds (Handstand-Position an Wand, Fokus auf Trapez)",

    # Supersatz 3 – Explosivität & End-Burnout
    "2x 12 explosive Trizeps-Dips an der Bank",
    "2x 15 sec Isometrische Y-Arm-Haltung in Bauchlage (Trapez aktiv halten)",

    # Cool-down (2 Minuten)
    "1x 30 sec Trizeps-Stretch an Wand (Ellenbogen über Kopf)",
    "1x 30 sec Massageball im oberen Rückenbereich (selbstständig an Wand)",
    "1x 30 sec Schulterkreisen langsam mit tiefer Atmung"
    ]
}
output.append(week)

week = {
    "Montag": [
        
    ]
}
outputs.append(output)

output = []

week = {
    ""
}

inoutputs = []

for i in range(min(len(inputs), len(outputs))):
    combined = {
        "input": inputs[i],
        "output": outputs[i]
    }
    inoutputs.append(combined)

print(inoutputs)

cred = credentials.Certificate("übungen.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Funktion zum Speichern beliebig vieler Übungen
def save_inoutputs(inoutputs):
    for inoutput in inoutputs:
        db.collection("Inputs & Outputs").add(inoutput)

save_inoutputs(inoutputs)