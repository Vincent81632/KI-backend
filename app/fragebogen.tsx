import axios from 'axios'
import React, { useState } from 'react'
import { Pressable, ScrollView, StyleSheet, Text, TextInput, View } from 'react-native'

const Fragebogen = () => {
  const [auswahl_ziel, setZiel] = useState<string | null>(null)
  const [auswahl_ort, setOrt] = useState<string | null>(null)
  const [auswahl_muskeln, setMuskel] = useState<string[]>([])
  const [auswahl_equipment, setEquipment] = useState<string[]>([])
  const [auswahl_zeit, setZeit] = useState<string>('')
  const [auswahl_schwierigkeitsgrad, setSchwierigkeitsgrad] = useState<string>('')
  const [auswahl_häufigkeit, setHäufigkeit] = useState<string>('')

  const ziele = [
    'Abnehmen',
    'Muskelaufbau',
    'Ausdauer'
  ]

  const orte = [
    'Zuhause',
    'Fitnessstudio'
  ]

  const muskeln = [
    'Bizeps',
    'Trizeps',
    'Unterarme',
    'Waden',
    'Quadrizeps', 
    'Hamstrings',
    'Gluten',
    'Autohthone',
    'Latissimus',
    'Trapez-Muskel',
    'Brust',
    'Six-pack',
    'Seitliche-Bauchmuskeln',
    'Schultern'
  ]
 
  const equipments = [
      "Sprossenwand", "Klimmzugstange", "Springseil", "Kurzhanteln", "Widerstandsbänder", "Beinschlingen", "Mini-Bands", "Blackroll", "Kettlebells", "Medizinball", "Sling-Trainer", "Multipresse", "Beinpresse", "Butterfly-Maschine", "Latzug-Maschine", "Rudermaschine", "Beinbeuer/Strecker", "Adduktoren-Maschine", "Kabelzugstation", "Pec-Deck", "Pull-over-Maschine", "Crosstrainer", "Stepper", "Fahrradergometer", "Langhantel", "Gewichtsscheiben", "Squat-Rack", "Bank", "Hex-Bar", "EZ-Curl_Bar", "Battle Ropes", "Massageball"
  ]
  const zielPress = (ziel: string) => {
    setZiel(prev => (prev === ziel ? null : ziel))
  }
  const ortPress = (ort: string) => {
    setOrt(prev => (prev === ort ? null : ort))
  }
const muskelPress = (muskel: string) => {
  setMuskel(prev => {
    if (prev.includes(muskel)) {
      // Muskel abwählen
      return prev.filter(m => m !== muskel);
    } else {
      // Muskel hinzufügen
      return [...prev, muskel];
    }
  });
};

const equipmentPress = (equipment: string) => {
  setEquipment(prev => {
    if (prev.includes(equipment)) {
      return prev.filter(m => m !== equipment)
    } else {
      return [...prev, equipment]
    }
  })
}

const generate = async () => {
  try {
    const response = await axios.post(
      "https://fastapi-backend-x3b7.onrender.com/generate_plan",
      {
        ziel: auswahl_ziel,
        ort: auswahl_ort,
        muskeln: auswahl_muskeln.join(", "),
        schwierigkeitsgrad: auswahl_schwierigkeitsgrad,
        zeit: parseInt(auswahl_zeit, 10),
        häufigkeit: parseInt(auswahl_häufigkeit, 10),
        equipment: auswahl_equipment
      },
      { timeout: 60000 } // 60 Sekunden Timeout
    );

    console.log("Trainingsplan:", response.data.trainingsplan);
  } catch (error) {
    console.error("Fehler:", error);
    alert("Fehler beim Generieren:\n" + error);
  }
};




  return (
    <ScrollView>
      <View style={styles.container}>
        <Text style={styles.title}>Fragebogen</Text>

        <Text style={styles.question}>1. Was ist dein Ziel?</Text>

        {ziele.map((ziel) => (
          <Pressable
            key={ziel}
            onPress={() => zielPress(ziel)}
            style={[
              styles.button,
              auswahl_ziel === ziel && styles.buttonAusgewählt,
            ]}
          >
            <Text style={styles.buttonText}>{ziel}</Text>
          </Pressable>
        ))}


        <Text style = {styles.question}>2. Wo möchtest du trainieren?</Text>
        {orte.map((ort) => (
          <Pressable
          key = {ort}
          onPress={() => ortPress(ort)}
          style={[
            styles.button,
            auswahl_ort === ort && styles.buttonAusgewählt
          ]}
          >
            <Text style = {styles.buttonText}>{ort}</Text>
          </Pressable>

          
        ))}

        <Text style = {styles.question}>3. Wie häufig möchtest du trainieren?</Text>
                <TextInput
         value={auswahl_häufigkeit}
          onChangeText={(text) => {
           const nurZahlen = text.replace(/[^0-9]/g, '')
            setHäufigkeit(nurZahlen)
          }}
          onBlur={() => {
            const zahl = parseInt(auswahl_häufigkeit || '0', 10)
            if (zahl < 1 || zahl > 7) {
              alert('Bitte gib eine Zahl zwischen 1 und 7 ein.')
              setHäufigkeit('')
            }
         }}
         keyboardType="numeric"
         placeholder="Gib eine Zahl zwischen 1 & 7 ein."
         placeholderTextColor="black"
         style={styles.zeit}
        />

        <Text style = {styles.question}>4. Wie viel Zeit hast du?</Text>
        <TextInput
         value={auswahl_zeit}
          onChangeText={(text) => {
           const nurZahlen = text.replace(/[^0-9]/g, '')
            setZeit(nurZahlen)
          }}
          onBlur={() => {
            const zahl = parseInt(auswahl_zeit || '0', 10)
            if (zahl < 15 || zahl > 120) {
              alert('Bitte gib eine Zahl zwischen 15 und 120 ein.')
              setZeit('')
            }
         }}
         keyboardType="numeric"
         placeholder="Gib eine Zahl zwischen 15 & 120 ein."
         placeholderTextColor="black"
         style={styles.zeit}
        />

                <Text style = {styles.question}>5. Welche Muskeln möchtest du trainieren</Text>
{muskeln.map((muskel) => (
  <Pressable
    key={muskel}
    onPress={() => muskelPress(muskel)}
    style={[
      styles.button,
      auswahl_muskeln.includes(muskel) && styles.buttonAusgewählt
    ]}
  >
    <Text style={styles.buttonText}>{muskel}</Text>
  </Pressable>
))}

<Text style = {styles.question}>6. Was für Equipment hast du?</Text>
{equipments.map((equipment) => (
  <Pressable
  key = {equipment}
  onPress={() => equipmentPress(equipment)}
  style = {[
    styles.button,
    auswahl_equipment.includes(equipment) && styles.buttonAusgewählt
  ]}
  >
    <Text style = {styles.buttonText}>{equipment}</Text>
  </Pressable>
))}

        <Text style = {styles.question}>7. Wie fortgeschritten bist du?</Text>
        <TextInput
         value={auswahl_schwierigkeitsgrad}
          onChangeText={(text) => {
           const nurZahlen = text.replace(/[^0-9]/g, '')
            setSchwierigkeitsgrad(nurZahlen)
          }}
          onBlur={() => {
            const zahl = parseInt(auswahl_schwierigkeitsgrad || '0', 10)
            if (zahl < 1 || zahl > 20) {
              alert('Bitte gib eine Zahl zwischen 1 und 20 ein.')
              setSchwierigkeitsgrad('')
            }
         }}
         keyboardType="numeric"
         placeholder="Gib eine Zahl zwischen 1 & 20 ein."
         placeholderTextColor="black"
         style={styles.zeit}
        />


        
        <Pressable
        onPress={() => generate()}
        style = {styles.generate}><Text style = {styles.text_generate}>Personalisierter Trainingsplan generieren</Text></Pressable>
      </View>
    </ScrollView>
    
  )
}

export default Fragebogen

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    paddingTop: 50,
  },
  title: {
    marginBottom: 20,
    fontSize: 24,
    fontWeight: 'bold',
  },

  text_generate: {
    fontSize: 18,
  },
  generate: {
    width: '80%',
    marginVertical: 30,
    backgroundColor: 'red',
    borderRadius: 100,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
    textAlign: 'center'
  },
  question: {
    marginTop: 30,
    marginBottom: 10,
    fontSize: 18,
  },
  zeit : {
    width: '80%',
    marginVertical: 10, 
    backgroundColor: 'white',
    borderColor: 'lightgray',
    borderRadius: 100,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    textAlign: 'center'
  },
  button: {
    width: '80%',
    marginVertical: 10,
    backgroundColor: 'lightgray',
    borderRadius: 100,
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
  },
  buttonAusgewählt: {
    backgroundColor: '#ADD8E6',
  },
  buttonText: {
    color: 'black',
    fontSize: 16,
  },
  input: {
    width: '80%',
    borderWidth: 1,
    borderColor: '#ccc',
    padding: 10,
    marginTop: 10,
  },
})
