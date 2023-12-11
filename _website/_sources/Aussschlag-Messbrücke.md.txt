---
blogpost: true
date: Dec 11, 2023
category: Übung
location: Zettel_10
tags: Widerstand, Messbrücke, Elektronik, Sensor, Empfindlichkeit
---


# Aussschlagsmessbrücke

Gegeben ist eine Ausschlagmessbrücke bestehend aus den beiden Spannungsteilern $R_1$ und $R_2$, bzw. $R_3$ und $R_4$.

```{figure} pictures/MB_1.png
:class: .dark-light
---
height: 150px
---
Messbrücke
```


## Aufgabe 1: Diagonalspannung

Berechnen Sie die Diagonalspannung $U_d$ einer Ausschlag-Messbrücke.

```{tip}
:class: dropdown
* Schreiben Sie die beiden Spannungsteiler-Gleichungen auf
* Subtrahieren Sie die beiden Spannungswerte, z.B. $U_d = U_2-U_4$
```

## Aufgabe 2: Sensor

Mit der Brücke soll die Widerstandsänderung $\Delta R$ eines Sensors, gegeben durch $R_2 = R_x = R_0 + \Delta R + \Delta R_T$ (Temperaturfehler $\Delta R_T$) erfasst werden. Die anderen Brückenwiderstände sind mit $R_0$ anzunehmen. 

* Skizzieren Sie die Schaltung
* Berechnen Sie $U_d = f(U_0, \Delta R, \Delta R_T, R_0)$.

```{tip}
:class: dropdown
* Ersetzen Sie $R_2$ in der Gleichung von Aufgabe 1, sowie alle anderen Widerstände durch $R_0$ und vereinfachen Sie die Gleichung für $U_d$.
```

## Aufgabe 3: Temperaturkompensation

Die Temperaturabhängigkeit $\Delta R_T$ soll verringert werden. Hierzu steht Ihnen ein Widerstand mit identischem Temperaturverhalten zur Verfügung: $R_K = R_0 + \Delta R_T$. Zeigen Sie, dass mit Hilfe von $R_K$ der Einfluss von $\Delta R_T$ stark reduziert werden kann. Gehen Sie folgendermaßen vor: 

* Geben Sie eine geeignete Brückenschaltung an.
* Berechnen Sie $U_d = f(U_0, \Delta R, \Delta R_T, R_0)$.(Zwischenergebnisse sind im nächsten Punkt angegeben.)
* Berechnen Sie die Empfindlichkeit in Abhängigkeit von $\Delta R_T$ für die beiden Fälle mit und ohne $R_K$.

$$E_{1}  = \frac{dU_d}{d\Delta R_T} \quad \textrm{mit} \quad U_d = \frac{U_0}{2} \cdot \frac{\Delta R + \Delta R_T}{2R_0 + \Delta R + \Delta R_T} \quad \textrm{ohne} \quad R_{K}$$
$$E_2 = \frac{dU_d}{d\Delta R_T} \quad \textrm{mit} \quad U_d = \frac{U_0}{2} \cdot \frac{\Delta R}{2R_0 + \Delta R + 2\Delta R_T} \quad \textrm{mit} \quad R_{K}$$

* Bilden Sie den Quotienten aus beiden Resultaten, $\frac{E_{1}}{E_{2}}$ und nähern Sie für $\Delta R_{T} << R_{0}$.

```{tip}
:class: dropdown
* Setzen Sie $R_K$ an die Stelle von $R_1$, also in den gleichen Spannungsteiler.
* Die Empfindlichkeit berechnen Sie über die Ableitung, hier die Ableitung nach $d \Delta R_T$, wenn Sie die Empfindlichkeit für $\Delta R_T$ haben möchten. 
```

* Setzen Sie Beispielwerte ein:

$$R_0 = 1\,\mathrm{k\Omega}$$

$$\Delta R = 100\,\mathrm\Omega$$

$$\Delta R_T = 0-1000\,\mathrm\Omega$$

$$U_0 = 10\,\mathrm V$$


```{admonition} Kontrollergebnisse
:class: dropdown
* Diagonalspannung allgemein:

$$\frac{U_d}{U_0} = U_2 - U_4 = \frac{R_2}{R_1+R_2} - \frac{R_4}{R_3+R_4}$$

* Diagonalspannung mit Sensor bei $R_2 = R_x = R_0 + \Delta R + \Delta R_T$ und Empfindlichkeit E_1$:

$$U_d = \frac{U_0}{2} \cdot \frac{\Delta R + \Delta R_T}{2R_0 + \Delta R + \Delta R_T}$$

$$E_1 = \frac{dU_d}{d\Delta R_T} = \frac{U_0}{2} \frac{2R_0}{(2R_0 + \Delta R + \Delta R_T)^2}$$

* Diagonalspannung mit Sensor bei $R_2 = R_x = R_0 + \Delta R + \Delta R_T$ und Korrekturwiderstand gegen Temperaturänderungen, $R_1 = R_K$ und Empfindlichkeit $E_2$:

$$U_d = \frac{U_0}{2} \cdot \frac{\Delta R}{2R_0 + \Delta R + 2\Delta R_T}$$

$$  = \frac{U_0}{2} \frac{-2\Delta R}{(2R_0 + \Delta R + \Delta 2R_T)^2}$$

* Verhältnis: Wir nehmen an, dass der Fehler aufgrund von Temperatur, $\Delta R_T$, klein im Vergleich zum Widerstandswert $R_0$ ist, sodass $2 \Delta R_T \approx \Delta R_T$. Dadurch kürzt sich der Nenner weg, wenn die beiden Empfindlichkeiten ins Verhältnis gesetzt werden und es folgt:

$$r \approx -\frac{R_0}{\Delta R} = \frac{10000}{100} = 100$$

Die Möglichkeit Temperatur zu unterdrücken wird hauptsächlich durch die Wahl von den nominellen Widerstandswerten $R_0$ bestimmt, die in der Brücke verbaut sind, und der zu messenden Größe $\Delta R$. Je größer der Abstand zwischen $R_0$ und $\Delta R$, desto besser ist die Rauschunterdrückung. 
```