#!/usr/bin/env python
# coding: utf-8

# # Checkliste für Protokolle
# 
# Dies ist eine Checkliste, die vor der Abgabe des Protokolls überprüft werden sollte. Sie dient als Leitfaden und sollte an jeden Versuch angepasst werden. Weitere Informationen zum Praktikum und worauf man achten sollte befinden sich auf der [**Praktikums Infoseite**](0_Praktikum.ipynb).
# 
# ## Allgemeine Anforderungen an das Protokoll
# 
# ::::{grid}
# :gutter: 2
# 
# :::{grid-item-card} [Online Latex-Vorlage](https://www.overleaf.com/latex/templates/vorlage-praktikum-messtechnik/zwjgtfpxrszg)
# 
# :::
# 
# :::{grid-item-card} [Word-Vorlage](https://hsuhhde.sharepoint.com/:w:/r/sites/MesstechnikHT23_mst/Freigegebene%20Dokumente/General/Praktikumsvorlagen/Word-Vorlage_Praktikum_Messtechnik.docx?d=wa845bbc7dd434471b44313d9275da187&csf=1&web=1&e=7N30sW)
# 
# :::
# ::::
# 
# - Bitte reiche den Praktikumsbericht unbedingt im **PDF-Format** ein.
# - Sind die Namen aller Teilnehmenden angegeben?
# - Ein Protokoll sollte die folgenden Teile enthalten: Einleitung, Versuchsaufbau, Rohdaten, Auswertung und eine Diskussion der Ergebnisse. Im Folgenden wird genauer auf die Bestandteile dieser Abschnitte eingegangen.
# 
# ## Einleitung
# Die Einleitung sollte einen kurzen Überblick über den Versuch geben und die Ziele des Versuchs sowie dessen Relevanz erläutern.
# - Welcher Versuch wird durchgeführt?
# - Welche Größen sollen bestimmt werden?
# - Welche Größen sollen gemessen werden?
# 
# ## Versuchsaufbau und Durchführung
# - Füge ein Foto des Versuchsaufbaus ein.
# - Beschreibe detailliert, wie der Versuch durchgeführt wurde. Es ist wichtig, dass der Versuch anhand deiner Beschreibung wiederholt und die Ergebnisse überprüft werden könnten. Es sollte klar hervorgehen, welche Größen im Laufe des Versuchs verändert wurden und welche Größen konstant gehalten wurden.
# - Dieser Abschnitt dient der reinen Beschreibung. Ergebnisse oder Fehler sollten hier noch nicht behandelt werden.
# 
# ## Auswertung und Darstellung der Daten
# - Die Auswertung bildet das Herzstück des Protokolls. Hier werden die Daten verarbeitet, und Schlussfolgerungen zu den gemessenen Größen gezogen. Alle Schritte und Gedankengänge sollten nachvollziehbar und deutlich dargestellt sein.
# - Die Daten sollten so aufbereitet werden, dass die gesuchte(n) Größe(n) klar erkennbar sind. Dies kann je nach Versuch eine einfache Berechnung, eine Linearisierung der Ergebnisse oder eine andere Form der Auswertung der Messdaten erfordern, z. B. eine Kurvenanpassung.
# - Alle Berechnungen sollten in SI-Einheiten durchgeführt werden, und die Ergebnisse sollten ebenfalls in geeigneten [**Einheiten**](1_Einheiten.ipynb) angegeben werden (z. B. mm).
# - Die Daten und die Auswertung sollten graphisch dargestellt werden und gegebenenfalls ein Modell angepasst ([**Kurvenanpassung**](1_Kurvenanpassung.ipynb)) werden. Besondere Aufmerksamkeit sollte auf folgende Punkte gelegt werden:
#     - Achsenbeschriftung: Sie sollte leicht lesbar sein und den Messwert sowie die Einheit enthalten. (Hinweis: Die Standardschriftgröße in Python ist möglicherweise zu klein.)
#     - Titel der Grafik oder aussagekräftige Bildunterschrift in Latex oder Word einfügen.
#     - Darstellung der Datenpunkte inklusive Fehlerbalken.
#     - Die Auswertung kann auch als Linie dargestellt werden.
#     - Es ist hilfreich, geeignete Achsenskalierungen zu verwenden, sowohl in Bezug auf den Bereich der Datenpunkte als auch auf eine mögliche logarithmische Darstellung (siehe [**Einheiten**](1_Einheiten.ipynb)).
#     - Die Daten sollten leicht ablesbar sein. Ein Gitternetz in der Grafik kann hierbei helfen.
# - Die [**Unsicherheiten**](1_Messunsicherheiten.ipynb) der Messungen sollten berücksichtigt werden. Welche Geräte oder Messwerte könnten abweichen? Welche Gründe gibt es für diese Annahme?.
# - Die Fehler der Daten sollten bestimmt werden. Dazu sollte eine [**Fehlerfortpflanzung**](1_Fehlerfortpflanzung.ipynb) durchgeführt werden.
# 
# ## Diskussion und Analyse
# In diesem Abschnitt sollten die Messergebnisse und die Auswertung kritisch betrachtet werden. Fragen, die bei Relevanz zu beantworten sind, könnten sein:
# - Sind die Werte realistisch? Wie verhalten sie sich im Vergleich zum Literaturwert? Was könnten mögliche Gründe für Abweichungen sein?
# - Wie groß ist der berechnete Fehler im Vergleich zu den Messwerten? Lässt sich eine genaue Aussage über das System treffen?
# - Deuten die Ergebnisse auf einen großen systematischen Fehler hin?
# - Können Fehlerquellen auf eine genaue Ursache zurückgeführt werden, z. B. das Austauschen des Messgeräts während des Versuchs, unzureichende Datenlage, Justierungen während des Versuchs usw.?

# In[ ]:




