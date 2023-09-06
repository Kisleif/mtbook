#!/usr/bin/env python
# coding: utf-8

# # Infos zum Praktikum
# 
# In den Vorlesungsunterlagen findest du Infos zu den Grundlagen des Messtechnik, die auch für das Praktikum gelten. Folgende Fragen solltest du die vor deinem ersten Praktikumsversuch einmal beantworten:
# 
# * [**Einheiten:**](1_Einheiten.ipynb) Welche Maßeinheiten gibt es? Was sind SI-EInheiten? Welche Vorsätze gibt es?
# * [**Messunsicherheiten:**](1_Messunsicherheiten.ipynb) [Welche Arten von Unsicherheiten gibt es?](1_Messunsicherheiten.ipynb) [Welche statistischen Methoden gibt es um Messreihen auszuwerten?](1_Mittelwert_StdAbw.ipynb) Wie gebe ich Messunsicherheiten an (Messwert und Fehlerbalken)?
# * [**Fehlerfortpflanzung:**](1_Fehlerfortpflanzung.ipynb) Wie betreibe ich Fehlerfortpflanzung? Was muss ich bei systematischen, zufälligen und korrelierten Unsicherheiten beachten?
# * [**Kurvenanpassung:**](1_Kurvenanpassung.ipynb) Wie plotte ich Messdaten sinnvoll? Wie kann ich Zusammenhänge in den Daten darstellen? 
# 
# :::{seealso}
# [Hier](0_Praktikum.ipynb) findest du ein Minimal-Beispiel zur Messdatendarstellung und anschließender Fehlerfortpflanzung unter Benutzung von Fit-Parametern.
# :::
# 
# 
# ## Programme für die Datenanalyse
# 
# Für das **Praktikum** müsst ihr [Daten aufnehmen, auswerten und grafisch darstellen](1_Datenanalyse). Verwende eine sinnvolle Software für die Datenanalyse und die grafische Darstellung, welche auch Fit-Analysen unterstützen. Wir werden hier im folgenden Beispiele in `python` aufführen und Jupyter Notebooks verwenden. 
# Weitere Software ist Qti-Plot (kostenlos) oder Matlab (Lizenzen über HSU verfügbar).
# 
# * [Python](https://www.python.org), frei-erhältlich und die [Tutorials](T_Tutorials) im *Lecture Book* nutzen Python ([Jupyter-Notebooks](https://docs.jupyter.org/en/latest/)). 
# * [Matlab](https://de.mathworks.com/products/matlab.html) (Lizenzen sind über die HSU erhältlich) 
# * [QtiPlot](https://qtiplot.com), freil erhältlich
# * Von einer Datenanalyse in Excel rate ich ab.
# 
# ```{warning}
# Alle Beispiele  im *Metrology Lecture Book* sind [Jupyter-Notebooks](T_Tutorials.ipynb) und benutzen `python`. Hier findet ihr auch eine Sammlung von hilfreichem Jupyter-Notebooks für das Messtechnik-Praktikum.
# ```
# 
# ### Programmieren mit Python
# 
# Es gibt zahlreiche Tutorials und Lernseiten über Python im Internet, womit ihr Python-Programmierung schnell und einfach lernen könnt. Für die Tutorials benötigt ihr folgende Grundkenntnisse, bzw. lernt sie innerhalb der Tutorials:
# 
# * **Basics:** Schleifen, Funktionen, Listen, Tuples, Sets, Dictionaries
# * **Algebra:** [numpy](https://numpy.org), [scipy](https://scipy.org)
#   * **Fit/Modellanpassungen:** [lmfit](https://pypi.org/project/lmfit/), [scipy](https://scipy.org) (z.B. curve_fit), [numpy](https://numpy.org) (z.B. polyfit)
#   * **Spektralanalyse:** [scipy](https://scipy.org) (z.B. rfft)
# * **Datenverarbeitung:** [pandas](https://pandas.pydata.org) (z.B. DataFrames)
# * **Datenvisualisierung:** [matplotlib](https://matplotlib.org)
# 
# 
# ## Grundidee: Messdaten sammeln
# 
# Aufgabe der Messtechnik ist es physikalische Messgrößen quantitativ zu beobachten und ist somit wichtiger Bestandteil in der Physik. Eine *quantitative* Beschreibung bedeutet immer, dass eine Messgröße mit einem Zahlenwert, $x$, und einer Maßeinheit, $E$, ausgedrückt wird. Um einen möglichst *guten* Zahlenwert experimentell zu ermitteln, wird neben der konkreten Durchführung ein Großteil der Experimentierzeit damit verbracht das Experiment vorzubereiten und zu planen, aber auch die Daten auszuwerten und darzustellen, Ergebnisse zu überprüfen und ggf. Messungen zu wiederholen. 
# Was sich beim Messen nicht umgehen lässt, und was der ein oder andere sicherlich schon im Praktikum beobachten konnte, ist, dass Beobachtungen immer statistischen (zufälligen) Schwankungen unterliegen. Dies führt dazu, dass sich das Messergebnis immer verändert. eine Messung wird prinzipiell niemals den *wahren* Wert liefern können, weshalb wir sorgfältig messen und auswerten müssen. Es gibt *best practice* Methoden und Techniken, die in der Wissenschaft benutzt werden, um Unsicherheiten und Schwankungen der Messgröße quantitativ zu beschreiben um so ein Qualitätsmaß der Messung bzw. unseres Experimentes zu erhalten. Durch die Einhaltung der *best practice* Methoden kannst du jederzeit Rechenschaft ablegen und das Ergebnis begründen. Die grundlegende Norm für die Messtechnik ist in der *DIN-Norm DIN 1319* und dem *GUM* (Guide to the Expression of Uncertainty in Measurement) offiziell festgehalten.
# 
# - **Planung:** Was soll gemessen werden? Was wird hierfür benötigt? Welche Fehlerquellen/Störeinflüsse könnten auftreten, bzw. welche sind bekannt? Welche systematischen Unsicherheiten sind bekannt?
# - **Durchführung:** Führe Protokoll! Wurde **alles**, was wichtig sein könnte, protokolliert und in Tabellen zusammengefasst, aufgeschrieben, fotografiert?
# - **Auswertung:** Prüfe die Ergebnisse auf Vollständigkeit und Übersichtlichkeit! Hierzu gehört auch eine vollständige Abschätzung von Messunsicherheiten.
# - **Prüfung:** Ergeben die Ergebnisse Sinn und sind diese konsistent mit anderen Ergebnissen aus der Literatur? Haben wir die Ergebnisse erwartet?
# - **Darstellung:** Vollständige Angabe des Messergebnisses, bestehend aus Zahlenwert, Maßeinheit und Messunsicherheit. Verwende die wissenschaftliche Notation für Zehnerpotenzen.
# 
# :::{seealso}
# In den Vorlesungsunterlagen findest du Infos zu [Messen, Einheiten, Kalibrieren](1_Messen_Einheit.ipynb), [Quellen und Ursachen von Messunsicherheiten](1_Messunsicherheiten.ipynb), [statistischen Messunsicherheiten](1_Mittelwert_StdAbw.ipynb) und [Fehlerfortpflanzung](1_Fehlerfortpflanzung.ipynb).
# :::
# 
# ## Diagramme zeichnen
# 
# Mittels Diagrammen (engl. *Plots*) werden Messwerte dargestellt. Die folgenden Regeln helfen dabei, dass die Diagramme anschaulich sind und der Betrachter direkt erkennt, worum es geht:
# 
# - **Achsenbeschriftung:** Beschrifte die Achsen richtig, eindeutig und mit vollständiger Angabe: physikalische Größe und Maßeinheit!
# - **Skalierung:** Wähle eine passende Skalierung in 1er-/2er-/5er oder 10er- (Dakaden) Schritten
# - **Markierungen:** Wähle eine gute erkennbare Markierung für Messpunkte und ggf. eine angebrachte Linienbreite für Kurven. Hierbei können unterschiedliche Farben, Strichdicken, Stricharten und Markierungspunkte verwendet werden, oder eine Kombination. 
# - **Titel:** Nutze passende Über-/ oder Unterschriften für das Diagramm, insbesondere wenn diese in der Auswertung im Text erwähnt werden.
# - **Anderes:** Weitere Punkte und Linien, die nicht gemessen wurden, sondern nur als *Hilfe* dienen (z.B. Fit-Funktionen, Modelle, Referenzlinien) oder Kommentare sind, sollten besonders gekennzeichnet werden. 
# - **Messunsicherheiten:** Für Messwerte (in Form von Fehlerbalken), aber auch für Funktionsterme und Ausgleichsgeraden, müssen Messunsicherheiten in den Graphen angegeben werden. 
# 
# :::{seealso}
# Das Einlesen und darstellen von Messdaten in `python` lernst du z.B. in diesem [Tutorial](T_Plotten) anhand von echten Klimadaten der NASA. Die Codes auf dieser Seite können direkt benutzt und ausgeführt werden. 
# :::
# 
# Im Folgenden sind zwei Diagramme dargestellt, die jeweils die gleichen (!) Klima-Messdaten der NASA zeigen. Das zweite Diagram weist einige Defizite auf... 
# 
# `````{admonition} Aufgabe
# :class: tip
# Welche Defizite fallen dir im 2. Diagramm im Vergleich zum 1. auf?
# `````

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

link = 'data/graph.csv' # Beispieldatei mit Klimadaten
global_mean = pd.read_csv(link, header = 1) # Daten einlesen
global_mean["uncertainty"] = 0.25 #Messunsicherheiten abschätzen, hier 0.25K Temperaturgenauigkeit angenommen

# Lineare Regression berechnen:
x=global_mean.loc[global_mean["Year"] >= 1980,"Year"]
y=global_mean.loc[global_mean["Year"] >= 1980,"No_Smoothing"]
y_err = global_mean.loc[global_mean["Year"] >= 1980,"uncertainty"]
model = np.polyfit(x, y, deg=1, w=1/y_err, cov=True) # 1. Wert = Anstieg , 2. Wert = Schnittpunkt mit y-Achse
y_model = model[0][0]*x+model[0][1] # Modell einer linearen Regression

# print(global_mean) # Eingelesene Daten ausgeben
plt.errorbar(global_mean["Year"],global_mean["No_Smoothing"], yerr=global_mean["uncertainty"], ls="-", lw=1, marker="s", ms=3, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(global_mean["Year"],global_mean["Lowess(5)"], lw=3,  color="tab:blue", label="Glättung (NASA)");
plt.plot(x,y_model, ls="-", lw=3, color="tab:red", label=f"lineare Regression y=({model[0][0]*1000:.3f}+-{np.sqrt(model[1][0][0]*1000):.3f})1e-3*x+({model[0][1]:.3f}+-{np.sqrt(model[1][1][1]):.3f})");
plt.xlabel('Jahr')
plt.ylabel("Jahresmitteltemperaturabweichung [°C]")
plt.legend();
plt.grid();

# Temperaturanstieg ausgeben:
print(f"Temperaturanstieg pro Jahr (von 1980 bis 2020): {model[0][0]:.3f}°C/Jahr")


# In[2]:


plt.figure(figsize=(10,5)) # Plot-Größe
plt.rcParams['font.size'] = 10; # Schriftgröße

# Lineare Regression berechnen:
x=global_mean["Year"]
y=global_mean["No_Smoothing"]
y_err = global_mean["uncertainty"]
model = np.polyfit(x, y, deg=1, w=1/y_err, cov=True) # 1. Wert = Anstieg , 2. Wert = Schnittpunkt mit y-Achse
y_model = model[0][0]*x+model[0][1] # Modell einer linearen Regression

plt.plot(global_mean["Year"],global_mean["No_Smoothing"], ls="-", lw=1, marker="s", ms=1, color="tab:gray", alpha=0.5, label="Werte");
plt.plot(global_mean["Year"],global_mean["Lowess(5)"], lw=1,  color="tab:blue", label="Kurve");
plt.plot(x,y_model, ls="-", lw=3, color="tab:red", label=f"Modell");
plt.ylabel("y")
plt.xlim([1850,2040])
plt.ylim([-5,5])
plt.legend();
plt.grid();

# Temperaturanstieg ausgeben:
print(f"Temperaturanstieg pro Jahr (von 1980 bis 2020): {model[0][0]:.3f}°C/Jahr")


# :::{admonition} Lösung
# :class: tip, dropdown
# * fehlende x-Achsenbeschriftung
# * y-Achsenbeschriftung ist nicht aussagekräftig
# * fehlende Einheiten
# * Legende ist nicht aussagekräftig
# * keine Fehlerbalken (oder zumindest nicht erkennbar)
# * y-Achsen-Skalierung ist zu groß gewählt, die Kurve nimmt nur einen sehr kleinen Teil des Diagramms ein
# * Aufgrund der ungenügenden Darstellung der y-Werte wurde die lineare Regression über den kompletten Messwertebereich durchgeführt, was bei näherer Betrachtung (siehe 1. Bild) eher ungünstig ist.
# * Aufgrund der fehlerhaften linearen Regression, ist der Temperaturanstieg der letzten Jahre um einen Faktor 2,375 zu gering abgeschätzt wurden! 
# :::
# 
# 
# ```{seealso}
# Wie du eine Kurve an deine Messdaten anpasst findet du unter [Kurvenanpassung](1_Kurvenanpassung.ipynb) und [Übungen in Python](T_Tutorials.ipynb).
# ```

# ## Latex-Template für den Praktikumsbericht
# 
# Wir stellen euch ein maßgeschneidertes LaTeX Template für eure Praktikumsberichte präsentieren zur Verfügung, welches ihr {Download}`hier herunterladen <Vorlage Praktikum Messtechnik.zip>` könnt. 
# Mit diesem Template könnt ihr professionelle Dokumente erstellen, die automatische Zitierungen, mathematische Formeln und eine gute Typografie unterstützen. Es enthält bereits vorgefertigte Abschnitte und Formatierungen, um euch den Einstieg zu erleichtern. Es eignet sich auch hervorragend für eure Bachelor- und Masterarbeiten. 
# 
# Ihr könnt das Template ganz einfach auf Overleaf nutzen, einer Online-Plattform für kollaboratives Schreiben in LaTeX. Folgt einfach diesen Schritten:
# 
# * Erstellt ein kostenloses Konto auf www.overleaf.com, falls ihr noch keines habt.
# * Klickt auf "New Project" und wählt "Upload Project" aus.
# * Lädt das heruntergeladene Praktikumsbericht Template hoch, indem ihr auf "Choose file" klickt und die Datei auswählt.
# * Nach dem Hochladen könnt ihr direkt mit dem Schreiben eures Praktikumsberichts beginnen. Das Template wird bereits in eurem Projekt geöffnet sein und ihr könnt es entsprechend anpassen.

# In[ ]:




