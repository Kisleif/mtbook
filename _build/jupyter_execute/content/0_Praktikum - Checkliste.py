#!/usr/bin/env python
# coding: utf-8

# # Kurze Checkliste für Protokolle
# 
# 
# Dies ist eine Checkliste, mit Dingen, die vor Abgabe des Protokolls überprüft werden sollten. Sie ist als Stütze gedacht, und sollte an jeden Versuch angepasst werden. Weitere Infos yum Praktikum und worauf geachtet werden sollte finden sich auch unter [**Praktikum**](0_Praktikum.ipynb).   
# 
# ## Generell zum Protokoll
# - Bitte reiche deine Praktikumsberichte unbedingt als **PDF** ein. In Absprache mit dem jeweiligen Praktikumsbetreuer, ist auch die Abgabe als Jupyter-Notebook möglich. </br>
# - Sind die Namen von allen Teilnehmenden angegeben </br>
# - Ein Protokoll besteht aus Einleitung, Versuchsaufbau, Rohdaten, Auswertung, und einer Diskussion der Ergebnisse. Im folgenden wird nochmal auf die Bestandteile der einzelnen Teile eingegangen </br>
# 
# ## Einleitung
# Die Einleitung sollte ein kurzer Abriss von dem Versuch sein, der einen kurzen Überblick über die Ziele des Versuchs und warum es relevant ist geben. 
# - Welcher Versuch ist es? </br>
# - Welche Größen sollen bestimmt werden? </br>
# - Welche Größen sollen gemessen werden? </br>
# 
# ## Versuchsaufbau- und Durchführung
# - Photo vom Aufbau einfügen </br>
# - Beschreiben wie der Versuch durchgeführt wurde. Hier ist es wichtig, dass der Versuch anhand der Beschreibeung wiederholt  und die Ergebnisse überprüft werden könnten. Es muss z.B. klar hervorgehen welche Größen im Laufe der Versuches geändert wurden und welche Größen konstant gehalten wurden.</br>
# - Dieser Abschnitt dient der Beschreibung. Auf Ergebnisse oder Fehler soll hier noch nicht eingegangen werden. </br>
# 
# ## Auswertung und Darstellung der Daten
# - Die Auswertung ist das Herzstück des Protokolls. Hier werden die Daten verarbeitet und Schlüsse über die gemessenen Größen gezogen. Generell ist wichtig, dass alle Schritte und Gedankengänge **nachvollziehbar und deutlich** dargestellt sind. </br>
# - Für die Auswertung sind die Daten so aufzubereiten, dass die gesuchte(n) Größe(n) klar erkennbar sind. Dies kann je nach Verusch eine reine Ausrechnung sein, eine linearisierung der Ergebnisse oder eine andere Auswertung der Messdaten, wie z.B. eine Kurvenbestimmung. </br>
# - **Es soll in SI Einheiten gerechnet werden.** Bei der Darstellung der Ergebnisse sind ebenfalls überall Einheiten anzugeben. Hierbei sind entweder Zehnerpotenzen oder geeignete Präfixe für die SI Einheiten zu gebrauchen (z.B. mm). Mehr zu Einheiten findest du auch hier: [**Einheiten:**](1_Einheiten.ipynb) </br>
# - Die Daten sowie die Auswertung sollen graphisch dargestellt werden. Das ist unter [**Kurvenanpassung:**](1_Kurvenanpassung.ipynb) auch nochmal nachzulesen. Besonders sind folgende Dinge zu beachten: 
#     - Achsenbeschriftung. Diese sollte einfach zu lesen sein und den Messwert sowei die Einheit enthalten (Tipp: Python Standardschriftgröße ist zu klein). </br>
#     - Titel der Graphik. </br>
#     - Datenpunkte inklusive **Fehlerbalken** als Punkte darstellen.</br>
#     - Die Auswertung kann als Linie dargestellt werden. </br>
#     - Es hilft, geeignete Achsenskalierungen zu verwenden. Dies ist sowohl im Bezug auf die Spanne der Datenpunkte als auch auf eine etwaige Logarithmische Darstellung bezogen. </br>
#     - Die Daten sollten leicht abzulesen sein, hierbei hilft z.B. ein "Grid" in der Darstellung. </br>
# - Die Messunsicherheiten müssen in betracht gezogen werden. Welche Geräte oder Messwerte können abweichen? Welche Gründe gibt es für diese Annahme? Mehr über Messunsicherheiten findet sich unter: [**Messunsicherheiten:**](1_Messunsicherheiten.ipynb).
# - Es sollen die Fehler der Daten bestimmt werden. Hierfür wird eine Fehlerfortpflanzung gemacht, die auch hier [**Fehlerfortpflanzung:**](1_Fehlerfortpflanzung.ipynb) besprochen wird. </br>
# 
# 
# ## Diskussion und Analyse
# - Hier sollten die Messergebnisse und die Auswertung nochmals kritisch betrachtet werden. Fragen die bei relevanz zu beantworten sind wären:
#     - Sind die Werte realistisch? Wie verhalten sie sich zum Literaturwert? Was sind mögliche Gründe für eine Abweichung? 
#     - Wie groß ist der berechnete Fehler im Vergleich zu den Messwerten? Lässt sich eine genaue Aussage über das System treffen? 
#     - Deuten die Ergebnisse auf einen großen systematischen Fehler hin? 
#     - Können Anteile des Fehlers auf eine genaue Ursache zurückgeführt werden? z.B. Tauschen des Messgerätes während des Versuches, unzureichende Datenlage, Justierungen während des Versuches etc.
# 
# 
