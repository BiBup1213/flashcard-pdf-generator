Flashcard PDF Generator (Karteikarten-PDF aus JSON)

Ein simples Python-Tool zur Erstellung druckbarer Lern-Karteikarten aus einer JSON-Datei.

Kurz gesagt:
Fragen & Antworten als JSON → druckfertige PDF mit Karteikarten.

🧠 Was macht das Tool?

Das Script liest eine JSON-Datei mit Frage-Antwort-Paaren ein und erzeugt daraus eine PDF im A4-Format.

Pro Seite werden 8 Karteikarten erstellt (4 Zeilen × 2 Spalten).
Die Rückseite wird automatisch so vorbereitet, dass beim beidseitigen Druck Frage und Antwort korrekt übereinanderliegen.

Das Tool erzeugt keine Inhalte – es kümmert sich ausschließlich um Layout und Druckformatierung.

🏁 Hintergrund

Das Projekt entstand während meiner Vorbereitung auf die Abschlussprüfung als Fachinformatiker für Anwendungsentwicklung.

Ich wollte:

Lerninhalte strukturiert in Frage/Antwort-Form bringen

daraus schnell physische Karteikarten erzeugen

keine komplexe Lernplattform nutzen

ein simples, kontrollierbares Tool

Das Ergebnis ist ein bewusst schlankes Script mit klarer Funktion:
JSON → Karteikarten-PDF

✨ Features

PDF-Erzeugung aus strukturierter Q&A-JSON

8 Karten pro A4-Seite (4 × 2 Raster)

Horizontale und vertikale Textzentrierung

Automatischer Zeilenumbruch

Automatische Schriftgrößenanpassung bei längeren Texten

Rahmen um jede Karte

Label „F“ (Frage) und „A“ (Antwort)

Druckoptimierte Rückseitenanordnung

📦 Voraussetzungen

Python 3

Python-Bibliothek: reportlab

🔧 Installation
1. Abhängigkeit installieren
pip install reportlab
2. Optional (empfohlen): Virtuelle Umgebung nutzen
python -m venv .venv

Aktivieren:

Windows

.venv\Scripts\activate

macOS / Linux

source .venv/bin/activate

Danach:

pip install reportlab
🚀 Projekt herunterladen
Variante A – Repository klonen
git clone https://github.com/<DEIN-USERNAME>/<DEIN-REPO>.git
cd <DEIN-REPO>
Variante B – ZIP herunterladen

Auf GitHub auf Code klicken

Download ZIP auswählen

ZIP entpacken

Ordner öffnen

🧾 JSON-Format

Die JSON-Datei muss folgendes Format besitzen:

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

Zeilenumbrüche können mit \n eingefügt werden

Die Reihenfolge bestimmt die Kartenreihenfolge

▶️ Nutzung
python import_fragenantworten.py

Falls du andere Dateinamen verwenden willst, passe den Funktionsaufruf im Script an:

create_flashcards_pdf("meine_datei.json", "output.pdf")
🖨️ Drucken

Beidseitig drucken

An der langen Kante wenden

Skalierung auf 100 % lassen

Die Rückseite wirkt gespiegelt – das ist technisch notwendig.

💡 Tipps für gute Karteikarten

1 Karte = 1 Kernpunkt

Antworten kurz und präzise halten

Lange Listen lieber auf mehrere Karten aufteilen

Definitionen, Unterschiede und Schritte funktionieren besonders gut

📁 Projektstruktur
.
├── import_fragenantworten.py
├── fragen_und_antworten.json
└── README.md
🔮 Ausblick

Mögliche Erweiterungen:

GUI zur Erstellung der JSON-Datei

Import aus Text oder PDF

Halbautomatische Q&A-Erstellung

Der aktuelle Fokus bleibt bewusst:
Einfaches, sauberes Tool für druckbare Karteikarten.
