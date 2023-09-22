#!/usr/bin/env python
# coding: utf-8

# # Messunsicherheiten
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Messunsicherheit erklärt in 4 Minuten (Kistler Group)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/8jK2o9NuA5E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Jede Messung, egal ob von Temperatur, Strecke oder Geschwindigkeit, ist immer mit einer Messunsicherheit verbunden. Der Messwerte, ohne Angabe einer Messunsicherheit, ist daher wertlos. 
# Die Messunsicherheit ist ein Maß für die Qualität der Messung: Desto kleiner die Messabweichung, desto *genauer* oder *präziser* ist die Messung. 
# 
# 
# :::{figure-md} coffee_toleranz
# <img src="draw/coffee_toleranz.jpg" alt="coffee_toleranz" class="bg-primary mb-1" width="800px" label = coffee_toleranz>
# 
# Kaffeehalter und Kaffeebecher zeigen den gleichen Wert auf dem Messschieber an. Warum passt es trotzdem nicht?
# :::
# 
# In {numref}`coffee_toleranz` ist ein Beispiel aus der Produktion gegeben. Für einen Kaffeebecher mit Durchmesser $x = 55\,\mathrm{mm}$ soll eine einfach Halterung produziert werden. Der Durchmesser $x$ des Kaffeebechers wird mit dem Messschieber bestimmt und an zwei Firmen weitergegeben. Im ersten Produkt ist der Halter zu groß, der Becher rutscht durch. Im zweiten Fall wird das Loch noch einmal mit dem Messschieber überprüft. Dieser zeigt den richtigen Wert von $55\,\mathrm{mm}$ an, dennoch passt der Becher nicht. Woran liegt das?
# 
# ## Toleranz
# 
# Was in diesem Beispiel fehlt ist die Angabe der *Toleranz*. 
# Die Toleranz erhält man durch die Bestimmung der *Messunsicherheit*. 
# Ohne die Kenntnis der verwendeten Messinstrumente, kann keine Fertigungstoleranz spezifiziert werden. 
# 
# Es gibt zwei Möglichkeiten, die Messunsicherheit zu bestimmten:
# 1. Der Durchmesser des Kaffeebechers wird 100 Mal gemessen. Dadurch erhalten wir eine Streuung der Messwerte, woraus ein Mittelwert der Streuung berechnet werden kann. Hierfür werden Formeln aus statistischen Mathematik verwendet, um die Messunsicherheit und somit die Toleranz zu bestimmen. 
# 2. Mittels dem Datenblatt des Herstellers des Messschiebers können die Spzifikationen direkt abgelesen werden. Es ist ratsam trotzdem noch mehrere Messungen durchzuführen, 10 genügen in den meisten Fällen aus. Die Angaben aus dem Datenblatt werden mit den gemittelten Streuwerten kombiniert und sollten eine ähnliche Toleranz ergeben.  
# 
# ```{admonition} Beispiel: Datenblatt eines digitalen Messschiebers
# :class: dropdown
# Laut [Angaben des Herstellers](https://shop.mitutoyo.de/web/mitutoyo/de_BE/mitutoyo/01.03.07a/Digital%20ABS%20Messschieber/$catalogue/mitutoyoData/PR/500-500-10/index.xhtml) ist die zulässige Längenmessabweichung (MPE E: maximum permissible error  = maximal zulässiger Wert der Messabweichung der Längenmessung) 0,05mm. Der Ziffernschrittwert von 0,01mm gibt die minimale Änderung des Messwertes auf der Skala an. Bei einem Digital-Messschieber ist dies die letzte Stelle der Digitalanzeige. 
# :::{figure-md} messschieber
# <img src="pictures/datenblatt_messschieber.jpg" alt="datenblatt_messschieber" class="bg-primary mb-1" width="800px" label = datenblatt_messschieber>
# 
# Screenshot der Produktdetails von der [Webseite](https://shop.mitutoyo.de/web/mitutoyo/de_BE/mitutoyo/01.03.07a/Digital%20ABS%20Messschieber/$catalogue/mitutoyoData/PR/500-500-10/index.xhtml) des Herstellers.
# :::
# ```
# 
# Der Messwert inklusive Toleranz (Messunsicherheit) muss an den Hersteller für Kaffeebecherhalter weitergegeben werden. Entweder in Form der *absoluten* Messunsicherheit $A$, die die gleiche Einheit wie der Messwert hat:
# 
# $$x \pm A = 55 \pm 1\,\mathrm{mm}$$
# 
# oder in Form der *relativen* Messunsicherheit:
# 
# $$x \pm A_\mathrm{rel} = x \pm \frac{A}{x} = 55\,\mathrm{mm} \pm 1,8\%$$
# 
# Hier ist die Einheit *einheitenlos* und wird in Prozent (%) wird.
# 
# 
# ```{admonition} Mess*unsicherheit* vs. Mess*fehler*
# :class: dropdown
# 
# Früher hat man statt *Abweichung* noch den Begriff *Messfehler* verwendet. Man dachte, dass man mit genügend Aufwand, Sorgfalt und bestmöglicher Technologie den Fehler vollständig eliminieren könne. Spätestens seit der Theorie der *Quantenphysik* ist uns allerdings bekannt, dass zufällige Einflüsse auf die beobachteten Messgrößen  unvermeidlich sind und auch nicht vorhergesagt werden können. Statt eines einzig *wahren* Wertes, $x_w$, werden in der Quantenphysik Messgrößen durch deren Erwartungswerte vorhergesagt. Diesen Messgrößen liegt eine Wahrscheinlichkeitsdichte zu Grunde, dessen Varianz (bzw. Standardabweichung) nicht verschwindet! Somit werden für ein und dieselbe physikalische Messgröße verschiedene Ergebnisse gemessen, obwohl nahezu identische Bedingungen herrschen. Das Eintreten eines bestimmten Messergebnisses ist an eine bestimmte Wahrscheinlichkeit gekoppelt, mit der dieses Ergebnis eintritt. 
# ```
# 
# ## Ursache von Messunsicherheiten
# 
# Warum erhält man überhaupt verschiedene Messwerte mit demselben, hochpräzisen Messinstrument? Das liegt daran, dass auf die Messung verschiedene Einflussfaktoren einwirken. z.B. Umgebungstemperatur, wie ich den Messschieber bediene und die Digitalanzeige haben Einfluss auf das Messergebnis, wie in {numref}`fehlerklassen` dargestellt.
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
# * **Beobachtungsfehler:** Wenn du eine Messung durchführst, kannst auch du, der Beobachter, zu einer Fehlerquelle werden, wenn z.B. die Anzeige falsch abgelesen wird (Müdigkeit, Sehschärfe, Übung). 
# * **Dynamische Fehler:** Jedes Messsystem braucht eine bestimmte Zeit um sich einzupendeln. Daher sollte man immer einen Moment warten, bis man das Messsignal abliest. Die Abweichung entspricht hierbei der Größe des Toleranzbereichs. Optimalerweise wird das gemessene Signal der eigentlichen Messgröße verzögerungsfrei folgen. Sollte dies nicht der Fall sein, wird dies als dynamischer Fehler bezeichnet.
# * **Rückwirkung** Jedes Messgerät braucht für den Messprozess Energie oder Leistung, die dem Prozess entzogen wird. Der Wert der Messgröße mit angeschlossener Messeinrichtung unterscheidet sich vom Wert, der ohne Messeinrichtung erreicht worden wäre. Auch bei externen Spannungsversorgungen entsteht eine Rückwirkung und Kopplung aufgrund von Wärme, die äußere Störgrößen antreibt. 
# * **Quantisierungsfehler**: Diese Fehler entstehen bei der Digitalisierung. Es existiert nur eine endliche Anzahl von Möglichkeiten einen analogen Messwerte mittels Bits darzustellen.
# 
# Um die Messunsicherheiten und Störungen zu reduzieren, sollten immer die vom Hersteller spezifizierten Normalbedingungen (Messbereich, Messgenauigkeit, Betriebsbedingung, Einbauvorschrift, Energieversorgung, Abmessungen) eingehalten werden.

# ## Typen von Unsicherheiten
# 
# Messungen liefern dennoch lediglich Schätzwerte für die *wahren* Werte einer Größe. Es gibt prinzipiell keine Möglichkeit, den wahren Wert einer Messgröße zu messen. Im Rahmen internationaler Anstrengungen für eine einheitliche Bewertung von Einflussgrößen auf eine Messung werden zwei Kategorien von Methoden der Berechnung von Unsicherheiten unterschieden [[GUM]](https://www.iso.org/sites/JCGM/GUM/JCGM100/C045315e-html/C045315e.html?csnumber=50461):
# - **Typ A (["Zufällige Abweichung"](1_StatistischeMessunsicherheit)):** Berechnung der Messunsicherheit durch statistische Analyse der Messungen
# - **Typ B (["Systematische Abweichung"](1_SystematischeMessabweichung)):** Berechnung der Messunsicherheit mit anderen Mitteln als der statistischen Analyse
# 
# :::{figure-md} zielscheibe
# <img src="draw/zielscheibe.jpg" alt="zielscheibe" class="bg-primary mb-1" width="800px" label = zielscheibe>
# 
# Darstellung von zufälligen und systematischen Fehlern anhand einer Zielscheibe. Die zufällige Abweichung gibt eine Art Streuung, die *Präzision*, der Messwerte an. Die systematische Abweichung gibt die *Genauigkeit* an.
# :::
# 
# ### Typ A-Unsicherheiten ("Zufällige Fehler")
# 
# Dies sind Messunsicherheiten, die nicht einseitig gerichtet sind, sondern einer zufälligen Streuung der Messwerte zugrunde liegen. Zur Behandlung dieser Messunsicherheiten nutzt man die Stochastik (Wahrscheinlichkeitslehre und Statistik). 
# * Zufällige Fehler kennt man nicht, er ist folglich **nicht korrigierbar**
# * Sie sind unter gleichen Messbedingungen auch **nicht reproduzierbar** 
# * Sie machen ein Ergebnis **unpräzise**
# * Es sind **wiederholte Messungen und statistische Analysen** notwendig, wodurch Mittelwert und Standardabweichung von sogenannten *Stichproben* ermittelt wird. 
# 
# Wie gewinnt man aus einer Messreihe $x_j$ den besten Schätzewert, der mit maximaler Wahrscheinlichkeit am nähesten am *wahren* Wert, $x_w$, liegt? Mit welcher Wahrscheinlichkeit liegt das Messergebnis innerhalb eines bestimmten Intervalls um den wahren Wert, $x = x_w + \Delta x ?$ Hiermit befassen wir uns im Kapitel [Statistische Messunsicherheiten](1_StatistischeMessunsicherheit).
# 
# ### Typ B-Unsicherheiten ("Systematische Fehler")
# 
# * Bei systematischen Unsicherheiten handelt es sich um **reproduzierbare** Messunsicherheiten. 
# * Sie werden durch **Unvollkommenheit in den Messgeräten** und Messverfahren verursacht.
# * Sie können durch Aufwand und Kalibrierung verbessert werden, was *nicht* für zufällige Messabweichungen gilt. 
# * Sie machen ein Ergebnis **unrichtig**
# * Systematische Messabweichungen (z.B. Kennlinienfehler) sollten in aller Regel am besten **korrigiert werden**, wenn dies möglich ist. Ansonsten sollte mindestens eine Angabe der Messabweichung erfolgen.
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Zufällige und systematische Messabweichungen (Christian Fingerhut)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/_XZ7r-PVwHY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Es gibt keine allgemeingültige Definition oder allgemeine Verfahren zur Korrektur. Das heißt für jeden Fall müssen neue Verfahren entwickelt werden. Hiermit befassen wir uns im Kapitel [Systematische Messabweichungen](1_SystematischeMessabweichung).

