---
blogpost: true
date: Oct 1, 2024
location: Übungszettel
category: Übung
tags: Abtastung, Dreieck, Aliasing
---

# Abtastung von Messsignalen

## A1: Abtastung eines Dreiecksignals in der Audiotechnik

Ein Musikproduktionsstudio verwendet Synthesizer, die Dreiecksignale erzeugen. Diese Signale müssen korrekt digitalisiert werden, um die Klangqualität zu bewahren.

Ein ideal angenommenes Dreiecksignal mit einer Periodendauer von $1\,\mathrm{ms}$ wird mit einer Abtastrate von $10\,\mathrm{kHz}$ digitalisiert.


1. **Überprüfung des Abtasttheorems:**

   * Geben Sie an, ob in diesem Fall das Abtasttheorem nach Shannon erfüllt ist!
   * Begründen Sie Ihre Antwort!

2. **Effekte bei Verletzung des Abtasttheorems:**

   * Welcher Effekt tritt ein, wenn das Abtasttheorem verletzt ist?
   * Erläutern Sie diesen Effekt mit einer einfachen Skizze.

3. **Praktische Anwendung:**

   * Erklären Sie, warum es in der Audiotechnik wichtig ist, die Abtastfrequenz korrekt zu wählen und welche Konsequenzen eine Verletzung des Abtasttheorems haben könnte.

## A2: Abtastung eines Rechtecksignals in der Radartechnik

GPS (Global Positioning System) ist ein satellitengestütztes Navigationssystem, das genaue Standort- und Zeitinformationen liefert. GPS basiert auf Satelliten, die mit codierten **Radiosignalen** ständig ihre aktuelle Position und die genaue Uhrzeit ausstrahlen. Aus den Signallaufzeiten können spezielle Empfänger ihre eigene Position und Geschwindigkeit berechnen. Theoretisch reichen die Signale von drei Satelliten aus, welche sich oberhalb ihres Abschaltwinkels befinden müssen, um daraus die genaue Position und Höhe zu bestimmen. Das GPS-Signal hat eine Wellenlänge von $19\,\mathrm{cm}$, was einer Frequenz von $1,57542\,\mathrm{GHz}$ entspricht. Aufgrund der hohen Frequenz und der zahlreichen Oberwellen ist es entscheidend, die Signale korrekt abzutasten, um Aliasing zu vermeiden und präzise Positionsdaten zu erhalten.
Ein Rechtecksignal (hier stellvertetend für den PRN code) mit einer Grundfrequenz von $10\,\mathrm{MHz}$ wird mit einer Abtastrate von $200\,\mathrm{MHz}$ digitalisiert.

1. **Überprüfung des Abtasttheorems:**

   * Geben Sie an, ob in diesem Fall das Abtasttheorem nach Shannon erfüllt ist!
   * Begründen Sie Ihre Antwort!

2. **Effekte bei Verletzung des Abtasttheorems:**

   * Welcher Effekt tritt ein, wenn das Abtasttheorem verletzt ist?
   * Erläutern Sie diesen Effekt mit einer einfachen Skizze.

3. **Praktische Anwendung:**

   * Erklären Sie, warum es in der Radartechnik wichtig ist, die Abtastfrequenz korrekt zu wählen und welche Konsequenzen eine Verletzung des Abtasttheorems haben könnte.
