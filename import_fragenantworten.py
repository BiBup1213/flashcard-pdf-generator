from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase.pdfmetrics import stringWidth
import json

# -----------------------------------------------------------
# Hilfsfunktion: Umbruch nach REALER Breite (statt Zeichenanzahl)
# -----------------------------------------------------------
def wrap_text_to_width(text, font_name, font_size, max_width):
    # Textaufbereitung: \n durch tatsächliche Zeilenumbrüche ersetzen
    text = text.replace("\\n", "\n")

    lines_out = []

    # Explizite Umbrüche respektieren
    for paragraph in text.split("\n"):
        if paragraph.strip() == "":
            lines_out.append("")  # leere Zeile beibehalten
            continue

        words = paragraph.split()
        line = words[0]

        for w in words[1:]:
            candidate = f"{line} {w}"
            if stringWidth(candidate, font_name, font_size) <= max_width:
                line = candidate
            else:
                lines_out.append(line)
                line = w

        lines_out.append(line)

    return lines_out

# -----------------------------------------------------------
# Funktion zum Hinzufügen von Text:
# - Umbruch nach Breite (pixelbasiert)
# - vertikal zentriert (Textblock)
# - Auto-Shrink, damit nix abgeschnitten wird
# -----------------------------------------------------------
def draw_wrapped_text(c, text, x, y, box_width, box_height, font_size=10, min_font_size=7, padding=12, leading=2):
    font_name = "Helvetica"

    # Innenfläche (damit Text nicht direkt am Rand klebt)
    usable_width = box_width - 2 * padding
    usable_height = box_height - 2 * padding

    current_size = font_size

    # Auto-Shrink: solange kleiner machen, bis der Textblock in die Höhe passt
    while current_size >= min_font_size:
        lines = wrap_text_to_width(text, font_name, current_size, usable_width)

        line_height = current_size + leading
        block_height = len(lines) * line_height

        if block_height <= usable_height:
            break

        current_size -= 1

    # Font setzen
    c.setFont(font_name, current_size)

    # Vertikale Zentrierung des Textblocks
    line_height = current_size + leading
    block_height = len(lines) * line_height

    # Start-Y so, dass der Block um y (Kartenmitte) zentriert ist
    start_y = y + (block_height / 2) - current_size  # Baseline-Korrektur

    for i, line in enumerate(lines):
        c.drawCentredString(x, start_y - i * line_height, line)

# Funktion zum Zeichnen von Rahmen um die Karteikarten
def draw_borders(c, x, y, width, height):
    c.rect(x, y, width, height)  # Rechteck zeichnen

# Funktion zum Hinzufügen von "F" (Frage) oder "A" (Antwort) in die obere Ecke
def draw_label(c, label, x, y, font_size=10):
    c.setFont("Helvetica-Bold", font_size)  # Fettschrift für das Label
    c.drawString(x + 0.2*cm, y - font_size, label)  # Position des Labels oben links in der Karte

# Funktion zum Erstellen der PDF mit Rahmen, gleicher Schriftgröße und "F"/"A"-Label
def create_flashcards_pdf(json_file_path, output_pdf_path):
    # JSON-Daten laden
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # PDF-Dokument auf A4 vorbereiten
    c = canvas.Canvas(output_pdf_path, pagesize=A4)
    width, height = A4

    # 4 Zeilen, 2 Spalten für DIN A7
    rows, cols = 4, 2
    card_width = width / cols
    card_height = height / rows
    font_size = 10  # Schriftgröße festlegen

    karten = data["karten"]

    for i in range(0, len(karten), 8):
        # Neue Seite für Fragen
        c.setFont("Helvetica", font_size)

        for j in range(8):
            if i + j >= len(karten):
                break
            karte = karten[i + j]
            # Spalte und Zeile berechnen
            row = j // cols
            col = j % cols

            # Position berechnen
            x = col * card_width
            y = height - (row + 1) * card_height

            # Frage einfügen (zentriert mit Zeilenumbruch)
            text = karte["frage"]
            draw_wrapped_text(
                c,
                text,
                x + card_width / 2,
                y + card_height / 2,
                card_width,
                card_height,
                font_size=font_size
            )
            draw_borders(c, x, y, card_width, card_height)  # Rahmen um die Karte zeichnen
            draw_label(c, "F", x, y + card_height)  # "F" oben links

        # Neue Seite für Antworten (gespiegelt)
        c.showPage()
        for j in range(8):
            if i + j >= len(karten):
                break
            karte = karten[i + j]
            row = j // cols
            # Spiegeln der Spalten für die Rückseite
            col = (cols - 1) - (j % cols)

            # Position berechnen
            x = col * card_width
            y = height - (row + 1) * card_height

            # Antwort einfügen (zentriert mit Zeilenumbruch)
            text = karte["antwort"]
            draw_wrapped_text(
                c,
                text,
                x + card_width / 2,
                y + card_height / 2,
                card_width,
                card_height,
                font_size=font_size
            )
            draw_borders(c, x, y, card_width, card_height)  # Rahmen um die Karte zeichnen
            draw_label(c, "A", x, y + card_height)  # "A" oben links

        # Neue Seite vorbereiten, falls es mehr Karten gibt
        c.showPage()

    # Speichern der PDF
    c.save()

# Beispielaufruf für gespiegelte Rückseiten mit Rahmen und "F"/"A"-Label
create_flashcards_pdf('fragen_und_antworten.json', 'Karteikarten_Fragen_Antworten_F_A_FINAL.pdf')