# ## Schreibweise eines Messwertes mit Messabweichung
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Absoluter und relativer Messfehler || Fehlerrechnung (Physikcoach)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/HqgrqLXmEN0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Die **Gesamt-Messabweichung** einer Messgröße $x$ setzt sich also wiefolgt zusammen:
# 
# $$A = A_r +  A_s$$
# 
# wobei $A_r$ die zufälligen Messunsicherheiten und die $A_s$ systematische Messabweichungen sind. Ein Messwert setzt sich also zusammen aus dem *wahren* oder *richtigen* Wert, den wir niemals kennen werden, und der Messabweichung. Es gelten folgende Zusammenhänge:
# 
# * Der **ermittelte Messwert** lässt sich wie folgt schreiben, wobei $x_w$ der *wahre*, aber uns unbekannte, Wert ist. $A$ ist die Messabweichung: 
# 
# $$x = x_w + A$$
# 
# * Die **absolute Messabweichung** ergibt sich aus Umstellen der obigen Gleichung. Häufig verwendet man auch die Notation $\Delta x$ für die Angabe der absoluten Messabweichung.
# 
# $$A = x - x_w = \Delta x$$
# 
# * Bei Angabe der **relativen Messabweichung** wird die Messabweichung auf einen Referenzwert, $r$, bezogen, der entweder der Messwert selber ist ($r = x$), oder manchmal auch die Spanne ($r = x_\mathrm{max} - x_\mathrm{min}$) oder Maximalwert/Messbereichsendwert ($r = x_\mathrm{max}$):
# 
# $$ A_\mathrm{rel} = \frac{A}{r} = \frac{\Delta x}{r}$$
# 
# ## Signifikante Stellen 
# 
# Die **Anzahl der Nachkommastellen** eines Messwertes ist niemals größer als die der angegebenen Messabweichung oder Unsicherheit. Die Anzahl der Nachkommastellen der Messabweichung wird über **signifikante Stellen** (= angegebene Ziffern ohne führende Nullen) definiert. Je mehr signifikante Stellen angegeben werden, desto größer ist die Genuigkeit, die reklamiert wird. Es gelten folgende Rechenoperationen nach DIN1333:
# 
# - Bei **Addition von Größen** bekommt das Ergebnis genauso viele Nachkommastellen wie die Zahl mit den *wenigsten* Nachkommastellen.
# - Bei **Multiplikation von Größen** bekommt das Ergebnis genauso viele signifikante Stellen wie die Zahl mit den wenigsten signifikanten Stellen.
# - **Messunsicherheiten** werden auf eine signifikante Stelle gerundet. Eine Ausnahme existiert, wenn die erste Ziffer eine "1" ist, weil sonst Rundungsfehler schnell zu groß werden. Beispiel: $u(g) = 0,1562\,\mathrm{m/s^2} = 0,16\,\mathrm{m/s^2}$. Die Darstellung $g = (9,81 \pm 0,1562)\,\mathrm{m/s^2}$ wäre unsinnig, da die Genauigkeit auf zwei Nachkommastellen durch den Messwert beschränkt ist. 
# - **Messwerte** werden so angegeben, dass die letzte signifikante Stelle die gleiche Größenordnung hat, wie die Messunsicherheit: Die Angabe $H=(13,13\pm 1)\,\mathrm m$ ist sinnlos, richtig wäre $H=(13\pm 1)\,\mathrm m$.
# 
# Um Rundungsfehler zu reduzieren, führen Sie in den Berechnungen so viele signifikante Stellen der Messunsicherheit mit, wie nötig.
# 
# ## Grafische Darstellung eines Messwertes mit Messabweichung
# 
# Die grafische Darstellung eines solchen Messwertes in einem Diagramm kann im folgenden Code-Block ausgeführt und angesehen werden. Prinzipiell gilt, dass für jeden Messwert in der Regel ein solcher **Fehlerbalken** stets anzugeben ist. 

# In[1]:


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
#plt.xkcd()
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


# ## Diskrepanz und Konsistenz
# 
# Die Diskrepanz zweier Messwerte derselben Größe ist der Absolutbetrag ihrer Differenz. Zwei Messungen sind konsistent, wenn ihre Diskrepanz geringer ist, als die (kleinere der) Messunsicherheiten:
# - $g = (9,73 \pm 0,05)\,\mathrm{m/s^2}$ und $g = (9,76 \pm 0,04)\,\mathrm{m/s^2}$ sind *konsistent*, nicht jedoch $g = (9,71 \pm 0,02)\,\mathrm{m/s^2}$ und $g = (9,76 \pm 0,04)\,\mathrm{m/s^2}$
# - Ist $g = (8.9 \pm 1,5)\,\mathrm{m/s^2}$ das Ergebnis einer Messung des Ortsfaktors, dann ist die Messung zwar nicht sonderlich präzise, aber mit dem Literaturwert von $g = 9,81\,\mathrm{m/s^2}$ vereinbar.

# In[2]:


plt.style.use('default') # Matplotlib Style wählen
plt.figure(figsize=(4,4)) # Plot-Größe
#plt.xkcd()
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

# In[ ]:





# In[ ]:




