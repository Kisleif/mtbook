#!/usr/bin/env python
# coding: utf-8

# # Über dieses Skript - Jupyter Notebooks
# Fast jede Webseite im Metrology Lecture Book ist ein **Jupyter-Notebook**. Das heißt es gibt Code-Zellen mit Python-Code, die ihr selbst verändern und ausführen könnt. 
# 
# ```{info}
# Um dem **Vorlesungsskript** zu folgen, sind **keine Python-Kenntnisse erforderlich**. 
# ```
# 
# Dadurch habt ihr die Möglichkeit, den Code selbst auszuführen, Parameter anzupassen, zu experimentieren und ganz nebenbei Python zu lernen. Zusätzlich könnt ihr Python nutzen, um eure Messdaten aus dem Praktikum auszuwerten. Wir stellen bereits eine Sammlung von Jupyter-Notebooks für ausgewählte Praktikumsversuche zur Verfügung, um den Einstieg zu erleichtern. Das Schöne daran ist, dass Python Open Source ist, und ihr  sofort loslegen könnt:
# 
# ## Live Code auf der Webseite
# Klickt oben auf die *Rakete* und wählt `Live Code` aus. Innerhalb der Webseite sollte nun ein Kernel gestartet werden. Jetzt könnte ihr den Code in den Zellen verändern und neu ausführen.  

# In[1]:


beispiel_string = 'Dies ist eine Python-Variable'
beispiel_zahl = 12345
print(beispiel_string, 'und die Zahl-Variable lautet: ' , beispiel_zahl + 1)


# ## Notebooks im Browser mit 'Colab'
# Ihr habt die Möglichkeit, die in unserem *Metrology Lecture Book* enthaltenen **Jupyter-Notebooks** direkt im Browser (*ohne lokale Python Installation*) auszuführen. Dazu klickt ihr oben auf das Symbol der *Rakete* und wählt anschließend `Colab` aus. Dies öffnet eine interaktive Umgebung im Browser, in der das Jupyter-Notebook gestartet wird. Beachtet, dass das Symbol der *Rakete* nur auf den Seiten erscheint, die als Jupyter-Notebooks vorliegen.
# Wenn Daten aus einer Mess*datei* innerhalb der Code-Zelle benutzt werden, funktioniert diese Methode leider nicht.
# 
# ## Installation
# Jede Webseite, die als Jupyter-Notebook existiert, könnt ihr über den Download Button oben als `.ipynb` herunterladen. Diese Datei könnt ihr dann auf eurem PC ausführen. Bitte beachtet, dass ihr für manche Notebooks Messdaten benötigt. Diese müsst ihr separat aus dem [**GitHub-Repository**](https://github.com/Kisleif/mtbook) herunterladen (`content/data/`). 
# 
# ### Jupyter Lab Desktop
# Wir empfehlen die Installation von [**Jupyter Lab Desktop**](https://github.com/jupyterlab/jupyterlab-desktop)
# <iframe width="560" height="315" src="https://www.youtube.com/embed/JYs2k9haGRM?si=BdMFQh9aNBsXyX0e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# Mit Jupyter Lab können die Jupyter-Notebooks (`.ipynb`-Dateien) ganz einfach per Doppelklick aus dem lokalen Dateisystem geöffnet werden.
# 
# Habt ihr einmal Jupyter Notebooks auf eurem PC installiert, könnt ihr auch ganz einfach Praktikums-Templates herunterladen und eure Messwerte auswerten. 
# 
# ### Anaconda
# Für eine vollständige Python Installation empfehlen wir als Alternative zu Jupyter Lab Desktop das Programm **Anaconda**. Mittels Anaconda werden sehr viele Bibliotheken bereits mitinstalliert, um die ihr euch später keine weiteren Gedanken mehr machen müsst. Eine Anleitung, wie ihr hiermit nicht nur Python, sondern auch Notebooks und auch Jupyter Lab auf euren PC bekommt, findet ihr im folgenden Video:
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/WUeBzT43JyY?si=slVswaODWeloo1BQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# ## Programmieren mit Python
# Es gibt zahlreiche Tutorials und Online-Ressourcen, die euch das Erlernen der Python-Programmierung leicht und verständlich ermöglichen. Für die Tutorials sind folgende Grundkenntnisse erforderlich, die ihr innerhalb der Tutorials erlernen könnt:
# 
# * **Grundlagen:** Schleifen, Funktionen, Listen, Tupel, Mengen, Wörterbücher.
# * **Algebra:** [numpy](https://numpy.org), [scipy](https://scipy.org)
#   * **Fit/Modellanpassungen:** [lmfit](https://pypi.org/project/lmfit/), [scipy](https://scipy.org) (z.B. curve_fit), [numpy](https://numpy.org) (z.B. polyfit)
#   * **Spektralanalyse:** [scipy](https://scipy.org) (z.B. rfft)
# * **Datenverarbeitung:** [pandas](https://pandas.pydata.org) (z.B. DataFrames)
# * **Datenvisualisierung:** [matplotlib](https://matplotlib.org)
# 
# ```{info}
# Installationshinweise & Grundlagen der Programmierung in Python findet ihr im [Github von Nils Fleischer](https://nbviewer.jupyter.org/github/nilsleiffischer/python-course/blob/master/setup.ipynb). 
# ```
# 

# In[ ]:




