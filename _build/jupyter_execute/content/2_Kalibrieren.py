#!/usr/bin/env python
# coding: utf-8

# # Kalibrieren und Eichen
# 
# Messgeräte sind unter Umständen unterschiedlichen Belastungen aus der Umgebung ausgesetzt, die sich im Laufe der Zeit unbemerkt auf die Messwerte auswirken können. Ist ein Gerät einmal ungenau geworden, kann dies zu Störungen in Prozessabläufen führen oder sogar gravierende Sicherheitsrisiken verursachen, was häufig mit hohen Kosten verbunden ist. Daher ist eine regelmäßige Überprüfung und Kalibrierung empfehlenswert und oft vorgeschrieben.
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
# ## Unterscheidung zwischen Messen, Prüfen, Kalibrieren und Eichen
# 
# In der Messtechnik ist es wichtig, zwischen verschiedenen Begrifflichkeiten zu unterscheiden, da in der Umgangssprache häufig Unklarheiten auftreten. Ein grundlegender Unterschied besteht zwischen dem **Messen** und dem **Prüfen** von Größen.
# 
# - **Messen**: Beim Messen erfasst man den Wert einer physikalischen Größe, ohne eine spezifische Prüfung oder Überprüfung durchzuführen.
# 
# - **Prüfen**: Das Prüfen hingegen bezieht sich auf die Überprüfung, ob ein Prüfgegenstand bestimmte Vorgaben oder Spezifikationen erfüllt. Dabei werden Prüfbedingungen festgelegt, die in Normen oder Standards festgehalten sind. Zum Beispiel kann die elektromagnetische Verträglichkeit (EMV) geprüft werden, wobei konkrete Randbedingungen für Messaufbauten bei Messgeräten definiert sind. Prüfen geht somit über das bloße Messen einer Größe hinaus.
# 
# ## Kalibrieren
# 
# Messsysteme weisen in der Regel Messgenauigkeiten auf, die die Präzision der Messungen begrenzen. Diese Messgenauigkeit kann werksseitig während des Herstellungsprozesses oder später in der gewünschten Testumgebung verbessert werden. Hierzu benötigt man eine **bekannte Referenz**, die an das Messgerät angeschlossen werden kann. Das Messsystem kann dann so eingestellt werden, dass der angezeigte Messwert möglichst genau dem **bekannten** Referenzwert entspricht. Alternativ kann auch ein Präzisionsmessgerät als Referenz benutzt werden, mit dem das zu kalibrierende Gerät verglichen wird. Das Referenzgerät muss genauer als das Messgerät sein und rückführbar sein.
# 
# Mittels der Referenz kann die Messabweichung bestimmt werden. Weicht der gemessene Wert stark von der Referenz ab, wird das Messgerät neu eingestellt, was als **Justieren** bezeichnet wird.
# 
# :::{figure-md} eichung
# <img src="draw/eichung.jpg" alt="eichung" class="bg-primary mb-1" width="600px" label = eichung>
# 
# Die Kalibrierung eines Messystems kann auf zwei Arten und Weisen entstehen: Entweder durch den Vergleich mit einem zusätzlichen Präzisionsmessgerät (links) oder durch Vermessung eines *Normals*, was den *wahren* Wert wiederspiegelt (rechts). 
# :::
# 
# ## Eichen
# 
# Unter dem Begriff **Eichen** versteht man einen speziellen Vorgang der Kalibrierung. Hier wird der Kalibriervorgang durch eine staatliche Stelle beglaubigt. Dies ist beispielsweise beim Verbraucherschutz vorgeschrieben.
# 
# Die Eichung beinhaltet die Prüfung und Stempelung eines Messgeräts, die gemäß den gesetzlichen Eichvorschriften erfolgt. Diese Eichung ist erforderlich, wenn Messsysteme im gewerblichen Verkehr oder Handel eingesetzt werden, wie beispielsweise bei einer Obst- und Gemüsewaage an der Kasse eines Supermarktes. Die Eichung gewährleistet dem Verbraucher eine gewisse Sicherheit, dass das Messgerät innerhalb bestimmter Toleranzgrenzen genau arbeitet. In Deutschland regelt die **Mess- und Eichverordnung** dieses Verfahren. Das Eichen ist ein hoheitlicher Akt und darf nur in von staatlichen Behörden autorisierten Eichämtern durchgeführt werden. Zudem muss die Eichung in regelmäßigen Abständen wiederholt werden.
# 
# Um eine möglichst gute Genauigkeit und Manipulationssicherheit zu gewährleisten, werden die meisten Messgeräte bereits während des Herstellungsprozesses kalibriert oder geeicht. In Deutschland ist die Physikalisch-Technische Bundesanstalt (PTB) in Braunschweig und Berlin für diese Aufgabe zuständig.
# 
# ## Normale
# 
# Normale sind Maßverkörperungen, die einfach handhabbar sind und von Basisgrößen abgeleitet werden können. Die Basiseinheiten oder von ihnen abgeleitete Einheiten werden in der Praxis oft über atomare Naturkonstanten definiert, was jedoch in vielen Fällen unpraktisch oder unumsetzbar ist.
# 
# Im **BIPM** (Internationales Büro für Maß und Gewicht) werden praktisch anwendbare **Primärnormale** direkt von Basisgrößen abgeleitet und hergestellt. Diese Primärnormale werden kontinuierlich überwacht, um ihre Genauigkeit sicherzustellen. Für nahezu jede Messgröße existieren solche Primärnormale, wie zum Beispiel für Ohm, Volt, Henry, Farad und viele mehr.
# 
# Jedes Land, das den Vertrag bei der Generalkonferenz für Maß und Gewicht unterzeichnet hat, erhält ein solches Primärnormal. Von diesen Primärnormalen werden **Sekundärnormale** innerhalb der Länder abgeleitet. Diese Sekundärnormale dienen wiederum zur Eichung von betrieblichen Arbeitsnormalen in Eichlaboren, Behörden oder Ämtern.
# 
# **Arbeitsnormale** sind Abwandlungen der Sekundärnormale und werden in Unternehmen verwendet, um betriebliche Messmittel eigenständig zu kalibrieren. Damit wird sichergestellt, dass die in der Industrie verwendeten Messgeräte den erforderlichen Genauigkeitsstandards entsprechen.
# 
# :::{figure-md} normal
# <img src="draw/normal.jpg" alt="normal" class="bg-primary mb-1" width="600px" label = normal>
# 
# Die verschiedenen Stadien eines *Normals* für verschiedene Anwendungen und Benutzer. 
# :::
