# 📋 Quiz: Elektrizitätslehre Klasse 8

## Stundenleistung: Stromstärke & Spannung

---

## 📁 Dateien

| Datei | Beschreibung |
|-------|--------------|
| `index.html` | Schüler-Quiz (alle 4 Niveaus) |
| `decoder.html` | Lehrer-Auswertung mit QR-Scanner |
| `qr-codes.html` | QR-Codes und Links zur Verteilung |
| `README.md` | Diese Dokumentation |

---

## 🎯 Niveaustufen

| Niveau | Symbol | Zielgruppe | Aufgaben | Punkte |
|--------|--------|------------|----------|--------|
| Basis | ○ | Förder/schwache SuS | 13 | 28 P |
| Stern 1 | ★ | BR-Niveau | 12 | 30 P |
| Stern 2 | ★★ | MR-Niveau | 9 | 30 P |
| Stern 3 | ★★★ | GY-Niveau | 14 | 52 P |

**Gesamt:** 48 Aufgaben, 140 Punkte

---

## 📊 Bewertungsskala (14-NP, Klasse 6-9)

| NP | % | Beschreibung |
|----|---|--------------|
| 14 | 100 | sehr gut + |
| 13 | 96 | sehr gut |
| 12 | 91 | sehr gut - |
| 11 | 86 | gut + |
| 10 | 80 | gut |
| 9 | 73 | gut - |
| 8 | 67 | befriedigend + |
| 7 | 60 | befriedigend |
| 6 | 53 | befriedigend - |
| 5 | 47 | ausreichend + |
| 4 | 40 | ausreichend |
| 3 | 33 | mangelhaft + |
| 2 | 27 | mangelhaft |
| 1 | 20 | mangelhaft - |
| 0 | <20 | ungenügend |

---

## 🚀 Durchführung

### Vorbereitung

1. **QR-Codes ausdrucken** (`qr-codes.html`)
2. **Sitzplan erstellen** (P01-P30)
3. **iPads bereitstellen** (Safari/Chrome)
4. **Decoder auf Lehrer-Gerät öffnen**

### Start

1. Schüler scannen Quiz-QR-Code oder öffnen Link
2. Niveau auswählen (wird von Lehrkraft vorgegeben)
3. Sitzplatz auswählen (P01-P30)
4. "Quiz starten" klicken

### Während des Quiz

- **Timer:** 45 Minuten automatisch
- **Navigation:** Frei zwischen Aufgaben springen
- **Persistenz:** Antworten werden automatisch gespeichert
- **Neustart-sicher:** Browser-Reload verliert keine Daten

### Abgabe

1. Letzte Frage → "Quiz abgeben" Button
2. Bestätigung im Dialog
3. Feedback-Screen mit:
   - Note und Punktzahl
   - QR-Code für Lehrkraft
   - Detailliertes Feedback
   - PDF-Export-Option

### Auswertung (Lehrkraft)

1. `decoder.html` öffnen
2. Kamera wählen und Scanner starten
3. QR-Code vom Schüler-Bildschirm scannen
4. "Zur Klasse hinzufügen"
5. Nach allen Scans: CSV exportieren

---

## 🔧 Technische Details

### 3-Screen-System

```
Setup → Quiz → Feedback (DIREKT nach Abgabe)
```

**Kein Result-Screen, kein Unlock-Timer!**

### Persistenz (localStorage)

Der Quiz-Zustand überlebt:
- ✅ Browser-Reload (F5)
- ✅ Tab schließen/öffnen
- ✅ Browser neu starten
- ✅ Tablet-Neustart

### Speicher-Keys

```
quiz_v10_elektrik_k8_basis
quiz_v10_elektrik_k8_stern1
quiz_v10_elektrik_k8_stern2
quiz_v10_elektrik_k8_stern3
```

### Reset

- **Lehrer-Code:** `2718`
- Eingabe über ⟳-Button im Quiz-Header

---

## 📝 Aufgabentypen

