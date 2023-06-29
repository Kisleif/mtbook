#!/usr/bin/env python
# coding: utf-8

# ## Dampfdruckthermometer
# 
# Mit dem Dampfdruckthermometer kann die Temperatur aus dem Dampfdruck einer Flüssigkeit bestimmt werden. Die Flüssigkeit wird mit der Messstelle in einen thermischen Kontakt gebracht. Der Dampfdruck nimmt mit der Temperatur der Flüssigkeit beschleunigt zu und kann durch folgende Exponentialfunktion beschrieben werden:
# 
# $$p_\mathrm{D}(T) = c \cdot \mathrm{e}^{-\frac{\Delta E}{kT}}$$
# 
# wobei $k = 1,380649\cdot 10^{-23}\,\mathrm{J/K}$ eine Konstante ist,  die Boltzmann-Konstante und $\Delta E$ die Verdampfungsenergie eines Moleküls. Durch Logarithmieren beider Seiten erhält man die äquivalente logarithmische Darstellung
# 
# $$\ln{p_\mathrm{D}} = A - B/T$$
# 
# mit den Materialkonstanten $A$ und $B$. 
# 
# Bei richtiger Anpassung der Flüssigkeit an den zu messenden Temperaturbereich können sehr hohe Empfindlichkeiten erreicht werden, so dass die erforderliche Druckmessung mit einfachen Mitteln (beispielsweise einem Quecksilbermanometer) ausgeführt werden kann.

# ## Dampdruckkurve von Wasser

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from IPython.display import Image
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 10),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
plt.rcParams.update(params)
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('pylab', 'inline')

# Definition der Exp-Funktion in Python-Code
k = 1.380649e-23 # in J/K
def pD(c,dE,T):
    return c * np.exp(-dE/(k*T)) # in bar

# Materialkonstanten für Wasser:
c = 4.5e5 # in bar
dE = 6.74e-20 # in J
A = 13.015 
B = 4882.35 # in K

T = np.arange(100e-3,573,1) # Temperatur in K
figure(figsize=(10,4))
ax1 = plt.subplot(121) # Plot für hohe Temperature
ax1.plot(T-273.15, pD(c,dE,T),'tab:red', linewidth=2)
ax1.set_xlim([0,300])
ax1.minorticks_on()
ax1.grid(True, which='both')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.set_xlabel('T (°C)')
ax1.set_ylabel(r'$p_\mathrm{D}$ (bar)')

ax2 = plt.subplot(122) # Plot für tiefere Temperaturen
ax2.plot(T-273.15, pD(c,dE,T), 'tab:blue', linewidth=2)
ax2.set_xlim([-20,60])
ax2.set_ylim([0,0.2])
ax2.minorticks_on()
ax2.grid(True, which='both')
ax2.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax2.set_xlabel('T (°C)')
ax2.set_ylabel(r'$p_\mathrm{D}$ (bar)')
plt.tight_layout()
plt.show()


# Abb.: Links: Kennlinie für den Temperaturbereich 0-300°C. 
#              Rechts: Kennlinie für den Temperaturbereich -20-60°C.

# ## Aufgabe 1
# Bestimmen Sie mithilfe der Abbildung die Materialkonstanten $A$, $B$ und $\Delta E$, $c$ für Wasser.
# 
# ## Aufgabe 2
# Bestimmen Sie die Empfindlichkeit bei den Temperaturen 20°C und 200°C (gerundetes Zwischenergebnis aus (a): $A=13$ , $B = 4882\,\mathrm K$ ). Recherchieren Sie, welche Flüssigkeiten anstelle von Wasser sich für tiefe Temperaturen (<100 K) eignen. Welche Empfindlichkeit erreicht ein Helium-Dampfdruckthermometer bei 1K ( $A_\mathrm{He} = 2$ und $B_\mathrm{He} = 2,5\,\mathrm{K}$ ) und ein Neon-Dampfdruckthermometer bei 20K ( $A_\mathrm{O2} = 4,6$ und $B_\mathrm{O2} = 106\,\mathrm{K}$)?
# 
# ## Aufgabe 3
# Das Wasser-Dampfdruckthermometer besteht aus einem Gefäß mit einem Volumen von 1 Liter und einer Druckfestigkeit von 50 bar. Aus Sicherheitsgründen wird beim Bau des Thermometers nur soviel Flüssigkeit eingefüllt, dass bei einer Temperatur von 250°C die ganze Flüssigkeit verdampft ist. Welche Flüssigkeitsmenge wird demnach eingebracht? 
# 
# ## Aufgabe 4
# Können Sie mit diesem Thermometer auch noch eine Temperatur von 300°C messen? Wenn ja, wie und mit welcher Empfindlichkeit? Skizzieren Sie die Kennlinie für den Temperaturbereich 250°C-350°C (gerundetes Zwischenergebnisse aus (c): $N = 6\cdot 10^{23}$, $V = 17\,\mathrm{ml}$).
# Hinweis zu (c) und (d): Ein Gasthermometer misst Druck  und Volumen. Wie lautet die Zustandsgleichung für ideale Gase? In einem abgeschlossenen System wird sich das Volumen nicht ändern. 

# In[ ]:




