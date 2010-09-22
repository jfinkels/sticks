#!/bin/sh

pdflatex sticks && bibtex sticks && pdflatex sticks && pdflatex sticks

exit 0
