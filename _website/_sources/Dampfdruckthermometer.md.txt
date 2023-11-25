---
blogpost: true
date: Oct 18, 2023
category: Übung
location: Zettel_3
tags: Kennlinie, Empfindlichkeit
---

# Dampfdruckthermometer

Mit dem Dampfdruckthermometer kann die Temperatur aus dem Dampfdruck einer Flüssigkeit bestimmt werden. Die Flüssigkeit wird mit der Messstelle in einen thermischen Kontakt gebracht. Der Dampfdruck nimmt mit der Temperatur der Flüssigkeit beschleunigt zu und kann durch folgende Exponentialfunktion beschrieben werden:

$$ p_\mathrm{D}(T) = c \cdot \mathrm{e}^{-\frac{\Delta E}{kT}} $$

wobei $c$ eine Konstante ist, $k = 1{,}380649\cdot 10^{-23}\,\mathrm{J/K}$ die Boltzmann-Konstante und $\Delta E$ die Verdampfungsenergie eines Moleküls. Durch Logarithmieren beider Seiten erhält man die äquivalente logarithmische Darstellung

$$\ln{p_\mathrm{D}} = A - B/T$$

mit den Materialkonstanten $A$ und $B$. 
Bei richtiger Anpassung der Flüssigkeit an den zu messenden Temperaturbereich können sehr hohe Empfindlichkeiten erreicht werden, so dass die erforderliche Druckmessung mit einfachen Mitteln (beispielsweise einem Quecksilbermanometer) ausgeführt werden kann.

```{figure} pictures/dampfdruck.png
---
height: 100px
name: dampfdruck
---
Kennlinie eines Dampfdruckthermometers

```

* Bestimmen Sie mithilfe der Abbildung die Materialkonstanten $A$, $B$  und $\Delta E$, $c$ für Wasser.
* Bestimmen Sie die Empfindlichkeit bei den Temperaturen 20°C und 200°C. 
* Welche Empfindlichkeit erreicht ein Helium-Dampfdruckthermometer bei 1K ($A_\mathrm{He} = 2$ und $B_\mathrm{He} = 2{,}5\,\mathrm{K}$) und ein Neon-Dampfdruckthermometer bei 20K ($A_\mathrm{O2} = 4{,}6$ und $B_\mathrm{O2} = 106\,\mathrm{K}$)?