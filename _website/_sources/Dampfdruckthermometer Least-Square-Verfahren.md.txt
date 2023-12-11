---
blogpost: true
date: Oct 25, 2023
location: Zettel_4
category: Übung
tags: Lineare Regression, Least-Square
---


# Dampfdruckthermometer Least-Square-Verfahren

Mit dem Dampfdruckthermometer kann die Temperatur aus dem Dampfdruck einer Flüssigkeit bestimmt werden. Die Flüssigkeit wird mit der Messstelle in einen thermischen Kontakt gebracht. Der Dampfdruck nimmt mit der Temperatur der Flüssigkeit beschleunigt zu und kann durch folgende Exponentialfunktion beschrieben werden:

$$ p_\mathrm{D}(T) = c \cdot \mathrm{e}^{-\frac{\Delta E}{kT}} $$

wobei $c$ eine Konstante ist, $k = 1{,}380649\cdot 10^{-23}\,\mathrm{J/K}$ die Boltzmann-Konstante und $\Delta E$ die Verdampfungsenergie eines Moleküls. Durch Logarithmieren beider Seiten erhält man die äquivalente logarithmische Darstellung

$$\ln{p_\mathrm{D}} = A - B/T$$

mit den Materialkonstanten $A$ und $B$. 

```{figure} pictures/dampfdruck.png
---
height: 100px
name: dampfdruck_ls
---
Kennlinie eines Dampfdruckthermometers
```


Bei der Least-Sqaure-Methode werden die Parameter (hier: $A$, $B$) wie folgt bestimmt:

$$b = A^{-1} \cdot y$$


Der Parametervektor $b$ bestimmt sich aus der Inversen der Funktionsmatrix $A$ und dem Messvektor $y$. Die Matrix $A$ enthält die Werte der Ansatzfunktion an den Messpunkten. Der Vektor $y$ enthält die Messwerte an den Stützstellen.

1. Bestimmen Sie die Materialkonstanten $A$, $B$ und $\Delta E$, $c$ mittels der Least-Square-Methode mit 3 Stützstellen.
1. Bestimmen Sie die Materialkonstanten $A$, $B$ und $\Delta E$, $c$ mittels der Least-Square-Methode mit 2 Stützstellen.

Hinweis: Um eine nicht quadratische Matrix zu invertieren, bilden Sie die Pseudoinverse $A^+$ der Matrix $A$:

$$A^+ = \left( A^T \cdot A\right)^{-1} \cdot A^T$$