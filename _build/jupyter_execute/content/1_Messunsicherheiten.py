#!/usr/bin/env python
# coding: utf-8

# # Quellen und Ursachen von Messunsicherheiten
# 
# Früher hat man statt *Abweichung* noch den Begriff *Messfehler* verwendet. Man dachte, dass man mit genügend Aufwand, Sorgfalt und bestmöglicher Technologie den Fehler vollständig eliminieren können. Spätestens seit der Theorie der *Quantenphysik* ist uns allerdings bekannt, dass zufällige Einflüsse auf die beobachteten Messgrößen  unvermeidlich sind und auch nicht vorhergesagt werden können. Statt eines einzig *wahren* Wertes, $x_w$, werden in der Quantenphysik Messgrößen durch deren Erwartungswerte vorhergesagt. Diesen Messgrößen liegt eine Wahrscheinlichkeitsdichte zu Grunde, dessen Varianz (bzw. Standardabweichung) nicht verschwindet! Somit werden für ein und dieselbe physikalische Messgröße verschiedene Ergebnisse gemessen, obwohl nahezu identische Bedingungen herrschen. Das Eintreten eines bestimmten Messergebnisses ist an eine bestimmte Wahrscheinlichkeit gekoppelt, mit der dieses Ergebnis eintritt.  
# 
# Das bedeutet, dass ein Messwert, $x$, immer mit einer Messabweichung, $A$, behaftet ist und somit nur bedingt dem *wahren* Wert, $x_w$, entspricht. 
# 
# $$x = x_w + A$$
# 
# ## Quellen und Ursachen
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
# * **Dynamische Fehler:** Jedes Messsystem braucht eine bestimmte Zeit um sich einzupendeln. Daher sollte man immer einen Moment warten, bis man das Messsignal abliest. Die Abweichung entspricht hierbei der Größe des Toleranzbereichs. Optimalerweise wird das gemessene Signal der eigentliche Messgröße verzögerungsfrei folgen. Sollte dies nicht der Fall sein, wird dies als dynamischer Fehler bezeichnet.
# * **Rückwirkung** Jedes Messgerät braucht für den Messprozess Energie oder Leistung, die dem Prozess entzogen wird. Der Wert der Messgröße mit angeschlossener Messeinrichtung unterscheidet sich vom Wert, der ohne Messeinrichtung erreicht worden wäre. Auch bei externen Spannungsversorgungen entsteht eine Rückwirkung und Kopplung aufgrund von Wärme, die äußere Störgrößen antreibt. 
# * **Quantisierungsfehler**: Diese Fehler entstehen bei der Digitalisierung. Es existiert nur eine endliche Anzahl von Möglichkeiten einen analogen Messwerte mittels Bits darzustellen.
# 
# Um die Messunsicherheiten und Störungen zu reduzieren sollten immer die vom Hersteller spezifizierten Normalbedingungen (Messbereich, Messgenauigkeit, Betriebsbedingung, Einbauvorschrift, Energieversorgung, Abmessungen) eingehalten werden.
# 
# Messungen liefern dennoch lediglich Schätzwerte für die *wahren* Werte einer Größe. Es gibt prinzipiell keine Möglichkeit, den wahren Wert einer Messgröße zu messen. Im Rahmen internationaler Anstrengungen für eine einheitliche Bewertung von Einflussgrößen auf eine Messung werden zwei Kategorien von Methoden der Berechnung von Unsicherheiten unterschieden [[GUM]](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e.html?csnumber=50461):
# - **Typ A ("Zufällige Abweichung"):** Berechnung der Messunsicherheit durch statistische Analyse der Messungen
# - **Typ B ("Systematische Abweichung"):** Berechnung der Messunsicherheit mit anderen Mitteln als der statistischen Analyse
# 
# :::{figure-md} zielscheibe
# <img src="draw/zielscheibe.jpg" alt="zielscheibe" class="bg-primary mb-1" width="800px" label = zielscheibe>
# 
# Darstellung von zufälligen und systematischen Fehlern anhand einer Zielscheibe. Die zufällige Abweichung gibt eine Art Streuung, die *Präzision*, der Messwerte an. Die systematische Abweichung gibt die *Genauigkeit* an.
# :::
# 
# ## Typ A-Unsicherheiten ("Zufällige Fehler")
# 
# Dies sind Messunsicherheiten, die nicht einseitig gerichtet sind, sondern einer zufälligen Streuung der Messwerte zugrunde liegen. Zur Behandlung dieser Messunsicherheiten nutzt man die Stochastik (Wahrscheinlichkeitslehre und Statistik). 
# * Zufällige Fehler kennt man nicht, er ist folglich **nicht korrigierbar**
# * Sie sind unter gleichen Messbedingungen auch **nicht reproduzierbar** 
# * Sie machen ein Ergebnis **unpräzise**
# * Es sind **wiederholte Messungen und statistische Analysen** notwendig, wodurch Mittelwert und Standardabweichung von sogenannten *Stichproben* ermittelt wird. 
# 
# Wie gewinnt man aus einer Messreihe $x_j$ den besten Schätzewert, der mit maximaler Wahrscheinlichkeit am nähesten am *wahren* Wert, $x_w$, liegt? Mit welcher Wahrscheinlichkeit liegt das Messergebnis innerhalb eines bestimmten Intervalls um den wahren Wert, $x = x_w + \Delta x ?$ Hiermit befassen wir uns im Kapitel [Statistische Größen](1_Mittelwert_StdAbw).
# 
# ## Typ B-Unsicherheiten ("Systematische Fehler")
# 
# 
# * Bei systematischen Unsicherheiten handelt es sich um **reproduzierbare** Messunsicherheiten. 
# * Sie werden durch **Unvollkommenheit in den Messgeräten** und Messverfahren verursacht.
# * Sie können durch Aufwand und Kalibration verbessert werden, was *nicht* für zufällige Messabweichungen gilt. 
# * Sie machen ein Ergebnise **unsichtig**
# * Systematische Messabweichungen (z.B. Kennlinienfehler) sollten in aller Regel am besten **korrigiert werden**, wenn dies möglich ist. Ansonsten sollte mindestens eine Angabe der Messabweichung erfolgen.
# 
# Es gibt keine allgemeingültige Definition oder allgemeine Verfahren zur Korrektur. Das heißt für jeden Fall müssen neue Verfahren entwickelt werden. Hier kommen ein paar Beispiele, wie man mit solchen *systematischen* Messunsicherheiten umgehen kann:
# 
# ### Anzeigefehler von Messgeräten
# 
# Messgeräte werden anhand ihrer Genauigkeit in Klassen eingruppiert. Die Klasse entspricht der relativen Messabweichung. Präzisionsmessgeräte besitzen somit Abweichungen die zwischen 0,001% und 0,05% liegen. Die Genauigkeitsklasse K 2,5 (Angabe auf der Mess- skala nach DIN EN 60051 Abb. 1) bedeutet: Ist der Endwert des eingestellten Messbereichs $U_\mathrm{end}$, dann beträgt die Typ B-Unsicherheit über den gesamten Messbereich $u(U) = 0,0025\cdot U_\mathrm{end}$. Für $U_\mathrm{end} = 15\,\mathrm V$ erhält man also:

# In[1]:


U_end = 15
u = 0.0025
print('eine absolute Unsicherheit von ', u*U_end, 'V')


# Dieser Wert von 0,375V gilt unabhängig davon, wie groß der Zeigerausschlag beim Messgerät ist. Um die relative Unsicherheit gering zu halten, sollte der Messbereich möglichst so gewählt werden, dass der Messwert am Skalen*ende* abgelesen wird.
# 
# ### Digitalstellenfehler
# 
# :::::{grid} 2
# 
# ::::{grid-item}
# | Messgerätekategorie | Genauigkeitsklasse (%) |
# |:--------------------|:-------------------|
# |Präzisionsmessgeräte | 0.001 |
# | | 0.002|
# | | 0.005|
# | | 0.01|
# | | 0.05|
# | Feinmessgeräte | 0.1|
# | | 0.2|
# | | 0.5|
# | Betriebsmessgeräte | 1.0|
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


# Man merkt, dass systematische Fehler sehr unangenehm sein können, da Gegenmaßnahmen fallabhängig entwickelt werden müssen. In einigen Fällen gelangt man zu einer brauchbaren Abschätzung der Unsicherheit, wenn man den „worst case“ annimmt.
# 
# ### Systematische Abweichung aufgrund von Verbindungskabel
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
# 
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

# In[3]:


zeta = 0.0175 #in Ohm mm^2 / m
l = 2 #in m
A = 0.5 #in mm^2
I = 100e-3 #in A

# Strom durch ein Zuleitungskabel
U = zeta * l / A * I
print('Die Spannung wird um ', 2*U*1000, 'mV zu hoch gemessen')


# ## Schreibweise eines Messwertes mit Messabweichung
# 
# Die **Gesamt-Messabweichung** einer Messgröße $x$ setzt sich also wiefolgt zusammen:
# 
# $$A = A_r +  A_s$$
# 
# wobei $A_r$ zufällige und $A_s$ systematische Messabweichungen sind. Ein Messwert setzt sich also zusammen aus dem *wahren* oder *richtigen* Wert, den wir niemals kennen werden, und der Messabweichung. Es gelten folgende Zusammenhänge:
# 
# * Der **ermittelte Messwert** lässt sich wiefolgt schreiben, wobei $x_w$ der *wahre*, aber uns unbekannte, Wert ist. $A$ ist die Messabweichung: 
# 
# $$x = x_w + A$$
# 
# * Die **absolute Messabweichung** ergibt sich aus Umstellen der Gleichung:
# 
# $$A = x - x_w = \Delta x$$
# 
# * Bei der Angabe **relativen Messabweichung** wird die Messabweichung auf einen Referenzwert, $r$, bezogen, der entweder der Messwert selber ist ($r = x$), oder manchmal auch die Spanne ($r = x_\mathrm{max} - x_\mathrm{min}$) oder Maximalwert/Messbereichsendwert ($r = x_\mathrm{max}$):
# 
# $$ A_\mathrm{rel} = \frac{A}{r} = \frac{\Delta x}{r}$$
# 
# ### Signifikante Stellen 
# 
# Die **Anzahl der Nachkommastellen** eines Messwertes ist niemals größer als die der angegebenen Messabweichung oder Unsicherheit. Die Anzahl der Nachkommastellen der Messabweichung wird über **signifikante Stellen** (= angegebene Ziffern ohne führende Nullen) definiert. Je mehr signifikante Stellen angegeben werden, desto größer ist die Genuigkeit, die reklamiert wird. Es gelten folgende Rechenoperationen nach DIN1333:
# 
# - Bei **Addition von Größen** bekommt das Ergebnis genauso viele Nachkommastellen wie die Zahl mit den *wenigsten* Nachkommastellen.
# - Bei **Multiplikation von Größen** bekommst das Ergebnis genauso viele signifikante Stellen wie der Zahl mit den wenigsten signifikanten Stellen.
# - **Messunsicherheiten** werden auf eine signifikante Stelle gerundet. Eine Ausnahme existiert, wenn die erste Ziffer eine "1" ist, weil sonst Rundungsfehler schnell zu groß werden. Beispiel: $u(g) = 0,1562\,\mathrm{m/s^2} = 0,16\,\mathrm{m/s^2}$. Die Darstellung $g = (9,81 \pm 0,03562)\,\mathrm{m/s^2}$ wäre unsinnig, da die Genauigkeit auf zwei Nachkommastellen durch den Messwert beschränkt ist. 
# - **Messwerte** werden so angegeben, dass die letzte signifikante Stelle die gleiche Größenprdnung hat, wie die Messunsicherheit: Die Angabe $H=(13,13\pm 1)\,\mathrm m$ ist sinnlos, richtig wäre $H=(13\pm 1)\,\mathrm m$.
# 
# Um Rundungsfehler zu reduzieren, führen Sie in den Berechnungen soviel signifikante Stellen der Messunsicherheit mit, wie nötig.
# 
# ### Grafische Darstellung eines Messwertes mit Messabweichung
# 
# Die grafische Darstellung eines solchen Messwertes in einem Diagramm kann im folgenden Code-Block ausgeführt und angesehen werden. Prinzipiell gilt, dass für jeden Messwert in der Regel ein solcher **Fehlerbalken** stets anzugeben ist. 

# In[4]:


#Benötigte Libraries:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.figure(figsize=(4,4)) # Plot-Größe
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

x = [1.0]  # Datenwerte für x-Achse, hier Nr der Messung
y = [1.0]  # Messwert (Datenpunkt)
delta_y = [0.3] # Messabweichung

# Diagrammdarstellung:
plt.errorbar(x, y, yerr=delta_y, fmt='bo', color="tab:blue")
plt.xlim(0.5, 1.5)
#plt.ylim(0.,1.1*(max(y)+max(delta_y)))
plt.ylabel("U (V)")
plt.xlabel("Nr. der Messung")
plt.show()


# ### Diskrepanz und Konsistenz
# 
# Die Diskrepanz zweier Messwerte derselben Größe ist der Absolutbetrag ihrer Differenz. Zwei Messungen sind konsistent, wenn ihre Diskrepanz geringer ist, als die (kleinere der) Messunsicherheiten:
# - $g = (9,73 \pm 0,05)\,\mathrm{m/s^2}$ und $g = (9,76 \pm 0,04)\,\mathrm{m/s^2}$ sind *konsistent*, nicht jedoch $g = (9,71 \pm 0,02)\,\mathrm{m/s^2}$ und $g = (9,76 \pm 0,04)\,\mathrm{m/s^2}$
# - Ist $g = (8.9 \pm 1,5)\,\mathrm{m/s^2}$ das Ergebnis einer Messung des Ortsfaktors, dann ist die Messung zwar nicht sonderlich präzise, aber mit dem Literaturwert von $g = 9,81\,\mathrm{m/s^2}$ vereinbar.

# In[5]:


plt.style.use('default') # Matplotlib Style wählen
plt.figure(figsize=(4,4)) # Plot-Größe
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

y=[9.73, 9.76, 9.71, 9.76, 8.9] # Messung 
u_y=[0.05,0.04,0.02,0.04,1.5] # Unsicherheit d
y_w=9.81 # wahrer / richtiger Wert 

plt.errorbar([1, 2, 3,4,5], y, yerr=u_y, fmt='bo', color = "tab:blue")

plt.axhline(y_w, color='tab:red', linewidth=3)
plt.text(1.2, 9.83, 'wahrer Wert', color='tab:red') 

plt.ylabel(r"Erdbeschleunigung")
plt.xlabel("Nr. der Messung")
plt.title("Messungen der Erdbeschleunigung")
plt.ylim([8.8,9.9])
plt.grid()
plt.show()


# Nur einer der Messwerte überlappt mit dem *wahren* Wert der Erdbeschleunigung Die Fehlerbalken der zweiten Messung hingegen sind davon entfernt, in den *wahren* Bereich überzulappen. D.h. es existiert hier ein Widerspruch zu vorherigen Messungen, die den wahren Wert kennzeichnete. Würde es sich hierbei nicht um die Messung der Erdbeschleunigung, sondern um die einer Natur*konstante* handeln, gäbe es sogar einen Widerspruch zum SI-Einheitensystem. 
