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
# :::{figure-md} messgroesse
# <img src="draw/messgroesse.jpg" alt="messgroesse" width="600px" label = messgroesse>
# 
# Darstellung der **Messkette**.
# :::
# 
# 
# Wie man an der oben dargestellten Temperaturmessung sieht, sind die Werte, die gemessen werden, nicht *exakt*, sondern weichen von dem *wahren* Wert $x_w$ ab. Dies ist die sogenannte Messabweichung deren Ursache unterschiedliche Gründe haben kann. Sie ist ein Maß für die Qualität der Messung: Desto kleiner die Messabweichung, die *genauer* oder *präziser* ist die Messung. Daher ist es wichtig, dass jeder Messwert, $x$, stets mit einer Messabweichung, $A$ oder häufig auch mit $\Delta x$ bezeichnet, versehen wird. Man schreibt dann:
# 
# $$x \pm \Delta x$$
# 
# wobei $\Delta x$ die *absolute Messabweichung* ist und dieselbe Einheit wie der eigentliche Messwert besitzt. 
# 
# Die *relative Messabweichung* wird auf einen Referenzwert bezogen, der häufig der Messwert $x$ ist:
# 
# $$\Delta x_\mathrm{relativ} = \frac{\Delta x}{x}$$
# 
# Die Einheit der relativen Messabweichung ist somit *einheitenlos* und wird häufig in Prozent (%) angeben.
# 
# Früher hat man statt *Abweichung* noch den Begriff *Messfehler* verwendet. Man dachte, dass man mit genügend Aufwand, Sorgfalt und bestmöglicher Technologie den Fehler vollständig eliminieren könne. Spätestens seit der Theorie der *Quantenphysik* ist uns allerdings bekannt, dass zufällige Einflüsse auf die beobachteten Messgrößen  unvermeidlich sind und auch nicht vorhergesagt werden können. Statt eines einzig *wahren* Wertes, $x_w$, werden in der Quantenphysik Messgrößen durch deren Erwartungswerte vorhergesagt. Diesen Messgrößen liegt eine Wahrscheinlichkeitsdichte zu Grunde, dessen Varianz (bzw. Standardabweichung) nicht verschwindet! Somit werden für ein und dieselbe physikalische Messgröße verschiedene Ergebnisse gemessen, obwohl nahezu identische Bedingungen herrschen. Das Eintreten eines bestimmten Messergebnisses ist an eine bestimmte Wahrscheinlichkeit gekoppelt, mit der dieses Ergebnis eintritt. 

# :::{admonition} Aufgabe
# :class: tip
# Wie groß ist die in {numref}`messgroesse` dargestellte absolute und relative Messabweichung?
# :::

# In[1]:


import numpy as np
x_wahr = 24.1286941
x_gemessen = 25.01
dx_absolut = np.abs(x_gemessen - x_wahr)

print('Die absolute Messabweichung beträgt: ', dx_absolut, '°C')
print('Die relative Messabweichung beträgt: ', dx_absolut/x_gemessen, ' = ', dx_absolut/x_gemessen*100, '%')


# :::{admonition} Lösung
# :class: tip, dropdown
# Die Differenz zwischen *wahren* und *gemessenen* Wert beträgt $\Delta x = 0,88°C$. Bezogen auf den Messwert beträgt die relative Messabweichung 3,52%.
# :::

# ## Typen von Unsicherheiten
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
# ### Typ A-Unsicherheiten ("Zufällige Fehler")
# 
# Dies sind Messunsicherheiten, die nicht einseitig gerichtet sind, sondern einer zufälligen Streuung der Messwerte zugrunde liegen. Zur Behandlung dieser Messunsicherheiten nutzt man die Stochastik (Wahrscheinlichkeitslehre und Statistik). 
# * Zufällige Fehler kennt man nicht, er ist folglich **nicht korrigierbar**
# * Sie sind unter gleichen Messbedingungen auch **nicht reproduzierbar** 
# * Sie machen ein Ergebnis **unpräzise**
# * Es sind **wiederholte Messungen und statistische Analysen** notwendig, wodurch Mittelwert und Standardabweichung von sogenannten *Stichproben* ermittelt wird. 
# 
# Wie gewinnt man aus einer Messreihe $x_j$ den besten Schätzewert, der mit maximaler Wahrscheinlichkeit am nähesten am *wahren* Wert, $x_w$, liegt? Mit welcher Wahrscheinlichkeit liegt das Messergebnis innerhalb eines bestimmten Intervalls um den wahren Wert, $x = x_w + \Delta x ?$ Hiermit befassen wir uns im Kapitel [Statistische Größen](1_Mittelwert_StdAbw).
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
# Es gibt keine allgemeingültige Definition oder allgemeine Verfahren zur Korrektur. Das heißt für jeden Fall müssen neue Verfahren entwickelt werden.

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
# wobei $A_r$ zufällige und $A_s$ systematische Messabweichungen sind. Ein Messwert setzt sich also zusammen aus dem *wahren* oder *richtigen* Wert, den wir niemals kennen werden, und der Messabweichung. Es gelten folgende Zusammenhänge:
# 
# * Der **ermittelte Messwert** lässt sich wie folgt schreiben, wobei $x_w$ der *wahre*, aber uns unbekannte, Wert ist. $A$ ist die Messabweichung: 
# 
# $$x = x_w + A$$
# 
# * Die **absolute Messabweichung** ergibt sich aus Umstellen der Gleichung:
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

# In[2]:


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

# In[3]:


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
