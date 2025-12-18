# Hinweise für Lehrkräfte

## Vor dem Quiz

### Technische Vorbereitung
- [ ] `index.html` auf Schülergeräten öffnen (oder lokal speichern)
- [ ] `decoder.html` auf Lehrergerät bereitlegen
- [ ] Dokumentenkamera oder Webcam für QR-Scanning bereit

### Organisatorisches
- [ ] Sitzplan festlegen (P01-P30)
- [ ] Niveau pro Schüler festlegen oder freie Wahl erlauben
- [ ] Zeitrahmen kommunizieren

## Während des Quiz

### Typische Probleme
| Problem | Lösung |
|---------|--------|
| Browser schließt versehentlich | Quiz wird automatisch fortgesetzt |
| iPad geht in Standby | Einfach entsperren, Quiz läuft weiter |
| Timer läuft ab | Quiz wird automatisch abgegeben |

### Reset-Code
Falls ein Schüler neu starten muss: **3141**

## Nach dem Quiz

### QR-Code Scanning
1. `decoder.html` öffnen
2. Kamera wählen (Dokumentenkamera = beste Qualität)
3. Schüler zeigen nacheinander ihren QR-Code
4. Alternativ: Code manuell eingeben

### Datenexport
- CSV-Export enthält: Sitzplatz, Niveau, Punkte, Prozent, Note
- Import in Excel/LibreOffice für Notenverwaltung

## Häufige Fragen

**Q: Können Schüler schummeln?**
A: Der QR-Code enthält alle Antworten verschlüsselt. Nachträgliche Änderungen sind nicht möglich.

**Q: Was passiert bei Internetausfall?**
A: Kein Problem - das Quiz funktioniert komplett offline.

**Q: Kann ich die Aufgaben anpassen?**
A: Ja, im QUESTIONS-Array in index.html. Dann auch MAX_POINTS anpassen!

**Q: Wie lange werden Daten gespeichert?**
A: Im Browser (LocalStorage) bis manuell gelöscht oder Browser-Daten geleert werden.
