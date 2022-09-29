#!/usr/bin/env python
# coding: utf-8

# # Impuls- und Sprungantwort
# <a id="SubSec-white_box"></a>
# 
# Bei dem Prinzip der black box kenne ich das Innenleben meines Messsystems nicht, und ich kann lediglich mittels Messungen darauf zurück schließen. Je nachdem, welches Signal an den Eingang angelegt wird, erhalte ich ein andere Ausgangssignal. Dies ist in den beiden Bildern aus dem vorausgegangenen Kapitel deutlich zu erkenne. In einem Fall wurde ein Sprung angelegt, im anderen Fall ein Impuls. 
# 
# 

# ## Impulsantwort und Faltung im Zeitraum
# <a id="SubSubSec-Impulsantwort_und_Faltung"></a>
# 
# In diesem Abschnitt wollen wir uns der Genialität der Impulsantwort in Kombination mit der Faltung widmen. 
# Hierfür müssen wir uns zuerst angucken, was *Faltung* überhaupt bedeutet. 
# 
# Die **Faltung** ist eine mathematische Operation, welche zwischen zwei Funktionen $f$ und $g$ ausgeführt werden kann. Die Kurzschreibweise ist das Sternchen zwischen den beiden Funktionen. Allgemein berechnet wird sie über ein Integral, welches die beiden Funktionen beinhaltet, wobei $g$ hierbei zeitlich gespiegelt und verschoben wird. 
# 
# $$(f \ast g)(t) = \int_{-\infty}^{\infty} f(\tau)g(t-\tau) \mathrm{d}\tau$$
# 
# Die resultierende „Überlagerung“ zwischen $f$ und gespiegelten und verschobenen Versionen von $g$ (man spricht auch von einer „Verschmierung“ von $f$) kann z. B. verwendet werden, um einen gleitenden Durchschnitt zu bilden.
# Das Faltungsintegral kann in drei Schritten verstanden werden:
# 
# 1. der Eingang $g$ wird in der Zeit umgekehrt and zeitverschoben
# 2. Dieses umgekehrte und verschobene $g$ wird nun an $f$ multipliziert
# 3. Und dann wird das Produkt über alle Zeiten summiert (Integralbildung).
# 
# Für viele Funktionen wurde das Faltungsintegral bereits bestimmt, da es sehr aufwendig ist, dieses i.Allg. zu lösen. 
# Das Integral zu lösen hilft außerdem kaum dabei genau zu verstehen, was das Integral, bzw. die Faltung, an sich überhaupt bedeutet. Die Faltung kann auch grafisch bestimmt werden, was wir uns in einer Übung einmal genauer ansehen werden. 
# 
# Das interessante der Faltung ist jedoch, dass wir durch diese mathematische Operation das Systemverhalten oder Ausgangssignale vorhersagen können, solange die Impulsantwort bekannt ist. Man kann sich das vereinfacht so vorstellen, dass eine beliebige Eingangsfunktion $f(t)$ durch undendliche viele *Impulse* beschrieben werden, mit infinitesimal kleiner Breite $dt$. Die Impulsantwort ist für einen Impuls (Delta-Peak) bekannt: sie ist die zeitverschobene Antwort $g(t-dt)$. Die Überlagerung vieler einzelner Impulse, eine beliebige Eingangsfunktion $f(t)$ zu modellieren, ist einfach die Aussummerierung aller Impulse. In einem LZI System ist die Impulsantwort ebenfalls die Aufsummerierung der Impulsantworten zu den zugehörigen Impulsen (*Linearitätsbedingung*). 
# Um den *realen* Werteverlauf der Eingangsfunktion sicher zu stellen, muss jeder Delta-Peak für jedes Zeitintervall mit dem Funktionswert skaliert werden.
# Die *Homogenitätsbedingung* stellt jetzt sicher, dass wir den Ausgang auch entsprechend skalieren dürfen. 
# Mathematisch betrachtet resultiert dies direkt darin, dass wir Antworten von beliebigen Anregungsfunktionen hervorsagen können, indem die Anregungsfunktion $f(t)$ mit der Impulsantwort gefaltet wird. 
# 
# ![Bild](pictures/faltung_zeit.png)
# 
# ## Faltung vs. Korrelation vs. Autokorrelation
# 
# Die Faltung ist nicht zu verwechseln mit der Kross-Korrelation von zwei Messsignalen. Obwohl die Integrale sehr ähnlich aussehen, so besteht ein signifikanter Unterschied zwischen diesen beiden Methoden, der sich im Minuszeichen der Verzögerung aufzeigt. Grafisch bedeutet dies, dass das zu faltende Signal im Falle der Kreuz-Korrelation *nicht* gespiegelt wird, wohingegen es bei der grafischen Faltung zeitlich gespiegelt werden muss. 
# Die **Faltung** berechnet man in der Regel, wenn man die Antwort eines Messsystems berechnen möchte.
# 
# $$(f \ast g)(t) = \int_{-\infty}^{\infty} f(\tau)g(t-\tau) \mathrm{d}\tau$$
# 
# Die **Kreuz-Korrelation** berechnet man um zu untersuchen, ob Rauschanteile von Signal $f$ auch in Signal $g$ vorkommen (Stichwort ist hier der *Korrelationsbegriff*, welcher häufig auf zwei *Signale* und nicht Messsysteme angewendet wird).
# 
# $$(f \star g)(t) = \int_{-\infty}^{\infty} f(\tau)g(t+\tau) \mathrm{d}\tau$$
# 
# Die **Auto-Korrelation** soll hier der vollständigkeitshalber noch einmal als Spezialfall der Kreuz-Korrelation aufgeführt werden. Hier berechnet man, wie ähnlich ein zeit-verschobenes Signal zu sich selbst ist (*zeitliche Korrelation*). 
# 
# $$(g \star g)(t) = \int_{-\infty}^{\infty} g(\tau)g(t+\tau) \mathrm{d}\tau$$
# 
# :::{figure-md} faltung_korr_auto
# <img src="draw/faltung_korr_auto.jpg" alt="faltung_korr_auto" class="bg-primary mb-1" width="700px" label = faltung_korr_auto>
# 
# Vergleich von Faltung, Korrelation und Autokorrelation.
# :::
# 
