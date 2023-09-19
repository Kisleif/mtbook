#!/usr/bin/env python
# coding: utf-8

# # Messunsicherheiten - Quellen, Ursachen und Korrektur
# 
# Jede Messung einer physikalischen Größe $x$ ist abhängig von den verwendeten Messgeräten, dem Messverfahren, dem Messobjekt, von Umwelteinflüssen (Temperatur, Feuchtigkeit, elektromagnetische Felder) und schließlich auch vom Beobachter (Müdigkeit, Sehschärfe, Übung), wie in {numref}`fehlerklassen` dargestellt.
# 
# :::{figure-md} fehlerklassen
# <img src="draw/fehlerklassen.jpg" alt="fehlerklassen" width="600px" label = fehlerklassen>
# 
# Vereinfachtes Modell eines Messsystems mit Störeinflüssen.
# :::
# 
# Folgende Störungen können während der Messung auftreten:
# * **Innere Störgrößen:** Hierbei handelt es sich um Störgrößen im Messgerät selbst. Beispiele dafür sind Alterungseffekte an für die Messung wichtigen Bauteilen. Bei Drehspulinstrumenten oder Waagen ist eine Feder eingebaut, deren Eigenschaften sich im Laufe der Lebensdauer verändert, was sich in einer fehlerhaften Anzeige bemerkbar macht.
# * **Äußere Störgrößen:** Messungen werden meist durch mehrere unerwünschte Einflüsse gestört. Eine Widerstandsbrückenschaltung ist beispielsweise temperaturabhängig. Hierbei gibt es sowohl systematische Abweichungen, d.h. man kann den Einfluss isolieren und deterministisch beschreiben und die Messung korrigieren. Eine andere Art von äußeren Störgrößen sind zufällige Einstreuungen, die man nicht kompensieren kann. Zu ihrer Unterdrückung kommen u. a. einfache Mittelwertfilter zum Einsatz.
# * **Beobachtungsfehler:** Wenn du eine Messung durchführst, kannst auch du, der Beobachter, zu einer Fehlerquelle werden, wenn z.B. die Anzeige falsch abgelesen wird. 
# * **Dynamische Fehler:** Jedes Messsystem braucht eine bestimmte Zeit um sich einzupendeln. Daher sollte man immer einen Moment warten, bis man das Messsignal abliest. Die Abweichung entspricht hierbei der Größe des Toleranzbereichs. Optimalerweise wird das gemessene Signal der eigentlichen Messgröße verzögerungsfrei folgen. Sollte dies nicht der Fall sein, wird dies als dynamischer Fehler bezeichnet.
# * **Rückwirkung** Jedes Messgerät braucht für den Messprozess Energie oder Leistung, die dem Prozess entzogen wird. Der Wert der Messgröße mit angeschlossener Messeinrichtung unterscheidet sich vom Wert, der ohne Messeinrichtung erreicht worden wäre. Auch bei externen Spannungsversorgungen entsteht eine Rückwirkung und Kopplung aufgrund von Wärme, die äußere Störgrößen antreibt. 
# * **Quantisierungsfehler**: Diese Fehler entstehen bei der Digitalisierung. Es existiert nur eine endliche Anzahl von Möglichkeiten einen analogen Messwerte mittels Bits darzustellen.
# 
# Um die Messunsicherheiten und Störungen zu reduzieren, sollten immer die vom Hersteller spezifizierten Normalbedingungen (Messbereich, Messgenauigkeit, Betriebsbedingung, Einbauvorschrift, Energieversorgung, Abmessungen) eingehalten werden.

# ## Anzeigefehler von Messgeräten (systematisch)
# 
# Messgeräte werden anhand ihrer Genauigkeit in Klassen eingruppiert. Die Klasse entspricht der relativen Messabweichung. Präzisionsmessgeräte besitzen somit Abweichungen die zwischen 0,001% und 0,05% liegen. Die Genauigkeitsklasse K 2,5 (Angabe auf der Messskala nach DIN EN 60051 Abb. 1) bedeutet: Ist der Endwert des eingestellten Messbereichs $U_\mathrm{end}$, dann beträgt die Typ B-Unsicherheit über den gesamten Messbereich $u(U) = 0,0025\cdot U_\mathrm{end}$. Für $U_\mathrm{end} = 15\,\mathrm V$ erhält man also:

# In[1]:


U_end = 15
u = 0.0025
print('eine absolute Unsicherheit von ', u*U_end, 'V')


# Dieser Wert von 0,375V gilt unabhängig davon, wie groß der Zeigerausschlag beim Messgerät ist. Um die relative Unsicherheit gering zu halten, sollte der Messbereich möglichst so gewählt werden, dass der Messwert am Skalen*ende* abgelesen wird.

