#!/usr/bin/env python
# coding: utf-8

# # Klimadatei (.csv) einlesen und analysieren
# 
# Zunächst werden die für dieses Jupyter Notebook benötigten Libraries geladen:

# In[1]:


#Benötigte Libraries:
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
plt.figure(figsize=(10,5)) # Plot-Größe
plt.rcParams['font.size'] = 10; # Schriftgröße


# ## .csv-Datei als *DataFrame* einlesen
# 
# Im Folgenden Nutzen wir globale Klimadaten, die auf der Webseite der NASA zu finden sind: https://data.giss.nasa.gov/gistemp/. Hierbei handelt es sich um Temperaturdaten, die Anomalien gegenüber dem Mittelwert in den Jahren 1951-1980 aufweisen.
# Es werden Daten von Dateien (online oder offline) eingelesen mit der Python Bilbiothek `pandas`. Die Daten werden in sogenannten *DataFrames* hier mit dem Namen `global_mean` abgespeichert. 

# In[2]:


#link = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv"
link = 'data/graph.csv'
global_mean = pd.read_csv(link, header = 1) 


# Wir geben das *DataFrame* aus um uns die Messdaten einmal anzusehen: 

# In[3]:


global_mean.head(6) # Ausgabe der ersten 5 Spalten
#global_mean.tail(5) # Ausgabe der letzten 5 Spalten
#global_mean # Ausgabe des DataFrames 


# In der ersten Spalte befinden sich lediglich die Indizes der Messungen. Die zweite Spalte beinhaltet das Jahr und die dritte Spalte zeigt den gemessenen globalen Temperaturunterschied im Vergleich zur gemittelten Temeratur der Jahre 1951-1980. Die letzte Spalte zeigt die gleichen Messwerte, jedoch gefiltert. 
# 
# Einzelne Spalten kann man sich anzeigen lassen, indem den Spaltel-Namen des zugehörigen *DataFrames* nutzt:

# In[4]:


global_mean['Year']


# ## Daten plotten mit 'matplotlib'
# 
# Als Beispiel für eine gelungene grafische Darstellung wollen wir die beiden Spalten, *No_Smoothing* and *Lowess(5)* gegenüber der Zeitachse *Year* plotten. Hierfür benützen wir die Python Library `matplotlib`:

# In[5]:


import matplotlib.pyplot as plt
plt.style.use('default')
plt.figure(figsize=(10,5))
plt.rcParams['font.size'] = 10;
plt.plot(global_mean["Year"],global_mean["No_Smoothing"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(global_mean["Year"],global_mean["Lowess(5)"], lw=4,  color="tab:blue", label="Glättung (NASA)");
plt.xlabel('Jahr')
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.legend();
plt.grid();


# ## Daten verarbeiten
# Die Bibliothek `pandas` ist sehr umfangreich und wird viel zur Datenverarbeitung genutzt. Im folgenden dazu einige Beispiele:
# 
# ### Statistische Größen: Mittelwert, Standardabweichung, Min, Max
# 
# Für jede Spalte lassen sich statistische Größen wie z.B. die Anzahl der Einträge pro Spalte, deren Mittelwert, Standardabweichung, Minimal- und Maximalwert bestimmen:

# In[6]:


global_mean.describe()


# ### Maximum und zugehöriges Jahr ausgeben
# 
# Dies können wir benutzen, um beispielsweise die *maximale Temperaturdifferenz* zu ermitteln:

# In[7]:


global_mean["No_Smoothing"].max()


# Wenn wir wissen wollen, *wann* diese *maximale Temperaturdifferenz* auftrat, muss der zugehörige Index dieses Events gespeichert werden:

# In[8]:


index_max = global_mean["No_Smoothing"].idxmax()
print(index_max)


# Diesen Index können wir nun benutzen, um mittels `.loc` Befehl den Eintrag zu diesem Index auszugeben:

# In[9]:


global_mean.loc[index_max]


# ### Daten aufsteigend/absteigend sortieren
# 
# Mit `.sort_values("Spaltenname")` können wir auch die Tabelle nach dem definierten Spaltennamen sortieren (standardmäßig in **ansteigender** Reihenfolge):

# In[10]:


global_mean.sort_values("No_Smoothing")


# Mit `ascending=False` wird absteigend sortiert:

# In[11]:


global_mean.sort_values("No_Smoothing", ascending = False)


# **WICHTIG**: Der Dataframe `global_mean` wird dadurch nicht verändert, es handelt sich nur um eine Anzeige!

# ## Daten glätten
# 
# Die von der NASA verwendete Glättung ist die **LO**cally **WE**ighted **S**catter-plot **S**moother (LOWESS). Dabei wird in einem lokal zu definierenden Bereich eine lineare Regression durchgeführt. Eine genauere Erklärung zur Methode findet ihr auf [Youtube](https://youtu.be/b7oryuMP3r8).
# 
# Es gibt natürlich viele Methoden und Filter, um Daten zu glätten. Wir wollen nun versuchen, die Methode der NASA zu rekonstruieren. Hierfür benutzen wir die Python Library `statsmodels` und erstellen eine weitere Spalte `Lowess(own)` in unserem DataFrame `global_mean`. In diese Spalte schreiben wir die geglätteten Werte von den Rohdaten `global_mean["No_Smoothing"]` indem wir die Funktion `lowess`aufrufen. Details zu Nutzung der Funktion findet ihr [https://www.statsmodels.org](https://www.statsmodels.org/devel/generated/statsmodels.nonparametric.smoothers_lowess.lowess.html):
# - an erster Stelle in der Funktion werden die Y-Werte eingegeben, hier `global_mean["No_Smoothing"]`
# - an zweiter Stelle in der Funktion werden die X-Werte eingegeben, hier `global_mean["Year"]`
# - die Option `frac` ist eine Zahl zwischen 0 und 1. Dies ist der Anteil der Daten, der bei der Schätzung der einzelnen y-Werte verwendet wird. 
# - Ausgegeben wird zweidimensionalas Array. Die erste Spalte enthält die sortierten x-Werte und die zweite Spalte die zugehörigen geschätzten y-Werte. Um die zweite Spalte in den DataFrame zu speichern, wählen wir diese mit `[:,1]` aus.

# In[12]:


from statsmodels.nonparametric.smoothers_lowess import lowess
global_mean["Lowess(own)"] = lowess(global_mean["No_Smoothing"],global_mean["Year"], frac=1/14)[:,1]


# In[13]:


global_mean


# In[14]:


import matplotlib.pyplot as plt
plt.style.use('default')
plt.figure(figsize=(10,5))
plt.rcParams['font.size'] = 10;
plt.plot(global_mean["Year"],global_mean["No_Smoothing"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(global_mean["Year"],global_mean["Lowess(5)"], lw=4,  color="tab:blue", label="Glättung (NASA)");
plt.plot(global_mean["Year"],global_mean["Lowess(own)"], lw=2,ls='-' ,  color="tab:red", label="Glättung (eigene)");
plt.xlabel('Jahr')
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.legend();
plt.grid();


# ## Messunsicherheiten als Fehlerbalken hinzufügen
# 
# Bei diesem Datenset stehen uns leider keine Messunsicherheiten zur Verfügung. Um Sie jedoch als Fehlerbalken miteinzubeziehen, wollen wir im Folgenden annehmen, dass der Temperaturunterschied auf 0.25K genau messen werden konnte und fügen die unserem Datensatz hinzu:

# In[15]:


global_mean["uncertainty"] = 0.25
print(global_mean)


# Grafisch darstellen tun wir Messunsicherheiten mittels Fehlerbalken und der Matplotlib-Funktion `plt.errorbar`. 

# In[16]:


plt.errorbar(global_mean["Year"],global_mean["No_Smoothing"], yerr=global_mean["uncertainty"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(global_mean["Year"],global_mean["Lowess(5)"], lw=4,  color="tab:blue", label="Glättung (NASA)");
plt.xlabel('Jahr')
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.legend();
plt.grid();


# ## Ausgleichsgerade berechnen und plotten
# 
# Mittels linearer Regression kann der Temperaturanstieg aus den Daten berechnet werden. Hierfür wird die Python Library `numpy` benutzt und die Funktion `polyfit` aufgerufen und in als `model` gespeichert. Diese Funktion benutzt die Least-Square Methode für polynomische Modelle. Weitere Informationen zu der Funktion findet ihr [hier](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html). Mit der Option `cov=True` wird die Kovarianz-Matrix berechnet, welche die Unsicherheiten für die Fit-Parameter beinhaltet. 

# In[17]:


import numpy as np
import pandas as pd

x=global_mean["Year"]
y=global_mean["No_Smoothing"]
y_err = global_mean["uncertainty"]
model = np.polyfit(x, y, deg=1, w=1/y_err, cov=True) # 1. Wert = Anstieg , 2. Wert = Schnittpunkt mit y-Achse
y_model = model[0][0]*x+model[0][1] # Modell einer linearen Regression

plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.xlabel("Jahr")
plt.errorbar(global_mean["Year"],global_mean["No_Smoothing"], yerr=global_mean["uncertainty"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(x,y_model, ls="-", lw=3, color="tab:red", label=f"lineare Regression y=({model[0][0]*1000:.3f}+-{np.sqrt(model[1][0][0]*1000):.3f})1e-3*x+({model[0][1]:.3f}+-{np.sqrt(model[1][1][1]):.3f})");
plt.legend(fontsize=12);
plt.grid();


# Das Model beinhaltet zwei Matrizen:

# In[18]:


model


# Im ersten Array stehen die Fit-Parameter der linearen Ausgleichsgeraden entsprechend der obigen Deklaration: `y_model = model[0][0]*x+model[0][1]`.
# Im zweiten Array, hier eine 2x2 Matrix, sind die Unsicherheiten in Form von der [Kovarianz-Matrix](sec_korr_cov) dargestellt.
# Der Temperaturanstieg kann entsprechend ausgegeben werden:

# In[19]:


print(f"Temperaturanstieg pro Jahr (von 1981 bis 2020): {model[0][0]:.3f}°C/Jahr")
print(f"Temperaturanstieg seit Beginn der Messung: {(y_model.iloc[-1]-y_model.iloc[0]):.3f}°C")


# ```{warning}
# Die lineare Regression bezieht hier den ganzen Zeitraum mit ein! Im folgenden betrachten wir für den Temperaturgradienten nur die Daten von 1980 bis 2020!
# ```

# In[20]:


x=global_mean.loc[global_mean["Year"] >= 1980,"Year"]
y=global_mean.loc[global_mean["Year"] >= 1980,"No_Smoothing"]
y_err = global_mean.loc[global_mean["Year"] >= 1980,"uncertainty"]

model = np.polyfit(x, y, deg=1, w=1/y_err, cov=True) # 1. Wert = Anstieg , 2. Wert = Schnittpunkt mit y-Achse
y_model = model[0][0]*x+model[0][1] # Modell einer linearen Regression
print(f"Temperaturanstieg pro Jahr (von 1980 bis 2020): {model[0][0]:.3f}°C/Jahr")


# In[21]:


plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.xlabel("Jahr")
plt.errorbar(global_mean["Year"],global_mean["No_Smoothing"], yerr=global_mean["uncertainty"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(x,y_model, ls="-", lw=3, color="tab:red", label=f"lineare Regression y=({model[0][0]*1000:.3f}+-{np.sqrt(model[1][0][0]*1000):.3f})1e-3*x+({model[0][1]:.3f}+-{np.sqrt(model[1][1][1]):.3f})");
plt.legend(fontsize=12);
plt.grid();

