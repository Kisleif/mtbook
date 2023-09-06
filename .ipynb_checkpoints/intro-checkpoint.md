# Welcome

Willkommen im *Metrology Lecture Book*, dem **Vorlesungsskript** zur Messtechnik an der Helmut-Schmidt-Universität. Hier hast du die Freiheit, selbstständig zu lernen. Dieses Vorlesungsskript wird deine Hauptinformationsquelle sein und die Grundlagen der Messtechnik vermitteln. Zusätzlich stehen dir begleitende YouTube-Videos und Literaturhinweise zur Verfügung, um Basiswissen zu lernen, zu wiederholen oder zu vertiefen.

## Kommentare und Markierungen
Du bestimmst dein Lerntempo und kannst die Videos nutzen, um das Skript zu ergänzen. Stelle Fragen, diskutiere mit anderen und gestalte dein Lernen aktiv mit, indem du zum Bepisiel die **Kommentier- und Highlight-Funktion** in https://hypothes.is/ benutzt: 

* Klickt ganz oben am rechten Seitenrand auf den Pfeil, das Auge oder das Papier.
* Unter https://hypothes.is/ registrieren bzw. einloggen, wenn bereits ein Account besteht.
* Ggf. auf https://hypothes.is/ eine neue Gruppe für eigene Notizen erstellen.
* Auf der Seite die entsprechende Gruppen auswählen, in der ihr Notizen anlegen wollt.
* Text auf der Seite markieren und ggf. Notizen hinzufügen. 

```{tip}
Legt eine gemeinsame Gruppe für die Klausurvorbereitung an!
```

```{tip}
Auf der Webseite https://hypothes.is/ findet ihr eure Kollektion von Notizen und könnt sie direkt als Karteikarten benutzen. 
```


## Python / Jupyter-Notebooks
Fast jede Webseite im Metrology Lecture Book ist ein *J*Jupyter-Notebook**. 

```{warning} Entwarnung
Um dem **Vorlesungsskript** zu folgen, sind **keine Python-Kenntnisse erforderlich**. 
```

Dadurch habt ihr die Möglichkeit, den Code selbst auszuführen, Parameter anzupassen, zu experimentieren und ganz nebenbei Python zu lernen. Zusätzlich könnt ihr Python nutzen, um eure Messdaten aus dem Praktikum auszuwerten. Wir stellen bereits eine Sammlung von Jupyter-Notebooks für ausgewählte Praktikumsversuche zur Verfügung, um den Einstieg zu erleichtern. Das Schöne daran ist, dass Python Open Source ist, und ihr  sofort loslegen könnt:

### Sofort Notebooks im Browser mit 'Colab' ausführen
Ihr habt die Möglichkeit, die in unserem *Metrology Lecture Book* enthaltenen **Jupyter-Notebooks** direkt im Browser (*ohne lokale Python Installation*) auszuführen. Dazu klickt ihr oben auf das Symbol der *Rakete* und wählt anschließend `Colab` aus. Dies öffnet eine interaktive Umgebung im Browser, in der das Jupyter-Notebook gestartet wird. Beachtet, dass das Symbol der *Rakete* nur auf den Seiten erscheint, die als Jupyter-Notebooks vorliegen.

### Notebooks auf eurem Computer ausführen 
Wenn ihr eure Analyse für die Praktikumsdaten mit Python durchführen möchtet, müsst ihr Python auf eurem Computer 
Wir empfehlen für Neueinsteiger die Installation von **Jupyter Lab**:
<iframe width="560" height="315" src="https://www.youtube.com/embed/jZ952vChhuI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

```{seealso}
Für einen schnellen Einstieg könnt ihr Jupyter-Lab auch sofort online ausprobieren: [Jupyter-Lab sofort ausprobieren](https://jupyter.org/try-jupyter/lab/).
```

Die Jupyter-Notebooks könnt ihr herunter laden, indem ihr oben rechts auf den Download-Button drückt und dann `ipynb`auswählt. 
Öffnet die Jupyter-Notebooks (`.ipynb`-Dateien) ganz einfach per Doppelklick auf eurem lokalen Dateisystem. 


::::{grid} 1 1 2 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: content/0_Praktikum
:link-type: doc
:class-header: bg-light
**Tips für's Praktikum** 👩‍🔬
^^^

Messdaten richtig sammeln, dokumentieren und analysieren.
:::

:::{grid-item-card}
:link: content/T_Tutorials
:link-type: doc
:class-header: bg-light
**Über dieses Skript** 🐍
^^^

Einführung in Python und Jupyter-Notebooks.
:::


:::{grid-item-card}
:link: content/Aufgabenpool
:link-type: doc
:class-header: bg-light
**Aufgabenpool** 🧑🏽‍💻
^^^

Übungen zur Messtechnik inkl. Klausurvorbereitung.
:::
::::

## Vorlesungsinhalt

Was ist die Aufgabe der Messtechnik, wozu wird sie benötigt und wo kommt sie zum Einsatz? Wer sind die Anwender?

Die Messtechnik ist ein unverzichtbarer Bestandteil unseres Alltags und manifestiert sich in verschiedensten Anwendungen. Sie ist in unseren Handys präsent, ermöglicht die genaue Erfassung von Temperatur- oder Stickstoffwerten in der Umwelt und spielt eine zentrale Rolle in der Prozess- und Fertigungstechnik. Um physikalische oder chemische Größen präzise zu beschreiben und auszuwerten, ist eine strukturierte Herangehensweise erforderlich.

Im Rahmen dieser Vorlesung werden wir die folgenden Fragen beantworten:
1. Welche Besonderheiten und Einheiten sind mit bestimmten physikalischen Messgrößen verbunden?
2. Welche Messgeräte stehen für diese Größen zur Verfügung?
3. Welche Aspekte müssen bei der Anwendung dieser Messgeräte berücksichtigt werden?
4. Mit welchen Methoden erfolgt die Auswertung von Daten?

Heutzutage basieren messtechnische Lösungen auf elektronischen Systemen. Dabei kommen häufig eigenständige Messgeräte oder elektronische Messmodule für Computer zum Einsatz, die auf elektronischen Bauteilen und Schaltungen basieren. Daher werden wir uns insbesondere mit der Messung elektrischer Kenngrößen wie Spannung, Strom, Leistung, Widerstand, Kapazität und Induktivität befassen.

Für die Messung nicht-elektrischer Größen werden in der Messtechnik spezielle Sensoren verwendet. Ein Sensor wandelt mithilfe eines bestimmten physikalischen oder chemischen Funktionsprinzips die nicht-elektrische Größe in ein elektrisches Signal um, das anschließend elektronisch weiterverarbeitet werden kann. Beispiele für nicht-elektrische Größen, die mithilfe von Sensoren erfasst werden können, sind Temperatur, Druck, Feuchtigkeit, Durchfluss, Abstand, Winkel, Kraft, Beschleunigung, CO2-Konzentration, Schalldruck und viele mehr.

::::{grid} 1 1 3 3
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: content/V1
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
:link: content/V2
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
:link: content/V3
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
:link: content/V4
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
:link: content/V5
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
:link: content/V6
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
:link: content/V7
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
:link: content/V8
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

:::{grid-item-card}
:link: https://www.hugendubel.de/de/ebook_epub/joerg_boettcher-kompendium_messtechnik_und_sensorik-39585264-produkt-details.html?utm_source=zxp&utm_medium=pdm&utm_campaign=pd&utm_campaign=RedBrainCSS&adCode=720R10B11W11A&utm_medium=af&awc=9362_1664124494_2a569d96f1d670a143e920798d1426c7&utm_source=zx&utm_content=Lkg
:link-type: url
:class-header: bg-light
**Böttcher 2020 {cite}`boettcher2020`**
^^^
```{image} content/pictures/2020_Book_Boettcher.png
:height: 150
```
**Kompendium**: Messtechnik und Sensorik
+++
Explore this book {fas}`arrow-right`
:::

::::




```{bibliography}
:filter: docname in docnames
```