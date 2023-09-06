#!/usr/bin/env python
# coding: utf-8

# # Das Schwerependel 
# 
# ## Ziele
# Oszillationsbewegungen faszinieren durch ihre harmonische Natur und dienen gleichzeitig als äußerst empfindliches Messinstrument, insbesondere im Kontext atomarer Oszillatoren. Das einfache Fadenpendel ermöglicht uns einen erstaunlich klaren Einblick in die zugrunde liegenden Kraftfelder.
# 
# Während dieses Experimentes werden wir verschiedene Techniken zur Berechnung von Mittelwerten, Streumaßen und Ausgleichsgeraden erlernen. Diese Fähigkeiten werden uns dabei helfen, die Erdbeschleunigung ($g$) im Rahmen des Pendelversuchs zu bestimmen und gleichzeitig die zugehörige Messunsicherheit zu berücksichtigen.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, widgets
from IPython.display import display

# Funktion zur Berechnung der Periodendauer eines Fadenpendels
def calculate_period(length):
    g = 9.81  # Erdbeschleunigung in m/s^2
    T = 2 * np.pi * np.sqrt(length / g)  # Berechnung der Periodendauer
    return T

# Funktion zur Aktualisierung der Visualisierung
def update_pendulum(length):
    T = calculate_period(length)  # Periodendauer berechnen

    # Zeitwerte für die Visualisierung
    t = np.linspace(0, 12, 1000)
    theta = np.sin(2 * np.pi * t / T)

    # Plot des Fadenpendels
    plt.figure(figsize=(8, 4))
    plt.plot(t, theta, label=f'Fadenlänge: {length} m, Periodendauer: {T:.2f} s')
    plt.xlabel('Zeit (s)')
    plt.ylabel('Winkel (Bogenmaß)')
    plt.title('Fadenpendel Ausschlag')
    plt.xlim([0,12])
    plt.legend()
    plt.grid(True)
    plt.show()

# Interaktive Steuerelemente für die Fadenlänge
length_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Fadenlänge (m)')
interact(update_pendulum, length=length_slider)

# Anzeige der Steuerelemente
display(length_slider)


# ## Grundlagen 
# In diesem Versuch analysieren wir die Eigenschaften der Oszillationen eines Massenkörpers (Masse: $m$), der an einem Faden befestigt ist. Wenn dieser Massenkörper um den Winkel $\varphi_0$ ausgelenkt und anschließend losgelassen wird, führt er ein Pendelbewegung aus. 
# Um die mathematische Beschreibung zu vereinfachen, werden wir im Verlauf dieses Experiments eine Reihe von Näherungen verwenden, die sich in unterschiedlichem Maße von der genauen physikalischen Realität entfernen.
# 
# (I) Die Dämpfung des Pendels ist vernachlässigbar gering. Das bedeutet, dass die Schwingungen nur sehr langsam an Energie verlieren. In der Tat ist die Anzahl der Schwingungen, nach der das Pendel die Hälfte seiner ursprünglichen Energie verloren hat, größer als 100.
# 
# (II) Die Auslenkung $\varphi(t)$ des Pendels bleibt während des Versuchs stets kleiner als 30 Grad. Diese Begrenzung in der Auslenkung stellt sicher, dass wir uns in einem Bereich befinden, in dem die Näherungen noch gültig sind.
# 
# (III) Die räumliche Ausdehnung des Pendelkörpers selbst ist so klein, dass sie vernachlässigbar ist. Dadurch können wir die gesamte Masse des Pendels auf einen Punkt konzentrieren, was die mathematische Analyse erheblich erleichtert.
# 
# (IV) Der Faden, an dem das Pendel befestigt ist, wird als massefrei angenommen. Das bedeutet, dass wir die Masse des Fadens selbst nicht berücksichtigen müssen und uns nur auf die Masse des Pendelkörpers konzentrieren können.
# 
# Diese Näherungen erlauben es uns, die Pendelbewegung auf eine einfachere Art und Weise zu analysieren, obwohl sie nicht vollständig der realen physikalischen Situation entsprechen.
# 
# :::::{grid} 2
# 
# ::::{grid-item}
# 
# Tangential-Kraft: $F_T = mg\sin(\varphi)$
# 
# Rückstellkraft: $F_R = m\cdot a_\mathrm{tan}  = m\cdot \ddot \varphi l$
# 
# Winkelgeschwindigkeit: $v_\mathrm{tan} = \omega \cdot r = \dot \varphi \cdot l$
# 
# Gleichsetzen der Kräfte: $mg\sin \varphi = \ddot \varphi l$
# ::::
# 
# ::::{grid-item}
# :::{figure-md} SI
# <img src="draw/fadenpendel.jpg" alt="fadenpendel" width="300px" label = fadenpendel>
# 
# Kräfte im Schwerependel. 
# :::
# ::::
# :::::
# 
# Die Zerlegung der Schwerkraft auf den Pendelkörper in die zwei Komponenten senkrecht und parallel zum Faden führt auf eine Kraft, die den Faden spannt ($F_R$) und eine, die ein Rückstellmoment bewirkt ($F_T = m \cdot g \cdot \sin(\varphi)$). Aus den Newtonschen Axiomen folgt damit die Momentengleichung:
# 
# $$
# J \cdot \ddot{\varphi} + mgl\sin(\varphi) - M_{\text{Reibung}} = 0
# $$
# 
# Unter Berücksichtigung der Näherungen ($M_{\text{Reibung}} \approx 0$ nach (I); $\sin(\varphi) \approx \varphi$ nach (II)) vereinfacht sich die obige Gleichung zu:
# 
# $$
# \ddot{\varphi} + \frac{mgl}{J} \varphi = 0
# $$
# 
# Eine Lösung der Differentialgleichung mit den Anfangswerten $\varphi(t = 0) = \varphi_0$ und $\dot{\varphi}(0) = 0$ ist gegeben durch:
# 
# $$
# \varphi(t) = \varphi_0 \cdot \cos(\omega t); \quad \omega = \frac{2 \pi}{T_0} = \sqrt{\frac{gl}{l^2 + 2r^2/5}}
# $$
# 
# Wenn wir die *effektive Länge* $l_{\text{eff}} = \frac{l^2 + \frac{2r^2}{5}}{l}$ einführen, wird der Ausdruck für die Periodendauer ($T_0$) handlicher:
# 
# $$
# T_0 = 2\pi\sqrt{\frac{l_{\text{eff}}}{g}}
# $$
# 
# Wichtig dabei: Die Länge $l$ reicht immer vom Aufhängungspunkt bis zum Schwerpunkt des Pendelkörpers. Der ganze Aufbau befindet sich an einem Ort mit dem Ortsfaktor (Erdbeschleunigung) $g$.

