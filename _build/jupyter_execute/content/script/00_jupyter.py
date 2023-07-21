#!/usr/bin/env python
# coding: utf-8

# # Über dieses Skript
# 
# Das *Metrology Lecture Book* ist eine Mischung aus Vorlesungsskript, Praktikumshinweisen und Tutorials als Jupyter-Notebooks. Es handelt sich hierbei um ein Jupyter-Book was es ermöglicht `Python`-Code direkt einzubinden.
# 
# ## Vorlesungsinhalte 
# Um dem **Vorlesungsskript** zu folgen sind **keine Python-Kenntnisse erforderlich**. 
# 
# * Den **Code** zu den Berechnungen und Plots sind meist versteckt und können über einen Klick auf dein *Pfeil* angezeigt werden. 
# * **Anmerkungen, Textmarker und Vorlesungsnotizen** könnt ihr direkt auf der Seite machen (oben ganz rechter Seitenrand). Hierfür müsst ihr euch unter https://hypothes.is/ registrieren. Möchtet ihr die Notizen mit mir oder der Jahrgangs-Gruppe teilen, dann müsst ihr der entsprechenden Hypothes-Gruppe beitreten. Dadurch könnt ihr direkt Fragen zum Skript stellen (und Antworten bekommen) oder auf Fehler hinweisen. Den Link für eure Jahrgangsgruppe findet ihr im [ILIAS](https://ilias.hsu-hh.de/ilias.php?ref_id=292726&cmd=frameset&cmdClass=ilrepositorygui&cmdNode=zm&baseClass=ilrepositorygui). 
# 
# ## Praktikum
# Für das **Praktikum** müsst ihr [Daten aufnehmen, auswerten und grafisch darstellen](1_Datenanalyse). Hierfür könnt ihr prinzipiell ein Programm eurer Wahl nehmen, wie z.B. 
# 
# * [Matlab](https://de.mathworks.com/products/matlab.html) (Lizenzen sind über die HSU erhältlich) 
# * [Python](https://www.python.org), frei-erhältlich und die [Tutorials](T_Tutorials) im *Lecture Book* nutzen Python ([Jupyter-Notebooks](https://docs.jupyter.org/en/latest/)). 
# * [QtiPlot](https://qtiplot.com), freil erhältlich
# * Von einer Datenanalyse in Excel rate ich ab.
# 
# Im *Metrology Lecture Book* findet ihr jedoch viele Beispiele zur Analyse und Darstellung von Messdaten in `python`. 
# 
# ## Tutorials
# Die Tutorials sind freiwillig. Hiermit lernt ihr aber nicht nur die Auswertung und Darstellung von Messdaten, sondern gleichzeitig auch die Programmiersprache `Python`.

# ## Programmieren mit Python
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
# Die einfachste Möglichkeit mit der Python Programmierung zu starten ist das ausführen von Jupyter-Notebooks.

# ## Quick introduction to Jupyter Notebook
# 
# Es gibt verschiedene Möglichkeiten Jupyter-Notebooks auszuführen.
# 
# * **Ohne Installation: Code direkt im Browser ausprobieren:**
#     * **Jupyter-Lab** sofort ausprobieren: https://jupyter.org/try-jupyter/lab/. Um einzelne *Zellen* auszuführen macht einen *Doppelklick* in den Abschnitt und führt diesen mit `Shift+Enter` aus.
#     * **Jupyter-Notebooks** sofort ausprobieren: https://jupyter.org/try-jupyter/retro/notebooks/?path=notebooks/Intro.ipynb. Um einzelne *Zellen* auszuführen macht einen *Doppelklick* in den Abschnitt und führt diesen mit `Shift+Enter` aus.
#     * **Tutorials** im *Lecture Book* sofort ausprobieren: klickt oben auf die *Rakete* und dann auf `Colab`. Diese ist eine weitere interaktive Umgebung, in der das Jupyter-Notebook gestartet wird. Die *Rakete* erscheint nur auf den Seiten, die als Jupyter-Notebook hinterlegt sind.
# 
# * **Installation auf dem Rechner:**
#     * ich empfehle die Installation von Python/Jupyter-Notebooks/Jupyter-Lab über [Anaconda](https://www.anaconda.com/products/distribution)
#     * außerdem gibt es neuerdings eine Desktop-Version von [Jupyter-Lab](https://pypi.org/project/jupyterlab/), die es erlaubt `.ipynb` Dateien ganz einfach per Doppelklick aus eurem lokalen Datei-System zu öffnen.

# <iframe width="560" height="315" src="https://www.youtube.com/embed/jZ952vChhuI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