| Typ | Beschreibung | Beispiel |
|-----|--------------|----------|
| `mc` | Multiple Choice (1 richtig) | Formelzeichen wählen |
| `multicheck` | Mehrfachauswahl | Regeln der Reihenschaltung |
| `dropdown` | Lückentext mit Auswahl | Messgeräte zuordnen |
| `number` | Zahleneingabe | Stromstärke berechnen |
| `text` | Texteingabe | Formelzeichen eingeben |
| `multi-number` | Mehrere Zahleneingaben | U₂ und U₃ berechnen |

---

## 🔌 Aufgabenübersicht

### Basis (○) – 13 Aufgaben, 28 P

| # | Typ | Punkte | Thema |
|---|-----|--------|-------|
| F1 | mc | 2 | Formelzeichen I |
| F2 | mc | 2 | Einheit Stromstärke |
| F3 | mc | 2 | Formelzeichen U |
| F4 | mc | 2 | Einheit Spannung |
| F5 | dropdown | 2 | Messgeräte |
| F6 | dropdown | 2 | Anschlussart |
| F7 | mc | 2 | Regel Reihenschaltung I |
| F8 | mc | 2 | Regel Reihenschaltung U |
| F9 | mc | 2 | Regel Parallelschaltung U |
| F10 | number | 2 | Berechnung Reihe I |
| F11 | number | 2 | Berechnung Parallel I |
| F12 | number | 3 | Berechnung Reihe U |
| F13 | number | 3 | Berechnung Parallel U |

### Stern 1 (★) – 12 Aufgaben, 30 P

| # | Typ | Punkte | Thema |
|---|-----|--------|-------|
| F1-F3 | dropdown | 6 | Definitionen |
| F4 | dropdown | 2 | Messgeräte-Zuordnung |
| F5-F6 | multicheck | 4 | Regeln (Mehrfachauswahl) |
| F7-F9 | number | 9 | Berechnungen I |
| F10-F12 | number | 9 | Berechnungen U + gemischt |

### Stern 2 (★★) – 9 Aufgaben, 30 P

| # | Typ | Punkte | Thema |
|---|-----|--------|-------|
| F1-F2 | text | 6 | Texteingabe Definitionen |
| F3-F4 | dropdown | 6 | Regeln-Zuordnung |
| F5-F7 | number | 9 | Berechnungen I + gemischt |
| F8-F9 | number/multi | 9 | Berechnungen U + gemischt |

### Stern 3 (★★★) – 14 Aufgaben, 52 P

| # | Typ | Punkte | Thema |
|---|-----|--------|-------|
| F1 | dropdown | 4 | Regeln-Zuordnung (verbal) |
| F2 | dropdown | 2 | Messgeräte |
| F3-F4 | multicheck | 6 | Regeln (nur verbal) |
| F5-F8 | number | 14 | Berechnungen I + Fehleranalyse |
| F9-F12 | number | 14 | Berechnungen U + Fehleranalyse |
| F13 | number | 6 | EXTREM: 5-Lampen I |
| F14 | multi-number | 6 | EXTREM: 5-Lampen U |

---

## ⚠️ Wichtige Hinweise

### Für Schüler
- Alle Antworten werden automatisch gespeichert
- Bei Problemen: Seite neu laden (Daten bleiben erhalten)
- Erst "Quiz abgeben" wenn fertig!
- QR-Code dem Lehrer zeigen

### Für Lehrkräfte
- Decoder auf eigenem Gerät öffnen (nicht auf Schüler-iPads)
- Nach jeder Stunde CSV exportieren
- Reset-Code nur bei technischen Problemen nutzen
- Bei Offline-Nutzung: Alle Geräte im selben WLAN

---

## 📅 Version

**Version:** 1.0  
**Erstellt:** Dezember 2024  
**Thema:** Elektrizitätslehre Klasse 8  
**Rahmenplan:** RP_PHYS_Gym_Ges_7_10 (MV)

---

## 🔗 Links

- **Quiz:** `index.html`
- **Decoder:** `decoder.html`
- **QR-Codes:** `qr-codes.html`

**GitHub:** `https://jpcrusius-hub.github.io/sciencesim/quiz/klasse8-elektrik/`
