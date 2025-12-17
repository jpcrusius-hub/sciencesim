# Quiz: Stromstärke und Spannung (Klasse 8)

Interaktives HTML5-Quiz zur Elektrizitätslehre für Klasse 8 (Gesamtschule MV).

## 🎯 Themenbereich

- Elektrische Stromstärke (*I*, Ampere)
- Elektrische Spannung (*U*, Volt)
- Messgeräte (Amperemeter, Voltmeter)
- Reihen- und Parallelschaltung
- Berechnungen in Schaltkreisen

## 📊 Struktur

| Level | Symbol | Aufgaben | Punkte | Schwierigkeit |
|-------|--------|----------|--------|---------------|
| Basis | ○ | 13 | 28 P | Grundwissen |
| Stern 1 | ★ | 12 | 30 P | Anwendung |
| Stern 2 | ★★ | 9 | 30 P | Vertiefung |
| Stern 3 | ★★★ | 14 | 52 P | Transfer |
| **Gesamt** | | **48** | **140 P** | |

## 🎮 Aufgabentypen

- Multiple Choice (mc)
- Dropdown-Auswahl (dropdown)
- Mehrfachauswahl (multicheck)
- Zahleneingabe (number)
- Mehrfach-Zahleneingabe (multi-number)
- Texteingabe (text, text-multi)

## 📱 Dateien

| Datei | Beschreibung | Zielgruppe |
|-------|--------------|------------|
| `index.html` | Schüler-Quiz | Schüler |
| `decoder.html` | Auswertungs-Tool | Lehrkraft |

## 🚀 Nutzung

### Für Schüler
1. `index.html` im Browser öffnen (oder via GitHub Pages)
2. Platznummer wählen
3. Schwierigkeitsstufe auswählen
4. Quiz bearbeiten (45 min Timer)
5. Abgeben → QR-Code zeigen

### Für Lehrkräfte
1. `decoder.html` öffnen
2. QR-Code scannen ODER Code manuell eingeben
3. Automatische Auswertung mit Notenpunkten (14-NP-Skala)

## 🔐 Codes

| Code | Funktion |
|------|----------|
| `STROM` | Unlock (vorzeitige Abgabe freischalten) |
| `3141` | Reset (Fortschritt löschen) |

## ⚙️ Technische Details

- **Bewertung:** 14-NP-Skala (Klasse 8 MV)
- **Timer:** 45 Minuten pro Level
- **Speicherung:** localStorage (Fortschritt bleibt erhalten)
- **QR-Code:** LZ-String komprimierte Ergebnisdaten
- **Offline:** Funktioniert ohne Server (nur CDN für Libraries)

### Externe Abhängigkeiten (CDN)
- `lz-string` (Komprimierung)
- `qrcodejs` (QR-Code Generierung)
- `html5-qrcode` (QR-Code Scanner im Decoder)

## 📋 Lehrplanbezug

**Rahmenplan Physik MV, Klasse 7-10:**
- Elektrischer Stromkreis
- Elektrische Grundgrößen
- Schaltungen

## 🖥️ GitHub Pages

Nach dem Push ist das Quiz erreichbar unter:
```
https://jpcrusius-hub.github.io/sciencesim/quiz/elektrik-stromstaerke-spannung-8/
```

## 📝 Lizenz

Erstellt für den Physikunterricht. Verwendung im schulischen Kontext gestattet.

---

*Erstellt mit dem ScienceSim Quiz-System*
