#!/usr/bin/env python
# coding: utf-8

# # Daten analysieren und präsentieren
# 
# Viele Studierende sammeln im Praktikum erstmals Erfahrung im Umgang mit Messdaten, nehmen eigene Messreihen auf und müssen diese begründbar und nachvollziehbar auswerten und darstellen. Im Studium, z.B. im Rahmen von Semester-, Abschluss- oder sogar Promotionsarbeiten müssen Analyse und Präsentation wissenschaftlich und sachgerecht sein. Auf den folgenden Seiten findet ihr das absolute Minimum an notwendigen Hilfsmitteln, Grundideen und Praktiken, die ihr bei der Auswertung von Messdaten im Praktikum berücksichtigen solltet! 
# 
# ```{tableofcontents}
# ```

# ## Zusammenfassung
# 
# | Begriff | Beschreibung |
# |:--------------------|:----------------------------------------|
# |Messgröße | die spezielle Größe der Messung, $x$ |
# |Wahrer Wert | tatsächlich vorhandener Wert einer Messgröße, dessen Wert niemals bekannt sein wird. |
# |Messergebnis | (Schätz-)Wert, den die Messgröße durch Auswertung einer Messung bekommt|
# |arithmetischer Mittelwert $\overline x$ | Schätzewert für den wahren Wert einer Messgröße aus einer Messreihe mit den Messwerten $x_j$ und der Anzahl der Messwerte $m$: $\overline x = \frac{1}{m}\sum_{j=1}^m x_j$|
# |Messunsicherheit $u(x)$ | Wichtiger Bestandteil zur Angabe eines Messergebnisses. Die Unsicherheit charakterisiert einen Vertrauensbereich, der der Messgröße zugeschrieben wird: $\overline x \pm u(x)$ |
# |relative Messunsicherheit | Messunsicherheit dividiert durch den Betrag des Mittelwerts: $A_{r} = \frac{u(x)}{|(\overline x)|}$| 
# |Varianz: mittlere quadratische Abweichung $s^2(x)$ | Ein Maß für die Messunsicherheit. Abweichung der Messwerte zum Mittelwert werden quadriert und gemittelt: $s^2 = \frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2$|
# |Standardabweichung | Wurzel aus der mittleren quadratischen Abweichung:  $s = \sqrt{\frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2}$ |
# |empirische Varianz $\sigma(x)^2$ | Schätzung der Varianz bezogen auf den *wahren* Wert (nicht auf den Mittelwert der Messreihe) der Messgröße: $\sigma^2 = \lim_{m\rightarrow \infty}\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2$|
# |empirische Standardabweichung $\sigma(x)$ | Wurzel aus der empirischen Varianz: $\sigma = \lim_{m\rightarrow \infty}\sqrt{\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2}$|
# |Wahrscheinlichkeitsverteilung $dP(x)$ | eine Fukntion, die die Wahrscheinlichkeit angibt, dass eine Messgröße $x$ durch Messung einen bestimmten Wert $x_j + dx$ annehmen wird.| 
