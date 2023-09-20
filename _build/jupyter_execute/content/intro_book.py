#!/usr/bin/env python
# coding: utf-8

# # Über dieses Lecture Book
# 
# Das Metrology Lecture Book ist eine Webseite (JupyterBook) für das Vorlesungsskript Messtechnik, welches aus einzelnen Jupyter-Notebooks (in Python programmiert) aufgebaut ist.
# Wie ihr diese Infastruktur optimal nutzen könnt, soll im Folgenden erläutert werden.
# 
# ```{info}
# Um dem **Vorlesungsskript** zu folgen, sind **keine Python-Kenntnisse erforderlich**. 
# ```
# 
# ## {fa}`check` Kommentare und Markierungen
# Stelle Fragen, diskutiere mit anderen und gestalte dein Lernen aktiv, indem du zum Beispiel die **Kommentier- und Highlight-Funktion** in https://hypothes.is/ benutzt: 
# 
# * Klickt ganz oben am rechten Seitenrand auf den Pfeil, das Auge oder das Papier.
# * Unter https://hypothes.is/ registrieren bzw. einloggen, wenn bereits ein Account besteht.
# * Ggf. auf https://hypothes.is/ eine neue Gruppe für eigene Notizen erstellen.
# * Auf der Seite die entsprechende Gruppen auswählen, in der ihr Notizen anlegen wollt.
# * Text auf der Seite markieren und ggf. Notizen hinzufügen. 
# 
# ```{seealso}
# Auf der Webseite https://hypothes.is/ findet ihr eure Kollektion von Notizen und könnt sie direkt als Karteikarten benutzen. 
# ```
# 
# ```{tip}
# Legt eine gemeinsame Gruppe für die Klausurvorbereitung an!
# ```
# 
# ## {fa}`download` Download
# Jede Webseite kann über den {fa}`download` Button in folgenden Formation heruntergeladen werden. 
# * `.pdf` geht immer
# * `.ipynb` wenn die Webseite als Jupyter-Notebook hinterlegt ist
# * `.md` wenn die Webseite als Markdown hinterlegt ist
# 
# ## {fa}`rocket` Python-Code im Browser
# Über die {fa}`rocket` oben könnt ihr jede Webseite, die als Jupyter-Notebook hinterlegt ist, direkt im Browser ohne lokale Python-Installation auf eurem Rechner ausführen. Dadurch habt ihr die Möglichkeit, den Code selbst auszuführen, Parameter anzupassen, zu experimentieren und ganz nebenbei Python zu lernen. 
# * {guilabel}`Live Code`: Innerhalb der Webseite sollte nun ein Kernel gestartet werden, dies kann ein paar Sekunden dauern. Jetzt könnte ihr den Code in den Zellen direkt auf der Webseite verändern und neu ausführen. Da der Live Code auf Binder basiert, kann es unter Umständen ein paar Minuten dauern, bis der Live Code ausgeführt werden kann. 
# * {guilabel}`Colab`: Das Jupyter-Notebook wird in der Python Umgebung von Goggle geöffnet und kann dort ausgeführt werden. Habt ihr einen Google-Account, könnt ihr dort auch eine Kopie des Notebooks ablegen.
# * {guilabel}`Binder`: Das Jupyter-Notebook wird im Binder-Browser gestartet. Dies kann einige Minuten dauern.
# 
# ```{admonition} Aufgabe
# :class: tip
# Probiert es direkt auf dieser Seite aus: ändert die Variablen im folgenden Code-Block und führt ihn erneut aus indem ihr auf {guilabel}`Run` klickt.
# ```
# 

# In[1]:


beispiel_string = 'Dies ist eine Python-Variable'
beispiel_zahl = 12345
print(beispiel_string, 'und die Zahl-Variable lautet: ' , beispiel_zahl + 1)


# ## 💻 Python Installation
# Zusätzlich könnt ihr Python nutzen, um eure Messdaten aus dem Praktikum auszuwerten. Wir stellen bereits eine Sammlung von Jupyter-Notebooks für ausgewählte Praktikumsversuche zur Verfügung, um den Einstieg zu erleichtern. 
# 
# ### Download der Jupyter-Botebooks
# Wie bereits erwähnt, könnte ihr jedes Notebook über den {fa}`download` Button als `.ipynb` herunterladen. Diese Datei könnt ihr dann auf eurem PC ausführen. Bitte beachtet, dass ihr für manche Notebooks Messdaten benötigt. Diese müsst ihr separat aus dem [**GitHub-Repository**](https://github.com/Kisleif/mtbook) herunterladen (`content/data/`). 
# 
# ### Jupyter Lab Desktop
# Wir empfehlen die Installation von [**Jupyter Lab Desktop**](https://github.com/jupyterlab/jupyterlab-desktop)
# <iframe width="560" height="315" src="https://www.youtube.com/embed/JYs2k9haGRM?si=BdMFQh9aNBsXyX0e" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# Mit Jupyter Lab können die Jupyter-Notebooks (`.ipynb`-Dateien) ganz einfach per Doppelklick aus dem lokalen Dateisystem geöffnet werden.
# 
# Habt ihr einmal Jupyter Notebooks auf eurem PC installiert, könnt ihr auch ganz einfach Praktikums-Templates herunterladen und dürft diese gerne zum Auswerten eurer Messdaten verwenden. 
# 
# ### Anaconda
# Für eine vollständige Python Installation empfehlen wir als Alternative zu Jupyter Lab Desktop das Programm **Anaconda**. Mittels Anaconda werden sehr viele Bibliotheken bereits mitinstalliert, um die ihr euch später keine weiteren Gedanken mehr machen müsst. Eine Anleitung, wie ihr hiermit nicht nur Python, sondern auch Notebooks und auch Jupyter Lab auf euren PC bekommt, findet ihr im folgenden Video:
# 
# <iframe width="560" height="315" src="https://www.youtube.com/embed/WUeBzT43JyY?si=slVswaODWeloo1BQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
# 
# ## 🐍 Programmieren mit Python
# Es gibt zahlreiche Tutorials und Online-Ressourcen, die euch das Erlernen der Python-Programmierung leicht und verständlich ermöglichen. Für die Tutorials sind folgende Grundkenntnisse erforderlich, die ihr innerhalb der Tutorials erlernen könnt:
# 
# * **Grundlagen:** Schleifen, Funktionen, Listen, Tupel, Mengen, Wörterbücher.
# * **Algebra:** [numpy](https://numpy.org), [scipy](https://scipy.org)
#   * **Fit/Modellanpassungen:** [lmfit](https://pypi.org/project/lmfit/), [scipy](https://scipy.org) (z.B. curve_fit), [numpy](https://numpy.org) (z.B. polyfit)
#   * **Spektralanalyse:** [scipy](https://scipy.org) (z.B. rfft)
# * **Datenverarbeitung:** [pandas](https://pandas.pydata.org) (z.B. DataFrames)
# * **Datenvisualisierung:** [matplotlib](https://matplotlib.org)
# 
# ```{seealso}
# Installationshinweise & Grundlagen der Programmierung in Python findet ihr im [Github von Nils Fleischer](https://nbviewer.jupyter.org/github/nilsleiffischer/python-course/blob/master/setup.ipynb). 
# ```
# 

# In[ ]:




