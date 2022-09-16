# Welcome

Willkommen zur Vorlesung Messtechnik an der HSU. Auf den folgenden Seiten findet ihr begleitende Informationen zur Vorlesung und zum Praktikum. Es handelt sich hierbei um ein Jupyter-Book was es ermöglicht `Python`-Code zu benutzen. 


```{warning} 
Dieses Jupyter-Book befindet sich aktuell im Aufbau und ihr könnt euch noch nicht auf Vollständigkeit verlassen. 
```

Um dem **Vorlesungsskript** zu folgen sind **keine Python-Kenntnisse erforderlich**. Ihr könnt euch aber den `code` zu den Berechnungen und Plots anzeigen lassen, falls es euch interessiert. 

Für das **Praktikum** müsst ihr [Daten aufnehmen, auswerten und grafisch darstellen](content/1_Datenanalyse). Hierfür könnt ihr ein Programm eurer Wahl nehmen, wie z.B. [Matlab](https://de.mathworks.com/products/matlab.html) (Lizenzen sind über die HSU erhältlich) oder [Python](https://www.python.org), was frei-erhältlich ist und wozu es bereits einige Beispiele im *Lecture Book* in Form von [Jupyter-Notebooks](https://jupyter.org) gibt. 

```{seealso}
Schaut euch die Weiteren Infos zum [*Lecture Book*](content/00_jupyter) an. 
```



::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: content/1_Datenanalyse
:link-type: doc
:class-header: bg-light
**Tips für's Praktikum** 👩‍🔬
^^^

Messdaten richtig sammeln, dokumentieren und analysieren.
:::

:::{grid-item-card}
:link: content/00_jupyter
:link-type: doc
:class-header: bg-light
**Über dieses Skript** 🐍
^^^

Einführung in Python und Jupyter-Notebooks.
:::


:::{grid-item-card}
:link: content/T_Tutorials
:link-type: doc
:class-header: bg-light
**Tutorials** 🧑🏽‍💻
^^^

Übungen zur Messtechnik mit Jupyter-Notebooks.
:::
::::

## Vorlesungsinhalt

::::{grid} 1 1 3 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: content/0_Basics
:link-type: doc
:class-header: bg-light
**Messen, Einheiten**
^^^
```{image} content/draw/SI.png
:height: 120
```
SI-Einheiten, Nicht-SI, Kalibrieren, Eichen, Prüfen
:::

:::{grid-item-card}
:link: content/1_Messunsicherheiten
:link-type: doc
:class-header: bg-light
**Messunsicherheiten**
^^^
```{image} content/draw/abweichung.png
:height: 120
```
Systematisch, zufällig, Vertrauensintervall, Normalverteilung, Fehlerfortpflanzung
:::

:::{grid-item-card}
:link: content/1_Kurvenanpassung
:link-type: doc
:class-header: bg-light
**Kurvenanpassung**
^^^
```{image} content/draw/regression.png
:height: 120
```
Regression, Fit, Korrelation, Kovarianz, Least-Squares
:::

:::{grid-item-card}
:link: content/2_Stationaer
:link-type: doc
:class-header: bg-light
**Stationäre Messsysteme**
^^^
```{image} content/draw/realeKennlinie.png
:height: 120
```
Ideale und reale Kennlinie
:::

:::{grid-item-card}
:link: content/3_Messsignale
:link-type: doc
:class-header: bg-light
**Messsignale**
^^^
```{image} content/draw/digitalisierung.png
:height: 120
```
Signale als Informationsträger, Digitalisierung, Kenngrößen
:::

:::{grid-item-card}
:link: content/3_FourierAnalyse
:link-type: doc
:class-header: bg-light
**Fourier-Analyse**
^^^
```{image} content/draw/fft.png
:height: 120
```
Fourier-Reihen, Fourier-Transformation
:::

:::{grid-item-card}
:link: content/5_Dynamische_Messsysteme
:link-type: doc
:class-header: bg-light
**Dynamische Messsysteme**
^^^
```{image} content/draw/übertragungsfunktion.png
:height: 120
```
LZI-Systeme, DGLs, Impuls- und Sprungantwort, Faltung, Übertragungsfunktion
:::


:::{grid-item-card}
:link: content/4_ElektrischeGroessen
:link-type: doc
:class-header: bg-light
**Messen elektrischer Größen**
^^^
```{image} content/draw/messbruecke.png
:height: 120
```
Messeingänge, Widerstandsbrücken, Wechselspannung, Messverstärker
:::

:::{grid-item-card}
:link: content/4_Sensoren
:link-type: doc
:class-header: bg-light
**Sensoren**
^^^
```{image} content/draw/ifo.png
:height: 120
```
optisch, kapazitiv, piezo-elektrisch, resistiv, magnetisch, gravitativ
:::

::::


## Literatur

::::{grid} 1 1 1 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: https://doi.org/10.1007/978-3-658-27131-2
:link-type: url
:class-header: bg-light
**Parthier 2020 {cite}`parthier2020`**
^^^
```{image} content/pictures/2020_Book_Messtechnik.png
:height: 150
```
**Messtechnik**: Vom SI-Einheitensystem über Bewertung von Messergebnissen zu Anwendungen der elektrischen Messtechnik
+++
Explore this book {fas}`arrow-right`
:::

:::{grid-item-card}
:link: https://doi.org/10.1007/978-3-662-59767-5
:link-type: url
:class-header: bg-light
**Léon 2019 {cite}`puenteleon2019`**
^^^
```{image} content/pictures/2019_Book_Messtechnik.png
:height: 150
```
**Messtechnik**: Grundlagen, Methoden und Anwendungen
+++
Explore this book {fas}`arrow-right`
:::
::::



```{bibliography}
```