# ## Digitalstellenfehler
# 
# :::::{grid} 2
# 
# ::::{grid-item}
# | Messgeräte-Kategorie | Genauigkeits-Klasse (%) |
# |:--------|:-----------|
# |Präzisions-Messgeräte | 0.001 |
# | | 0.002|
# | | 0.005|
# | | 0.01|
# | | 0.05|
# | Fein-Messgeräte | 0.1|
# | | 0.2|
# | | 0.5|
# | Betriebs-Messgeräte | 1.0|
# | | 1.5|
# | | 2.5|
# | | 5.0|
# ::::     
#         
# ::::{grid-item}
# :::{figure-md} voltmeter
# <img src="draw/voltmeter.jpg" alt="voltmeter" width="175px" label = voltmeter>
# 
# Voltmeter mit Digitalanzeige.
# :::
# ::::
# :::::
# 
# 
# Das Gerät im Bild zeigt den Messwert 5.847V an. Laut Hersteller ist die Maximalabweichung (unter Referenzbedingungen) $a = \pm$ (0,5% vom *Messwert* + 9 Digit). Die Anzahl der Nachkommastellen (also der Digits) ist in diesem Falle 3, also 0,001V. Genauer kann das Messgerät keine Spannung angeben. Die Messabweichung setzt sich also wiefolgt zusammen (zwei signifikante Stellen reichen hierbei, da der Messwert selber nicht genauer angezeigt wird):
# 
# $$a = \pm (0,5\% \cdot 5,847\,\mathrm{V} + 9 \cdot 0,001\,\mathrm V) \approx \pm 0,038\,\mathrm V = \pm 38,235\,\mathrm{mV}$$
# 
# Innerhalb dieses $\pm$ Bereiches der Breite $2a$ unterstellt man eine Gleichverteilung der Messwerte und bekommt damit die Standardunsicherheit:
# 
# $$u(U) = \frac{a}{\sqrt{3}} = \frac{38,235\,\mathrm{mV}}{\sqrt{3}} \approx 22\,\mathrm{mV}$$
# 
# Ist nichts weiter bekannt, schätzt man die Unsicherheit über einen Mindestfehler von a = 1 Digit ab.

# In[2]:


import numpy as np
Messwert = 5.847 # in V
Nachkommastellen = 5
A_rel = 0.005 # = 0.5%
Digit = 0.001 # in V 
A_total = A_rel * Messwert + 9 * Digit
print('Die Messtoleranz beträgt: +-',round(A_total,Nachkommastellen), 'V = +-', round(A_total*1000,Nachkommastellen), 'mV')
print('Die Unsicherheit beträgt: +-',round(A_total/np.sqrt(3),Nachkommastellen), 'V = +-', round(A_total*1000/np.sqrt(3),Nachkommastellen), 'mV')


# ## Abweichung aufgrund von Verbindungskabel (systematisch)
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Leitungswiderstand und Spannungsabfall einer Leitung berechnen (Kfz-Technik einfach erklärt)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/kzjpePkDTjQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Verbindungskabel besitzen Innenwiderstände, wo ebenfalls Spannungen abfallen:
# 
# $$R_L = \frac{\zeta \cdot l}{A}$$
# 
# Hierbei ist $\zeta$ der spezifische Widerstand, der für Kupfer $0,0175\,\mathrm{\Omega mm^2/m}$ beträgt. $l$ ist die Länge der Zuleitung und $A$ der Querschnittfläche des Kabels.
# 
# Eine gemessene Spannung ist also zu hoch und muss korrigiert werden.
# 
# :::{admonition} Aufgabe
# :class: tip
# Angenommen man habe ein $2\,\mathrm m$ langes Kabel, das einen Querschnitt von $0,5\,\mathrm{mm^2}$ aufweist und aus Kupfer (mit einem spezifischen Widerstand von $0,0175\,\mathrm{\Omega mm^2/m}$) ist. Wie groß ist die systematische Messabweichung für eine Stromstärke von $I = 100\,\mathrm{mA}$, wenn jeweils ein solches Kabel zum Anschluss der Spannungsmessung genommen wird?
# :::

# In[3]:


zeta = 0.0175 #in Ohm mm^2 / m
l = 2 #in m
A = 0.5 #in mm^2
I = 100e-3 #in A

# Strom durch ein Zuleitungskabel
U = zeta * l / A * I
print('Die Spannung wird um ', 2*U*1000, 'mV zu hoch gemessen')


# :::{admonition} Lösung
# :class: tip, dropdown
# Angenommen man habe keine Zuleitungskabeln, wo wäre die Spannung an einem Widerstand $R_x$ durch $U_x = R_x \cdot I$ gegeben. 
# Bei Zuleitungskabeln werden die unvermeidbaren Zusatz-Widerstände in Reihe zu dem eigentlichen Widerstand $R_x$ geschaltet. Das heißt die gemessene Spannung setzt sich nun aus der Spannung an $R_x$ und an den jeweils 2 Kabeln, $U_L$ zusammen: $U = U_x + 2\cdot U_L$. 
# Der Wert für $U_L$ beträgt:
# 
# $$U_L = \frac{\zeta \cdot l}{A} \cdot I = 7\,\mathrm{mV}$$
# 
# Damit wird die Spannung mit 2m-Kupferkabeln um $14\,\mathrm{mV}$ zu hoch gemessen!
# :::

# ## Korrektur von systematischen Messabweichungen
# 
# Man merkt, dass systematische Fehler sehr unangenehm sein können, da Gegenmaßnahmen fallabhängig entwickelt werden müssen. In einigen Fällen gelangt man zu einer brauchbaren Abschätzung der Unsicherheit, wenn man den „worst case“ annimmt. 
# 
# Abschätzungen von systematischen Messabweichungen, wie es z.B. im vergangenen Beispiel des Verbindungskabels geschehen ist, müssen unbedingt benutzt werden, um den Messwert am Ende zu korrigieren! Ansonsten misst man einen *ungenauen* Wert, der entweder zu groß oder zu klein ist. Dies wird auch häufig als "Offset" bezeichnet. Die Messung kann dann noch so *präzise* wie möglich sein, der Wert ist dennoch *falsch*.
# 
# Bei zufälligen Messabweichungen ist eine Korrektur nicht möglich. In diesem Fall muss die Messabweichung mit Methoden der Statistik bestimmt und mit dem Messwert zusammen angegeben werden. 
# 
# :::{figure-md} messabw
# <img src="draw/zusammenfassung_abw.jpg" alt="messabw" width="600px" label = messabw>
# 
# Korrektur und Angabe des Messergebnisses
# :::

# In[ ]:




