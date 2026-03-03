# Flashcard PDF Generator (Karteikarten-PDF aus JSON)

Ein kleines, simples Python-Tool, mit dem du dir aus einer JSON-Datei **eigene Lern-Karteikarten als druckbare PDF** erzeugen kannst.

---

## 🧠 Was macht das Tool?

Du gibst eine JSON-Datei mit **Fragen & Antworten** vor – das Script erzeugt daraus eine **A4-PDF** im Raster **4 × 2** (also **8 Karten pro Seite**).

Gedacht ist das für alle, die sich auf Prüfungen (oder generell Lernstoff) vorbereiten und lieber **physische Karteikarten** nutzen, statt alles nur digital zu konsumieren.

---

## 🏁 Warum gibt’s das?

Ich habe das Tool damals gebaut, als ich mich auf meine Abschlussprüfung (Fachinformatiker Anwendungsentwicklung) vorbereitet habe.

Ich wollte:
- Lerninhalte flexibel in **Frage/Antwort** strukturieren
- daraus schnell **druckbare Karten** machen
- ohne großen Overhead oder fancy Plattform

Das ist bewusst kein „Riesenprojekt“, sondern ein pragmatisches Hilfstool.

---

## ✨ Features

- PDF-Erzeugung aus Q&A-JSON
- 8 Karten pro A4-Seite (4 Zeilen × 2 Spalten)
- Text wird **horizontal & vertikal zentriert**
- Zeilenumbrüche werden unterstützt (`\n`)
- Rahmen + Label (F = Frage / A = Antwort)
- **Rückseiten-Layout wird passend vorbereitet**, damit Frage und Antwort beim beidseitigen Druck korrekt zusammenpassen 
 *(Hinweis: Dadurch wirkt die Rückseite “gespiegelt” – das ist Absicht.)*

---

## 📦 Voraussetzungen

- **Python 3**
- Python-Paket **reportlab**

Installation:

```bash
pip install reportlab

## 🚀 Installation / Download
Variante A: Repository klonen
git clone https://github.com/<DEIN-USERNAME>/<DEIN-REPO>.git
cd <DEIN-REPO>
Variante B: ZIP herunterladen
Auf GitHub: Code → Download ZIP


ZIP entpacken


Ordner öffnen



🧾 JSON-Format
Die JSON-Datei muss so aufgebaut sein:
{
 "karten": [
   {
     "frage": "Was ist ein Monopol?",
     "antwort": "Eine Marktform mit nur einem Anbieter und vielen Nachfragern."
   },
   {
     "frage": "Nenne die vier klassischen Marktformen.",
     "antwort": "Polypol, Oligopol, Monopol, bilaterales Monopol."
   }
 ]
}
Hinweise
Die Schlüssel heißen exakt: karten, frage, antwort


Zeilenumbrüche in Texten kannst du mit \n einbauen (z.B. für Listen)


Die Reihenfolge in der Datei ist die Reihenfolge in der PDF



▶️ Nutzung
Wenn dein Script (wie in deinem aktuellen Setup) am Ende direkt create_flashcards_pdf(...) aufruft, reicht:
python import_fragenantworten.py
Danach liegt die erzeugte PDF im Projektordner (Dateiname hängt vom Script ab, z.B. Karteikarten_....pdf).

🖨️ Drucken (kurzer Hinweis)
Beidseitig drucken


In den Druckeinstellungen idealerweise: an langer Kante wenden (Duplex)


Skalierung/Anpassung: 100% (nicht “An Seite anpassen”)


Dass die Rückseiten „gespiegelt“ wirken, ist normal – das sorgt dafür, dass Frage/Antwort nach dem Schneiden passen.

💡 Tipps zum Erstellen guter Q&A-Karten
Ein paar einfache Regeln machen Karteikarten deutlich besser:
1 Karte = 1 Kernpunkt


Antwort kurz halten (nicht essayartig)


lieber mehrere kleine Karten statt einer riesigen


Definitionen, Unterschiede, Aufzählungen und Schritte funktionieren besonders gut


Q&A mit Weblinks / KI erstellen (pragmatisch)
Du kannst dir Fragen & Antworten auch mit Tools generieren lassen (z.B. über KI) und dann in das JSON übertragen.
Beispiel-Prompt-Idee (für dich oder andere Tools):
„Erstelle mir Lernkarteikarten im Frage/Antwort-Format zum Thema X.
 Niveau: Y (z.B. Klassenarbeit 10. Klasse / IHK / Uni).
 Antworten bitte maximal 2–4 Sätze.
 Nutze klare, prüfungsnahe Fragen.“
Danach:
Output kurz durchgehen (Dopplungen raus, zu lange Antworten kürzen)


ins JSON übernehmen


PDF generieren



🧩 Projektstruktur (typisch)
.
├── import_fragenantworten.py
├── fragen_und_antworten.json
└── README.md

🔮 Ausblick (optional)
Langfristig wäre es denkbar, das Ganze zu erweitern, z.B.:
einfache UI zur Erstellung der JSON-Datei


Import aus Text/PDF


(später) halbautomatische Q&A-Erstellung aus Material


Aktuell bleibt es bewusst bei der Kernfunktion: JSON → druckbare Karteikarten-PDF.

