#!/bin/bash
# Build-Script für Schaltplan-SVGs
# Benötigt: pdflatex, pdftocairo (poppler-utils)

cd schaltplaene

for tex in *.tex; do
    name="${tex%.tex}"
    echo "Building $name..."
    pdflatex -interaction=nonstopmode "$tex" > /dev/null 2>&1
    pdftocairo -svg "${name}.pdf" "${name}.svg"
    rm -f "${name}.aux" "${name}.log" "${name}.pdf"
done

echo "Done! SVGs in schaltplaene/"
