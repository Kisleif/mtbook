#!/usr/bin/env python
# coding: utf-8

# # Satellitennavigationssysteme
# 
# https://ciechanow.ski/gps/
# 
# 

# ## Positionsbestimmung
# 
# Positionsbestimmung mittels Satellitennavigationssystemen basiert auf dem Messprinzip der Triangulation. 
# Mehrere Satelliten befinden sich einem Orbit der Erde und umkreisen diese. Mit einer bestimmten Rate sendet jeder Satellit seine Uhrzeit und Position regelmäßig aus. Die genaue Uhrzeit erhält jeder Satellit durch eine Atomuhr (tatsächlich sogar zwei, eine Cäsium und eine Rubidium), die an Bord mitfliegt. 
# 
# Ein Empfänger auf der Erde benötigt die Signale von insgesamt vier Satelliten und seine Position möglichst präzise zu bestimmen. Der Empfänger hat seine eigene Zeitbasis und ermittelt für jedes der vier Satellitensignale die Sendezeit. Mittels dieser Laufzeitmessung weiß der Empfänger, in welchem Abstand er sich zu den vier Satelliten befindet, solange die Geschwindigkeit der ausgesandte Satellitensignale als konstant angenommen werden kann:
# 
# $$x_{1,2,3,4} = v \cdot t_{1,2,3,4}$$
# 
# Rein geometrisch kann man sich das so vorstellen, dass jeder der vier Satelliten ein GPS-Signal in Form einer Kugelwelle aussendet. Der Schnittpunkt der vier Kugelwellen ist die Position des Empfängers. Theoretisch würden hierfür auch nur 3 Satelliten ausreichen. Der 4. Satellit dient dazu die mitunter ungenaue Zeitmessung seitens des Empfängers zu verbessern. 
# 
# Es gilt wieder: Je mehr desto besser. Wird die Anzahl der Satelliten erhöht, so können Ungenauigkeiten in der Positionsermittlung reduziert werden. 
# 
# ### Der Einfluss der Relativitätstheorie 
# Während des Flugs eines Satelliten kommen auch relativistische Effekte mit ins Spiel. Bewegt sich eine Uhr so erfährt sie eine Zeitdilaation nach Einsteins spezieller Relativitätstheorie. Bewegte Uhren gehen langsamer gegenüber einee stationären Uhr. Je geringer die Erdumlaufbahn eines Satelliten, desto schneller ist der Satellit und desto größer wird dieser Effekt. Andererseits besagt die Allgemeine Relativitätstheorie, dass Uhren in schwächeren Gravitationsfeldern schneller gehen, was diesem Effekt entgegenwirkt. Diese beiden Effekte sind jedoch nicht immer gleich und hängen von der Absoluthöhe und anderen Parametern ab. Die GPS-Satelliten bewegen sich etwa mit $3,87\,\mathrm{km/s}$ relativ zu Erde, wodurch die Uhren langsamer gehen. Dadurch dass das Erdschwerefeld jedoch mit der Höhe abnimmt, wird dieser Effekt kompensiert, und die Uhren laufen sogar am Ende schneller, um etwa $4,5 \cdot 10^{-10}\,\mathrm s$ pro Sekunde. Dies entspricht $38\,\mathrm{ms}$ pro Tag. 
# 
# ## Geschwindigkeitsbestimmung
# 
# Mittels der Satellitendaten und der Signallaufzeiten lässt sich nicht nur die Position bestimmen, sondern auch die Geschwindigkeit des Empfängers. Hierfür kann entweder die Dopplereffekt im Satellitensignal gemessen werden, oder man differenziert den Ort nach der Zeit. Beides ist nur möglich, nachdem sich der Empfänger bewegt hat!
# 
# ## Satelliten und Umlaufbahnen
# 
# Aktuell gibt es verschiedene Satellitensysteme in Erdumlaufbahnen, die im Einsatz sind:
# 
# * GPS (Global Positioning System), bzw. der ausführliche Name NAVSTAR GPS (Navigational Satellite Timing and Ranging), USA
# * GLONASS (Global Navitation Satellite System), Russland
# * Galileo, Europa
# * BeiDou, China
# 
# Die 25-30 GPS-Satelliten befinden sich auf einer Erdumlaufbahn in etwa 20.200km Höhe, wobei sich deren Position ständig ändert. Es gibt insgesamt 6 Bahnebenen, die um 55° gegen den Äquator geneigt sind. Die Satellitenkonstellation in diesen Bahnebenen wurde so gewählt, dass immer mindestens 4 Satelliten weltweit für die Positionsbestimmung zur Vefügung stehen. 
# Dies gilt jedoch nicht für die Polregionen, hier müssen andere Satellitensysteme anstelle von GPS eingesetzt werden, den Satelliten in anderen Bahnen fliegen. 
# 
# Jeder Satellit umkreist die Erde zweimal in etwa 24h (um genau zu sein innerhalb eines *Sterntags*). 
# 
# Sollte ein Satellit einmal ausfallen, gibt es verschiedene Prozedere:
# 
# * ein neuer Satellit wird gestartet
# * ein schalfender Satellit in der Umlaufbahn wird aktivitiert
# * ein aktiver Satellit wird an eine andere Position manövriert
# 
# Jede dieser Prozeduren ist sehr zeitintensiv und es kann Monate dauern, bis der ausgefallene Satellit ersetzt wird. Satelliten haben sehr schwache Triebwerke und kann sich nicht selber in höhere Umlaufbahnen befördern. Der Treibstoff dient eigentlich nur dafür, dass exakte Position in der Umlaufbahn zu behalten und kann nur begrenzt dafür eingesetzt werden, mittels einer Folge von Brems- und Beschleunigungsmanövern eine neue Position anzusteuern. 
# 
# ## Daten 
# 
# Die Daten für Empfänger auf der Erde werden alle 30s ausgesendet. Die aktuelle Genaugikeit der Positionsbestimmung liegt bei etwa 2m. Mittels Differential-GPS (DPGS) kann die Genauigkeit auf Milimeter verbessert werden! Das DGPS benötigt hierfür eine Referenzstation auf der Erde die sich in der Nähe des Empfängers befindet. An diese Referenzstation sendet der Satellit zusätzliche Daten mit entsprechenden Messabweichungen, die beispielsweise durch die Atmosphärenzusammensetzung und Temperatur verursacht werden. Mittels Sensorik an Bord kann der Satellit diese Messabweichungen abschätzen und zur Verfügung stellen. Der Empfänger kann Kontakt zu der Referenzstation aufnehmen und seine Positionsmessung mittels der Referenzdaten korrigeren. In Deutschland übernimmt diese Aufgabe SAPOS, den Satellitenpositionierungsdienst der deutschen Landesvermessung. Die Korrekturdaten können in einem Internetprotokoll in Echtzeit abgerufen werden (https://sapos.de). 
# 
# Die Position eines Satelliten beinhaltet folgende Informationen (6 Kepler Elemente):
# 
# * Größe und Proportionen der Kepler-Ellipse
#     * Halb-Hauptachse von etwa 26.560km für GPS Satelliten
#     * Ekzentrität von etwa 0,02 oder kleiner für GPS Satelliten
# * Orbitebene:
#     * Inklination/Kippung (z.B. 55° gegenüber des Äquators)
#     * Longitude 
# * Position der Ellipse und des Satelliten:
#     * Perigee Argument
#     * Anomalien
#     
# In Realität reichen diese 6 Parameter jedoch nur bedingt aus, um die genaue Position eines Satelliten zu ermitteln. Externe Störungen, wie z.B. Gravitationseinflüsse von Mond, Sonne und Strahlung  beeinflussen die reale Satellitenbahn. Daher beinhaltet die GPS Nachricht zudem die Rate, mit welcher sich die Parameter ändern. Dadurch kann der Empfänger Korrekturen der Bahntrajektorie durchführen. 
# 
# Dadurch, dass man jetzt die Position des Satelliten im Orbit kenntn, können die x,y,z Koordinaten auf der Erde aus den Kepler-Bahnen bestimmt werden. Die Berechnung wollen wir uns nicht genauer ansehen, doch sie ist mitunter nicht gant trivial, da hierbei auch die Erdrotation miteinbeziehen muss, die vergangen ist, während Sender und Empfänger miteinander kommunizieren. 
# 
# ### Woher kennt der Satellit diese Daten?
# 
# Alle GPS Satellinte werden von Stationen auf der Erde nachverfolgt. Diese Stationen sind Teil des Kontrollsegmentes des GPS Systems, welches die Satelliten und deren Nachrichten überwacht. Alle zwei Stunden werden Orbitparameter und Uhrenjustierungen auf den Satelliten neu hoch geladen. 
# 
# ## Signale
# 
# Der Satellit misst seine eigene Umlaufbahn mit Sensoren an Bord und sendet **Funksignale** mit einer Frequenz von früher 100-500MHz, und heutzutage bis zu 20GHz aus. Diese Radiosignale wird entsprechend codiert, d.h. deren Positionsdaten und andere Informationen werde auf die Radiowelle **aufmoduliert**. 
# 
# * Der Satellit sendet alle 30 s ein Signal aus
# * Die Nachricht wird mit einer Datenrate von 50 bit / s aufgeprägt 
# * Die Nachteinlänge beträgt 1500 Bits
# 
# Diese Daten werden auf zwei Frequenzen ausgesendet:
# 
# * **1575,42MHz**: Dies ist die erste **L1**-Frequenz und überträgt zwei Codes:
#     * für zivile Nutzung (C/A-Code = Coarse/Application)
#     * trennbar-überlagert nicht-öffentliche Codes für die militärische Nutzung (P/Y-Code = Precision/Encrypted)
#     
# * **1227,60MHz**: Dies ist die zweite **L2**-Frequenz und überträgt nur den P/Y-Code für militärische Zwecke. Wahlweise kann auf der zweiten Frequenz auch der C/A-Code übertragen werden. 
#     * Die Übertragung einer zweiten Frequenz erlaubt es Störeffekte aus der Ionosphäre zu eliminieren, die die Übertragungsgeschwindigkeit beeinflussen.
# 
# * **1176,45MHz**: Die ist die dritte **L5**-Frequenz, welche sich im Aufbau befindet. 
# 
# ### Navigations-Nachricht
# 
# In {numref}`gps` ist im Zeitverlauf die Codierung eines GPS-Signals dargestellt.
# 
# :::{figure-md} gps
# <img src="draw/gps.jpg" alt="gps" width="500px" label = gps>
# 
# Codierung der GPS-Signal. (PRN: Pseudo Random Noise)
# :::
# 
# Die **Navigations-Nachricht** enthält die Informationen über Position und Zeit, was in eine binäre Zahlenfolge, bestehend aus 0 und 1, umgewandelt wird. 
# * Die Frequenz des Signals beträgt 50 Hz (50 bit / s)
# * Die einzelne Bit-Länge beträgt 20 ms
# 
# Die Nachricht besteht aus 1500 Bits (= 5 x 30 Bits), dies nennt man auch den **Frame** (*Rahmen*). Ingesamt gibt es 25 Frames, jeder dieser Frames besteht aus 5 Subframes mit jeweils 10 Worten mit je 30 bit.
# 
# Die ersten zwei Worte jedes Subframes haben immer die gleiche Struktur:
# * 1. Wort im Subframe: **TLM**, dies enthält eine feste Präambel, die leicht zu erkennen ist, und einige Bits zur Überprüfung.
# * 2. Wort im Subframe: Das **HOW** Wort (Handover-Word) ist für die GPS-Funktionalität von entscheidender Bedeutung, da es den Subframe mit einem Zeitstempel versieht, der es dem Empfänger ermöglicht herauszufinden, wann er gesendet wurde.
# 
# Die restlichen 8 Wörter im Subframe enthalten je nach Subframe unterschiedliche Daten. 
# 
# * 1. Subframe enthält die Korrekturen der Satellitenuhr und die Wochennummer der GPS-Zeit, die es dem Empfänger zusammen mit dem feineren Zeitstempel aus dem Übergabewort ermöglichen, die genaue Zeit zu berechnen, zu der die Nachricht gesendet wurde. Dieser Subframe enthält auch ein "Health"-Bit, das angibt, ob sich die Navigationsdaten in einem guten Zustand befinden. Wenn die Umlaufbahn eines GPS-Satelliten angepasst werden muss, schaltet das Kontrollsegment dieses Bit vorübergehend um, um den Empfängern mitzuteilen, dass sie sich nicht auf die Informationen dieses Satelliten verlassen sollten, wenn er seine Position ändert.
# * 2. und 3. Subframe enthalten die bereits erwähnten Bahnparameter, erweitert um Geschwindigkeitsinformationen, die zusammen als Ephemeridenparameter bezeichnet werden - sie ermöglichen es dem Empfänger, die Position des Satelliten zu berechnen.
# * Die letzten beiden Subframes 4. und 5. enthalten die groben Ephemeridendaten für alle Satelliten - diese Sammlung ist als Almanach bekannt. Damit kann der Empfänger ungefähr abschätzen, wann ein neuer Satellit über dem Horizont auftauchen wird. Zu den weiteren Informationen, die in diesen Unterrahmen übertragen werden, gehören der Zustand anderer Satelliten und einige Parameter, mit denen der Empfänger versucht, die ionosphärische Verzögerung zu berücksichtigen. Die komplette Übertragung der Daten dauert 12,5 Minuten. Der komplette Almanach muss mindestens einmal bei der primären Initialisierung eines Empfängers durchgeführt werden.
# 
# Die Gesamtzeit der Übertragung beträgt somit mindestens 30 s (= 1500 x 20 ms) für die aktuelle GPS-Position. Die komplette Übertragung des kompletten Artikels würde 2,5 Stunden benötigen. 
# Eine Übertragung des *kompletten P/Y-Codes* würde aufgrund der detaillierten Informationen theoretisch 276 Tage benötigen für eine *vollständige* Übermittlung der Daten. In der Praxis sendet jeder Satellit ein 7-tägiges Fragment aus. 
# 
# 

# ### Modulation der Nachricht auf den Träger
# Die Navigations-Nachricht wird in eine binäre Zahlenfolge konvertiert, welche auf die Funkwelle aufgeprägt wird. Diese Modulation kann über verschiedene Varianten geschehen, beispielsweise durch Multiplzieren der Trägerwelle (Funkwelle bei GHz-Frequenz) mit der binären Nachrichten-Folge, bestehend aus 0 und 1. 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from scipy import signal
from random import randint, choice
import random

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

num = 2000
fig, ax = plt.subplots(3,1,figsize=(6,3))

line0, = ax[0].plot([], [], lw=2, color = 'tab:blue')
line1, = ax[1].plot([], [], lw=2, color = 'tab:red')
line2, = ax[2].plot([], [], lw=2, color = 'tab:gray')

def init():
    line0.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    return line0, line1, line2


ax[0].set_xlim(0,2)
ax[1].set_xlim(0,2)
ax[2].set_xlim(0,2)
ax[0].set_ylim(-0.1,1.1)
ax[1].set_ylim(-1.1,1.1)
ax[2].set_ylim(-1.1,1.1)

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')

ax[0].set_title('GPS-Nachricht:')
ax[1].set_title('Träger:')
ax[2].set_title('GPS-Nachricht x Träger:')

