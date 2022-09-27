#!/usr/bin/env python
# coding: utf-8

# # Leistungsmessung
# 
# Wir kennen nun bereits die Prinzipien zur Spannungs- und Strommessung. Der elektrische Stromnfluss dient dazu, Systeme anzutreiben, die **elektrische Leistung (in der Einheit Watt, W)** benötigen, wie z.B. einen Elektromotor. 
# Um die Leistung in einem Schaltkreis zu bestimmen, müssen wir gleichzeitig die Spannung $U$ und Stromstärke $I$ messen. Das Grundprinzip der Leistungsmessung ist in {numref}`leistungsmessung_motor_stromrichtig` dargestellt. Diese beiden Messgrößen werden anschließend miteinander multipliziert. 
# 
# :::{figure-md} leistungsmessung_motor_stromrichtig
# <img src="draw/leistungsmessung_motor_stromrichtig.jpg" alt="leistungsmessung_motor_stromrichtig" class="bg-primary mb-1" width="300px" label = leistungsmessung_motor_stromrichtig>
# 
# Schaltung zur Messung elektrischer Leistungen.
# :::
# 
# ## Leistungsmessung bei Gleichstrom
# 
# Bei Gleichstrom gilt folgendes: 
# 
# $$P = U \cdot I$$
# 
# Es gibt verschiedene Messgeräte, die bereits intern eine Spannungs- und Stromstärkemessung integriert haben. Manche Geräte haben nur einen Ein- und Ausgang und man muss sich über die Beschaltung keine Gedanken machen, da es nur eine Möglichkeit gibt. Andere Messgeräte bieten die Flexibilität selber entscheiden zu können, wo Volt- und Amperemeter in der Schaltung angeschlossen werden können. Hierbei gibt es zwei Möglichkeiten:
# 
# * **Stromrichtige** Leistungsmessung: Die Spannungsmessung erfolt an der Quelle und die Strommessung direkt am Verbraucher. 
# * **Spannungsrichtige** Leistungsmessung: Die Spannungsmessung wird an dem Verbraucher angelegt und somit *richtig* gemessen. 
# 
# Bei der Messung zwischen diesen beiden Varianten wird es zu relevanten Unterschieden kommen, die das Messergebnis und die Abweichung beeinflussen.
# 
# ### Stromrichtige Leistungsmessung
# 
# In {numref}`stromrichtig_innen` ist die *stromrichtige* Beschaltung der Leistungsmessung gezeigt, wobei die Innenwiderstände der einzelnen Messgeräte, $R_V$ und $R_A$ angegeben sind. Der Verbraucher hat den Widerstand $R_L$ (Last-Widerstand). Rechts daneben ist ein Ersatzschaltbild der stromrichtigen Leistungsmessung skizziert.  Die Stromstärke wird direkt (*richtig*) am Motor, an der Last, gemessen. 
# 
# :::{figure-md} stromrichtig_innen
# <img src="draw/stromrichtig_innen.jpg" alt="stromrichtig_innen" class="bg-primary mb-1" width="500px" label = stromrichtig_innen>
# 
# Stromrichtige Schaltung zur Messung elektrischer Leistungen.
# :::
# 
# Die Messeingänge liefern die Messgräßen $U$ und $I$, woraus wir die Leistung ermitteln:
# 
# $$P = U \cdot I = (U_{R_A} + U_{R_L}) \cdot I = R_A \cdot I^2 + U_{R_L} = P_{R_A} + P_{R_L}$$
# 
# In dieser Anschaltung wird nicht nur der Spannungsabfall an der Last, sondern fälschlicherweise auch am Strommessgerät. Dadurch wird ebenfalls der Leistungsverbrauch am Innenwiderstand $R_A$ des Strommessgeräts gemessen. 
# Hierbei handelt es sich allerdings um eine systematisch Abweichung, die korrigiert werden kann. Im Datenblatt des Strommesseingangs wird der Innenwiderstand abgelesen oder extern ermittelt. Die systematisch Messabweichung ergibt sich zu
# 
# $$A = R_A \cdot I^2$$
# 
# und muss daher nur noch mit dem Quadrat der gemessenen Stromstärke multipliziert werden. 
# Anhand dieser Gleichung für die Messabweichung erkennt man, dass **je kleiner der Innenwiderstand $R_A$, desto kleiner die Messabweichung**. 
# 
# 
# ### Spannungsrichtige Leistungsmessung
# 
# In {numref}`spannungsrichtig_innen` ist die *spannungsrichtige* Beschaltung der Leistungsmessung gezeigt, wobei die Innenwiderstände der einzelnen Messgeräte, $R_V$ und $R_A$ angegeben sind. Der Verbraucher hat den Widerstand $R_L$ (Last-Widerstand). Rechts daneben ist ein Ersatzschaltbild der spannungsrichtigen Leistungsmessung skizziert. Die Spannung wird nun direkt (*richtig*) am Motor, an der Last, gemessen. 
# 
# :::{figure-md} spannungsrichtig_innen
# <img src="draw/spannungsrichtig_innen.jpg" alt="spannungsrichtig_innen" class="bg-primary mb-1" width="550px" label = spannungsrichtig_innen>
# 
# Spannungsrichtige Schaltung zur Messung elektrischer Leistungen.
# :::
# 
# In dieser Anschaltung wird nun ein zu hoher Strom gemessen, nämlich der, der durch den Motor fließt und der Stromverlust aufgrund des Innenwiderstands des Spannungsmessgeräts:
# 
# $$P = U \cdot I = U \cdot \left( \frac{U}{R_V} + \frac{U}{R_L} \right) = \frac{U^2}{R_V} + \frac{U^2}{R_L} = P_{R_V} + P_{R_L}$$
# 
# Die Leistungsmessung gibt einen zu hohen Wert aus, der aufgrund des Leistungsverbrauchs des Spannungsmessgeräts anfällt. Auch hierbei handelt es sich um eine systematische Messabweichung, die mit der Kenntnis des Innenwiderstand $R_V$ korrigiert werden kann:
# 
# $$A = \frac{U^2}{R_V}$$
# 
# Sollte die Korrektur nicht vorgenommen werden, so **steigt die Messabweichung indirekt proportional mit $R_V$**, bei gleichbleibender Spannung. 
# 
# :::{admonition} Aufgabe
# :class: tip
# Wie groß ist die Messabweichung für eine stromrichtige, bzw. spannungsrichtige Anschaltung einer Leistungsmessung an einem Lastwiderstand von $R_L = 10\,\Omega$, der mit einer Gleichspannung von $U = 22\,\mathrm{V}$ und einem Nennstrom von $I = 5\,\mathrm{A}$ betrieben wird? Die Innenwiderstände für Spannungs- bzw. Strommesseingang betragen $R_V = 2\,\mathrm{M\Omega}$ und $R_A = 1\,\Omega$. Was ändert sich, wenn wir einen schlechteren Strommesseingang mit $R_A = 10\,\Omega$ verwenden? Die Ausgabe des folgenden Code-blocks liefert euch die Ergebnisse.
# :::

# In[1]:


U = 22 #V Gleichspannung
I = 5 #A Nennstrom
R_L = 10 #Ohm, Innenwiderstand Gleichstrommotor
#print('Ein Gleichstrommotor mit Innenwiderstand R_L =',R_L,'Ohm wird mit', U, 'V Gleichspannung und', I, 'A Nennenstrom betrieben.')
print('Die Leistungsaufnahme am Gleichstrommotor beträgt demnach P =', U*I, 'W.')
R_V = 2e6 #Ohm, Innenwiderstand Spannungsmesseingang
R_A = 1 #Ohm, Innenwiderstand Strommesseingang
#print('Zur Leistungsbestimmung benutzen wir einen Spannungsmesseingang mit einem Innenwiderstand von R_V=',R_V/1e6,'MOhm und einen Strommesseingang mit einem Innenwiderstand von R_A=',R_A,'Ohm.')


print('\n-------- Messabweichung bei gutem Strommesseingang (R_A =',R_A,'Ohm): ------------')

# Stromrichtige Anschaltung:
A_stromrichtig = R_A * I**2

# Spannungsrichtige Anschaltung:
A_spannungsrichtig = U**2 / R_V

print('Stromrichtige Anschaltung: \t P_A=', A_stromrichtig, 'W')
print('Spannungsrichtige Anschaltung: \t P_A=', A_spannungsrichtig, 'W')


