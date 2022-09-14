#!/usr/bin/env python
# coding: utf-8

# # Grundlagen
# 
# ## Maßeinheiten
# <a id="SubSec-Das_International_Einheitensystem"></a>
# 
# ### SI-Einheiten 
# 
# Im Rahmen der Meterkonvention im Jahr 1960 wurde das **Internationale Einheitensystem**, kurz SI, benannt nach „le Système Internationale d’unités“, eingeführt. Die Definitionen der Basiseinheiten basierten nach wie vor teilweise auf materiellen Prototypen (bis 2019 war dies tatsächlich beim Kilogramm der Fall). Das SI basiert auf der Idee, dass sich im Prinzip alle relevanten Messgrößen über physikalische Gesetze auf genau 7 Basisgrößen zurückführen lassen. Diese 7 Basisgrößen sind die Basiseinheiten, aus denen alle weiteren Einheiten abgeleitet werden können:
# * Meter (m) als Einheit für die Länge
# * Kilogramm (kg) als Einheit für die Masse
# * Sekunde (s) als Einheit für die Zeit
# * Ampere (A) als Einheit für die elektrische Stromstärke
# * Kelvin (K) als Einheit für die thermodynamische Temperatur
# * Candela (Cd) als Einheit für die Lichtstärke und 
# * Mol (mol) als Einheit für die Stoffmenge
# 
# ![Bild](pictures/SI.png)
# 
# Seit 2018 werden alle SI-Einheiten von Naturkonstanten abgeleitet. Das war nicht immer so. So gabs es bepsielsweise bis 2018 noch das *Ur-Kilo*, ein Klotz der in einem Verließ in Paris aufbewahrt wurde aber mit der Zeit immer leichter wurde. 
# 
# * Die **Sekunde** ist ab sofort dadurch definiert, dass die Frequenz der Cäsium-Strahlung, $\Delta \nu_\mathrm{133Cs}$, exakt den Wert 9192631770 annimmt, wenn man diese in 1/s ausdrückt:
# 
# $$1\,\mathrm s = \frac{9192631770}{\Delta \nu_\mathrm{133Cs}}$$
# 
# (Cäsiumuhren haben übrigens eine Störanfälligkeit von 1:1e13, das entspricht einer Abweichung von 1s in 300000 Jahren.)
# * Das **Meter** wird ähnlich wie zuvor über die Lichtgeschwindigkeit $c$ ausgedrückt: 
# 
# $$1\,\mathrm m = \frac{c}{299 792 458} s = 30,663318...\frac{c}{\Delta \nu_\mathrm{133Cs}}$$
# 
# * Die **Candela** wird von der photometrische Strahlungsäquivalent $\mathrm K_\mathrm{cd}$ (ebenfalls eine Naturkonstante) abgeleitet. Sie wird über die SI-Einheiten kg, m, s und Steradiant (sr = m$^2$/m$^2$) definiert.
# 
# Anders sieht es bei den weiteren vier Basiseinheiten aus, für die Naturkonstanten gefunden und festgelegt wurden:
# * Das **Kilogramm** ist nun durch Ableitung aus dem Planckschen Wirkungsquantum $h = 6,62607015 \cdot 10^{-34}\,\mathrm{Js}$ definiert, wobei die Einheit J (Joule), wie unten noch aufgeführt wird, nichts anderes als kgm$^2$/s$^2$ ist. 
# 
# $$1\,\mathrm{kg} = \frac{h}{6,626070040 \cdot 10^{-34}}\,\mathrm{m^{−2} s} = 1,475521... \cdot 10^{40} h \cdot \frac{\Delta \nu_\mathrm{133Cs}}{c}$$
# 
# $h$ wird dabei in Kooperation der metrologischen Institutionen in Form aufwendiger Experimente in entsprechender Genauigkeit bestimmt. 
# * Das **Ampere** wird dadurch definiert, dass die Elementarladung $e = 1,602 176 620 8 \cdot 10^{−19}\,\mathrm{As}$ beträgt:
# 
# $$ 1\,\mathrm A = \frac{e}{1,6021766208\cdot 10^{−19}}s^{−1} = 6,789687...\cdot 10^8 \Delta \nu_\mathrm{133Cs}\cdot e $$
# 
# * Das **Kelvin** ist die Einheit der thermodynamischen Temperatur, über die Boltzmann-Konstante $k_B = 1,380 648 52 \cdot 10^{−23}\,\mathrm{kg m^2 s^{−2} K^{−1}}$.
# 
# $$ 1\,\mathrm K = \frac{1,38064852\cdot 10^{−23}}{k_B}\,\mathrm{kg m^2 s^{−1}} = 2,266665 \Delta \nu_\mathrm{133Cs} \cdot \frac{h}{k_B} $$
# 
# * Das **Mol** ist dadurch definiert, dass die Avogadro-Konstante $N_A = 6,022 140 857 \cdot 10^{23}\,\mathrm{mol^{−1}}$ beträgt. 
# 
# $$ 1\,\mathrm{mol} = \frac{6,022 140 857 \cdot 10^23}{N_A}$$
# 
# $N_A$ ist die Zahl, der in einem Mol enthaltenen Atome. Sie ist so definiert, dass 12 g Kohlenstoff (12C) genau einem Mol entspricht.
# 
# ![Bild](pictures/SI-konst.png)
# 
# ### Abgeleitete / Ergänzende SI-Einheiten
# <a id="SubSec-Abgeleitete_Ergänzende_SI-Einheiten"></a>
# 
# SI umfasst auch eine Aufzählung weiterer Einheiten, welche von den 7 Basiseinheiten, oder über physikalische Gesetzmäßigkeiten, abgeleitetet werdem können. Hier nur einige Beispiele:
# * 1 Hz (Hertz für Frequenz) = 1/s
# * 1 N (Newton für Kraft) = kgm/s$^2$
# * 1 Pa (Pascal für Druck) = 1 N/m$^2$ = 1 kg/ms$^2$
# * 1 J (Joule für Energie) = 1 Nm = 1 kg$^2$/s$^2$
# * 1 W (Watt für Leistung) = 1 J/s = 1 kgm$^2$/s$^3$
# * 1 V (Volt für Spannung) = 1 W/A = 1 kgm$^2$/s$^3$A
# * 1 H (Henry für Induktivität) = 1 Vs/A = 1 kgm$^2$/s$^2$A$^2$
# * 1 F (Farad für Kapazität) = 1 As/V = 1 s$^4$A$^2$/kgm$^2$
# 
# Zwischen verschiedenen physikalischen Teildisziplinen kann nun auch mit den Einheiten hin und her jongliert werden. So kommt die Leistung (W) sowohl in mechanischen, als auch auch elektrische Gesetzmäßigkeiten vor. Man kann durch die elektrische Spannung (V) durch eine Kombination des Amperes (elektrische Basiseinheit) mit mechanischen verknüpfen. 
# 
# Ergänzende Einheiten im SI-System sind beispielsweise:
# * 1 rad (Radiant) = 1 m/m, welches der ebene Winkel zwischen zwei Radien eines Kreises ist, falls der dadruch beschriebene Kreisbogen genauso groß ist wie der Radius. Der Umfang eines Kreises ist bekannterweise $2\pi \cdot r$, wobei $r$ der Kreisradius ist. Dadurch entspricht eine komplette Drehung einem Winkel von $2\pi\,\mathrm{rad}$
# * 1 sr (Steradiant) = 1 m$^2$/m$^2$ ist der räumliche Winkel (analog zum Radiant). Dieser schließt mit der Kugelmitte als Scheitelpunkt eine Fläche auf der Kugeloberfläche sein. Diese Fläche ist quadratisch mit einer Seitenlänge die dem Kugelradius entspricht. Die Einheit kann also ebenfalls auf Basiseinheiten zurückgeführt werden, hier 1 sr = m$^2$/m$^2$.
# 
# ### Nicht-SI-Einheiten
# <a id="SubSec-Nicht-Si-Einheiten"></a>
# 
# Es gibt diverse zusätzliche Einheiten, welche keine offiziellen SI-Einheiten sind, aber aufgrund ihrer großen Beliebheit und Handbarkeit gerne benutzt werden. Im Allgemeinem gibt es aber immer Zusammenhänge zu den SI-Einheiten, sodass sie sich in solche umformen lassen. Beispiele sind z.B.:
# * Grad Celsius: 1°C = K + 273,15
# * Grad Fahrenheit: 9/5 K - 459,67
# * Minute: 1 min = 60 s
# * (Winkel-)Grad: 1° = $\pi$/180 rad
# * (Winkel-)Minute: 1'  1/60°
# * Liter: 1 l = 1 dm$^3$
# * Tonne: 1 t  10$^3$ kg
# * Bar: 1 bar = 10$^5$ Pa
# 
# Dann gibt es noch historisch gewachsene Einheiten, wie z.B. die Meile, yard, foot, inch, once, pound, gallon, welche sich analog in SI-Einheiten umrechnen lassen. Diese Umrechnung ist global nicht immer die gleiche und es existieren für dieselbe Einheit unterschiedliche Umrechnungen (USA und UK sind hier die wohl bekanntesten Beispiele). Doch auch je nach Anwednungsgebiet gibt es Unterschiede:
# * 1 mile = 1 Landmeile = 1.609,344 m (US)
# * 1 nautical mile = 1 Seemeile (oder Luftfahrt) = 1.853,2 m (UK)
# * 1 mile = exakt 1.852 m (international)
# 
# Einheiten, die zwar in Gebrauch sind, aber nicht auf SI-Einheiten zurückzuführen sind, wurden für spezifische Einsatzgebiete konkret festgelegt: 
# * die Wasserhärte
# * das Mostgewicht
# * den Feingehalt von Gold- und Silberlegierungen
# * die Windstärke
# * den Seegang
# * die Stärke von Erdbeben
# 
# ### Vorsätze und Präfix im SI
# 
# Zum SI, bzw. prinzipiell angewendet in allen anderen Einheiten, sind sogenannte Präfixe / Vorsätze definiert. Teile oder Vielfach von SI-Einheiten können in Kurzform geschrieben werden, was das Lesen erleichtert. So können besonders große oder besonders kleine Zahlen übersichtlicher dargestellt werden. Dafür muss der oder die Forschende oder Ingeneur:in lediglich ein paar Vokabeln können: 
# 
# ![Bild](pictures/praefix.png)
# 
# ### Logarithmische Einheiten
# <a id="SubSec-Logarithmische_Einheiten"></a>
# 
# In der Messtechnik können unter Umständen Messwerte in ganz unterschiedlichen Größenordnungen anfallen. Daher haben wir uns ja im Kapitel vorher die Präfixe bzw. Vorsätze angesehen. Für eine Darstellung im Diagramm, bei dem die Achsen typischerweise eine feste Einheit besitzen, wird es dennoch schwierig, die Gesamtheit der Messreihe übersichtlich darzustellen. Daher bedient man sich häufig der logarithmischen Darstellung, welche im ersten Moment relativ umständlich und kompliziert erscheint, aber einen hohen Nutzen hat. Diese Darstellung ist auch im SI-System vorgesehen.
# 
# Der eigentlich Messwert auf einen wohl definierten Referenzwert bezogen wird. Man bildet also den Quotienten aus Messwert und Referenzwert, $P/P_\mathrm{ref}$ (bei Leistungen) oder $U/U_\mathrm{ref}$ bei Spannungen. Danach werden diese Quotienten logarithmiert, *fast ausschließlich* mit der 10er-Logarithmus (log). Der neue Wert ist per Definition einheitenlos, wird aber die Einheit **Dezibel** (dB) zugeordnet, also das Zehntel eines **Bels**. Ganz selten wird der natürlich Logarithmus benutzt, dann wird die Einheit Neper (Np) angewendet. 
# 
# In der Messtechnik hat es sich etabliert (ungeschriebenes Gesetz), dass in erster Linie Leistungen gemäß der eben beschriebenen Gesetzmäßigkeit in der Einheit dB umgewandelt werden, man spricht hierbei von der **Leistungsgröße**:
# 
# $$1\,\mathrm{dB} = 10 \cdot \log\frac{P}{P_\mathrm{ref}}$$
# 
# Man spricht von der **Feldgröße**, wenn Spannungen in die Einheit dB umgewandelt werden:
# 
# $$1\,\mathrm{dB} = 20 \cdot \log\frac{U}{U_\mathrm{ref}}$$
# 
# `````{admonition} Aufgabe
# :class: tip
# Beweise die Umformung von Leistungsgröße in Feldgröße! Hinweise: Es gilt $P \propto U^2$
# `````
