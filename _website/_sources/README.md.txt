#  [Übungspool](https://kisleif.github.io/mtbook/_website/uebungen/index.html) der Messtechnik der HSU

In diesem Repository werden alle Übungsaufgaben der Messtechnik als Markdown (.md) Dateien gesichert. 
Dies sind die Quelldateien, woraus später die HTML Webseite kompiliert wird.

## Issues nutzen!!!
1. Bevor ihr eine Aufgabe korrigiert, erstellt erst ein Issue, mit dem Titel der Aufgabe, und assigned es entsprechend an euch selber. So umgehen wird das Problem, dass mehrere Leute die gleiche Aufgabe korrigieren. Optimal wäre noch ein Link zur Aufgabe im Git, also eine Verlinkung zur Markdown Datei. 
2. Bevor ihr eine Aufgabe korrigiert, kontrolliert bitte erst, ob es bereits ein Issue zu der Aufgabe gibt ;) (siehe 1.)
3. Wenn ihr eine Lösung zu einer Aufgabe erstellt, dann markiert ihr das Issue zu der Aufgabe mit dem Tag `Lösung`. Sollte noch kein Issue zu der Aufgabe existieren, dann erstellt eins (siehe 1.). 

## Aufgaben korrigieren und neue erstellen
Dies geht bereits ohne Klonen des Repositories direkt im Browser:
1. Ihr möchtet eine Aufgabe **korrigieren**? Wann sucht die dazugehörige .md Datei raus und editiert sie im Browser (oder dem geklonten Repository auf eurem Rechner).
2. Ihr möchtet eine neue Aufgabe **hinzufügen**? Dann erstellt eine neue .md Datei im Hauptordner im Browser (oder dem geklonten Repository auf eurem Rechner). Bitte als Header an anderen Markdown Dateien orientieren, bzw. den folgenden kopieren. Später wird `date` und `location` für den jeweiligen Jahrgang neu gesetzt. Ein Datum, was in der Zukunft liegt, erscheint später nicht online im Übungspool!

```
---
blogpost: true
date: Dec 11, 2023
category: Übung
location: Zettel_10
tags: Widerstand, Messbrücke, Elektronik, Sensor, DMS
---
```

Solltet ihr im Repository auf eurem Rechner arbeiten, vergesst nicht im Anschluss zu committen and pushen. 

## Aufgaben als HTML kompilieren
Dafür müsst ihr dieses Repository auf eurem PC klonen. 
Navigiert im Terminal in den Hauptordner (mtbook_uebungen) und führt folgenden Terminal-Befehl aus: `ablog build`.
Danach findet ihr die HTML Datein jeder einzelnen ÜBungsaufgabe im Unterordner `_website`. Klickt diese einfach an (z.B. `index.html`).

Bei Fehlern/Errors versucht `ablog clean` mit anschließendem `ablog build`.

Ihr könnt diesen Ordner auch pushen. 

## Upload der Aufgaben in den Online Pool 
KSI wird die Übungen online stellen, welche aus diesem Repository mittels `ablog build` erstellt werden. Hier für eine kurze Nachricht an KSI schreiben. Sie wird dann neue HTMLs generieren und im  [Übungspool](https://kisleif.github.io/mtbook/_website/uebungen/index.html) veröffentlichen. 


