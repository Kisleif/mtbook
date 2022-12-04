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
# ### Codierung
# 
# In {numref}`gps` ist im Zeitverlauf die Codierung eines GPS-Signals dargestellt.
# 
# :::{figure-md} gps
# <img src="draw/gps.jpg" alt="gps" width="500px" label = gps>
# 
# Codierung der GPS-Signal. (PRN: Pseudo Random Noise)
# :::
# 
# * Die **Navigations-Nachricht** enthält die Informationen über Position und Zeit, was in eine binäre Zahlenfolge, bestehend aus 0 und 1, umgewandelt wird. 
#     * Die Frequenz des Signals beträgt 50 Hz (50 bit / s)
#     * Die einzelne Bit-Länge beträgt 20 ms
#     * Die Nachricht besteht aus 1500 Bits (= 5 x 30 Bits), dies nennt man auch den **Frame** (*Rahmem*). Jeder Frame besteht aus 5 Subframes mit jeweils 10 Worten mit je 30 bit:
#         * 1. Frame: Uhrenkorrektion, Übertragung alle 30 s
#         * 2. Frame: Bahndaten, Übertragung alle 30 s
#         * 3. Frame: Bahndaten, Übertragung alle 30 s
#         * 4. Frame: Das Refraktionsmodell der aktuellen Ionosphäre
#         * 5. Frame: Die Abweichung zur berechneten Keplerbahn (Almanach), komplette Übertragung der Daten dauert 12,5 Minuten. Der komplette Almanach muss mindestens einmal bei der primären Initialisierung eines Empfängers durchgeführt werden.
#     * Die Gesamtzeit der Übertragung beträgt somit mindestens 30 s (= 1500 x 20 ms) für die aktuelle GPS-Position
#     * Eine Übertragung des *kompletten P/Y-Codes* würde aufgrund der detaillierten Informationen theoretisch 276 Tage benötigen für eine *vollständige* Übermittlung der Daten. In der Praxis sendet jeder Satellit ein 7-tägiges Fragment aus. 
#     
# * Der **PRN** Code ist eine pseudo-Zufallszahlenfolge bestehend aus Nullen und Einsen 
#     * Die Frequenz des PRN Codes beträgt 10,23 MHz, was einer Länge von 29,31m entspricht.
#     * Die Chip-Dauer beträgt 1 us.
#     * Somit besteht ein PRN Code aus 1023 Chips. 
#     
# * **Träger** 
#     * eine Funkwelle mit einer Frequenz von 1575,42 MHz wird verwendet

# In[ ]:




