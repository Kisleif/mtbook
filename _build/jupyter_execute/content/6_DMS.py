#!/usr/bin/env python
# coding: utf-8

# # Dehnungsmessstreifen (DMS)
# 
# Ein Dehnungsmessstreifen (DMS) ist lediglich eine elektrische Leiterbahn, die auf einer kleinen Trägerfolie z.B. mäanderförmig aufgebracht ist, wie in {numref}`dms` dargestellt. Meistens besteht diese Folie aus einem chemisch sehr robusten Material, wie z.B. Kapton (Polyimid), welches auch bei hohen Temperaturen verwendet werden kann. Hierauf wird die Leiterbahn mit einem speziellen Kleber aufgebracht, sodass diese den Oberflächendehnungen eines Körpers folgen kann. Dadurch können Dehnungen, Stauchungen, Kräfte oder Drücke auf der Oberfläche gemessen werden. Die Dehnung wird dann in Richtung des Leiterbahnabschnittes gemessen, dessen ohm'scher Widerstand sich ändert:
# 
# $$R = \frac{\rho \cdot l}{r^2 \pi}$$
# 
# $\rho$ ist der spezifische Widerstand, der vom Material der Leiterbahn abhängt und $l$ und $r$ sind Länge und Radius der Leiterbahn. In der Formel wird durch die Querschnittsfläche geteilt, die näherungsweise dem kreisförmigen Querschnitt $A = \pi r^2$ entspricht.  
# 
# :::{figure-md} dms
# <img src="draw/dms.jpg" alt="dms" width="400px" label = dms>
# 
# Dehnungsmessstreifen(DMS). 
# :::
# 
# Für
# * **Leiter** ist $\rho < 100\,\mathrm{\frac{\Omega mm^2}{m}}$, 
# * **Halbleiter** liegt $\rho$ zwischen $100\,\mathrm{\frac{\Omega mm^2}{m}}$ bis $10^{12}\,\mathrm{\frac{\Omega mm^2}{m}}$, 
# * **Isolatoren oder Nichtleiter** ist $\rho > 10^{^12}\,\mathrm{\frac{\Omega mm^2}{m}}$
# 
# Als Material für die Leiterbahn wird beispielsweise Konstanten, eine Legierung aus 55% Cu, 44% Ni, 1 % Mn, verwendet, deren spezifischer Widerstand kaum von der Temperatur abhängt und $\rho = 0,5\,\mathrm{\frac{\Omega mm^2}{m}}$ beträgt.
# 
# Nehmen wir nun, dass es sich um sehr kleine Änderungen handelt, können wir die obige Gleichungs wieder mittels Taylor-Entwicklung abschätzen, wie wir es auch bei der Fehlerfortpflanzung gemacht haben:
# 
# $$\frac{\Delta R}{R} \approx \frac{\Delta \rho}{\rho} + \frac{\Delta L}{L} - 2\cdot \frac{\Delta r}{r} = \left( \frac{\frac{\Delta \rho}{\rho}}{\epsilon} + 1 + 2\cdot \mu\right) \cdot \epsilon = K\cdot \epsilon$$
# 
# wobei 
# 
# $$\epsilon = \frac{\Delta l}{l}$$
# 
# die **Dehnung $\epsilon$** des zu untersuchenden Stücks ist und 
# 
# $$\mu = - \frac{\frac{\Delta r}{r}}{\frac{\Delta l}{l}}$$
# 
# die **Poisson-Zahl $\mu$**.
# $K$ ist der *K-Faktor* und ist für Konstantan 2,05. Die Änderung des spezifischen Widerstands ist für die Bestimmung der K-Faktors vernachlässigbar.
# Schon bei kleinen Dehnungen, minimalen Kräften oder anderen kleinen Belastungen ändert sich der Widerstandswert, wenn auch nur wenig, und wird mit dem K-Faktor skaliert. Typische Widerstandswerte im Grundzustand sind $100-1000\,\Omega$, welcher sich je nach K-Faktor für Dehnungsänderungen im Promill-Bereich ebenfalls um nur diesen kleinen Betrag ändert. 
# Aus diesem Grund werden DMSs häufig Widerstands-Messbrücken verwendet. Mittels verschiedenen Anordnungen können damit auch Querkräfte, Scherkräfte und andere Belastungen gemessen werden und Kompensation in Bezug auf Temperaturempfindlichkeiten können dadurch eliminiert werden. 
# 
# * Kraft (und somit auch Beschleunigung)
# * Waagen (Haushaltswaagen bis hin zu Kranwaagen) 
# * Druck
# * Drehmoment
# * Verformungsmessungen (experimentelle Beanspruchungsanalyse, Spannungsanalyse) auf vielen Werkstoffen
#     * Biegung
#     * Druck und Zug
#     * Scherkräfte
# 
# :::{admonition} Beispiel
# :class: tip
# Ein unbekannter Metalldraht hat die Länge $l = 2\,\mathrm m$ und einen Querschnitt von $A = 0,01\,\mathrm{mm^2}$. Die Testspannung beträgt $U=2\,\mathrm V$ und wir messen einen Strom von $I = 0,75\,\mathrm A$. Wie hoch ist der spezifische Widerstand des Metalldrahtes?
# :::
# 
# :::{admonition} Lösung
# :class: tip, dropdown
# $$\rho = \frac{R\cdot A}{l} = \frac{U \cdot A}{I \cdot l} = \frac{3,5\,\Omega \cdot 0,01\,\mathrm{mm^2}}{2\,\mathrm m} = 0,0175\,\mathrm{\frac{\Omega \cdot mm^2}{m}}$$
# 
# Es könnte sich um Kupfer handeln!
# :::
# 
# 
# Es gibt auch Halbleiter-DMS. Bei diesen Materialien ist die Änderung des spezifischen Widerstands nicht mehr zu vernachlässigen, da er sich aufgrund des **piezoresistiven Effekts** sehr stark ändert. P-dotiertes Silizium weist beispielsweise ein K von bis zu 190 auf, n-dotiertes Silizium sinkt den K-Faktor auf - 100 ab. Das heißt, dass der Widerstandswert mit zunehmender Dehnung kleiner wird!
# Eine eleganten Zusammensatzung wäre ein n- und p-dotierter Silizium-DMS mit jeweils dem gleichen, aber entgegengesetzten K-Faktor, welche in einer Messbrücke zusammengeschaltet werden. 
# 
# 

# In[ ]:





# 
