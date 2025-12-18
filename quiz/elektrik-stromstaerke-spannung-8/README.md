# ⚡ Quiz Elektrik - Stromstärke & Spannung

Ein interaktives HTML5-Quiz für den Physikunterricht in Klasse 8.
**Thema:** Elektrische Stromstärke und Spannung in Reihen- und Parallelschaltungen.

## 🔗 Live-Links

| Ressource | URL |
|-----------|-----|
| **Quiz** | https://jpcrusius-hub.github.io/sciencesim/quiz/elektrik-stromstaerke-spannung-8/ |
| **Decoder** | https://jpcrusius-hub.github.io/sciencesim/quiz/elektrik-stromstaerke-spannung-8/decoder.html |

## 🎯 Features

- **3 Niveaustufen** in einem Quiz (⭐ Stern 1 / ⭐⭐ Stern 2 / ⭐⭐⭐ Stern 3)
- **27 Aufgaben** zu Definitionen, Umrechnungen, Schaltungsberechnungen
- **15 Schaltbilder** (inline als SVG eingebettet)
- **Offline-fähig** - keine Internetverbindung nötig
- **QR-Code-Auswertung** für schnelles Scannen
- **Automatische Musterlösung** nach Abgabe
- **PDF-Export** der Auswertung

## 📊 Niveaustufen

| Niveau | Punkte | Zeit | Bewertete Aufgaben |
|--------|--------|------|--------------------|
| ⭐ Stern 1 | 38 P | 45 min | nur (*) Aufgaben |
| ⭐⭐ Stern 2 | 54 P | 45 min | (*) und (**) |
| ⭐⭐⭐ Stern 3 | 65 P | 60 min | alle Aufgaben |

## 🚀 Quick Start

### Für Schüler
1. QR-Code scannen oder Link öffnen
2. Niveau wählen
3. Sitzplatz wählen (P01-P30)
4. Quiz bearbeiten
5. Abgeben → Musterlösung ansehen

### Für Lehrkräfte
1. `decoder.html` öffnen (oder QR-Code scannen)
2. Kamera wählen (Dokumentenkamera empfohlen)
3. QR-Codes der Schüler scannen
4. Ergebnisse als CSV exportieren

## 📁 Dateistruktur

```
quiz/elektrik-stromstaerke-spannung-8/
├── index.html              # Das Quiz (445 KB, SVGs eingebettet)
├── decoder.html            # Auswertungstool für Lehrkräfte
├── README.md               # Diese Datei
├── docs/
│   ├── sitzplatzkarten.html   # 🪑 Druckvorlage P01-P30 mit QR
│   ├── qr-poster.html         # 📋 Poster für Klassenraum
│   ├── uebersicht.html        # Aufgabenübersicht + QR-Codes
│   ├── KONZEPT.md             # Didaktisches Konzept
│   └── LEHRER_INFO.md         # Hinweise für Lehrkräfte
├── src/
│   ├── build_diagrams.sh      # Build-Script für SVGs
│   └── schaltplaene/          # 15 LaTeX-Quelldateien
└── svg/                       # 15 Schaltbilder als SVG
```

## 🔐 Codes

| Code | Funktion |
|------|----------|
| `3141` | Quiz zurücksetzen (Lehrer-Code) |

## 📄 Druckmaterialien

- **[sitzplatzkarten.html](docs/sitzplatzkarten.html)** - 30 Platzkarten mit QR-Code
- **[qr-poster.html](docs/qr-poster.html)** - Poster zum Aufhängen im Klassenraum
- **[uebersicht.html](docs/uebersicht.html)** - Komplette Aufgabenübersicht

## 📄 Lizenz

MIT License - Frei verwendbar für Bildungszwecke.

---

**Rahmenplan-Bezug:** Physik Klasse 8, Elektrizitätslehre  
**Bundesland:** Mecklenburg-Vorpommern
