# Dioden-Kennlinie

In diesem Praktikum wird das Oszilloskop des Moku:Go-Messgerätes und sein integrierter Wellenformgenerator verwendet um die Kennlinien von Dioden zu untersuchen. Bringe deinen eigenen Laptop mit und installiere (vorab) die [Moku:Go Software](https://www.liquidinstruments.com/products/desktop-apps/).

<img src="pictures/IMG_5597.jpeg" alt="kennlinienversuch" label = kennlinienversuch></img>

## Downloads

* {Download}`Hier<lab/Kennlinie/main.pdf>` kann die Praktikumsanleitung herunterladen werden.
* {Download}`Hier<Vorlage Praktikum Messtechnik.zip>` steht das LaTeX Template für euren Praktikumsbericht zum Download bereit. 

## Verständnisfragen zur Vorbereitung
1. Erkläre mithilfe einfacher Skizzen die Gleichrichterwirkung einer Halbleiterdiode.
2. Beschreibe die I(U)-Kennlinie eines p-n-Übergangs.
3. Beschreibe das Messverfahren zur Bestimmung einer I(U)-Kennlinie.
4. Erkläre strom- und spannungsrichtige Messungen.
5. Der Strom durch eine unbekannte LED soll 20 mA keinesfalls überschreiten. Zum Schutz der Diode wird ein Vorwiderstand RV vor die Diode geschaltet. Wie groß muss der Vorwiderstandswert sein, um den Stromfluss ganz sicher unter 20 mA zu halten, wenn die verwendete Quelle eine Spannung von 6,0 V besitzt? Hinweis: Da wir uns ganz sicher sein wollen und uns die Diode unbekannt ist, kann der Widerstand der Diode selbst vernachlässigt werden.

## Stichwörter, die du kennen solltest...
Kennlinie, Diode, LED, p-n-Übergang, stromrichtig und spannungsrichtig

## Topics to prepare aus dem Vorlesungsskript
- ...

## Auswerteskript als Jupyter Notebook 
Als Grundlage für die Datenanalyse der Messdaten stellen wir euch ein [Jupyter-Notebook](lab/Kennlinie/Kennlinien.ipynb) und {Download}`Musterdaten<lab/Kennlinie/MokuOscilloscopeData_20221007_133233_Traces.csv>` zur Verfügung. Dies bietet jedoch nur die Grundlage und beinhaltet nicht die komplette Versuchauswertung, die ihr durchführen müsst!

## Literatur
::::{grid} 1 1 1 2
:class-container: text-center
:gutter: 3

:::{grid-item-card}
:link: https://doi.org/10.1007/978-3-658-27131-2
:link-type: url
:class-header: bg-light
**Parthier 2020 {cite}`parthier2020`**
^^^
```{image} pictures/2020_Book_Messtechnik.png
:height: 150
```
**Messtechnik**: Vom SI-Einheitensystem über Bewertung von Messergebnissen zu Anwendungen der elektrischen Messtechnik
+++
Explore this book {fas}`arrow-right`
:::

:::{grid-item-card}
:link: https://link.springer.com/content/pdf/10.1007/978-3-658-14387-9.pdf
:link-type: url
:class-header: bg-light
**Stiny 2015 {cite}`stiny2015`**
^^^
```{image} pictures/2015_Book_AktiveBauelemente.png
:height: 150
```
Aktive elektronische Bauelemente
+++
Explore this book {fas}`arrow-right`
:::

::::


```{bibliography}
:filter: docname in docnames
```