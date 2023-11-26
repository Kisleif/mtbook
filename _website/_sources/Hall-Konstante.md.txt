---
blogpost: true
date: Oct 25, 2023
location: Zettel_4
category: Übung
tags: Lineare Regression, Mittelwert
---


# Hall-Konstante: Lineare Regression

Um die Hall-Konstante $A_\mathrm H$ eines neuen Werkstoffs zu bestimmen haben Sie eine Messreihe durchgeführt, bei welcher in bestimmten Arbeitspunkten jeweils Strom und Spannung an einem Hall-Element gemessen wurden. Unter Berücksichtigung der relevanten Konstanten – magnetische Flussdichte und Dicke des Hall-Elements – erhalten Sie die in nachfolgender Tabelle zusammengefassten $x-y$-Wertepaare:

| $x / (\mathrm{kV\cdot C/m^3})$ |  0,5  | 0,75  |  1,0  | 1,25  |  1,5  |
|-------------------------------|-------|-------|-------|-------|-------|
| $y/\mathrm{V}$                |  3,6  | 6,02  | 7,96  | 9,99  | 12,03 |


* Prüfen Sie anhand des Korrelationskoeffizienten wie stark die Messwerte gestreut sind:

$$r = \frac{\mathrm{cov}_{xy}}{s_x \cdot s_y} = \frac{\sum_{i=1}^N (x_i-\overline x)\cdot (y_i-\overline y)}{\sqrt{\sum_{i=1}^N (x_i-\overline x)^2} \cdot \sqrt{ \sum_{i=1}^N (y_i-\overline y)^2}}.$$

* Berechnen Sie die gesuchte Hall-Konstante $A_\mathrm H$, welche sich aus dem Regressionskoeffizienten der obigen Messwerte ergibt:

$$ m = \frac{N \cdot \sum_{i=1}^N (x_i y_i) - \sum_{i=1}^N x_i \sum_{i=1}^N y_i}{N \cdot x_i^2 - \left( \sum_{i=1}^N x_i\right)^2}.$$