# :::{admonition} Aufgabe
# :class: tip
# Prüfe, ob die Annäherung $\sin(\varphi) \approx \varphi$ für Werte von $\varphi$ unter 30 Grad mit einer Genauigkeit von weniger als 5 % zutrifft. Berechne den Fehler zwischen den beiden Ausdrücken und vergleiche ihn mit der Schwelle von 5 %, um festzustellen, ob die Annäherung gültig ist oder nicht.
# :::
# 
# :::{admonition} Lösung
# :class: tip, dropdown
# Um zu überprüfen, ob die Näherung $\sin(\varphi) \approx \varphi$ für $\varphi < 30^\circ$ mit einer Genauigkeit besser als 5 % gilt, können wir den Fehler zwischen den beiden Ausdrücken berechnen und überprüfen, ob der Fehler kleiner als 5 % ist.
# 
# Die Formel für den Fehler zwischen den beiden Ausdrücken lautet:
# 
# $$
# \text{Fehler} = \frac{|\sin(\varphi) - \varphi|}{\sin(\varphi)} \times 100\%
# $$
# 
# Wir werden diesen Ausdruck für $$\varphi = 30^\circ$$ berechnen:
# 
# $$
# \text{Fehler} = \frac{|\sin(30^\circ) - 30^\circ|}{\sin(30^\circ)} \times 100\%
# $$
# 
# Berechnung:
# 
# $$
# \text{Fehler} = \frac{|0.5 - 0.5236|}{0.5} \times 100\% \approx 4.72\%
# $$
# 
# Der Fehler zwischen den beiden Ausdrücken beträgt etwa 4,72 %. Da dieser Fehler kleiner als 5 % ist, können wir sagen, dass die Näherung $\sin(\varphi) \approx \varphi$ für $\varphi < 30^\circ$ mit einer Genauigkeit von besser als 5 % gilt.
# :::

# :::{admonition} Aufgabe
# :class: tip
# Erläutere, wie sich das Trägheitsmoment der schwingenden Kugel unter Verwendung von Annahme (IV), die besagt, dass der Faden massefrei ist, und dem Steinerschen Satz berechnet. Die Formel für das Trägheitsmoment sollte als $J = m \cdot l^2 + J_K$ angegeben werden, wobei $J_K$ das Trägheitsmoment bei Drehung um den Kugelmittelpunkt ist.:::
# 
# :::{admonition} Lösung
# :class: tip, dropdown
# Der Steinersche Satz besagt, dass das Trägheitsmoment eines Körpers bezüglich einer Achse, die parallel zur ursprünglichen Achse und einen Abstand $d$ von dieser entfernt verläuft, berechnet werden kann, indem man das Trägheitsmoment bezüglich der ursprünglichen Achse und das Produkt der Masse des Körpers mit dem Quadrat des Abstands $d$ zur neuen Achse addiert:
# 
# $$I = I_0 + m \cdot d^2$$
# 
# In unserem Fall ist $I_0$ das Trägheitsmoment der Kugel bezüglich einer Achse, die durch ihren Schwerpunkt verläuft (das ist $J_K$), und $d$ ist der Abstand zwischen dieser Achse und der Achse, um die das Pendel schwingt. Da der Faden als massefrei angenommen wird (Annahme IV), liegt der Schwerpunkt der Kugel auf der Achse des Pendels.
# 
# Daher ist $d = l$, wobei $l$ die Länge des Fadens ist. Das Trägheitsmoment des Pendels wird daher wie folgt berechnet:
# 
# $$J = J_K + m \cdot l^2$$
# 
# Das ist die gewünschte Formel, die das Trägheitsmoment des schwingenden Pendels unter Berücksichtigung von Annahme (IV) und dem Steinerschen Satz darstellt.
# :::

# In[ ]:




