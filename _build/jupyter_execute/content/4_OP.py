#!/usr/bin/env python
# coding: utf-8

# # Operationsverstärker (OP)

# Liegen kleine Signale vor, wie z.B. kleine Stromstärken $I$,  Spannungswerte $U$ oder Widerstandswerte $R$, so werden die Signale häufig als erstes verstärkt, was mittels einem Operationsverstärker (OP) realisiert wird. In {numref}`op` ist eine schematische Zeichnung eines OPs dargestellt. 
# 
# :::{figure-md} op
# <img src="draw/op.jpg" alt="op" width="600px" label = op>
# 
# Schematische Darstellung eines Operationsverstärkers (OPs) mit Eingangs-Innenwiderstand $R_e$, Ausgangs-Innenwiderstand $R_i$ und Spannungsversorgung $U_V$. $U_d$ ist die angelegte Eingangsspannung an dem differentiellen Eingang des OPs. $U_a$ ist die Ausgangsspannung.
# :::

# ## Eigenschaften

# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Operationsverstärker
# 
# <iframe width="220" src="https://www.youtube.com/embed/nl3JZbj9kHs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ::::
# :::::
# ::::::

# Dies sollte möglichst **rückwirkungsfrei** geschehen, das heißt dass die Verstärkerschaltung möglichst wenig Einfluss auf die Messgröße und die weiterführende Signalverarbeitung hat. 
# Für eine Spannung, die man anlegt, sollte der **Eingangs-Innenwiderstand $R_e$** also **möglichst groß** sein, um den kompletten Spannungsabfall zu messen. 
# Typische *reale* Werte liegen zwischen $R_e' \approx 10^6 - 10^{12}\,\mathrm{\Omega}$. Der Innenwiderstandswert eines *idealen* OPs wäre $R_e = \infty$. 
# 
# Desweiteren möchte man eine **hohe Empfindlichkeit** und eine **große Verstärkung** erreichen, weshalb eine zusätzliche Strom- bzw. **Spannungsversorgung $U_V$** von Nöten ist, da die zusätzlich Energie von Außen dem System zugeführt werden muss. Dies ist der allgemein Sinn von Operationsverstärkern. Die Verstärkung ist allgemein definiert als 
# 
# $$ k' = \frac{U_\mathrm a}{U_\mathrm d} $$
# 
# wobei $k'$ die reale Verstärkung des OPs ist, $k$ wäre die des *idealen* OPs ($k = \infty$) und $U_\mathrm a$ ist die Ausgangsspannung und $U_\mathrm d$ die differentielle Eingangsspannung. Reale Verstärkungsfaktoren liegen in der Größenordnung von $k' \approx 10^6$. 
# 
# Das Ausgangssignal sollte weiterdessen direkt mit dem Eingangssignal korreliert sein, d.h. wir wünschen uns ein **definiertes Übertragungsverhalten**. Dem Eingangssignal sollte zudem möglichst gut und schnell gefolgt werden, d.h. es sollten keine allzu großen Verzögerungen auftreten. Dies wird über das **dynamische Verhalten** des verwendeten OPs bestimmt. Reale OPs haben eine begrenzte Bandbreite die berücksichtigt werden muss. 
# Am Ausgang sollte ein möglichst kleiner Innenwiderstand vorzufinden sein, sodass wir ein **eingeprägtes Ausgangssignal** annehmen können, d.h. das Ausgangssignal ist gut weiterverwendbar und beeinflusst nicht die folgende Schaltung. 
# 

# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Elektrometer und weitere Beispiele
# 
# <iframe width="220" src="https://www.youtube.com/embed/wiq93KjXwao" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
