#!/usr/bin/env python3
"""
Scannt alle info.md Dateien und generiert simulations.json
"""
import os
import json
import yaml
import re
from pathlib import Path

def parse_info_md(filepath):
    """Liest info.md und extrahiert YAML-Header"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # YAML-Header zwischen --- ... --- extrahieren
    match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None
    
    try:
        data = yaml.safe_load(match.group(1))
        return data
    except yaml.YAMLError:
        return None

def find_materials(folder):
    """Findet alle Begleitmaterialien im Ordner"""
    materials = []
    for file in os.listdir(folder):
        if file.endswith('.html') and file != 'index.html':
            # Titel aus Dateinamen ableiten
            name = file.replace('.html', '').replace('-', ' ').replace('_', ' ')
            name = ' '.join(word.capitalize() for word in name.split())
            materials.append({
                'datei': file,
                'titel': name
            })
        elif file.endswith('.pdf'):
            name = file.replace('.pdf', '').replace('-', ' ').replace('_', ' ')
            name = ' '.join(word.capitalize() for word in name.split())
            materials.append({
                'datei': file,
                'titel': name
            })
    return materials

def main():
    root = Path('.')
    simulations = []
    
    # Erlaubte Fächer/Kategorien (inkl. Tools)
    ERLAUBTE_FAECHER = ['physik', 'chemie', 'informatik', 'tools']
    
    # Alle info.md Dateien finden
    for info_path in root.rglob('info.md'):
        folder = info_path.parent
        
        # Nur in Fach-Unterordnern
        parts = folder.parts
        if len(parts) < 2:
            continue
        
        fach = parts[0]
        if fach not in ERLAUBTE_FAECHER:
            continue
        
        # info.md parsen
        data = parse_info_md(info_path)
        if not data:
            print(f"Warnung: Konnte {info_path} nicht parsen")
            continue
        
        # Prüfen ob index.html existiert
        if not (folder / 'index.html').exists():
            print(f"Warnung: Keine index.html in {folder}")
            continue
        
        # Pfad relativ zum Root
        rel_path = str(folder) + '/'
        
        # Materialien finden
        materials = find_materials(folder)
        
        # Simulation-Objekt erstellen
        sim = {
            'pfad': rel_path,
            'titel': data.get('titel', folder.name),
            'fach': data.get('fach', fach.capitalize()),
            'thema': data.get('thema', ''),
            'unterthema': data.get('unterthema', ''),
            'klassenstufe': data.get('klassenstufe', ''),
            'kurzbeschreibung': data.get('kurzbeschreibung', ''),
            'stichworte': data.get('stichworte', []),
            'materialien': materials
        }
        
        simulations.append(sim)
        print(f"Gefunden: {sim['titel']} ({rel_path})")
    
    # Nach Fach und Thema sortieren
    simulations.sort(key=lambda x: (x['fach'], x['thema'], x['titel']))
    
    # JSON schreiben
    output = {
        'generiert': True,
        'anzahl': len(simulations),
        'simulationen': simulations
    }
    
    with open('simulations.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ simulations.json erstellt mit {len(simulations)} Simulation(en)")

if __name__ == '__main__':
    main()
