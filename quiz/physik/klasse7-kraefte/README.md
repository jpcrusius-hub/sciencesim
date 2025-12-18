# 📋 Mini-Stundenleistung: Kraft und ihre Wirkungen – Klasse 7

## Übersicht

| Eigenschaft | Wert |
|-------------|------|
| **Fach** | Physik |
| **Klassenstufe** | 7 |
| **Thema** | Kraft und ihre Wirkungen |
| **Dauer** | 30 Minuten |
| **Bewertung** | 14-NP-Skala (Klasse 6-9) |
| **Reset-Code** | `2718` |

## 3-Sterne-Differenzierung

| Niveau | Symbol | Beschreibung | Aufgaben | Max. Punkte |
|--------|--------|--------------|----------|-------------|
| ★ | stern1 | BR-Niveau | A1–A5 | 26 P |
| ★★ | stern2 | MR-Niveau | A1–A7 | 34 P |
| ★★★ | stern3 | GY-Niveau | A1–A9 | 44 P |

**Wichtig:** Alle Schüler sehen ALLE 9 Aufgaben. Das gewählte Niveau bestimmt nur, welche Aufgaben zur Note zählen. Nicht gewertete Aufgaben werden im Feedback angezeigt, aber nicht zur Punktzahl addiert.

## Aufgabenübersicht

| Nr. | Titel | Level | Punkte | Typ |
|-----|-------|-------|--------|-----|
| A1 | Lückentext Grundwissen | ★ | 10 P | fill-in-blank (Dropdown) |
| A2 | Kraftwirkungen zuordnen | ★ | 6 P | table-radio |
| A3 | Verformungsarten | ★ | 5 P | table-dropdown (E/P/Z) |
| A4 | Kraftpfeil-Grundlagen | ★ | 3 P | matching-dropdown |
| A5 | Bewegungsänderung genauer | ★ | 2 P | mc-multiple (2 richtig) |
| A6 | Kraftpfeile interpretieren | ★★ | 4 P | multi-part + Diagramm |
| A7 | Kräfte in gleicher Richtung | ★★ | 4 P | multi-part + Diagramm |
| A8 | Tauziehen-Analyse | ★★★ | 5 P | multi-part |
| A9 | Kraftwirkungen im Alltag | ★★★ | 5 P | multi-part |

## Themen (laut Rahmenplan)

- ✅ Kraftwirkungen (Verformung, Bewegungsänderung)
- ✅ Verformungsarten (elastisch, plastisch, Zerstörung)
- ✅ Bewegungsänderung (Richtung, Geschwindigkeit)
- ✅ Kraftpfeil-Darstellung (Betrag, Richtung, Angriffspunkt)
- ✅ Messgerät (Kraftmesser/Federkraftmesser)
- ✅ Formelzeichen (F) und Einheit (Newton)
- ✅ Maßstab und resultierende Kraft
- ✅ Tauziehen-Analogie
- ✅ Kräftegleichgewicht

## Dateien

```
quiz/physik/klasse7-kraefte/
├── index.html           # Schüler-Quiz
├── decoder.html         # Lehrer-Auswertung (QR-Scanner)
├── platzkarten.html     # 30 Platzkarten zum Drucken (5 Seiten A4)
├── qr-codes.html        # QR-Codes & Links Übersicht für Lehrkraft
├── aufgaben-druck.html  # Aufgaben-Papierversion (2 Seiten A4)
└── README.md            # Diese Datei
```

## Verwendung

### Schüler (index.html)

1. **Niveau wählen:** ★, ★★ oder ★★★
2. **Sitzplatz wählen:** P01–P30
3. **Quiz starten:** 30 Minuten Bearbeitungszeit
4. **Abgeben:** QR-Code wird generiert

### Lehrer (decoder.html)

1. **QR-Code scannen** oder Code manuell eingeben
2. **Ergebnisse** werden automatisch gespeichert
3. **CSV-Export** für Excel/Notenbuch

## Technische Details

- **Persistenz:** localStorage (überlebt Reload, Tab-Schließen)
- **Kompression:** LZString für QR-Codes
- **QR-Scanner:** html5-qrcode 2.3.8
- **Offline-fähig:** Ja (nach erstem Laden)

## GitHub Pages Deployment

```
sciencesim/
└── quiz/
    └── physik/
        └── klasse7-kraefte/
            ├── index.html
            ├── decoder.html
            └── README.md
```

**Live-URLs:**
- Quiz: `https://jpcrusius-hub.github.io/sciencesim/quiz/physik/klasse7-kraefte/`
- Decoder: `https://jpcrusius-hub.github.io/sciencesim/quiz/physik/klasse7-kraefte/decoder.html`

## Bewertungsskala (14-NP)

| NP | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
|----|----|----|----|----|----|----|---|---|---|---|---|---|---|---|
| % | 100 | 96 | 90,67 | 86 | 80 | 73,33 | 66,67 | 60 | 53,33 | 46,67 | 40 | 33,33 | 26,67 | 20 |

## Changelog

### v1.0 (2024-12)
- Initiale Version mit 9 Aufgaben
- 3-Sterne-Differenzierung
- QR-Code-Abgabe
