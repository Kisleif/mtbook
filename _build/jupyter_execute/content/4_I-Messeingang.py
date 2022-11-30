#!/usr/bin/env python
# coding: utf-8

# # Strommesseingang
# 
# Im Bild {numref}`strommesseingang_motor` ist dargestellt, wie elektrische Ströme gemessen werden. $R_L$ stellt hierbei einen Lastwiderstand, z.B. den einen Motors oder eines anderen Verbrauchers, dar. 
# 
# :::{figure-md} strommesseingang_motor
# <img src="draw/strommesseingang_motor.jpg" alt="strommesseingang_motor" class="bg-primary mb-1" width="600px" label = strommesseingang_motor>
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
# 
# $$u = R_0 \cdot I_0 = R_\mathrm{mess} \cdot I_\mathrm{mess}$$
# 
# Für die gemessene Stromstärke nach Anlegen des Messeingangs gilt also:
# 
# $$I_\mathrm{mess} = \frac{R_0}{R_\mathrm{mess}} \cdot I_0 = \frac{200\,\mathrm{k\Omega}}{200,001\,\mathrm{k\Omega}} \cdot 1\,\mathrm A = 0,99999\,\mathrm A$$
# 
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
# * Ein **hoher Shunt-Widerstandswert** liefert einen hohen Spannungswert, was gut für die nachfolgende Spannungsmessung ist. Allerdings ist $R_s$ gleichzeitig der Innenwiderstand $R_i$ der Strommessung und sollte eigentlich möglichst kein sein, um die Strommessung $i$ nicht zu verfälschen.
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

# ### Drehspulmesswerk
# 
# Bei dem Drehspulmesswerk handelt es sich um elektromechanisches Messgerät zur Messung der elektrischen Stromstärke. 
# Es wird eine drehbare Spule auf Kuferdraht in einem Dauermagneten eingebaut. Zwei Spiralfedern dienen der Strumzufuhr und für die Rückstellkraft des Zeigers in seiner Ausgangslage. Der Aufbau ist in {numref}`messwerk` dargestellt. 
# Der Zeiger sollte möglichst starr, leicht und dünn sein, damit der Skalenbereich gut ablesbar ist. 
# 
# :::{figure-md} messwerk
# <img src="draw/messwerk.jpg" alt="messwerk" class="bg-primary mb-1" width="500px" label = messwerk>
# 
# Aufbau eines Drehspulmesswerk.
# :::
# 
# Der zu messende Strom wird nun über die Anschlussklemme und die Federn in die Spule geleitet. Auf die Leiter in der Spule wirkt die Lorentzkraft, wodurch sich der Spulenkörper im Feld des Magneten anfängt zu drehen, wobei die Federkraft dem entgegenwirkt, bis das Drehtmoment, $M_L$, aus der Lorentzkraft, $F_L$, dem Drehmoment $M_F$ der Rückstellkraft der Spiralfedern, gleicht:
# 
# $$M_L = 2 F_L r = n \cdot I \cdot l \cdot B \cdot 2r$$
# 
# $$M_F = D \cdot \alpha$$
# 
# wobei $n$ die Windungsanzahl der Spule ist, $r$ der Radius, $l$ die Höhe der Spule, $I$ die Stromstärke, $B$ die magnetische Flussdichte im Luftspalt, $D$ die Federkonstante, und $\alpha$ der Drehwinkel. Nach Gleichsetzen der beiden Gleichung erhält man den Drehwinkel:
# 
# $$\alpha = \mathrm{const.}\cdot I$$
# 
# mit $\mathrm{const.} = n\cdot I \cdot B \cdot A / D$, wobei  $A$ die Fläche der Spule ist ($A = l \cdot 2r$).
# 
# Bei diesem Winkel bleibt die Spule stehen und die Zeigerposition kann auf einer Skala abgelesen werden, was den zugehörigen Stromstärkewert liefert. Wird der Strom wieder abgeschaltet, bringen die Federn den Zeiger zurück in seiner Ausgangslage. Da die Federkraft proportional zum Drehwinkel (hookesches Gesetz) und die Lorentzkraft proportional zur Stromstärke ist, ergibt sich eine linear geteilte Skale über einen Drehwinkel von etwa 90°.
# 
# Beim umpolen des Stroms würde der Zeiger in die andere Richtung ausschlagen. Daher können **nur Gleichströme** gemessen werden. Für Wechselströme wird ein zusätzlicher Gleichrichter benötigt. 
# Außerdem können Stromänderungen aufgrund der Trägheit des Zeigers nur bis zu einer gewissen Rate gemessen werden. Bei Wechselstrom aber einer bestimmten Frequenz (circa ab 10 Hz), wird nur noch der Gleichwert des Stroms angezeigt, also Null.
# 
# Das Dreheisenmesswerk zeigt eine quadratische Abhängigkeit vom Strom und zeigt den Effektivwert an, was im nachfolgenden Abschnitt erläutert wird. 
# 
# 
# ### Dreheisenmesswerk
# 
# Ströme können auch mittels einem Dreheisenmesswerk direkt angezeigt werden. Hierbei handelt es sich um ein analoges Strommessgerät. Es wnadelt die Stromstärke direkt in einen Zeigerausschlag um, der entsprechend kalibriert werden muss. 
# 
# :::{figure-md} dreheisen
# <img src="draw/dreheisen.jpg" alt="dreheisen" class="bg-primary mb-1" width="500px" label = dreheisen>
# 
# Aufbau eines Dreheisenmesswerks.
# :::
# 
# Hierfür wird eine einzelne Spule benutzt, wie sie es in {numref}`dreheisen` dargestellt ist. Innerhalb dieser Spule befindet sich ein fixierter Eisenkern und ein weiterer beweglicher Eisenkern an der Zeigerachse. Fließt nun ein Strom durch die Spule, so magnetisieren sich die Eisenkernen gleichsinnig und stoßen sich ab. Dadurch kommt es zu einer Rotation des beweglichen Eisenkerns und der Zeiger bewegt sich. Dadurch wird eine Feder gespannt, bis die die magnetische Kraft ausgeglichen ist. Wird der Strom abgeschaltet, bringt die Feder den Zeiger zurück in seiner Ausgangslage. 
# 
# Der Ausschlag ist im Gegensatz zum Zeigerausschlag in einem Drehspulmesswerk nicht mehr proportional sondern hängt von $I^2$ ab. Dadurch misst das Dreheisenmesswerk den Effektivwert der Stromstärke. 
# 

