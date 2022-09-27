#!/usr/bin/env python
# coding: utf-8

# # Frequenzmessung
# 
# Häufig liegen uns frequenzmodulierte Spannungssignale vor. Die Frequenz ist hierbei der Informationsträger und muss ausgelesen werden, um die Messgröße $x$ zu bestimmen. 
# Das Grundprinzip der Frequenzmessung ist in {numref}`F_messung` dargestellt.
# 
# :::{figure-md} F_messung
# <img src="draw/F_messung.jpg" alt="F_messung" class="bg-primary mb-1" width="600px" label = F_messung>
# 
# Grundprinzip der Frequenzmessung.
# :::
# 
# * In der ersten Stufe wird das periodische Eingangssignal in eine binäres Signal mit der gleichen Frequenz umgewandelt. Hierfür werden üblicherweise Operationsverstärker benutzt
# * Dann zählt über eine bestimmte Zeit, die **Torzeit $T$** die **Anzahl $z$** der Perioden.
# * Der Messwert ergibt sich aus dem Verhältnis von gezählten Perioden und der Torzeit:
# 
# $$f_a = \frac{z}{T}$$
# 
# Hierbei können **Zählfehler** passieren, da die Torzeit $T$ unabhängig von der Periodendauer und dem Messsignal ist. D.h. im schlimmsten Fall kann man sich um eine ganze Periode verzählen, weshalb die Messabweichung der Zählung $\Delta z = 1$ ist. Dieses Phänomen ist in {numref}`F_zählung` dargestellt.
# 
# :::{figure-md} F_zählung
# <img src="draw/F_zählung.jpg" alt="F_zählung" class="bg-primary mb-1" width="300px" label = F_zählung>
# 
# Zählfehler
# :::
# 
# Die maximal zu erwartende Quantisierungsabweichung bezogen auf der Frequenzmessung beträgt also 
# 
# $$A = f_a - f_w = \frac{1}{T}$$
# 
# Wenn wir also die Frequenz eines $100\,\mathrm{Hz}$-Signals über eine Torzeit von $1\,\mathrm{s}$ bestimmen (was schon eine verdammt lange Messzeit ist) erhalten wir eine Maximalabweichung von $1\,\mathrm{Hz}$, also 1% bezogen auf den Messwert. Je niederiger die Frequenz, desto länger müssen wir messen, um ein genaues Ergebnise zu erhalten. 

# In[1]:


T = 1000e-3
print('Die maximale Messabweichung beträgt:' ,1/T, 'Hz')


# Bei ganz niedrigen Frequenzen wird deshalb die Periodendauer gemessen, also z.B. von einem Nulldurchgang zum nächsten.
# 
# :::{note} 
# Macht euch vorher Gedanken darüber, welche signifikanten Messabweichungen auftreten können, wenn ihr in bestimmten Frequenzbereichen Messungen vornehmt. Wählt eine sinnvolle Messzeit!
# :::
# 
# 

# In[ ]:




