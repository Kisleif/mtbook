#!/usr/bin/env python
# coding: utf-8

# ---
# # Lösung: Systematische Messabweichung
# Prof. Dr. rer. nat. Katharina-Sophie Isleif
# 
# Helmut-Schmidt-Universität
# 
# ---
# 
# > Dies ist eine interaktive Lösung in Form eines Jupyter Notebooks. Lade das Jupyter Notebook herunter und öffne es mit JupyterLab. 
# Grundkenntnisse in _python_ sind hilfreich, werden aber nicht zwingend benötigt. 
# Kompiliere jede Zelle, die Code enthält, mit _Shift+Enter_ und alle Berechnungen sollten funktionieren.
# Es gibt andere Tutorials, um _python_-Kenntnisse oder den Umgang mit den Paketen 
# _numpy_ und _matplotlib_ zur Visualisierung und Auswertung von Daten zu vertiefen.

# In[1]:


# In diesem Code-Block werden ein paar wichtige Libraries geladen.
# Code-Blocks erkennst du an der Hintergrundfarbe dieser Zelle.
# Einfach mal hier rein klicken und per "Shift+Enter" ausführen. 
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
#plt.xkcd() # plots in xkcd-style


# Der Dampfdruck, $p_\mathrm D$, ist der Druck, der sich einstellt, wenn sich in einem abgeschlossenen System ein Dampf mit der zugehörigen flüssigen Phase im thermodynamischen Gleichgewicht befindet. Für verschiedene Temperaturen folgt die Dampfdruckkurve der Exponentialfunktion
# 
# $$ p_\mathrm{D} = c \cdot \mathrm{e}^{-\frac{\Delta E}{kT}}$$
# 
# wobei $c$ eine Konstante ist, $k = 1,380649\cdot 10^{-23}\,\mathrm{J/K}$ die Boltzmann Konstante und $\Delta E$ die Verdampfungsenergie eines Moleküls.

# In[2]:


# Definition der Exp-Funktion in Python-Code
k = 1.380649e-23 # in J/K
def pD(c,dE,T):
    return c * np.exp(-dE/(k*T)) # in bar


# ## Lösung 1: Materialkonstanten bestimmen
# 
# Durch Logarithmieren beider Seiten erhält man die äquivalente logarithmische Darstellung
# 
# $$\ln{p_\mathrm{D}} = A - B/T$$
# 
# wobei $A$ und $B$ wieder die Materialkonstanten sind. 
# durch Vergleichen der exponentielle und logarithmischen Schreibweise können die Materialkonstanten ineinander umgerechnet werden:
# 
# $$c = \mathrm e^{A}$$
# $$\Delta E = B\cdot k$$

# In[3]:


# Definition von Funktionen um die Materialkonstanten ineinander umzurechnen
def calc_c(A):
    return np.exp(A)
def calc_dE(B):
    return B*k


# ### Dampfdruckkurve von Wasser <a id="Ü21.a"> </a>
# 
# In der Übung haben wir anhand der gegebenen Dampfdruckkurve in der Abbildung die Materialskonstanten $A$, $B$, $\Delta E$ und $c$ abgeleitet:

# In[4]:


# Materialkonstanten für Wasser:
c = 4.5e5 # in bar
dE = 6.74e-20 # in J
A = 13.015 
B = 4882.35 # in K
print('c =', calc_c(A), 'bar')
print('dE =', calc_dE(B), 'J')


# Als Vergleich plotten wir noch einmal die Dampfdruckkurven mit diesen Parametern:

# In[5]:


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


# ## Lösung 2: Empfindlichkeit des Dampfdruckthermometers 
# 
# ### ... für Wasser
# 
# Um die Empfindlichkeit anhand der Kennlinie zu bestimmen, müssen wir die Dampfdruckgleichung von oben ableiten:

# In[6]:


# Funktion um pD abzuleiten. 
# Es werden einfach zwei aufeinanderfolgende Funktionswerte analysiert und die Steigung berechnet
def d_pD(c,dE,T): # in bar/K
    h = 1e-5 # in der Theorie wäre h infinitesimal klein (Abstand zwischen zwei Temperaturen)
    return (pD(c,dE,T+h)-pD(c,dE,T))/h


# Mit Hilfe dieser einfachen Funktion in Python können wir nun für verschiedene Temperaturen (20°C, 200°C) die Empfindlichkeit eines Dampfdruckthermometers für Wasser bestimmen. Achtung bei den Einheiten für die Temperaturwerte!

# In[7]:


T1 = 20 + 273.15 # in Kelvin
T2 = 200 + 273.15 # in Kelvin
print('T =  ', T1-273.15, '°C: ', d_pD(calc_c(A),calc_dE(B), T1), 'bar/K')
print('T = ', T2-273.15, '°C: ', d_pD(calc_c(A),calc_dE(B), T2), 'bar/K')


# ### ... für tiefsiedende Flüssigkeiten <a id="Ü21.c"> </a>
# 
# Um die Empfindlichkeit eines Dampfdruckthermometers bei tiefen Temperaturen zu verbessern wird Wasser durch eine tiefsiedende Flüssigkeit ausgetauscht. Je nach gewünschter Temperatur können hier zum Beispiel Sauerstoff (für 54K - 94K), Stickstoff (für 63K - 84K), Neon (für 24K - 40K) und Wasserstoff (13K - 25K) zum Einsatz kommen. 
# 
# Die Materialkonstanten $A$ und $B$ sind im folgenden Code-Block für jede Flüssigkeit angegeben. 

# In[8]:


A_O2 = 5.961546 # Materialkonstanten für Sauerstoff
B_O2 = 467.45576 # in K

A_N2 = 5.893271 # Materialkonstanten für Stickstoff
B_N2 = 403.96046 # in K

A_Ne = 4.61152 # Materialkonstanten für Neon
B_Ne = 106.3851 # in K

A_H2 = 1.711466 # Materialkonstanten für Wasserstoff
B_H2 = 44.01046 # in K

A_He = 2.24846 # Materialkonstanten für Helium
B_He = 2.49174


# Um ein Vergleich der unterschiedlichen Flüssigkeiten sichbar zu machen, werden die Dampfdruckkurven anhand der Materialkonstanten und der oben gegebenen Gleichung geplottet:

# In[9]:


T = np.arange(10e-3,110,0.1) # Temperatur in K
figure(figsize=(10,4))
ax1 = plt.subplot(111) # Plot für hohe Temperature
#ax1.plot(T, pD(calc_c(A_H2),calc_dE(B_H2),T),'tab:green', linewidth=2, label='H2')
ax1.plot(T, pD(calc_c(A_He),calc_dE(B_He),T),'tab:orange', linewidth=2, label='He')
ax1.plot(T, pD(calc_c(A_Ne),calc_dE(B_Ne),T),'tab:red', linewidth=2, label='Ne')
ax1.plot(T, pD(calc_c(A_N2),calc_dE(B_N2),T),'tab:green', linewidth=2, label='N2')
ax1.plot(T, pD(calc_c(A_O2),calc_dE(B_O2),T),'tab:purple', linewidth=2, label='O2')
ax1.plot(T, pD(calc_c(A),calc_dE(B),T),'tab:blue', linewidth=2, label='H2O')
ax1.set_xlim([0,100])
ax1.set_ylim([-0.1,1.3])
ax1.minorticks_on()
ax1.grid(True, which='both')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.set_xlabel('T (K)')
ax1.set_ylabel(r'$p_\mathrm{D}$ (bar)')
ax1.legend()
plt.show()


# Bei tiefen Temperaturen müssen eigentlich weitere Materialkonstanten hinzugezogen werden, damit die Dampfdruckkurve die experimentell ermittelten Werte tatsächlich widerspiegelt. Uns soll an dieser Stelle allerdings die Genauigkeit der Kennlinie unter Berücksichtigung von nur 2 Materialkonstanten vorerst genügen, da sie sich in der richtigen Größenordnung befinden.
# 
# Der Graph verdeutlicht, für welchen Temperaturbereich welche Flüssigkeit benutzt werden sollte, um mittels Dampfdruckverfahren eine möglichst genaue Temperaturmessung zu erhalten. 

# Wie oben definiert, können wir die Ableitung der Dampfdruckkurve an bestimmten Temperaturen berechnen um die Empfindlichkeit zu bestimmen:

# In[10]:


T1 = 1 # in Kelvin
print('He-Dampfdruckthermometer bei T =  ', T1, 'K: ', d_pD(calc_c(A_He),calc_dE(B_He), T1), 'bar/K')
T1 = 20 # in Kelvin
print('Ne-Dampfdruckthermometer bei T =  ', T1, 'K: ', d_pD(calc_c(A_Ne),calc_dE(B_Ne), T1), 'bar/K')


# ## Lösung 4: Übergang zum Gasthermometer <a id="Ü21.e"> </a>
# 
# Das Wasser-Dampfdruckthermometer besteht aus einen Gefäß mit einem Volumen von 1 Liter und einer Druckfestigkeit von 50 bar. Aus Sicherheitsgründen wird beim Bau des Thermometers nur soviel Flüssigkeit eingefüllt, dass bei einer Temperatur von 250°C die ganze Flüssigkeit verdampft ist. Dadurch liegt uns nun ein "normales" Gasthermometer vor, dessen physikalisches Verhalten durch das ideale Gasgesetz
# 
# $$ p \cdot V = N \cdot k \cdot T$$
# 
# beschrieben wird. Für das Volumen gilt $V = 1\,\mathrm l = 1\,\mathrm{dm}^3 = 1\cdot 10^{-3}\,\mathrm m^3$ und für den Druck bei $T=250\,^\circ \mathrm C = 523.15\,\mathrm K$ gilt $p = 40\,\mathrm{bar} = 40\cdot 10^5\,\mathrm{Pa}$.

# In[11]:


V = 1e-3 # in m^3
T = 250 + 273.15 # in K
p = 40e5 # in Pa
N = p*V/(k*T)
print(N, 'Moleküle')


# Dies entspricht fast der Avogadro-Konstanten $N_A = 6.022\cdot 10^{23}/\,\mathrm{mol}$, welche die Anzahl von Molekülen in 1 mol definiert.

# In[12]:


N_A = 6.02214086e23 # in mol^-1
Mol = N / N_A
print(Mol, 'mol')


# 
# Die molare Masse von Wasser ergibt sich mithilfe von Gleichung:
# 
# $$M_\mathrm{H2O} = 2M_\mathrm H + 1M_\mathrm O$$
# 
# wobei $M_H = 1.00794\,\mathrm{\frac{g}{mol}}$ und $M_H = 15.994\,\mathrm{\frac{g}{mol}}$

# In[13]:


M_H20 = 2 * 1.00794 + 1 * 15.994
print('Molare Masse von Wasser: ', M_H20, 'g/mol')


# Bezogen auf unsere eben berechnete Mol-Größe ergibt sich also folgende Masse:

# In[14]:


m_H2O = M_H20 * Mol
print(m_H2O, 'g')


# Dies können wir nun mittels der Dichte von Wasser, $\rho = 1000\,\mathrm{\frac{kg}{m^3}} = 1000\,\mathrm{\frac{g}{l}}$ in ein Volumen umrechnen:

# In[15]:


r = 1000 # in g/l
V_H2O = m_H2O / r
print('Es werden demnach ',V_H2O*1000, 'ml Flüssigkeitsmenge benötigt, damit bei 250°C alles verdampft ist.')


# Auch bei 300°C kann mit dem Thermometer noch gemessen werden, es handelt sich dann allerdings nicht mehr um ein Dampfdruckthermometers, sondern lediglich um ein Gasthermometer. Bei gleichbleibenden Volumen (abgeschlossenes System) gilt also folgende Gleichung:
# 
# $$\frac{p_1}{T_1} = \frac{p_2}{T_2}$$
# 
# mittels welcher wir den Druck bei 300°C bestimmen können.

# In[16]:


p1 = 40 #in bar
T1 = 250 + 273.15 #in K
T2 = 300 + 273.15 #in K
p2 = T2/T1*p1
print(p2, 'bar')


# Um die Empfindlichkeit eines Gasthermometers zu bestimmen, wird die (ideale) Gasgleichung entsprechend umgestellt und nach der Temperatur abgeleitet:
# 
# $$p = \frac{NkT}{V} \quad \rightarrow \quad \frac{dp}{dT} = \frac{Nk}{V}$$

# In[17]:


E = N*k/V # Achtung Einheiten!!
print('Empfindlichkeit = ', E, 'J / K m^3 ')
print('                = ', E, 'Pa / K' )
print('                = ', E/1e5, 'bar / K' )
print('                = ', E/1e5*1e3, 'mbar / K' )


# Durch die Ableitung ist die Temperaturabhängigkeit verschwunden. Damit ist die Empfindlichkeit eines Gasthermometers konstant und beträgt etwa 76.5 mbar / K.

# In[18]:


T = np.arange(240+273.15,351+273.15,1) # Temperatur in K
figure(figsize=(10,4))
ax1 = plt.subplot(111) # Plot für hohe Temperature
ax1.plot(T-273.15, N*k*T/V/1e5,'tab:blue', linewidth=2)
ax1.minorticks_on()
ax1.grid(True, which='both')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.set_xlim([240,350])
ax1.set_xlabel('T (°C)')
ax1.set_ylabel(r'$p_\mathrm{D}$ (bar)')
plt.show()

