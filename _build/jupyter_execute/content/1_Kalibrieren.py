#!/usr/bin/env python
# coding: utf-8

# # Messsysteme kalibrieren
# <a id="Sec-Kalibrieren_und_Eichen_und_Prüfen"></a>
# 
# Es gibt verschiedene Sprachlichkeiten in der Messtechnik, die im Folgenden einmal kurz definiert werden, da es hier in der Umgangssprache häufig zu Unkorrektheiten kommt. Der Unterschied zwischen *messen* und *prüfen* ist nicht immer klar. Im technischen Bereich versteht man unter **prüfen**, ob ein Prüfgegenstand bestimmte Vorgaben erfüllt. Diese werden dann auch in Form von Prüfbedingungen spezifiziert. Zum Beispiel kann man auf elektromagnetische Verträglichkeit (EMV) prüfen. Diese werden in Normen festgehalten, welche wiederum ganz konkrete Randbedingungen für Messaufbauten - zur Messung von elektromagnetischen Störungen - bei Messgeräten gegeben sein müssen. Messgeräte können also darauf geprüft werden, ob diese Normen eingehalten werden und die Messungen entsprechend durchgeführt und ausgeführt werden. Prüfen ist also etwas mehr, als nur das Messen einer Größe. 
# 
# ## Kalibrieren und Eichen
# <a id="SubSec-Kalibrieren_und_Eichen"></a>
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Messgeräte kalibrieren | Was ist der Unterschied zwischen Kalibrierung, Eichung und Justage? (WIKA Gruppe)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/QJuB-Sijdu0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Messsysteme haben bekannterweise Messgenauigkeiten (darauf kommen wir später noch mal zurück), welche eine Messung limitieren. Die erzielbare Messgenauigkeit kann werksseitig während des Herstellprozesses oder später, in der gewünschten Testumgebung, verbessert werden. Hierzu benötigt man eine *bekannte* Referenz, die an das Messgerät angeschlossen werden kann. Nun kann das Messsystem entweder eingestellt werden, sodass der angezeigte Messwert möglichst genau dem *bekannten* Referenzwert entspricht. Dieses Verfahren nennt man auch **Justieren** oder **Kalibrieren**.
# 
# :::{figure-md} eichung
# <img src="draw/eichung.jpg" alt="eichung" class="bg-primary mb-1" width="600px" label = eichung>
# 
# Die Kalibrierung eines Messystems kann auf zwei Arten und Weisen entstehen: Entweder durch den Vergleich mit einem zusätzlichen Präzisionsmessgerät (links) oder durch Vermessung eines *Normals*, was den *wahren* Wert wiederspiegelt (rechts). 
# :::
# 
# Unter dem Begriff **Eichen** hingegen versteht man die Prüfung und Stempelung eines Messgeräts, welches nach gesetzlichen Eichvorschriften erfolgt ist. Geeicht werden müssen Messsysteme, die im gewerblichen Verkehr oder Handel eingesetzt werden sollen, wie z.B. eine Obst- und Gemüsewaage an der Kasse eines Supermarktes. Dem Verbraucher wird damit eine bestimmte Sicherheit gegeben, dass die Waage - innerhalb bestimmter Grenzen - genau arbeitet. In Deutschland existiert dafür die sogenannten *Mess- und Eichverordnung*
# (Die Mess- und Eichverordnung löste 2015 die *Eichordnung* ab, um sich internationalen Standards anzupassen).
# Da das Eichen ein hoheitlicher Akt ist, kann es nur in vom Statt autorisierten Behörden durchgeführt werden, in den sogenannten Eichämtern, und muss in bestimmten Abständen wiederholt werden. Um generell eine möglichst gute Genauigkeit und hohe Manipulationssicherheit sicherzustellen, werden die meisten Messgeräte bereits während des Herstellungsprozesses kalibirert oder geeicht. In Deutschland macht dies häufig die Physikalisch-Technische Bundesanstalt (PTB) in Braunschweig und Berlin. 
# 
# ## Normale
# <a id="SubSec-Normale"></a>
# 
# Normale sind Maßverkörperungen, welche einfach handhabbar sind und von Basisgrößen abzuleiten sind. 
# Wir wissen, dass die Basiseinheiten - bzw. die von ihnen abgeleiteten Einheiten - über atomare Naturkonstanten definiert sind. Dies ist in der Praxis allerdings sehr unpraktisch und in Betrieben nicht realisierbar. 
# Im BIPM (Internationales Büro für Maß und Gewicht) werden praktisch anwendbare **Primärnormale** direkt von Basisgrößen abgeleitet und hergestellt. Diese werden ständig überwacht, um deren Genauigkeit sicherzustellen. Für so ziemlich jede Messgröße existieren solche Primärnormale, wie z.B. für Ohm, Volt, Henry, Farad usw.
# Alle Staaten, die damals bei der Generalkonferenz für Maß und Gewicht den Vertrag unterzeichnet haben, erhalten jeweils ein solches Primärnormal. Von diesen werden dann sogenannte **Sekundärnormale** innerhalb der Staaten abgeleitet, welche dann wiederum zur Eichung von betrieblichen Arbeitsnormalen in Eichlaboren (oder Behören oder Ämtern) zur Verfügung stehen. 
# **Arbeitsnormale**, abgeleitet von den Skundärnormalen, werden in Firmen verwendet, um ihre betrieblichen Messmittel eigenhändig kalibrieren zu können. 
# 
# :::{figure-md} normal
# <img src="draw/normal.jpg" alt="normal" class="bg-primary mb-1" width="600px" label = normal>
# 
# Die verschiedenen Stadien eines *Normals* für verschiedene Anwendungen und Benutzer. 
# :::
# 

# In[ ]:




