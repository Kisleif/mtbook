#!/usr/bin/env python
# coding: utf-8

# # Grundstruktur eines Messsystems
# 
# {numref}`grundstruktur` zeigt die generelle Struktur eines Messsystems.
# 
# :::{figure-md} grundstruktur
# <img src="draw/grundstruktur.jpg" alt="grundstruktur" class="bg-primary mb-1" width="800px" label = grundstruktur>
# 
# Generelle Grundstruktur eines Messsystems, bzw Messkette.
# :::
# 
# Dies ist eine der ersten Messketten, die wir kennenlernen. Allgemein findet man immer wieder die gleichen Komponenten in solchen Ketten, die im Folgenden aufgelistet werden:
# 
# * **Aufnehmer/Sensor** (auch Messgrößenaufnehmer genannt): Die Erfassung der physikalischen Messgröße, $u$, wird mit einem entsprechend geeigneten *Sensor* realisiert. Mit konkreten Sensoren werden wir uns noch am Ende der Vorlesung genauer beschäftigen. Einige Beispiele werden uns aber während der kompletten Veranstaltung immer mal wieder begegnen. Ein Sensor nimmt eine Messgröße auf, z.B. die Umgebungstemperatur, wandelt diese beispielsweise in eine Widerstandänderung um, welche wiederum in ein weiterverarbeitungsfähiges Signal (hier elektrisch) mit einer geeigneten Schaltung umgewandelt wird. 
# * **Verstärkung**: An dieser Stelle startet die Messsignalverarbeitung. Da das elektrische Primärsignal mitunter sehr  klein sein kann, muss es deshalb vielleicht noch verstärkt werden, bevor es einer Digitalisierung zugeführt werden kann.
# * **Anpassung** (optional): Die meist elektrische Größe wird in einen darstellbaren Messwert umgewandelt. Hierfür werden Messschaltungen mit Messverstärkern oder Computern verwendet.
# * **Messwertausgabe** (diverse): Anzeige, Registrierung, Speicherung, Dokumentation in analoger oder digitaler Form können an dieser Stelle in die Messkette implementiert werden.
# * **Digitalisierung**: Dies ist die häufigste Art der *Messwertausgabe*. Das analog vorliegende elektrische Signal wird in ein Digitalwort umgewandelt. 
# * **Digitale Signalverarbeitung**: Durch Algorithmik wird der Messwert digital weiterverarbeitet. Häufig können an dieser Stelle auch Korrekturen vorgenommen werden, um beispielsweise Kennenlinienfehler zu minimieren und zu korrigieren. Dies werden wir gleich noch genauer betrachten. Ausgegeben wird schließlich ein Messwert $y$.
# 
# 
# ## Verhalten
# 
# Jede einzelne der Komponenten wandelt das jeweilige Eingangssignal in ein Ausgangssignal um. Dies wird durch den **Übertragungsfaktor** $k$ beschrieben und stellt eine der wichtigsten **statischen** Kenngrößen eines Messsystems dar. Der Übertragungsfaktor sollte für jede Komponente ein lineares Verhalten aufweisen, was bedeutet, dass sich die Ausgangsgröße verdoppeln sollte, wenn sich die Eingangsgröße verdoppelt.
# 
# Zusätzlich zum statischen Verhalten hat jedes Messsystem auch ein **dynamisches Verhalten**. Dabei geht es nicht um die Linearität zwischen Ausgangs- und Eingangsgröße, sondern darum, wie das System auf schnelle Änderungen der Eingangsgröße reagiert. Je schneller sich die Eingangsgröße ändert, desto schneller müssen das Messsystem und der Sensor reagieren, um die Ausgangsgröße anzupassen. Hierbei zeigen sich unterschiedliche Verhaltensweisen, da Sensoren und Messgeräte in ihrer Reaktionsgeschwindigkeit nach oben oder unten begrenzt sein können.
# 
# Im Folgenden werden wir die wichtigste statische Kenngröße, den **Übertragungsfaktor** $k$, genauer kennenlernen. Dieser gilt auch für dynamische Systeme, sobald sie sich in einem eingeschwungenen Zustand befinden und als stationär betrachtet werden können. Der Übertragungsfaktor $k$ wird auch als **Verstärkungsfaktor** bezeichnet. Über den gesamten Eingangsbereich der Messeinrichtung wird der Übertragungsfaktor durch die statische **Kennlinie** beschrieben. Diese beschreibt das Verhältnis zwischen einem bestimmten Bereich der Eingangsgröße und dem korrespondierenden Bereich der Ausgangsgröße.

# In[ ]:




