#!/bin/bash

INFORME="./informe.tex"
PRESENTACION="./presentacion.tex"

if [ -f "$INFORME" ]; then
	pdflatex "$INFORME"
	rm informe.aux informe.toc informe.log
fi

if [ -f "$PRESENTACION" ]; then
	ipdflatex "$PRESENTACION"
	rm presentacion.toc presentacion.log presentacion.aux
fi