ax[0].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[1].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[2].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')


def animate(i):
    x = np.linspace(0, 2, num)
    y0 = 0.5*signal.square(2 * np.pi * 1 * (x - 0.01 * i))+0.5
    y1 = np.sin(2 * np.pi * 10* (x - 0.01 * i))
    y2 = (0.5*signal.square(2 * np.pi * 1 * (x - 0.01 * i))+0.5)*np.sin(2 * np.pi * 10* (x - 0.01 * i))
    line0.set_data(x,y0)
    line1.set_data(x,y1)
    line2.set_data(x,y2)
    return line0, line1, line2

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

plt.tight_layout()
plt.close()
HTML(anim.to_jshtml())


# Bei GPS wird **binary phase-shift keying** benutzt. 
# Das binäre Signal aus Einsen und Nullen wird so angepasst, dass jede 0 durch -1 ersetzt wird, und dann wird dieses Signal mit der Trägerwelle multipliziert. Eine Multiplikation mit -1 sorgt für einen Phasensprung (daher auch der Name dieser Methode). 

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from scipy import signal
from random import randint, choice
import random

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

num = 2000
fig, ax = plt.subplots(3,1,figsize=(6,3))

line0, = ax[0].plot([], [], lw=2, color = 'tab:blue')
line1, = ax[1].plot([], [], lw=2, color = 'tab:red')
line2, = ax[2].plot([], [], lw=2, color = 'tab:gray')

def init():
    line0.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    return line0, line1, line2

ax[0].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[1].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[2].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')

ax[0].set_xlim(0,2)
ax[1].set_xlim(0,2)
ax[2].set_xlim(0,2)
ax[0].set_ylim(-1.1,1.1)
ax[1].set_ylim(-1.1,1.1)
ax[2].set_ylim(-1.1,1.1)

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')

ax[0].set_title('Angepasste GPS-Nachricht:')
ax[1].set_title('Träger:')
ax[2].set_title('GPS-Nachricht x Träger:')


def animate(i):
    x = np.linspace(0, 2, num)
    y0 = signal.square(2 * np.pi * 1 * (x - 0.01 * i))
    y1 = np.sin(2 * np.pi * 10* (x - 0.01 * i))
    y2 = (signal.square(2 * np.pi * 1 * (x - 0.01 * i)))*np.sin(2 * np.pi * 10* (x - 0.01 * i))
    line0.set_data(x,y0)
    line1.set_data(x,y1)
    line2.set_data(x,y2)
    return line0, line1, line2


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)


plt.tight_layout()
plt.close()
HTML(anim.to_jshtml())


# Würde es sich um einen einzelnen Satelliten handeln, wäre diese Kodierungsmethode ausreichend, da der Empfänger einfach den Träger aus dem eingehenden Signal entfernen und die Datenbits dekodieren könnte. In Wirklichkeit gibt es viele Satelliten, die gleichzeitig senden, so dass sich die Datenbits von allen überschneiden. Außerdem sind die GPS-Signale, die die Erde erreichen, unglaublich schwach und werden von Rauschen überlagert, so dass eine reine Datennutzlast nicht entziffert werden kann. GPS löst dieses Problem, indem es einen anderen Binärcode verwendet. Dieser Code wiederholt sich im Laufe der Zeit und besteht aus einer vorher festgelegten Anzahl von so genannten Chips. Der Chipping-Code ändert sich mit einer höheren Rate als die Nachrichten-Bits. Um das Signal zu kodieren, multipliziert der Satellit die Datenbits der Navigationsnachricht mit diesem Code. Jeder Satellit hat einen eigenen Code. 
# Auch wenn die Codes wie binäres Zufallsrauschen aussehen, sind sie in Wirklichkeit pseudozufällig, was ihren Namen erklärt - PRN steht für pseudozufälliges Rauschen. Jeder dieser Codes ist gut bekannt und kann leicht nachgebildet werden.

# ### PRN Code
# * Der **PRN** Code ist eine pseudo-Zufallszahlenfolge bestehend aus Nullen und Einsen 
#     * Die Frequenz des PRN Codes beträgt 10,23 MHz, was einer Länge von 29,31m entspricht.
#     * Die Chip-Dauer beträgt 1 us.
#     * Somit besteht ein PRN Code aus 1023 Chips. 
# 
# PRN Codes haben wichtige Eigenschaften:
# 
# * 1. Die Korrelation des Codesignals mit einer Kopie von sich selbst, die **Autokorrelation**, ist nur dann sehr hoch, wenn genau die richtige zeitliche Verzögerung eingestellt wurde. 
# * 2. Die zweite wichtige Eigenschaft ist die **Kreuzkorrelation**, d. h. die Korrelation mit dem Kodierungssignal eines anderen Satelliten, die verschwindend gering ist und man somit Signale unterschiedlicher Satelliten hervoragend voneinander unterscheiden kann. 

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
from scipy import signal
from random import randint, choice
import random

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.xkcd()
plt.rcParams['font.size'] = 10; # Schriftgröße

num = 2000
fig, ax = plt.subplots(5,1,figsize=(6,5))

line0, = ax[0].plot([], [], lw=2, color = 'tab:blue')
line1, = ax[1].plot([], [], lw=2, color = 'tab:green')
line2, = ax[2].plot([], [], lw=2, color = 'tab:cyan')
line3, = ax[3].plot([], [], lw=2, color = 'tab:red')
line4, = ax[4].plot([], [], lw=2, color = 'tab:gray')

def init():
    line0.set_data([], [])
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    return line0, line1, line2, line3, line4

ax[0].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[1].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[2].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[3].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')
ax[4].axhline(y=0, lw = 1, color = 'tab:gray', ls = ':')

ax[0].set_xlim(0,2)
ax[1].set_xlim(0,2)
ax[2].set_xlim(0,2)
ax[3].set_xlim(0,2)
ax[4].set_xlim(0,2)
ax[0].set_ylim(-1.1,1.1)
ax[1].set_ylim(-1.1,1.1)
ax[2].set_ylim(-1.1,1.1)
ax[3].set_ylim(-1.1,1.1)
ax[4].set_ylim(-1.1,1.1)

ax[0].axis('off')
ax[1].axis('off')
ax[2].axis('off')
ax[3].axis('off')
ax[4].axis('off')

ax[0].set_title('GPS:')
ax[1].set_title('PRN:')
ax[2].set_title('GPS x Code:')
ax[3].set_title('Träger:')
ax[4].set_title('GPS x Code x Träger:')

x = np.linspace(0, 200, 100*num)
y0_full = signal.square(2 * np.pi * 1 * x)
y1_full = signal.square(2 * np.pi * 5 * x)*np.random.randint(-1,1)
y2_full = y0_full*y1_full
y3_full = np.sin(2 * np.pi * 10* x)
y4_full = y3_full*y2_full

def animate(i): # i geht bis frames = 200
    x = np.linspace(0, 2, num)
    y0 = signal.square(2 * np.pi * 1 * (x - 0.01 * i))
    y1 = signal.square(2 * np.pi * 10 * (x - 0.01 * i))
    y2 = y0*y1
    y3 = np.sin(2 * np.pi * 20* (x - 0.01 * i))
    y4 = y2*y3
    line0.set_data(x,y0)
    line1.set_data(x,y1)
    line2.set_data(x,y2)
    line3.set_data(x,y3)
    line4.set_data(x,y4)
    return line0, line1, line2, line3, line4


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)


plt.tight_layout()
plt.close()
HTML(anim.to_jshtml())


# ### Zurückgewinnung der GPS-Nachricht
# Angenommen wir haben ein einziges einkommendes sauberes Signal eines Satelliten. Der Empfänger kann die sinusförmige Trägerwelle entfernen und erhält das Signal, das ein Produkt aus der Navigationsnachricht und dem PRN-Code ist. Der Empfänger kann dann eine Kopie des PRN-Codes für einen Satelliten erstellen, den er zu verfolgen versucht, und dann prüfen, ob er einen hohen Korrelationspeak zwischen dem Eingangssignal und dieser Kopie, gemessen in der hervorgehobenen Region, finden kann. Der Empfänger passt den Offset an, bis er einen hohen Unterschied zwischen den Bereichen findet, der ihn wissen lässt, dass er den richtigen Offset-Wert gefunden hat. Nachdem der korrekte Offset gefunden wurde, kann der Empfänger einfach das Vorzeichen dieser Differenz betrachten, um die Datenbits zu dekodieren.
# 
# Der Zeitversatz der PRN-Code-Kopie liefert dem Empfänger zusätzliche Zeitinformationen, die es ihm ermöglichen, die genau verstrichene Flugzeit zu berechnen. Es sei daran erinnert, dass jeder TeiSubframe einer GPS-Nachricht mit einem Zeitstempel von 6 Sekunden versehen ist, was für sich genommen eine erschreckend geringe Genauigkeit wäre.
# Indem wir jedoch verfolgen, wie viele Bits wir gesehen haben, wie viele PRN-Codewiederholungen wir gesehen haben und den Chip-Offset im Code, können wir diese Präzision erheblich verbessern. Der Empfänger weiß, wie viel Zeit jede dieser Komponenten beansprucht, so dass er diese Dauer zu dem am übertragenen, kodierten Zeitstempel hinzufügen kann. So wird jeder Chip oder sogar seine Bruchteile mit einem Zeitstempel versehen. Wenn der Empfänger die Flugzeit misst, kann er mit dieser Methode die Dauer sehr genau berechnen.
# 
# ### Fehlerquellen bei der Datenübertragung
# 
# GPS-Signale propagieren nicht komplett störungsfrei durch die Atmosphäre. Im oberen Teil der Atmosphäre, der Ionosphäre, verursacht die Sonnenstrahlung eine Ionisierung der Gase, wodurch freie Elektronen entstehen, die die Funkwelle verlangsamen. Die Anzahl von freien Elektronen und der Geschwindigkeitsabnahme ist zudem abhängig von der Tageszeit und der Sonnenaktivität. 
# 
# Im untersten Teil der Atmosphäre, der Troposphäre, #ndert sich der Brechungsindex in Abhängigkeit von der Dichte von Gas und Wasserdampf, was die Radiosignale ebenfalls verlangsamt. Insbesondere die Dichte von Wasserdampf variiert sehr stark, wodurch die Verzögerung der Laufzeitmessung sehr unvorhersagbar wird. 
# 
# Die Effekte in beiden Atmosphären und die entsprechenden Laufzeitverzögerungen hängen zudem auch noch von der Weglänge ab, die die Funkwelle durch die Atmosphäre zurück legen muss. Die Weglänge hängt hierbei vom Orbit ab und wie flach die Funkwelle auf der Erde bei einem Empfänger eintrifft. Je flacher der Einfallswinkel, desto länger ist der Weg durch die Atmosphäre. GPS-Empfänger ignorieren daher häufig Daten von Satelliten, deren Signale unter sehr flachen Winkeln eintreffen. 
# 
# Zudem existieren weitere Fehlerquellen, wie z.B. dass die Uhren an Bord der Satelliten nicht perfekt synchronisiert sein können. Auch die Orbitparameter und deren Änderungen weisen eine bestimmte Abweichung auf, wie auch die Position und Zeitstempel, die von den Satelliten empfangen werde. Auf der Erde können Funkwellen relfketiert werden und laufen so längere Strecken bis sie am Empfänger eintreffen. 
# 
# GPS-Empfänger versuchen immer ein Set von 4 Lösungen zu finden, die die 3 Positionskoordination und die Zeit mit minimaler Unsicherheit zu bestimmt. Mit mehr als 4 Satelliten kann die Genauigkeit verbessert werden. 