R_A = 10 #Ohm, Innenwiderstand Strommesseingang
print('\n-------- Messabweichung bei schlechtem Strommesseingang (R_A =',R_A,'Ohm): ------------')

# Stromrichtige Anschaltung:
A_stromrichtig = R_A * I**2

# Spannungsrichtige Anschaltung:
A_spannungsrichtig = U**2 / R_V

print('Stromrichtige Anschaltung: \t P_A=', A_stromrichtig, 'W')
print('Spannungsrichtige Anschaltung: \t P_A=', A_spannungsrichtig, 'W')


# Nach dem Lösen der Aufgabe sollte euch aufgefallen sein, dass bei einem schlechteren Strommmesseingang sogar mehr Leistung bei der Strommessung verbraucht wird als an dem Motor selber. Die spannungsrichtige Anschaltung liefert hierbei einen deutlichen Vorteil und ist standardmäßig in den vielen Messgeräten bereits genau so eingebaut. Werden die Messströme $I$ jedoch recht klein, so kann die stromrichtige Anschaltung zu ggf. genaueren Messungen und geringerem Leistungsverbrauch führen.
# 
# ### Energieverbrauch
# 
# Eine weitere häufig benutzt Messgröße ist die **elektrische Energie E (in der Einheit Ws)**. Diese gibt an, wie hoch der Verbraucht über eine bestimmte Zeitspanne ist und ist somit ein Maß für die aufgewandte elektrische Arbeit:
# 
# $$E = U \cdot I \cdot t$$
# 
# Besteht eine Zeitabhängigkeit bei $U$ und $I$, so muss man zusätzlich über die Zeit integrieren:
# 
# $$E = \int P(t) dt = \int U(t)\cdot I(t) dt$$
# 
# $U(t)$ und $I(t)$, hier großgeschrieben, sind immer noch Gleichgrößen, die sich zwar mit der Zeit ändern, jedoch keine Wechselgrößen sind. D.h. Kenngrößen wie Gleichrichtwert oder Effektivwert existieren nicht.

# ## Leistungsmessung bei Wechselstrom
# 
# Im Kapitel [Messsignal und Kenngrößen](3_Kenngroessen.ipynb) haben wir uns die Kenngrößen von Wechselgrößen angesehen. Bei der Leistungsmessung von Wechselstromsystemen kommen fast ausschließlich Sinussignale *ohne Gleichanteil* vor. Die Wechselgrößen $u(t)$ und $i(t)$ durch einen Verbraucher können wir also wiefolgt annehmen:
# 
# $$u(t) = \hat u \cdot \sin(\omega t)$$
# 
# und 
# 
# $$i(t) = \hat i \cdot \sin(\omega t + \phi)$$

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
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

A = 1.0   # Amplitude
f = 10    # Frequenz in Hz
phi = 0.  # Phase in radian
T = 1/f   # Perdiodendauer
t = np.linspace(0,2*T,100) # Zeitwerte der Sinusfunktion in sec

fig = plt.figure(figsize=(7,3))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(t,A * np.sin(2*np.pi*f*t + phi), 'tab:blue',label = r'$u(t) = \hat u \cdot \sin(\omega t)$')
ax.plot(t,A * np.sin(2*np.pi*f*t + 1.), 'tab:red', label = r'$i(t) = \hat i \cdot \sin(\omega t + \phi)$')
plt.annotate(r'', xy=(0.87*T, 0.25*A), xytext=(1.05*T, 0.25*A), arrowprops=dict(arrowstyle='->'))
plt.annotate(r'$+ \phi$', xy=(0.25*T, 0.25*A), xytext=(0.94*T, 0.35*A))
ax.set_xlabel('Zeit')
ax.set_ylabel('Spannung (V) bzw. Strom (A) ')
ax.set_xlim(0,2*T)
ax.set_xticks([0, T, 2*T])
ax.set_xticklabels(['0','T','2T'])
ax.set_yticks([-A, 0, A])
ax.set_yticklabels([r'$-\hat u, \hat i$','0','$\hat u, \hat i$'])
#ax.set_title(r'u(t) =%5.1f $\cdot$ sin(%5.1f Hz $\cdot t$ + $\phi$)' %(A, 2*np.pi*f))
ax.grid()
ax.legend()
plt.show()


