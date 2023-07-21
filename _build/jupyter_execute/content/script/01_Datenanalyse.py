#!/usr/bin/env python
# coding: utf-8

# # Messabweichung
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
# |Wahrer Wert | Tatsächlich vorhandener Wert einer physikalischen Größe, er ist durch eine endliche Genauigkeit der verwendeten Messmittel nicht exakt bestimmbar. |
# |Richtiger Wert|Mit denkbar größtem technischem und theoretischem Aufwand ermittelter Messwert, der als Bezugswert zur Bewertung eines Messergebnisses benutzt wird. |
# |Messergebnis / Messwert | (Schätz-)Wert, den die Messgröße durch Auswertung einer Messung bekommt|
# |Messreihe|Aufnahme von mehreren Messwerten von einem Messaufbau unter möglichst identischen Messbedingungen, d. h. unter Wiederholbedingungen. Die Messreihe wird zur statistischen Analyse und damit zur Bewertung der zufälligen Einflüsse auf ein Messergebnis benötigt.|
# |Messabweichung|Differenz zwischen ermitteltem Messwert (Schätzwert der Messgröße) und dem richtigen Wert der Messgröße|
# |Unsicherheit|Von zufälligen Einflüssen verursachte Abweichungen eines Messergebnisses (z.B. über Statistik abschätzen)|
# |arithmetischer Mittelwert $\overline x$ | Schätzwert für den wahren Wert einer Messgröße aus einer Messreihe mit den Messwerten $x_j$ und der Anzahl der Messwerte $m$: $\overline x = \frac{1}{m}\sum_{j=1}^m x_j$|
# |Erwartungswert|Mittelwert einer unendlichen Gesamtheit|
# |Messunsicherheit $u(x)$ | Wichtiger Bestandteil zur Angabe eines Messergebnisses. Die Unsicherheit charakterisiert einen Vertrauensbereich, der der Messgröße zugeschrieben wird: $\overline x \pm u(x)$ |
# |relative Messunsicherheit | Messunsicherheit dividiert durch den Betrag des Mittelwerts: $A_{r} = \frac{u(x)}{\lvert (\overline x)\rvert}$| 
# |Varianz: mittlere quadratische Abweichung $s^2(x)$ | Beschreibt die quadratische Abweichung einer Zufallsvariable von dem Erwartungswert der betrachteten Gesamtheit. Ein Maß für die Messunsicherheit. $s^2 = \frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2$|
# |Standardabweichung | In der Messtechnik auch als Streuung bezeichnet, sie ist die Quadratwurzel aus der von zufälligen Einflüssen verursachte Abweichung eines Messergebnisses (Wurzel der Varianz). Wurzel aus der mittleren quadratischen Abweichung:  $s = \sqrt{\frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2}$ |
# |empirische Varianz $\sigma^2(x)$ | Schätzung der Varianz bezogen auf den *wahren* Wert (nicht auf den Mittelwert der Messreihe) der Messgröße: $\sigma^2 = \lim_{m\rightarrow \infty}\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2$|
# |empirische Standardabweichung $\sigma(x)$ | Wurzel aus der empirischen Varianz: $\sigma = \lim_{m\rightarrow \infty}\sqrt{\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2}$|
# |Wahrscheinlichkeitsverteilung $dP(x)$ | eine Funktion, die die Wahrscheinlichkeit angibt, dass eine Messgröße $x$ durch Messung einen bestimmten Wert $x_j + dx$ annehmen wird.| 
# |Korrektur|Von der systematischen Abweichung abgeleiteter Korrekturwert zur Berichtigung eines Schätzwertes einer Messgröße.|
# |Genauigkeitsklasse|Von den Fehlergrenzen abgeleitete Genauigkeitsangabe für Messeinrichtungen.|
# |Korrelation|Maß für die lineare Korrelation zweier Messgrößen!|

# :::{figure-md} zusammenfassung_abw
# <img src="draw/zusammenfassung_abw.jpg" alt="zusammenfassung_abw" width="600px" label = zusammenfassung_abw>
# 
# Korrektur und Angabe des Messergebnisses
# :::
