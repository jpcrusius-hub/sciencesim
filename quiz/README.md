# 📐 Quiz: Bewegungslehre – Klasse 10 GY

Interaktives Quiz zur Stundenleistung im Themenbereich **Gleichförmige und beschleunigte Bewegung**.

## 🔗 Links

| Komponente | URL |
|------------|-----|
| **Quiz (Schüler)** | [index.html](https://jpcrusius-hub.github.io/sciencesim/quiz/index.html) |
| **Decoder (Lehrer)** | [decoder.html](https://jpcrusius-hub.github.io/sciencesim/quiz/decoder.html) |
| **QR-Codes** | [qr-codes.html](https://jpcrusius-hub.github.io/sciencesim/quiz/qr-codes.html) |

## 📊 Übersicht

| Eigenschaft | Wert |
|-------------|------|
| **Fach** | Physik |
| **Klassenstufe** | 10 GY (Gymnasium) |
| **Thema** | Bewegungslehre (Kinematik) |
| **Basispunkte** | 88 P |
| **Bonuspunkte** | 3 P (🎄 Weihnachtsmann) |
| **Bearbeitungszeit** | 90 Minuten |
| **Hilfsmittel** | Keine |
| **Bewertung** | 15-NP-Skala (Sonstige Leistungen) |

## 📝 Aufgabenstruktur

### Block 1: MC Grundwissen (20 P)
- **F1–F10**: Multiple-Choice-Fragen zu Grundbegriffen (je 2P)

### Block 2: Berechnungen (16 P)
- **F11–F18**: Rechenaufgaben mit Einheiten-Auswahl (je 2P)

### Block 3: Diagramme (22 P)
- **A (8 P)**: v(t)-Diagramm analysieren (8 Phasen, je 1P)
- **B (4 P)**: s(t)-Diagramm analysieren (4 Phasen, je 1P)
- **C (6 P)**: a(t)-Diagramm Aufzug (6 Phasen, je 1P)
- **D (4 P)**: Zuordnung v(t) ↔ s(t) (4 Paare, je 1P)

### Block 4: Komplexe Aufgaben (30 P)
- **E (20 P)**: Komplexe v(t)-Analyse mit Berechnungen (10 Teilaufgaben, je 2P)
- **F (10 P)**: Ampelstart-Szenario (5 Teilaufgaben, je 2P)

### Bonus (3 P)
- 🎄 Weihnachtsmann in MV – Geschwindigkeitsberechnung

## ⚙️ Features

### Quiz (index.html)
- ✅ Auto-Save bei jeder Eingabe
- ✅ Automatisches Fortsetzen bei Reload
- ✅ Progress-Anzeige (Zeit + bearbeitete Punkte)
- ✅ Navigation per Fragen-Dots
- ✅ Reset nur mit Lehrer-Code (`3141`)
- ✅ **Großer QR-Code (350×350 px)** bei Abgabe
- ✅ **Textcode + Copy-Button** als Fallback
- ✅ Vollständige Musterlösung mit PDF-Export
- ✅ **Submission-Info auf Musterlösung** (QR + Code)
- ✅ Einheiten-Mehrfach-Akzeptanz (m/km, m/s/km/h, etc.)

### Decoder (decoder.html)
- ✅ **Große Scan-Box (350×350 px)**
- ✅ **Kamera-Auswahl Dropdown**
- ✅ Text-Eingabe als Alternative
- ✅ Akustisches Feedback bei Scan
- ✅ Duplikat-Erkennung
- ✅ Statistik-Übersicht
- ✅ Detail-Ansicht pro Schüler
- ✅ CSV-Export
- ✅ Feedbackbögen für alle Schüler

## 🔐 Codes

| Funktion | Code |
|----------|------|
| Quiz zurücksetzen | `3141` |
| Musterlösung entsperren | `PHYSIK` |

## 📱 Kompatibilität

- ✅ Desktop (Chrome, Firefox, Safari, Edge)
- ✅ Tablet/iPad (empfohlen: Landscape)
- ✅ Smartphone (Portrait/Landscape)
- ✅ Offline-fähig nach erstem Laden

## 📄 Dateien

```
quiz/
├── index.html      # Quiz für Schüler
├── decoder.html    # Decoder für Lehrer
├── qr-codes.html   # Druckbare QR-Codes
└── README.md       # Diese Datei
```

## 🎓 Didaktische Hinweise

- **Kopfrechenbar**: Alle Zahlenwerte ohne Taschenrechner lösbar
- **g = 10 m/s²**: Vereinfachter Wert für Fallbeschleunigung
- **AFB-Verteilung**: ca. 30% AFB1, 40% AFB2, 30% AFB3

---

**Version:** 5.2  
**Stand:** Dezember 2024
