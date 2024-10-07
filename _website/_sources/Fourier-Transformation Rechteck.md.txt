---
blogpost: true
date: Nov 01, 2023
location: Zettel_5
category: Übung
tags: Fourier-Transformation, Rechteck
---


# Fourier-Transformation Rechteck

Gegeben ist die folgenden Zeitfunktionen $x(t)$:

```{figure} pictures/FT_rechteck.png
:class: .dark-light
---
height: 100px
---
Rechteckimplus $x(t)$ mit einer Amplitude $\hat x = 1$.

```

Berechnen Sie die Spektralfunktion $X(f)$ von $x(t)$ durch Anwendung der Rechenregeln der Fourier-Transformation.

Die Fourier-Transformation berechnet sich über: 

$$X(\omega) = \int_{-\infty}^{\infty} x(t) \mathrm e^{-j\omega t} dt$$