# ### Stromzange
# 
# Eine weitere Möglichkleit Störme zu messen ist die Messung des Magnetfeldes, welches zwangsläufig in einem stromdurchflossenen Leiter hervor gerufen wird. 
# Bei den oben genannten Möglichkeiten muss immer der Stromkreis aufgetrennt werden und das Strommessgerät in den Schaltkreis integriert werden. Die Stromzange ist so aufgebaut, dass der Eisenkern an einer Stelle geöffnet werden kann, wie eine Zangen, und das stromdurchflossene Kabel hindruchgelegt werden kann. Dadurch kann der Strom gemessen werden, ohne dass aktiv in den Stromkreis eingegriffen wird, was eines der großen Vorteile dieses Messprinzips ist. Die Messung erfolgt somit potentialfrei und berührunglos und eignet sich auch zur Messung von Strömen in laufenden Anlagen, ohne die Ausschaltung zu müssen. 
# Einschränkungen ergeben sich nur in der Querschnittsfläche des Leiters, da dieser vollständig von der Stromzangen umschlossen werden muss. 
# 
# #### Wechselstrom-Zangenstrommesser
# Mit dem einfachen Prinzip der Stromzange können nur Wechselströme gemessen werden, dies sind sogenannte **Wechselstrom-Zangenstrommesser** und basieren auf dem **Transformator-Prinzip**. Dies ist in {numref}`stromzange_wechsel` dargestellt. 
# 
# :::{figure-md} stromzange_wechsel
# <img src="draw/stromzange_wechsel.jpg" alt="stromzange_wechsel"  width="400px" label = stromzange_wechsel>
# 
# Darstellung der Strommessung mittels Stromzange für Wechselstrom mittels Sekundärspule.
# :::
# 
# Ein Eisenkern fundiert als Trafokern. In diesen Eisenkern wird der stromdurchflossene Leiter eingeführt und bildet eine Spule mit nur einer Windung, die **Primärspule**. Das Magnetfeld, was durch den stromdurchflossenen Leiter hervor gerufen wird, wird an den Eisenkern übertragen und magnetisiert diesen. Die Magnetisierung induziert in einer **Sekundärspule** einen **Sekundärstrom**, der proportional zu dem zu messenden Primärstrom ist. Der Sekundärstrom kann mittels Shunt-Widerstand, Oerationsverstärker oder mit einem Dreheisenmesswerk betrieben gemessen werden kann. Um diese anschließende direkte Stromstärkemessung zu gerantieren wird die Sekundärspulenwicklung direkt so gewählt, dass der resultierende Sekundärstrom groß genug für die folgenden Messgeräte ist. Die Energie zum Antrieb eines Dreheisenmesswerks wird hierbei dem Stromkreis entnommen. 
# 
# #### Allstrom-Messer
# Gleichstrom kann mittels dem eben genannten Prinzip nicht gemessen werden, da die Wechselfelder für die Magnetfeldänderungen fehlen.
# Für Gleichstrommessungen wird der Eisenkern an einer Stelle aufgetrennt und ein Magnetfeld-Sensor (Hall-Sensor oder magnetoresisitiver Widerstand) eingebaut, der auch statische Magnetfelder messen kann und somit nicht auf sich verändernde Wechselfelder angewiesen ist. Dies ist in {numref}`stromzange_gleich` dargestellt. 
# 
# :::{figure-md} stromzange_gleich
# <img src="draw/stromzange_gleich.jpg" alt="stromzange_gleich"  width="400px" label = stromzange_gleich>
# 
# Darstellung der Strommessung mittels Stromzange auch für Gleichströme, in dem in einem Luftspalt im Eisenkern ein Magnetfeld-Sensor (Hall-Sensor) eingebaut wird, der eine Hall-Spannung generiert. 
# :::
# 
# Nachteil hierbei ist jedoch, dass nur sehr schwache Signale erzeugt werden, welche elektronisch verstärkt werden müssen. Dafür wird eine zusätzliche Spannungsversorgung benötigt. Wechselströme können allerdings ebenso mit diesem Messgerät gemessen werden. 

# In[ ]:




