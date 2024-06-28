---
blogpost: true
date: Dez 24, 2022
location: Klausur
category: Übung
tags: Übertragungsfunktion, DGL, Sägezahn, Fourierreihe
---

# Tiefpass mit Sägezahnspannung

Ein Messgerät mit einem Verzögerungsverhalten 1. Ordnung, also einem Tiefpassverhalten, und einer 3\,dB-Grenzfrequenz von $f_0 = 1\,\mathrm{MHz}$ soll im Folgenden charakterisiert werden. 

- Skizzieren Sie das elektronische Schaltbild des RC-Tiefpasses 1. Ordnung und leiten Sie die Differentialgleichung her. Wie erhalten Sie hieraus die Übertragungsfunktion

  $$G(jf) = \frac{1}{{1 + j \frac{f}{f_0}}}$$
  
  eines Tiefpasses? Geben Sie die Gleichung für den Amplituden- und Phasengang des Messgerätes an.

- Das Messgerät wird mit einer periodischen Sägezahnspannung mit einer Amplitude von $A = 10\,\mathrm V$ und einer Periodendauer von $T = 2\,\mathrm{\upmu s}$ beaufschlagt. Zerlegen Sie hierfür das in der Abbildung dargestellte Signal in eine Fourier-Reihe: Berechnen Sie die Fourier-Koeffizienten $a_0$, $a_k$ und $b_k$ für $k = 1,2,3$ und formulieren Sie die drei Eingangsspannungen $u_{e,k}(t)$.

```{figure} pictures/functions2.png
:class: .dark-light
---
height: 100px
---
Sägezahnsignal

```

- Berechnen Sie die drei zugehörigen Ausgangsspannungen und Phasen nachdem die drei Eingangssignale den Tiefpassfilter passiert haben. Skizzieren Sie das Amplitudenspektrum für Eingangs- und Ausgangssignale.

- Ein hochfrequentes sinusförmiges Störsignal mit einer Frequenz von $100\,\mathrm{MHz}$ liegt nun ebenfalls am Eingang ihres Messgerätes an. Sie können aber guten Gewissens eine Restamplitude von $1\%$ nach dem Tiefpassfilter tolerieren. Erfüllt ihr Messgerät diese Anforderung?
