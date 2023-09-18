#!/usr/bin/env python
# coding: utf-8

# # Einführung in die Messtechnik
# 
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/nuuRDvRqePg?si=zK4wNP_FB-8r-yKe" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# Ein Messobjekt hat eine bestimmte **Messgröße** $x$ (physikalische Größe, Temperatur, Stromstärke, ..., chemische Messgröße, ...) von welcher der Messwert bestimmt werden soll. Hierfür wird ein Verfahren benötigt, um die Größe zu extrahieren, was durch ein passendes Messgerät geschieht. 
# 
# ## Messgröße, -wert und -kette
# 
# In {numref}`messgroesse` wird ist das Beispiel einer Messkette für eine Temperaturmessung gezeigt. An einem bestimmten Ort herrschende **Messgröße**, hier 24,1286941…°C, wird mittels eines geeigneten Aufbaus in einen **Messwert** von 25,01°C überführt. 
# Der Messwert kann uns direkt angezeigt werden oder er kann in nachfolgenden elektronischen Systemen zur Weiterverarbeitung in geeigneter Form zugeführt werden. 
# 
# :::{figure-md} messgroesse
# <img src="draw/messgroesse.jpg" alt="messgroesse" width="600px" label = messgroesse>
# 
# Darstellung der **Messkette**.
# :::
# 
# ## Messsignal
# 
# Von einem **Messsignal**, $x_1$ (im Gegensatz zur Begrifflichkeit *Messgröße*) spricht man, wenn direkt mit der Messgröße zusammenhängende elektrische Signale zwischen den beiden Stellen, an denen Messgröße und Messwert anfallen, gemessen werden (zum Beispiel das Kabel in der Skizze). Messsignale tragen die Information über die Messgröße, welche auf unterschiedlichste Weise realisiert werden z.B. als analoger Spannungs- oder Stromwert, als frequenzmoduliertes Signal, als Digitalwort oder ähnliches. Häufig bezeichnet man mit einem Signal einen zeitabhängigen Messwert, d.h. $x_1(t)$. 
# 
# ## Einheit 
# 
# Wird ein Messwert, $x$, bestimmt, so entspricht dieser im Rahmen der Messtechnik einem Vielfachen, $n$, von einer Einheit, $E$:
# 
# $$ x = n \cdot E$$
# 
# Ein Messgerät bestimmt ein Vielfaches einer Einheit. Damit dies überall auf der Welt gleich gut funktioniert muss ein Messgerät entsprechend *geeicht* oder *kalibriert* werden. 
# Außerdem gibt es auch noch den Begriff des *Justierens*. Dieser beschreibt die Anpassung eines Messgerät an verschiedene Umgebungen. Evtl. müssen Messgeräte bei unterschiedlichen Temperaturen anders behandelt werden und entsprechend *einjustiert* werden.
# 
# ## Blockdiagramme
# 
# Häufig werden Prozesse in der Messtechnik mittels **Blockdiagrammen** dargestellt. Für die Messkette in {numref}`messgroesse` würde das Blockdiagramm wie in {numref}`messsystem_block`  dargestellt aussehen:
# 
# :::{figure-md} messsystem_block
# <img src="draw/messsystem.jpg" alt="messsystem" width="600px" label = messsystem_block>
# 
# Blockdiagramm der Messkette.
# :::
# 
# ## Beispiel: Prozess einer Heizungsregelung
# 
# In diesem Beispiel spielt Messtechnik eine entscheidende Rolle. In einem Gebäude sind Temperatursensoren installiert, die kontinuierlich die Raumtemperatur ($T$) messen. Diese gemessene Temperatur ($T$) wird als Eingangsgröße in das System eingebracht. Das System verarbeitet diese Eingangsgröße, die als $\hat{x}$ bezeichnet wird, und ermittelt die Differenz $T-\hat x$ zwischen der gemessenen Temperatur und der Solltemperatur.
# 
# Diese Differenz wird dann einem Regler zugeführt, der eine bestimmte Regellogik implementiert. Wenn die gemessene Temperatur zu niedrig ist, bedeutet dies, dass es zu kalt im Raum ist. Infolgedessen wird der Regler entscheiden, die Heizung zu aktivieren, um die Temperatur zu erhöhen. Die Heizung wird somit als Aktor verwendet, um die Temperatur im Raum zu regulieren. 
# 
# Nachdem die Heizung aktiviert wurde, wird die Temperatur erneut gemessen, und der Prozess setzt sich fort. Dieses Beispiel veranschaulicht auf anschauliche Weise die grundlegenden Prinzipien der Messtechnik, die darin bestehen, physikalische Größen zu erfassen (in diesem Fall die Temperatur), sie zu analysieren, zu steuern und zu regulieren, um einen gewünschten Zustand oder eine Solltemperatur zu erreichen. Dieses Konzept des Messens, Regulierens und Steuerns ist ein charakteristisches Merkmal der Messtechnik und wird in einer Vielzahl von Anwendungen eingesetzt.
# 
# :::{figure-md} beispiel_mt
# <img src="draw/beispiel_mt.jpg" alt="beispiel_mt" width="600px" label = beispiel_mt>
# 
# Beispiel-Messkette einer Regelschleife für eine Heizungsregelung.
# :::
# 
# ## Messabweichung
# 
# Wie man an der oben dargestellten Temperaturmessung sieht, sind die Werte, die gemessen werden, nicht *exakt*, sondern weichen von dem *wahren* Wert ab. Dies ist die sogenannte [Messabweichungen](1_Messunsicherheiten.ipynb) deren Ursache unterschiedliche Gründe haben kann. Sie ist ein Maß für die Qualität der Messung: Desto kleiner die Messabweichung, die *genauer* oder *präziser* ist die Messung. Daher ist es wichtig, dass jeder Messwert, $x$, stets mit einer Messabweichung, $\Delta x$, versehen wird. Man schreibt dann:
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

# :::{admonition} Aufgabe
# :class: tip
# Wie groß ist die in {numref}`messgroesse` dargestellte absolute und relative Messabweichung?
# :::
# 
# :::{admonition} Lösung
# :class: tip, dropdown
# Die Differenz zwischen *wahren* und *gemessenen* Wert beträgt 0,88°C, was der absoluten Messabweichung entspricht. Bezogen auf den Messwert beträgt die relative Messabweichung 3,52%.
# :::

# In[1]:


import numpy as np
x_wahr = 24.1286941
x_gemessen = 25.01
dx_absolut = np.abs(x_gemessen - x_wahr)

print('Die absolute Messabweichung beträgt: ', dx_absolut, '°C')
print('Die relative Messabweichung beträgt: ', dx_absolut/x_gemessen, ' = ', dx_absolut/x_gemessen*100, '%')


# In[ ]:




