#!/usr/bin/env python
# coding: utf-8

# # Strommesseingang
# 
# Im Bild {numref}`strommesseingang` ist dargestellt, wie elektrische Ströme gemessen werden. $R_L$ stellt hierbei einen Lastwiderstand, z.B. den einen Motors oder eines anderen Verbrauchers, dar. 
# 
# :::{figure-md} strommesseingang
# <img src="draw/strommesseingang.jpg" alt="strommesseingang" class="bg-primary mb-1" width="400px" label = strommesseingang>
# 
# Schaltung zur Messung elektrischer Ströme.
# :::
# 
# Der Strom $i$, der gemessen werden soll, fließt nun durch das Messgerät und bestimmt werden. Hierbei wollen wir sicherstellen, dass der Innenwiderstand $R_i$ möglichst klein ist, um die Messabweichung der Strommessung möglichst klein zu halten. Typischerweise liegt der Wert des Innenwiderstands zwischen $0,01\,\Omega$ und $10\,\Omega$. Ein Wert von $0\,\Omega$ kann in der Praxis nicht erreicht werden. Die kleineren Innenwiderstandswerte werden meist gewählt, wenn es sich um hohe Stromflüsse von mehreren Ampere handelt. Eine Kapazität $C_i$ ist im Ersatzschaltbild nicht vorhanden. Kapazitäten existieren bei Potentialunterschieden (also elektrische Spannungen) und versuchen diese Unterschiede aufrecht zu erhalten, wodurch eigentlich kein Stromfluss existiert. 
# 
# ## Messabweichung
# 
# An unsere Schaltung aus dem letzten Kapitel, bestehend aus zwei Widerständen $R_1$ und $R_2$ zu je $100\,\mathrm{k\Omega}$ schließen wir nun den Strommesseingang an, wie in {numref}`strommesseingang_R1R2` dargestellt. Der Innenwiderstand soll $R_i = 1\,\mathrm{\Omega}$ betragen. 
# 
# :::{figure-md} strommesseingang_R1R2
# <img src="draw/strommesseingang_R1R2.jpg" alt="strommesseingang" class="bg-primary mb-1" width="400px" label = strommesseingang_R1R2>
# 
# Strommesseingang an einer Schaltung.
# :::
# 
# Der Gesamtwiderstand der Reihenschaltung beträgt nun
# 
# $$R_\mathrm{ges} = R_1 + R_2 + R_i = 100\,\mathrm{k\Omega} + 100\,\mathrm{k\Omega} + 1\,\mathrm{\Omega} = 200,001\,\mathrm{k\Omega}$$
# 
# :::{admonition} Aufgabe
# :class: tip
# Angenommen die Spannung am Eingang der Reihenschaltung bleibt konstant, $u = \mathrm{const.}$. Welche Stromstärke würde gemessen werden, wenn der Strom $I_0 = 1\,\mathrm A$ beträgt, wenn *kein* Strommesseingang hinzu geschaltet ist und die oben genannten Widerstandswerte für $R_1, R_2, R_i$ angenommen werden?
# :::

# In[1]:


R_1 = 100e3 # in Ohm
R_2 = 100e3 # in Ohm
I_0 = 1 # in Ampere
R_i = 1 # in Ohm
R_0 = R_1 + R_2

R_ges = R_1 + R_2 + R_i
print('Ergebnisse für R_1 =', R_1,',Ohm R_2 =', R_2, 'Ohm, R_i =', R_i, 'Ohm, I_0 =', I_0, 'A')
print('Der Gesamtwiderstand beträgt:', R_ges/1000, 'kOhm')
print('Die gemessene Stromstärke mit Messeingang: ', R_0/R_ges*I_0)
print('Die Messabweichung beträgt: ', R_0/R_ges*I_0 - I_0, 'A = ', (1-R_0/R_ges)*100, '%')


# :::{admonition} Lösung
# :class: tip, dropdown
# Es gilt 
# $$u = R_0 \cdot I_0 = R_\mathrm{mess} \cdot I_\mathrm{mess}$$
# Für die gemessene Stromstärke nach Anlegen des Messeingangs gilt also:
# $$I_\mathrm{mess} = \frac{R_0}{R_\mathrm{mess}} \cdot I_0 = \frac{200\,\mathrm{k\Omega}}{200,001\,\mathrm{k\Omega}} \cdot 1\,\mathrm A = 0,99999\,\mathrm A$$
# :::

# Ihr werdet nach dem Lösen der Aufgabe feststellen, dass es bei dem Anlegen eines Strommesseingangs zu einer vernachlässigbaren Messabweichung kommt. Wenn sich allerdings die Widerstände in unserer Schaltung stark ändern, wird dies Messabweichung beeinflussen. Sollten sich die Werte für $R_1$ und $R_2$ in der Größenordnung von $R_i$ bewegen, wird die Messabweichung einen signifikanten Einfluss auf die Strommessung haben. 
# 
# :::{admonition} Aufgabe
# :class: tip
# Wie groß ist die Messabweichung für Schaltungswiderstände $R_1, R_2$ von je $100\,\Omega$? 
# :::

# In[2]:


R_1 = 100 # in Ohm
R_2 = 100 # in Ohm
I_0 = 1 # in Ampere
R_i = 1 # in Ohm
R_0 = R_1 + R_2

R_ges = R_1 + R_2 + R_i
print('Ergebnisse für R_1 =', R_1,',Ohm R_2 =', R_2, 'Ohm, R_i =', R_i, 'Ohm, I_0 =', I_0, 'A')
print('Die gemessene Stromstärke mit Messeingang: ', R_0/R_ges*I_0, 'A')
print('Die Messabweichung beträgt: ', R_0/R_ges*I_0 - I_0, 'A = ', (1-R_0/R_ges)*100, '%')


# Die Messabweichung steigt nun von 0,0005% ($R_1 = R_2 = 100\,\mathrm{k\Omega}$) auf fast 0,5% ($R_1 = R_2 = 100\,\mathrm{\Omega}$) an, bei einem Innenwiderstand von $R_i = 1\,\mathrm{\Omega}$. Hat das Messgerät einen schlechten Eingang, also einen höheren Innenwiderstand, wird die Messung noch schlechter und die Messabweichung beträgt nun bereits fast 20%. 

# In[3]:


R_1 = 100 # in Ohm
R_2 = 100 # in Ohm
I_0 = 1 # in Ampere
R_i = 50 # in Ohm
R_0 = R_1 + R_2

R_ges = R_1 + R_2 + R_i
print('Ergebnisse für R_1 =', R_1,',Ohm R_2 =', R_2, 'Ohm, R_i =', R_i, 'Ohm, I_0 =', I_0, 'A')
print('Die gemessene Stromstärke mit Messeingang: ', R_0/R_ges*I_0, 'A')
print('Die Messabweichung beträgt: ', R_0/R_ges*I_0 - I_0, 'A = ', (1-R_0/R_ges)*100, '%')


# ## Innerer Aufbau
# 
# Bei einem Strommesseingang sind zwei typische Varianten häufig vorzufinden. 
# 
# ### Shunt-Widerstand
# 
# Wie in {numref}`strommesseingang_shunt` wird ein kleiner (typischerweise $1\,\Omega$) ohmscher *Hilfs-Widerstand*, der sogenannte **Shunt-Widerstand** in einem Strommesseingang verwendet. 
# 
# :::{figure-md} strommesseingang_shunt
# <img src="draw/strommesseingang_shunt.jpg" alt="strommesseingang" class="bg-primary mb-1" width="400px" label = strommesseingang_shunt>
# 
# Strommesseingang mit Shunt-Widerstand $R_s$. Typische Größenordnungen von Shunt-Widerständen sind $R_s = 1\,\Omega$.
# :::
# 
# Der Strom $i$, der gemessen werden soll, wird mittels Shunt-Widerstand $R_s$ in eine Spannung $u$ umgewandelt:
# 
# $$u = R_s \cdot i$$
# 
# Die Spannung wird dann mittels Spannungsmesseingang aus dem vorangenenen Kapitel gemessen. Der hohe Innenwiderstand des nachgeschalteten Spannungsmesseingangs ist gegenüber dem kleinen Shunt-Widerstand vernachlässigbar. 
# Die Wahl eines korrekten Wertes für den Shunt-Widerstand ist wichtig und kann unter Umständen auch zu Abweichungen kommen:
# * Ein **hoher Shunt-Widerstandswert** liefert einen hohen Spannungswert, was gut für die nachfolgende Spannungsmessung ist. Allerdings ist $R_s$ gleichzeitig der Innenwiderstand $R_i$ der Strommessung und sollte eigentlich möglichst kein sein, um die Strommessung $i$ nicht zu verfälschen (siehe {numref}`strommesseingang`).
# * Als Kompromiss findet man häufig $R_s \approx 1\,\Omega$.
# * Der Shunt-Widerstandswert sollte außerdem möglichst **genau bekannt** sein, da bereits kleinste Abweichung von $R_s \approx 1\,\Omega$ ansonsten zu verfälschten Ergebnissen führen. Daher verwendet man häufig **Präzisionswiderstände**. Diese weisen weniger Toleranzen, geringe Fertigungsstreuung und eine kleinere Temperaturabhängigkeit im Vergleich zu üblichen Widerständen auf. Alternativ kann den Widerstandswert vorher auch *kalibrieren*.
# * Shunt-Widerstände zur Messung **höherer Ströme** haben außerdem mehr Anschlüsse, an jedem Ende zwei statt einem. An zwei wird der Strom geleitet, die anderen beiden dienen dem Strommesseingang. Dadurch können Kontaktspannungen, die typischerweise bei den Kontakten abfallen, nach innen verlegt werden und fließen nicht mehr in die Messung mit ein. 
# 
# ### Strom-Spannungs-Messumformer
# 
# Die Variante der Strommessung mittels Shunt-Widerstand für Ströme ab $1\,\mathrm A$ verwendet. Bei kleinere Strömen, oder wenn man eine besonders hohe Messgenauigkeit erreichen möchte, verwendet man eine Verstärkerschaltung, wie in {numref}`strommesseingang_shunt` dargestellt.
# 
# :::{figure-md} strommesseingang_OP
# <img src="draw/strommesseingang_OP.jpg" alt="strommesseingang" class="bg-primary mb-1" width="400px" label = strommesseingang_OP>
# 
# Strommesseingang mit Strom-Spannungs-Messumformer.
# :::
# 
# Der Strom $i$, der gemessen werden soll, wird zunächst in eine Verstärkerschaltung eingespeist. Die Verstärkerschaltung wandelt Ströme ebenfalls in eine dazu proportional Spannung um. Hierbei handelt es sich meist um sogenannte **Operationsverstärker**, die aufgrund ihrer Bauweise sehr geringe Innenwiderstände $R_i$ aufweisen. Dadurch erhält man sehr genaue Strommessungen. Diese Variante ist jedoch auch etwas kostspieliger als die mittels Shunt-Widerstand. 
