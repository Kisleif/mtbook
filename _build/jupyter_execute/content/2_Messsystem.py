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
# Dies ist einer der ersten Messketten, die wir kennenlernen. Allgemein findet man immer wieder die gleichen Komponenten in solchen Ketten, die im folgenden aufgelistet werden:
# 
# * **Aufnehmer/Sensor** (auch Messgrößenaufnehmer genannt): Die Erfassung der physikalischen Messgröße, $u$, wird mit einem entsprechend geeigneten *Sensor* realisiert. Mit konkreten Sensoren werden wir uns noch am Ende der Vorlesung genauer beschäftigen. Einige Beispiele werden uns aber während der kompletten Veranstaltung immer mal wieder begneten. Ein Sensor nimmt eine Messgröße auf, z.B. die Umbegungstemperatur, wandelt diese beispielsweise in eine Widerstandänderung um, welche wiederum in ein weiterverarbeitungsfähigen Signals (hier elektrisch) mit einer geeigneten Schaltung umgewandelt wird. 
# * **Verstärkung**: An dieser Stelle startet die Messsignalverarbeitung. Da das elektrische Primärsignal mitunter sehr  klein sein kann, muss es deshalb vielleicht noch verstärkt werden, bevor es einer Digitalisierung zugeführt werden kann.
# * **Anpassung** (optional): Die meist elektrische Größe wird in einen darstellbaren Messwert umgewandelt. Hierfür werden Messschaltungen mit Messverstärken oder Computern verwendet.
# * **Messwertausgabe** (diverse): Anzeige, Registrierung, Speicherung, Dokumentation in analoger oder digitaler Form können an dieser Stelle in die Messkette implementiert werden.
# * **Digitalisierung**: Dies ist die häufigste Art der *Messwertausgabe*. Das analog vorliegende elektrische Signal wird in ein Digitalwort umgewandelt. 
# * **Digitale Signalverarbeitung**: Durch Algorithmik wird der Messwert digital weiterverarbeitet. Häufig können an dieser Stelle auch Korrekturen vorgenommen werden, um beispielsweise Kennenlinienfehler zu minimieren und zu korrigieren. Dies werden wir gleich noch genauer betrachten. Ausgegeben wird schließlich ein Messwert $y$.
# 
# Jede einzelne der Komponenten führt das jeweilige Eingangssignal in ein Ausgangssignal über. Im Folgenden werden wir die wichtigste statische Kenngröße, nämlich den **Übertragungsfaktor** $k$ kennenlernen. Dieser gilt auch für dynamische Systeme, sobald diese sich in einem eingeschwungenen Zustand befinden und als stationär angenommen werden können. 
# Der Übertragungsfaktor $k$ wird auch *Verstärkungsfaktor* genannt. 
# Über den gesamten Eingangsbereich der Messeinrichtung wird der Übertragungsfaktor durch die statische **Kennlinie** beschrieben. Danach ergibt sich mit einem bestimmten Eingangsbereich der Messeinrichtung ein korrespondierender Ausgangssbereich. 