# Die Phasenverschiebung des Stroms um $\phi$ ist je nach elektronischer Komponente unterschiedlich:
# 
# * bei einem rein **ohmschen Verbraucher**, wie z.B. einem Widerstand oder Heizmatte, ist $\phi = 0$
# * bei einer **idealen Spule (Induktivität)** ist $\phi = -90^\circ$
# * bei einem **idealen Kondensator (Kapazität)** ist $\phi = +90^\circ$
# 
# Ein negatives Vorzeichen bedeutet, dass sich das Stromsignal auf der Zeitachse nach rechts verschiebt. Im Bild oben handelt es sich um einen nicht idealen Kondensator mit weniger als $\phi = +90^\circ$ Phasenverschiebung.  Dies kommt in Schaltungen vor, die auch andere Komponenten besitzen. Die Gesamtcharakteristik ist jedoch kapazitiv. 
# 
# ### Wirkleistung
# 
# Um die **Leistung $P$** zu bestimmen, wir in einem Verbraucher wirkt, müssen wir die Momentanleistungen über eine Perdiode $T$ mitteln. Die **Momentanleistung** ergibt sich aus der Multiplikation der zu dem Zeitpunkt angenommen Strom- bzw. Spannungswerte, also folgt für die gemittelte Leistung:
# 
# $$
# \begin{align}
# P &= \frac{1}{T} \int_0^T \hat u \cdot \sin(\omega t) \cdot \hat i \cdot \sin(\omega t + \phi) dt \\
# &= \frac{1}{2T} \hat u \hat i \int_0^T \left[ \cos(-\phi) - \cos(2\omega t + \phi) \right] \\
# &= \frac{\hat u}{\sqrt{2}} \cdot \frac{\hat i}{\sqrt{2}}\cdot \cos(\phi) \\
# &= u_\mathrm{eff} \cdot i_\mathrm{eff} \cdot \cos(\phi)
# \end{align}
# $$
# 
# :::{admonition} Aufgabe
# :class: tip
# Beweise die obige Formel für die Leistung $P$. Verwende für den ersten Schritt das Additionstheorem
# 
# $$\sin x \sin y = \frac{1}{2}\left[ \cos(x-y) - \cos(x+y) \right]$$
# 
# Was gilt für das Integral der 2. Cosinus-Funktion über eine Periode $T$?
# :::

# Die Leistung kann also direkt aus den Effektivwerten der Wechselgrößen bestimmt werden, sofern die Phasenverschiebung $\phi$ bekannt ist. 
# 
# :::{warning} 
# Achtung, die Formel gilt nur bei Sinusschwingungen!
# :::
# 
# Diese Leistung nennt man auch **Wirkleistung** im Verbraucher, und $\cos(\phi)$ nennt man auch **Leistungsfaktor oder Wirkfaktor, Wirkleistungsfaktor**.
# 
# ### Messung der Wirkleistung
# 
# Um im Labor die Wirkleistung zu messen, müssen wir die beiden Effektivwerte für Spannung und Strom bestimmen, sowie die Phasenbeziehung zwischen den beiden Wechselgrößen, und zwar bei genau des Messfrequenz $f$. Hierfür gibt es verschiedene Varianten:
# 
# * es werden Zeitserien für die beiden Wechselgrößen mit einem Oszilloskop aufgenommen
# * es können theoretische Betrachtungen über das innere des Verbrauchers gemacht werden (wenn es denn seitens des Herstellers überhaupt möglich ist). Dies benötigt aber ein gewisses elektrotechnisches Know-How
# * viele Verbraucher werden mit 230V Wechselspannung betrieben und der Leistungsfaktor ist seitens des Herstellers hierfür direkt angegeben. In Deutschland haben wir eine Netzfrequenz von 50Hz, wofür der Leistungsfaktor dann gilt. Typischerweise liegt der Wert zwischen 0.85-0,95.
# 
# ### Stromrichtige und spannungsrichtige Anschaltung
# 
# Die Betrachtungen, die wir weiter oben für die Leistungsmessung mit Gleichstrom, gemacht haben, gelten unverändert auch für Leistungsmessungen im Wechselstromssystem. Auch hier gibt es stromrichtige und spannungsrichtige Anschaltungen. 
# 
# ### Blindleistung
# 
# Zusätzlich zur Wirkleistung gibt es noch die **Blindleistung**. Befinden sich beispielsweise Induktivitäten im Verbraucher, so wir diesen ein periodischer Strom zugeführt, der das magnetische Feld in der Spule erzeugt. Beim Zusammenbruch des magnetischen Feldes wird dieser Strom zurück gespeist. Das gleich gilt auch für Kapazitäten und elektrische Felder. Das heißt es existieren **Blindströme**, die im Leitungsnetz zwischen Quelle und Verbraucher hin und her pendeln. Die korrespondierende **Blindleistung** werden jedoch nicht in Arbeit umgesetzt und *wirken* daher nicht im Verbraucher, wie es bei der *Wirkleistung* der Fall ist. Es handelt sich jedoch um *echte* Leistungen, weshalb sie das Leitungsnetz entsprechend *belasten* und beim Design von Schaltungen berücksichtigt werden müssen. 
# 
# Die Blindleistung wird mi t $Q$ angeben und berechnet sich ähnlich wie die Wirkleistung. nur wird der Cosinus durch einen Sinus ausgetauscht:
# 
# $$Q = u_\mathrm{eff} \cdot i_\mathrm{eff} \cdot \sin(\phi)$$
# 
# $Q$ wird oftmals in der **Einheit Var (var)** angegeben.
# 
# ### Scheinleistung
# 
# Die Scheinleistung, $S$, ist die vektorielle Addition von Wirk- und Blindleistung:
# 
# $$S = \sqrt{P^2 + Q^2} = u_\mathrm{eff} \cdot i_\mathrm{eff}$$
# 
# $S$ wird oftmals in der **Einheit Voltampere (VA)** angegeben.
# 
# ### Energieverbrauch
# 
# Der Energieverbrauch in einem Wechselstromsystem berechnet sich zu
# 
# $$E = \int P(t) dt = \int u_\mathrm{eff} \cdot i_\mathrm{eff} \cdot \cos(\phi) dt$$

# ## Leistungsmessung in Drehstromsystemen
# 
# Wenn man einen Verbraucher hat, der einen etwas höheren Leistungsverbrauch hat, wie z.B. Kochherde, werden diese üblicherweise nicht mit dem 230V-Wechselstromnetz betrieben. Statt dessen nutzt man den sogenannten **Drehtstrom (oder auch Dreiphasenwechselstrom, oder Kraftstrom)**. Maschinen in der Industrie werden fast nur mit Drehstrom betrieben. 
# 
# :::{figure-md} drehstrom_netz
# <img src="draw/drehstrom_netz.jpg" alt="drehstrom_netz" class="bg-primary mb-1" width="300px" label = drehstrom_netz>
# 
# Anschluss eines Verbrauchers, einer Last, an ein Drehtstromnetzwerk.
# :::
# 
# In {numref}`drehstrom_netz` der Anschluss eines Verbrauchers an das Drehstromnetzwerk dagestellt. Über drei **Außenleiter $L_1, L_2, L_3$** wird der Verbraucher versorgt und  der **Neutralleiter $N$** dient als gemeinsame Rückführung.
# 
# Der Verlauf der *drei Phasen* mit jeweils 50Hz Netzfrequenz ist in folgendem Diagramm in Bezug auf den Neutralleiter dargestellt:

# In[3]:


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
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

A = 1.0   # Amplitude
f = 50    # Frequenz in Hz
phi = 0.  # Phase in radian
T = 1/f   # Perdiodendauer
t = np.linspace(0,2*T,100) # Zeitwerte der Sinusfunktion in sec

fig = plt.figure(figsize=(7,3))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.plot(t,A * np.sin(2*np.pi*f*t + phi), 'tab:blue',label = r'$u_{1N}(t) = \hat u \cdot \sin(\omega t)$')
ax.plot(t,A * np.sin(2*np.pi*f*t - 2*np.pi/3), 'tab:red', label = r'$u_{2N}(t) = \hat u \cdot \sin(\omega t - 120^\circ)$')
ax.plot(t,A * np.sin(2*np.pi*f*t - 4*np.pi/3), 'tab:orange', label = r'$u_{3N}(t) = \hat u \cdot \sin(\omega t - 240^\circ)$')
#plt.annotate(r'', xy=(0.87*T, 0.25*A), xytext=(1.05*T, 0.25*A), arrowprops=dict(arrowstyle='->'))
#plt.annotate(r'$+ \phi$', xy=(0.25*T, 0.25*A), xytext=(0.94*T, 0.35*A))
ax.set_xlabel('Zeit (s)')
ax.set_ylabel('Spannung (V)')
ax.set_xlim(0,2*T)
ax.set_xticks([0, T, 2*T])
#ax.set_xticklabels(['0','T','2T'])
ax.set_yticks([-A, 0, A])
ax.set_yticklabels([r'$-\hat u$','0','$\hat u$'])
#ax.set_title(r'u(t) =%5.1f $\cdot$ sin(%5.1f Hz $\cdot t$ + $\phi$)' %(A, 2*np.pi*f))
ax.grid()
ax.legend()
plt.show()


# Diese Spannungen werden auch häufig **Sternspannungen** genannt und liegen jeweils 120° außer Phase zueinander. Diese Phasenverschiebung hat einen historischen Hintergrund. Damals hat man klassische Drehstromgeneratoren aus drei, um 120° versetzte, Spulen realisiert. Durch einen rotierbaren Magneten wurde dann sinusförmig Spannungen induziert, mit halt 120° Phasenverschiebung. 
# 
# ### Effektivwert
# 
# In Deutschland und den meisten anderen europäischen Ländern beträgt der Effektivwert der Sternspannung 230V, also genau der gleiche Wert wie im klassichen 230V Haushaltsnetz. Allerdings ist die Strombelastbarkeit deutlich erhöht, indem Leitungen mit größeren Querschnitten verwendet werden. Die **Effektivwerte** zwischen zwei beliebigen Außenleitern betragen immer:
# 
# $$u_{12} = u_{23} = u_{31} = 230\,\mathrm V \cdot \sqrt{3} \approx 400\,\mathrm V$$
# 
# Daher kommt auch der umgangssprachliche Begriff 400V-Drehstrom. 
# 
# :::{admonition} Aufgabe
# :class: tip
# Wenn 230V der Effektivwert unseres Haushaltsstroms sind, welche Amplitude $\hat u$ hat dann die Sinusspannung?
# :::
# 
# ### Wirkleistung
# 
# In {numref}`drehstrom_wirk` ist dargestellt, wie die Wirkleistung in einem Drehstromnetzwerk gemessen wird. 
# 
# :::{figure-md} drehstrom_wirk
# <img src="draw/drehstrom_wirk.jpg" alt="drehstrom_wirk" class="bg-primary mb-1" width="500px" label = drehstrom_wirk>
# 
# Messung der Wirkleistung in einem Drehstromnetzwerk.
# :::
# 
# Wie auch bei der klassichen Wirkleistungsmessung wird parallel Strom und Spannung gemessen, bzw. deren Effektivwerte natürlich. Aus den Effektivwerten wird dann jeweils die Wirkleistung in jedem Außenleiter bestimmt:
# 
# $$P = u_\mathrm{eff} \cdot i_\mathrm{eff} \cdot \cos(\phi)$$
# 
# Die Gesamtleistung ergibt sich aus der Summe der Einzelmessungen:
# 
# $$P = P_1 + P_2 + P_3$$
# 
# Auch hier gelten wieder die Regeln und abweichungen für strom- bzw. spannungsrichtige Anschaltung der Messinstrumente während der Leistungsmessung. 

# In[ ]:




