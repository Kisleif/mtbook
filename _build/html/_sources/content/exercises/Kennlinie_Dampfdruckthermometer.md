---
title: "Kennlinie eines Dampfdruckthermometers"
keywords:
  - Übung
  - Messtechnik
  - Kennlinie
  - Empfindlichkeit
...

# Kennlinie eines Dampfdruckthermometers

Mit dem Dampfdruckthermometer kann die Temperatur aus dem Dampfdruck einer Flüssigkeit bestimmt werden. Die Flüssigkeit wird mit der Messstelle in einen thermischen Kontakt gebracht. Der Dampfdruck nimmt mit der Temperatur der Flüssigkeit beschleunigt zu und kann durch folgende Exponentialfunktion beschrieben werden:

$$p_\mathrm{D}(T) = c \cdot \mathrm{e}^{-\frac{\Delta E}{kT}}$$

wobei $k = 1,380649\cdot 10^{-23}\,\mathrm{J/K}$ eine Konstante ist,  die Boltzmann-Konstante und $\Delta E$ die Verdampfungsenergie eines Moleküls. Durch Logarithmieren beider Seiten erhält man die äquivalente logarithmische Darstellung

$$\ln{p_\mathrm{D}} = A - B/T$$

mit den Materialkonstanten $A$ und $B$. 

Bei richtiger Anpassung der Flüssigkeit an den zu messenden Temperaturbereich können sehr hohe Empfindlichkeiten erreicht werden, so dass die erforderliche Druckmessung mit einfachen Mitteln (beispielsweise einem Quecksilbermanometer) ausgeführt werden kann.

![Links: Kennlinie für den Temperaturbereich 0-300°C. Rechts: Kennlinie für den Temperaturbereich -20-60°C.](./pictures/Kennlinie_Dampfdruckthermometer.png)


## Aufgabe 1: Materialkonstanten bestimmen
Bestimmen Sie mithilfe der Abbildung die Materialkonstanten $A$, $B$ und $\Delta E$, $c$ für Wasser.

## Aufgabe 2: Empfindlichkeit des Dampfdruckthermometers für Wasser
Bestimmen Sie die Empfindlichkeit bei den Temperaturen 20°C und 200°C (gerundetes Zwischenergebnis aus (a): $A=13$ , $B = 4882\,\mathrm K$ ). Recherchieren Sie, welche Flüssigkeiten anstelle von Wasser sich für tiefe Temperaturen (<100 K) eignen. Welche Empfindlichkeit erreicht ein Helium-Dampfdruckthermometer bei 1K ( $A_\mathrm{He} = 2$ und $B_\mathrm{He} = 2,5\,\mathrm{K}$ ) und ein Neon-Dampfdruckthermometer bei 20K ( $A_\mathrm{O2} = 4,6$ und $B_\mathrm{O2} = 106\,\mathrm{K}$)?

## Aufgabe 3: Empfindlichkeit des Dampfdruckthermometers 
Das Wasser-Dampfdruckthermometer besteht aus einem Gefäß mit einem Volumen von 1 Liter und einer Druckfestigkeit von 50 bar. Aus Sicherheitsgründen wird beim Bau des Thermometers nur soviel Flüssigkeit eingefüllt, dass bei einer Temperatur von 250°C die ganze Flüssigkeit verdampft ist. Welche Flüssigkeitsmenge wird demnach eingebracht? 

## Aufgabe 4: Übergang zum Gasthermometer
Können Sie mit diesem Thermometer auch noch eine Temperatur von 300°C messen? Wenn ja, wie und mit welcher Empfindlichkeit? Skizzieren Sie die Kennlinie für den Temperaturbereich 250°C-350°C (gerundetes Zwischenergebnisse aus (c): $N = 6\cdot 10^{23}$, $V = 17\,\mathrm{ml}$).
Hinweis zu (c) und (d): Ein Gasthermometer misst Druck  und Volumen. Wie lautet die Zustandsgleichung für ideale Gase? In einem abgeschlossenen System wird sich das Volumen nicht ändern. 
