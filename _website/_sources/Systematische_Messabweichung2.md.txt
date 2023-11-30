---
blogpost: true
date: Nov 29, 2023
category: Übung
tags: Systematisch, Stromrichtig, Spannungsrichtig, Messabweichung, Elektronik
---


# Systematische Messabweichung II
Zwei unbekannte Widerstände $R$ im $\mathrm{k\Omega}$-Bereich werden mit zwei Messschaltungen bestimmt:

```{figure} pictures/strom_spannungsrichtig.png
:class: .dark-light
---
height: 150px
name: optional-label
---
Schaltungen zur Bestimmung von Widerständen nach $R = U/I$

```

* Welches Schaltbild stellt die stromrichtige und welche die spannungsrichtige Schaltung dar?
* Berechnen Sie für beide Fälle den wahren ($R$) und den gemessenen ($R'$) Widerstandswert. 
* Berechnen Sie für beide Fälle den systematischen absoluten und relativen Fehler in Abhängigkeit von $R$ und den Innenwiderständen $R_{A}$ und $R_{V}$ der Messgeräte. 
* Zeichnen Sie den Betrag der Fehler in ein Diagramm in Abhängigkeit von $R$ für beide Fälle. Für welche Grenzwerte von $R$ sollte man strom- bzw. spannungsrichtig messen? Setzen Sie $R_{A} = 10\,\mathrm \Omega$ und $R_{V} = 20\,\mathrm{k\Omega}$.


````{admonition} Ergebnisse
:class: dropdown

| Messung | wahrer Wert $R$ | gemessener Wert $R'$ |
| --------|-----------------|----------------------|
| stromrichtig | $R = \frac{U_R}{I} = R'-R_A$ | $R' = \frac{U}{I} = R+R_A$ |
spannungsrichtig | $R = \frac{U}{I_R} = \frac{R'R_V}{R_V-R'}$ | $R' = \frac{U}{I} = \frac{RR_V}{R+R_V}$

| Messung | absoluter Fehler | relativer Fehler |
| --------|-----------------|----------------------|
| stromrichtig | $R'-R = R_A$ | $\frac{R'-R}{R} = \frac{R_A}{R} $
| spannungsrichtig | $R'-R = -\frac{R^2}{R+R_V}$ | $\frac{R'-R}{R} = -\frac{R}{R+R_V} $

* stromrichtig: $R' = R+R_A \approx R$ wenn $R >> R_A$
* spannungsrichtig: $\frac{1}{R'} = \frac{1}{R} + \frac{1}{R_V} \approx \frac{1}{R}$ für $\frac{1}{R} >> \frac{1}{R_V}$ bzw. $R << R_V$

* für die Grenze gleichsetzen... 

$$R = \frac{R_{A}}{2} + \sqrt{\frac{R_{A}^2}{4} \cdot R_A R_V} = ... = 452{,}24\,\Omega $$
````

