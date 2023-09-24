# *Richtig* Messen

Wie messen wir *richtig* im Praktikum? In der ersten Vorlesung klären wir die wichtigsten Begrifflichkeiten eines Messsystems. Außerdem beginnen wir direkt mit einer kleinen Einführung in die Messunsicherheiten, damit ihr perfekt für den Praktikumsversuch vorbereitet seid. 

## Inhaltsverzeichnis

```{tableofcontents}
```

## Zusammenfassung

| Begriff | Beschreibung |
|:--------------------|:----------------------------------------|
|Messen|Ermittlung des Messwertes zu einer Messgröße. (Wie oft geht eine Einheit in eine Messgröße hinein?)|
|Maßeinheit|Festgelegter Vergleichswert für eine physikalische Messgröße|
|Messwert|Bei der Messung ermittelter Faktor. Zahlenmäßiges Verhältnis zwischen Einheit und Messgröße|
|Messgröße|Physikalische Größe, die Gegenstand einer Messung ist|
|Richtiger Wert|Mit denkbar größten technischem und theoretischem Aufwand ermittelter Messwert, der als Bezugswert zur Bewertung eines Messergebnisses benutzt wird. |
|Wahrer Wert|Tatsächlich vorhandener Wert einer physikalischen Größe, er ist durch eine endliche Genauigkeit der verwendeten Messmittel nicht exakt bestimbar. |
|SI-Einheitensystem|Vereinbartes System von Maßeinheiten|
|Dezibel|Logarithmisches Übertragungsmaß, dessen Zahlenwert mit einer vereinbarten Berechnungsvorschrift ermittelt wird.|
|Messsignal|Ein Signal mit dem Messinformationen transportiert werden|
|Messergebnis / Messwert | (Schätz-)Wert, den die Messgröße durch Auswertung einer Messung bekommt|
|Messreihe|Aufnahme von mehreren Messwerten von einem Messaufbau unter möglichst identischen Messbedingungen, d. h. unter Wiederholbedingungen. Die Messreihe wird zur statistischen Analyse und damit zur Bewertung der zufälligen Einflüsse auf ein Messergebnis benötigt.|
|Messabweichung|Differenz zwischen ermitteltem Messwert (Schätzwert der Messgröße) und dem richtigen Wert der Messgröße|
|Unsicherheit|Von zufälligen Einflüssen verursachte Abweichungen eines Messergebnisses (z.B. über Statistik abschätzen)|
|arithmetischer Mittelwert $\overline x$ | Schätzwert für den wahren Wert einer Messgröße aus einer Messreihe mit den Messwerten $x_j$ und der Anzahl der Messwerte $m$: $\overline x = \frac{1}{m}\sum_{j=1}^m x_j$|
|Erwartungswert|Mittelwert einer unendlichen Gesamtheit|
|Messunsicherheit $u(x)$ | Wichtiger Bestandteil zur Angabe eines Messergebnisses. Die Unsicherheit charakterisiert einen Vertrauensbereich, der der Messgröße zugeschrieben wird: $\overline x \pm u(x)$ |
|relative Messunsicherheit | Messunsicherheit dividiert durch den Betrag des Mittelwerts: $A_{r} = \frac{u(x)}{\lvert (\overline x)\rvert}$| 
|Varianz: mittlere quadratische Abweichung $s^2(x)$ | Beschreibt die quadratische Abweichung einer Zufallsvariable von dem Erwartungswert der betrachteten Gesamtheit. Ein Maß für die Messunsicherheit. $s^2 = \frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2$|
|Standardabweichung | In der Messtechnik auch als Streuung bezeichnet, sie ist die Quadratwurzel aus der von zufälligen Einflüssen verursachte Abweichung eines Messergebnisses (Wurzel der Varianz). Wurzel aus der mittleren quadratischen Abweichung:  $s = \sqrt{\frac{1}{m-1} \sum_{j=1}^m (x_j - \overline x)^2}$ |
|empirische Varianz $\sigma^2(x)$ | Schätzung der Varianz bezogen auf den *wahren* Wert (nicht auf den Mittelwert der Messreihe) der Messgröße: $\sigma^2 = \lim_{m\rightarrow \infty}\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2$|
|empirische Standardabweichung $\sigma(x)$ | Wurzel aus der empirischen Varianz: $\sigma = \lim_{m\rightarrow \infty}\sqrt{\frac{1}{m} \sum_{j=1}^m (x_j - \mu)^2}$|
|Kalibrieren|Untersuchen, ob der Prüfgegenstand bestimmte Bedingungen erfüllt (Entspricht der Messwert eines Messgeräts dem „richtigen“ Wert des Messgröße?)|
|Eichen|Prüfung und Stempelung des Messsystems nach Eichvorschriften (Entspricht der Messwert eines Messgeräts dem „richtigen“ Wert des Messgröße unter staatlicher Hoheit?)|
|Justieren|Einstellen eines Messsystems so, dass der Messwert der Messgröße möglichst gut entspricht|
|Normale|Eine handhabbare Verkörperung einer Maßeinheit|
|Korrektur|Von der systematischen Abweichung abgeleiteter Korrekturwert zur Berichtigung eines Schätzwertes einer Messgröße.|
|Genauigkeitsklasse|Von den Fehlergrenzen abgeleitete Genauigkeitsangabe für Messeinrichtungen.|
|Korrelation|Maß für die lineare Korrelation zweier Messgrößen!|
|Wahrscheinlichkeitsverteilung $dP(x)$ | eine Funktion, die die Wahrscheinlichkeit angibt, dass eine Messgröße $x$ durch Messung einen bestimmten Wert $x_j + dx$ annehmen wird.| 
|Interpolation | Analytische Kennlinie läuft exakt durch alle Messpunkte und wird beispielsweise unter Verwendung von Polynomen bestimmt. |
|Regression | statistisches Analyseverfahren zur Feststellung funktionaler Beziehungen zwischen einer abhängigen und einer oder mehreren unabhängigen Variablen (Untersuchung von Korrelationen) |
| Anpassung| Wie Regression, aber unter Berücksichtigung von Messfehlern (Fehlerbalken) |
| Approximation | Kennlinienannäherung mittels Linearkombination geeigneter analytischer Basisfunktionen (beispielsweise durch Fourier-Reihen, siehe kommende Kapitel (Regression und Anpassung sind Approximationen)|
|Bestimmtheitsmaß | Das Bestimmtheitsmaß, auch Determinationskoeffizient (von lateinisch determinatio „Abgrenzung, Bestimmung“ bzw. determinare „eingrenzen“, „festlegen“, „bestimmen“ und coefficere „mitwirken“), R2, ist in der Statistik eine Kennzahl zur Beurteilung der Anpassungsgüte einer Regression – beispielsweise, um zu bewerten, wie gut Messwerte zu einem Modell passen. Das Bestimmtheitsmaß beruht auf der Quadratsummenzerlegung, bei der die totale Quadratsumme in die (durch das Regressionsmodell) erklärte Quadratsumme und in die Residuenquadratsumme zerlegt wird.|
| Methode der kleinsten Quadrate | ist das mathematische Standardverfahren zur Ausgleichungsrechnung. |
| Residuenquadratsumme | Die Residuenquadratsumme, Quadratsumme der Residuen, oder auch Summe der Residuenquadrate, bezeichnet in der Statistik die Summe der quadrierten (Kleinste-Quadrate-)Residuen (Abweichungen zwischen Beobachtungswerten und den vorhergesagten Werten) aller Beobachtungen |


```{bibliography}
:filter: docname in docnames
```