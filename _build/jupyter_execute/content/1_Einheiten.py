#!/usr/bin/env python
# coding: utf-8

# # Einheiten
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/5iXyyQBGl-Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# Die monumentalen Pyramiden Ägyptens, faszinierende Meisterwerke der antiken Baukunst, stellen bis heute ein beeindruckendes Rätsel dar. Wie konnten die Erbauer vor über 4.600 Jahren, im Jahr 2600 v. Chr., eine solch bemerkenswerte Präzision und Symmetrie in ihren Bauwerken erreichen? Eine entscheidende Antwort auf diese Frage liegt in der erstaunlichen Methode, mit der die alten Ägypter die Präzision im Pyramidenbau sicherten.
# 
# ```{admonition} Wunder an Präzision (2600 v. Chr.): Cheops-Pyramide
# :class: dropdown
# 
# Die Cheops-Pyramide ist die älteste und größte der 3 Pyramiden von Gizeh. Sie wurde als Grabmal für den ägyptischen König (Pharao) Cheops errichtet, der während der 4. Dynastie im Alten Reich regierte (2620-2580 v. Chr.) und sie gehört zu den 7 Weltwundern der Antike. Sie ist eines der einzigen Weltwunder, welches bis heute erhalten geblieben ist. 
# Die Seitenlänge beträgt $230,33\,\mathrm m \pm 4\,\mathrm{cm}$ und die Höhe $146,59\,\mathrm m$ und war damit 4000 Jahre lang das höchste Bauwerk der Welt.
# Ihre Einmessung wurde in sehr hoher Genauigkeit vorgenommen, welches in nachfolgenden Bauten nicht mehr erreicht wurde.
# Sie ist genau nach den vier Himmelsrichtungen ausgerichtet und der Unterschied in den Längen ihrer vier Seiten beträgt weniger als ein Promille!
# 
# Im Allgemeinen sind ‚nur‘ drei Parameter maßgeblich, um die Präzision einer Pyramide zu bestimmen:
# 
# * die waagrechte Ausrichtung des Fundaments und aller folgenden Bauschichten,
# * die Orientierung nach den Himmelsrichtungen,
# * die Seitenneigung der Flächen.
# 
# Alle drei Parameter müssen nicht nur bei Baubeginn exakt festgelegt, sondern vor allem auch während des Baus kontinuierlich kontrolliert und nachgemessen werden, sonst wird das ganze Bauwerk sichtbar unregelmäßig. Es genügt nicht, beispielsweise die horizontale Ausrichtung lediglich bei Baubeginn festzulegen und dann drauflos zu bauen. Bei der enormen Höhe der großen Pyramiden von Gizeh würde ein sich wiederholender Messfehler von wenigen Millimetern nach oben hin multipliziert.
# Erwägt man also mögliche Messmethoden im Hinblick auf ihre Tauglichkeit beim Pyramidenbau, müssen drei wesentliche Bedingungen erfüllt werden:
# 
# * Die Messtechnik ist mit steinzeitlichem Werkzeug und Wissen möglich.
# * Sie ist realistisch geeignet, bei den beträchtlichen Dimensionen der Pyramiden zumindest die erreichte Genauigkeit zu liefern.
# * Sie ist auch in großer Höhe und auf kleiner Fläche anwendbar, so dass sie bei jeder neuen Schicht wiederholt werden kann.
# 
# ```
# 
# Die Ägypter vertrauten dabei auf sogenannte Körpermaße, wie die Elle und den Fuß, die in ihrem Alltag üblich waren. Doch für die Bauwerke von solch monumentaler Bedeutung wie den Pyramiden bedurfte es verbindlicher und reproduzierbarer Maßeinheiten. Diese Maßeinheiten wurden in Form von Längennormalen aus Holz geschaffen, die eine entscheidende Rolle in der präzisen Konstruktion der Pyramiden spielten. Jeden Monat wurden diese "Normale" mit der "königlichen Elle" oder "meh" kalibriert, einem sogenannten "Primärnormal" aus Granit, das genau der Unterarmlänge des Pharaos entsprach. Dieses Verfahren zur Sicherung der Präzision erwies sich als äußerst effektiv, denn eine Fahrlässigkeit bei der Kalibrierung hatte schwerwiegende Konsequenzen, die mit dem Tod bestraft wurden.
# 
# Die beeindruckende Präzision im Pyramidenbau wird besonders deutlich, wenn man bedenkt, dass die Abweichungen zwischen den Kantenlängen der Basis einer Pyramide, wie beispielsweise bei der Cheops-Pyramide (mit einer Basislänge von 230,33 Metern), lediglich 0,06 % betrugen. Dieses erstaunliche Maß an Genauigkeit ist ein eindrucksvolles Zeugnis für die handwerkliche Fähigkeiten und die mathematische Raffinesse der ägyptischen Baumeister in einer Zeit, in der moderne Technologie und Instrumente noch in weiter Ferne lagen.

# In[1]:


laenge_pyramide = 230.33   # in m
abweichung = 0.14          # in m
relative_abweichung = abweichung / laenge_pyramide
print('relative Messabweichung der Cheops-Pyramide: ', relative_abweichung*100, '%')


# Die Vielfalt und regionalen Unterschiede in den Maßeinheiten bis zum 18. Jahrhundert, wie zum Beispiel die unterschiedlichen Ellenmaße wie die Regensburger Elle mit $81,1\,\mathrm{cm}$ und die Bremer Elle mit $54,7\,\mathrm{cm}$, führten zu erheblichen Schwierigkeiten in Handel, Wissenschaft und Kommunikation. Um diese Herausforderungen zu bewältigen und eine weltweite Vergleichbarkeit von Messungen sicherzustellen, wurde das Internationale Einheitensystem (SI) entwickelt. Dieses System basiert auf Naturkonstanten und schafft eine global akzeptierte Standardgrundlage für wissenschaftliche und technische Messungen, was essentiell für die Präzision, Zuverlässigkeit und Effizienz in verschiedenen Bereichen ist.
# 
# ```{admonition} Weitere regionale Maßstäbe
# :class: dropdown
# 
# :::{figure-md} massstab
# <img src="pictures/massstab.jpg" alt="massstab" width="400px" label = massstab>
# 
# Maßstäbe in der Vergangenheit.
# :::
# 
# * Die Griechen übernahmen beispielsweise die ägyptischen Längenmaße und führten das Stadion ein (die Länge, die ein geübter Läufer schnell zurücklegen kann, etwa $180\,\mathrm m$).
# * Die Römer führten zur Messung der großen Entfernungen in ihrem Straßennetz die Meile als neues Längenmaß hinzu.
# * 1101 führt Heinrich I. von England die Längeneinheit Yard (Abstand von seiner Nasenspitze bis zum Daumen seines ausgestreckten Armes) und Inch (Breite seines Daumens) ein. 
# * Eduard II. von England erklärt die Länge von einem Zoll zum Längenmaß. Es hat die Länge dreier hintereinandergelegter Gerstenkörner.
# * Der Mathematiker J. Kölbel schlägt an Stelle eines Körpermaßes ein sogenanntes Naturmaß vor: "16 Männer groß und klein", die nach einer Messe der Reihe nach aus der Kirche kommen, stellen ihre Füße hintereinander. Der sechzehnte Teil der Gesamtlänge soll dann ein Fuß sein.
# ````
# 
# Es wird deutlich, wie zufällig jedes Herzogtum seine eigenen Einheiten eingeführt hatte was teilweise zu großem Chaos geführt hatte. 
# Die Körpermaße einzelner Herrscher wurden als Längeneinheit benutzt, die nur lokal Gültigkeit besaßen und auch lokal Individuell festgelegten Einheiten erschwerten internationalen Handel und Probleme in Forschung, Technik und Kommunikation.
# ```

# ## Maßeinheiten
# 
# Die Nationalversammlung während der französischen Revolution strebte die Schaffung eines neuen Einheitensystems an, unter dem Motto „À tous les temps, à tous les peuples“ (Für alle Zeiten, für alle Völker). Der erste Antrag für die Definition der Maßeinheit Meter wurde am 7. Oktober vorgelegt. Dabei sollte ein Meter als der zehnmillionste Teil des Erdmeridianquadranten festgelegt werden. Eine Gelehrtenkommission, bestehend aus Borda, Condorcet, Lagrange, Laplace und Monge, definierte zwei Maßeinheiten wie folgt:
# 
# - Der Meter, als universelle Einheit der Länge, sollte den zehnmillionsten Teil der Entfernung vom Nordpol zum Äquator über Paris ausmachen.
# - Das Kilogramm, als universelle Einheit der Masse, sollte der Masse eines Kubikdezimeters Wasser entsprechen.
# 
# Im Jahr 1799 wurde das naturbasierte Meter wieder durch eine künstliche Einheit ersetzt, da die Messung des Meters in Bezug zur Erde sehr aufwendig war. Ein Platin-Maßstab wurde hergestellt und als Urmeterstab in Paris aufbewahrt. Im Jahr 1889 wurde dieser Platinstab durch einen Platin-Iridium-Körper mit X-förmigem Querschnitt ersetzt (bestehend aus 90% Platin und 10% Iridium). Auf diesem Körper wurden zwei Mittelstriche markiert, um den Meter zu kennzeichnen. Temperaturänderungen von 0°C auf 20°C verursachten eine Längenänderung des "Meters" um 0,3 mm, wobei die Messgenauigkeit bei 0,01 mm lag.
# 
# :::{figure-md} meter
# <img src="draw/erde_platin.jpg" alt="meter" width="400px" label = meter>
# 
# Die anfängliche Definition des *Meters*.
# :::

# ## SI-Einheiten - "The big 7"
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/bELd5_zkhKQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/-mSO24hkRxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# SI-System: Die Basiseinheiten des SI-Systems I (Lehrer-Online)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/bELd5_zkhKQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# SI-System: Die Basiseinheiten des SI-Systems II (Lehrer-Online)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/-mSO24hkRxE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# 
# 
# 
# 
# Im Rahmen der Meterkonvention im Jahr 1960 wurde das **Internationale Einheitensystem**, kurz SI, benannt nach „le Système Internationale d’unités“, eingeführt. 
# Dies ist das am weitesten verbreitete Einheitensystem und beruht auf den 7 Basisgrößen:
# 
# 
# :::::{grid} 2
# 
# ::::{grid-item}
# * **Meter (m)** als Einheit für die Länge
# * **Kilogramm (kg)** als Einheit für die Masse
# * **Sekunde (s)** als Einheit für die Zeit
# * **Ampere (A)** als Einheit für die elektrische Stromstärke
# * **Kelvin (K)** als Einheit für die thermodynamische Temperatur
# * **Candela (Cd)** als Einheit für die Lichtstärke und 
# * **Mol (mol)** als Einheit für die Stoffmenge
# ::::
# 
# ::::{grid-item}
# :::{figure-md} SI
# <img src="draw/SI.jpg" alt="SI" width="300px" label = SI>
# 
# Die sieben SI-Einheiten.
# :::
# ::::
# :::::
# 
# Diese 7 Basisgrößen sind die Basiseinheiten, aus denen alle weiteren Einheiten abgeleitet werden können.
# Das SI-System folgt einigen grundsätzlichen Regeln, um Missverständnisse im Umgang mit Größen verzubeugen.
# 
# * Es ist ein **metrisches** Einheitensystem. Die Basisgröße ist das Meter.
# * **Dezimal**, d.h. die Einheiten unterscheiden sich um 10er Potenzen.
# * Es ist ein **kohärentes System**, d.h. alle Einheiten können von den Basiseinheiten abgeleitet werden. 
# 
# Die Definitionen der Basiseinheiten basierten nach wie vor teilweise auf materiellen Prototypen (bis 2019 war dies tatsächlich beim Kilogramm der Fall):
# ```{admonition} Das Ur-Kilo in Paris
# :class: dropdown
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Das Urkilogramm geht in Rente | Gut zu wissen (Bayerischer Rundfunk)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/bu-wGOhw1Zw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# Mit Ausnahme des Kilogramms wurden bis vor Kurzem alle Basiseinheiten über reproduzierbare Experimente eindeutig festgelegt. Die Sekunde ist zum Beispiel darüber definiert, als das sie das 9192631770-fache der Periodendauer einer bestimmten Strahlung ist, nämlich der des Übergangs zwischen den beiden Hyperfeinstrukturniveaus des Grundzustands von Atomen des Nuklids 133-Cäsium. Im Prinzip könnte sich also jeder das Element Cäsium besorgen, eine Atomuhr betreiben, und somit seine Sekunde zuhause definieren. Oder man spart sich die Arbeit und sucht eine der Kalibrierbehörden auf. 
# 1983 wird die Länge eines Meters als "jene Wegstrecke, die das Licht im Vakuum während der Dauer von 1/299792458-tel einer Sekunde zurücklegt", festgelegt. Somit war das Meter die erste Einheit, welche durch eine Naturkonstanten, nämlich die Lichtgeschwindigkeit c = 299792458 m/s definiert, bzw. festgelegt wurde. Andere Einheiten waren in der Praxis schwieriger umzusetzen, wie z.B. das Ampere. Für die Definition eines Amperes wurde die Kraft zwischen 2 stromdurchflossenen Leitern gemessen, was extrem unpraktisch ist. 
# Eine große Ausnahme ist und blieb das Ur-Kilo, welches als Prototyp von 1889-2018 in Paris als internationale Referenz sicher (bzw. vermeintlich sicher) aufbewahrt wurde. Das Ur-Kilo war:
# * ein 3,9 cm hoher und 3,9 cm dicker Metallzylinder, der zu 90% aus Platin und zu 10% aus Iridium besteht
# * Seit 1889 ist dieser "Block" das Referenznormal für Kilogramm
# * es wird unter drei Glasglocken in einem Tresor des "Internationalen Büros für Maß und Gewicht" (BIPM) in Paris aufbewahrt
# * keine Lösung für die Ewigkeit, denn - keiner weiß warum - aber das Ur-Kilo wird immer leichter
# * 50 Mikrogramm hat es in den letzten 129 Jahren im Vergleich zu seinen 70 offiziellen Kopien weltweit verloren
# 
# :::{figure-md} ur_kilo
# <img src="pictures/ur-kilo.jpg" alt="ur_kilo" width="400px" label = ur_kilo>
# 
# Bericht zur Ablösung des Ur-Kilogramms.
# :::
# 
# Das klingt erstmal nicht viel, wird aber in unserer Hightech-Welt, in der schon in Nanometern (Millionstel Millimeter) oder Femtosekunden (Millionstel einer Milliardstel Sekunde) gemessen wird, mehr und mehr zum Problem.
# ```
# 
# Seit 2019 werden alle SI-Einheiten von **Naturkonstanten** abgeleitet. Dies zeichnet sich dadurch aus, dass sie unabhängig von Ort und Zeit sind. Wenn wir die Dimensionen der festgelegten Konstanten betrachten, ergibt sich automatisch ein Zusammenhang zwischen der Konstanten und der Einheit. Das SI-System wird durch ein System von Zahlen mit präzise festgelegten Werten definiert.
# 
# * Die **Sekunde** ist ab sofort dadurch definiert, dass die Frequenz der Cäsium-Strahlung, $\Delta \nu_\mathrm{133Cs}$, exakt den Wert 9192631770 annimmt, wenn man diese in 1/s ausdrückt     (Cäsiumuhren haben übrigens eine Störanfälligkeit von 1:1e13, das entspricht einer Abweichung von 1s in 300000 Jahren.):
# 
#     $$1\,\mathrm s = \frac{9192631770}{\Delta \nu_\mathrm{133Cs}}$$
# 
# * Das **Meter** wird über die Lichtgeschwindigkeit $c$ ausgedrückt.  Wir kennen den Zahlenwert der Lichtgeschwindigkeit und wissen, dass sich elektromagnetische Strahlung im Vakuum immer gleich schnell ausbreitet, nämlich $c = 299 792 458\,\mathrm{m/s}$. Dadurch können wir bestimmen, wie weit sich Licht in $1/299792458\,\mathrm s$ ausbreitet. Dies bestimmt die Länge des Meters: 
# 
#     $$1\,\mathrm m = \frac{c}{299 792 458} s = 30,663318...\frac{c}{\Delta \nu_\mathrm{133Cs}}$$
# 
# * Das **Kilogramm** ist nun durch Ableitung aus dem Planckschen Wirkungsquantum $h = 6,62607015 \cdot 10^{-34}\,\mathrm{Js}$ definiert, wobei die Einheit J (Joule), wie unten noch aufgeführt wird, nichts anderes als kgm$^2$/s$^2$ ist. $h$ wird dabei in Kooperation der metrologischen Institutionen in Form aufwendiger Experimente in entsprechender Genauigkeit bestimmt. Wie schwer ein Kilogramm ist, misst die Watt-Waage mittels einer elektromagnetischen Kraft durch das Ausgleichen der Gewichtskraft.  
# 
#     $$1\,\mathrm{kg} = \frac{h}{6,626070040 \cdot 10^{-34}}\,\mathrm{m^{−2} s} = 1,475521... \cdot 10^{40} h \cdot \frac{\Delta \nu_\mathrm{133Cs}}{c}$$
#    
# * Das **Kelvin** ist die Einheit der thermodynamischen Temperatur, über die Boltzmann-Konstante $k_B = 1,380 648 52 \cdot 10^{−23}\,\mathrm{kg m^2 s^{−2} K^{−1}}$. Im Alltag benutzen wir die davon abgeleitete Einheit °C. $0\,\mathrm K$ entsprechen $-273,15\,\mathrm K$ und drücken den absoluten Temperaturnullpunkt aus. 
# 
# $$ 1\,\mathrm K = \frac{1,38064852\cdot 10^{−23}}{k_B}\,\mathrm{kg m^2 s^{−1}} = 2,266665 \Delta \nu_\mathrm{133Cs} \cdot \frac{h}{k_B} $$
# 
# * Das **Ampere** wird dadurch definiert, dass die Elementarladung $e = 1,602 176 620 8 \cdot 10^{−19}\,\mathrm{As}$ beträgt. Im Experiment wird zur Bestimmung des Ampere $e$ benutzt und im Stromfluss die Anzahl der Elektronen pro Sekunde gemessen. 
# 
# $$ 1\,\mathrm A = \frac{e}{1,6021766208\cdot 10^{−19}}s^{−1} = 6,789687...\cdot 10^8 \Delta \nu_\mathrm{133Cs}\cdot e $$
# 
# Die Basisgrößen für Licht und Stoffmenge begegnen uns im Alltag nicht so häufig und werden meist von Wissenschaftlern verwendet. 
# 
# * Das **Mol** ist dadurch definiert, dass die Avogadro-Konstante $N_A = 6,022 140 857 \cdot 10^{23}\,\mathrm{mol^{−1}}$ beträgt. $N_A$ ist die Zahl, der in einem Mol enthaltenen Atome. Sie ist so definiert, dass 12 g Kohlenstoff (12C) genau einem Mol entspricht.
# 
# $$ 1\,\mathrm{mol} = \frac{6,022 140 857 \cdot 10^{23}}{N_A}$$
# 
# * Die **Candela** wird vom photometrischen Strahlungsäquivalent $\mathrm K_\mathrm{cd}$ (ebenfalls eine Naturkonstante) abgeleitet. Sie wird über die SI-Einheiten kg, m, s und Steradiant (sr = m$^2$/m$^2$) definiert.
# 
#    
# :::{figure-md} SI_konst
# <img src="draw/SI-konst.jpg" alt="SI_konst" class="bg-primary mb-1" width="600px" label = SI_konst>
# 
# Die Definition der SI-Einheiten mittels Naturkonstanten und wie sich diese voneinander ableiten.
# :::
# 
# 
# Diese Einheiten bilden die Grundlage für die Messung aller anderen physikalischen Größen. Geschwindigkeit, Beschleunigung und alles, was wir messen, leitet sich von diesen Basiseinheiten ab.

# ## Abgeleitete / Ergänzende SI-Einheiten
# <a id="SubSec-Abgeleitete_Ergänzende_SI-Einheiten"></a>
# 
# SI umfasst auch eine Aufzählung weiterer Einheiten, welche von den 7 Basiseinheiten, oder über physikalische Gesetzmäßigkeiten, abgeleitetet werden können. Es gibt insgesamt 22 abgeleitete Einheiten, im Folgenden eine Auswahl:
# * 1 m$^2$ (Quadratmeter für Fläche) = 1 m$\cdot$m
# * 1 Hz (Hertz für Frequenz) = 1/s
# * 1 N (Newton für Kraft) = kgm/s$^2$
# * 1 Pa (Pascal für Druck) = 1 N/m$^2$ = 1 kg/ms$^2$
# * 1 J (Joule für Energie) = 1 Nm = 1 kg$^2$/s$^2$
# * 1 W (Watt für Leistung) = 1 J/s = 1 kgm$^2$/s$^3$
# * 1 V (Volt für Spannung) = 1 W/A = 1 kgm$^2$/s$^3$A
# * 1 H (Henry für Induktivität) = 1 Vs/A = 1 kgm$^2$/s$^2$A$^2$
# * 1 F (Farad für Kapazität) = 1 As/V = 1 s$^4$A$^2$/kgm$^2$
# 
# Zwischen verschiedenen physikalischen Teildisziplinen kann nun auch mit den Einheiten hin und her jongliert werden. So kommt die Leistung (W) sowohl in mechanischen, als auch elektrischen Gesetzmäßigkeiten vor. 
# 
# Ergänzende Einheiten im SI-System sind beispielsweise:
# * 1 rad (Radiant) = 1 m/m, welches der ebene Winkel zwischen zwei Radien eines Kreises ist, falls der dadurch beschriebene Kreisbogen genauso groß ist wie der Radius. Der Umfang eines Kreises ist bekannterweise $2\pi \cdot r$, wobei $r$ der Kreisradius ist. Dadurch entspricht eine komplette Drehung einem Winkel von $2\pi\,\mathrm{rad}$
# * 1 sr (Steradiant) = 1 m$^2$/m$^2$ ist der räumliche Winkel (analog zum Radiant). Dieser schließt mit der Kugelmitte als Scheitelpunkt eine Fläche auf der Kugeloberfläche ein. Diese Fläche ist quadratisch mit einer Seitenlänge die dem Kugelradius entspricht. Die Einheit kann also ebenfalls auf Basiseinheiten zurückgeführt werden, hier 1 sr = m$^2$/m$^2$.

# ## Nicht-SI-Einheiten (Akzeptierte Einheiten)
# <a id="SubSec-Nicht-Si-Einheiten"></a>
# 
# Es gibt diverse zusätzliche Einheiten, welche keine offiziellen SI-Einheiten sind, aber aufgrund ihrer großen Beliebtheit und Handhabbarkeit gerne benutzt werden. Im Allgemeinen gibt es aber immer Zusammenhänge zu den SI-Einheiten, sodass sie sich in solche umformen lassen. Beispiele sind z.B.:
# * Grad Celsius: 1°C = K + 273,15
# * Grad Fahrenheit: 9/5 K - 459,67
# * Minute: 1 min = 60 s
# * (Winkel-)Grad: 1° = $\pi$/180 rad
# * (Winkel-)Minute: 1'  1/60°
# * Liter: 1 l = 1 dm$^3$
# * Tonne: 1 t  10$^3$ kg
# * Bar: 1 bar = 10$^5$ Pa
# 
# Dann gibt es noch historisch gewachsene Einheiten, wie z.B. die Meile, yard, foot, inch, once, pound, gallon, welche sich analog in SI-Einheiten umrechnen lassen. Diese Umrechnung ist global nicht immer die gleiche und es existieren für dieselbe Einheit unterschiedliche Umrechnungen (USA und UK sind hier die wohl bekanntesten Beispiele). Doch auch je nach Anwendungsgebiet gibt es Unterschiede:
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

# ## Vorsätze und Präfix im SI
# 
# Zum SI, bzw. prinzipiell angewendet in allen anderen Einheiten, sind sogenannte Präfixe / Vorsätze definiert. Teile oder Vielfache von SI-Einheiten können in Kurzform geschrieben werden, was das Lesen erleichtert. So können besonders große oder besonders kleine Zahlen übersichtlicher dargestellt werden. Dafür muss der oder die Forschende oder Ingeneur:in lediglich ein paar Vokabeln können.
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :link: https://www.htwins.net/scale2/
# 
# :::{figure-md} dimensionen
# <img src="pictures/dimensionen.jpg" alt="dimensionen" label = dimensionen>
# 
# [Klicke hier](https://www.htwins.net/scale2/) für eine Reise durch die Dimensionen.
# :::
# ::::
# :::::
# ::::::
# 
# ::::{grid} 2
# 
# :::{grid-item}
# | Zeichen | Name | Multiplikator
# |:-------|:-------|:-------|
# | Y | Yotta | $10^{24}$|
# | Z | Zetta | $10^{21}$|
# | E | Exa | $10^{18}$|
# | P | Peta | $10^{15}$|
# | T | Tera | $10^{12}$|
# | G | Giga | $10^{9}$|
# | M | Mega | $10^{6}$|
# | k | Kilo | $10^{3}$|
# | h | Hekto | $10^{2}$|
# | da | Deka | $10^{1}$|
# :::
# 
# :::{grid-item}
# | Zeichen | Name | Multiplikator
# |:-------|:-------|:-------|
# | d | Dezi | $10^{-1}$|
# | c | Zenti | $10^{-2}$|
# | m | Milli | $10^{-3}$|
# | μ | Mikro | $10^{-6}$|
# | n | Nano | $10^{-9}$|
# | p | Pico | $10^{-12}$|
# | f | Femto | $10^{-15}$|
# | a | Atto | $10^{-18}$|
# | z | Zepto | $10^{-21}$|
# | y | Yokto | $10^{-24}$|
# :::
# 
# ::::

# ## Logarithmische Einheiten
# 
# ::::::{margin}
# :::::{grid}
# ::::{grid-item-card}
# :class-header: bg-light
# Logarithmische Achsen – Grundlagen (horizontale Achse) (Mathe - simpleclub)
# 
# <iframe width="200" height="113" src="https://www.youtube.com/embed/tC3vqTB_IrA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# ::::
# :::::
# ::::::
# 
# In der Messtechnik können Messwerte in sehr unterschiedlichen Größenordnungen auftreten. Wir haben bereits im vorherigen Kapitel die Präfixe und Vorsätze betrachtet, um diese Vielfalt zu handhaben. Dennoch kann es schwierig sein, die gesamte Messreihe übersichtlich auf einem Diagramm darzustellen, da die Achsen normalerweise feste Einheiten haben. Aus diesem Grund greifen wir oft auf die logarithmische Darstellung zurück, obwohl sie auf den ersten Blick komplex erscheinen mag. Diese Methode bietet jedoch erhebliche Vorteile und ist auch im Rahmen des SI-Systems anerkannt.

# In[2]:


import scipy.signal as signal
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
#plt.xkcd()
plt.figure(figsize=(8,5)) # Plot-Größe
plt.rcParams['font.size'] = 10; # Schriftgröße

# Transfer Funktion für das Model eines Tiefpasses:
num = np.array([1])
den = np.array([1 , 1, 1])
H = signal.TransferFunction(num , den)

# Bode-Plot Daten:
w2 = np.logspace(-3,2,200)
w, mag, phase = signal.bode(H,w2)
data = {"frequenz": w, "amplitude": mag, "phase": phase}
data_df = pd.DataFrame(data)
data_df["amplitude_V"] = 10**(data_df["amplitude"]/20)

plt.subplot(2,2,1)
plt.plot(data_df["frequenz"], data_df["amplitude_V"])
plt.fill_between(data_df["frequenz"],data_df["amplitude_V"],0,color='tab:blue', alpha=0.2)
plt.ylabel("Amplitude (V)")
plt.xlabel("Frequenz (Hz)")
plt.title('Lineare Achsen')

plt.subplot(2,2,2)
plt.semilogx(data_df["frequenz"], data_df["amplitude_V"])
plt.fill_between(data_df["frequenz"],data_df["amplitude_V"],0,color='tab:blue', alpha=0.2)
plt.ylabel("Amplitude (V)")
plt.xlabel("Frequenz (Hz)")
plt.title('x-Achse logarithmisch')

plt.subplot(2,2,3)
plt.plot(data_df["frequenz"], data_df["amplitude"])
plt.fill_between(data_df["frequenz"],data_df["amplitude"],-80,color='tab:blue', alpha=0.2)
plt.ylabel("Amplitude (dB)")
plt.xlabel("Frequenz (Hz)")
plt.title('y-Achse logarithmisch: dB')

plt.subplot(2,2,4)
plt.semilogx(data_df["frequenz"], data_df["amplitude"])
plt.fill_between(data_df["frequenz"],data_df["amplitude"],-80,color='tab:blue', alpha=0.2)
plt.ylabel("Amplitude (dB)")
plt.xlabel("Frequenz (Hz)")
plt.title('Doppel-logarithmisch')
plt.tight_layout()
plt.savefig('log_plot1.png')
plt.savefig('log_plot1.pdf')


# Der Messwert wird im Vergleich zu einem definierten Referenzwert bewertet, indem der Quotient aus Messwert und Referenzwert gebildet wird. Dies ergibt $P/P_\mathrm{ref}$ für Leistungen oder $U/U_\mathrm{ref}$ für Spannungen. Anschließend werden diese Quotienten logarithmiert, in der Regel unter Verwendung des Zehnerlogarithmus (log). Der resultierende Wert ist per Definition dimensionslos, wird jedoch der Einheit "Dezibel" (dB) zugeordnet, was einem Zehntel eines "Bels" entspricht. Gelegentlich wird auch der natürliche Logarithmus verwendet, wodurch die Einheit "Neper" (Np) entsteht.
# 
# In der Messtechnik hat sich eine ungeschriebene Regel etabliert, die besagt, dass Leistungen gemäß dieser Vorgehensweise in die Einheit dB umgewandelt werden, wobei dies als "Leistungsgröße" bezeichnet wird:
# 
# $$1\,\mathrm{dB} = 10 \cdot \log\frac{P}{P_\mathrm{ref}}$$
# 
# Wenn Spannungen nach dieser Methode in die Einheit dB umgewandelt werden, spricht man von der "Feldgröße":
# 
# $$1\,\mathrm{dB} = 20 \cdot \log\frac{U}{U_\mathrm{ref}}$$
# 
# Logarithmische Darstellungen finden normalerweise bei elektrischen Leistungen und Spannungen Anwendung. Das Dezibel wird häufig in der Hochfrequenztechnik und bei der Charakterisierung von Frequenzgängen verwendet. Im Allgemeinen spricht man von "Pegeln", wenn Messwerte logarithmisch ausgedrückt werden. Bei der Verwendung der Einheit Dezibel ist es **unbedingt erforderlich**, den Referenzwert anzugeben. Typische Schreibweisen sind beispielsweise:
# 
# - dB(mW): Dies bezieht sich auf einen Leistungspegel mit einem Referenzwert von 1 mW.
# - dB(mV): Dies bezieht sich auf einen Spannungspegel mit einem Referenzwert von 1 mV.
# - dB($\mu$V): Dies bezieht sich auf einen Spannungspegel mit einem Referenzwert von 1 $\mu$V.
# 
# Ohne Angabe des Referenzwerts sind weder die physikalische Größe noch der Skalierungsfaktor bekannt, was besonders wichtig ist, wenn der Dezibel-Wert später in absolute Einheiten zurückkonvertiert werden muss.
# 
# Für Leistungspegel gilt im Allgemeinen (bei einem typischen Referenzwert von 1 mW):
# 
# - 1 $\mu$W = 0,000001 W = -30 dB(mW)
# 
# **Hinweis**: In der folgenden Übung können Sie verschiedene Umrechnungen für Messwerte ausprobieren. Sie können den Referenzwert $P_\mathrm{ref}$ ändern, den Messwert $P$ anpassen und beobachten, wie sich der Dezibel-Wert ändert. Beachten Sie dabei, dass der Dezibel-Wert immer den Referenzwert in Klammern beinhalten muss.
# 
# ```{admonition} Aufgabe
# :class: tip
# In folgendem Code-Block können Umrechungen für verschiedene Messwerte ausprobiert werden:
# * Änder den Referenzwert `P_ref` von 1mW auf 1W und 1$\mu$W.
# * Änder den Messwert `P`
# * Beachte, dass bei der Angabe des Pegelwertes der Referenzwert immer in Klammern mitangebeben werden muss!
# ```

# In[3]:


import numpy as np # lade numpy Library
P = 1e-6     # Messwert, hier 1 uW
P_ref = 1e-3 # Referenzwert = 1 mW
P_dB = 10 * np.log10(P/P_ref) # Achtung: in numpy ist "log" der natürlich Logarithmus ln
print('Leistungswert = %.e W = %.10f W' %(P, P))
print('Pegel in dB: ', P_dB, '(%.3f)' %(P_ref))


# In[ ]:




