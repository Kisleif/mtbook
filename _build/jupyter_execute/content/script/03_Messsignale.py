#!/usr/bin/env python
# coding: utf-8

# # Messsignale

# Bisher haben wir uns mit dem stationären Messungen einer physikalischen Größe befasst. Bis zu diesem Punkt sollte jedem bekannt sein was eine Kennlinie $y(x)$ ist und was die Sensitivität bedeutet. Außerdem haben wir uns mit Störungen und Unsicherheiten befasst, die während Messungen auftreten können und wie wir diese anhand von Fehlerabschätzungen und Fehlerfortpflanzungen abschätzen können. Außerdem sollte jede/r in der Lage eine Kurvenanpassung inkl. Fehlerbalken und Fehlerfortpflanzung auf gemessene Werte anwenden zu können.
# 
# ```{tableofcontents}
# ```

# ## Zusammenfassung
# 
# | Begriff | Beschreibung |
# |:--------------------|:----------------------------------------|
# |Messsignal|Träger der Information von physikalischen Größen: Messinformation die von der Messgröße ermittelt wurde|
# |(zeit-) kontinuierlich|Messwert besitzt zu jedem Zeitpunkt einen bestimmten Wert|
# |wertkontinuierlich / analog|Ein Signal mit einem unendlichen Wertevorrat für die Messwerte|
# |zeitdiskret / diskontinuierlich|Messwerte sind nur zu bestimmten Zeitpunkten definiert|
# |wertdiskret / amplitudendiskret|Ein Signal mit einem endlichen Wertevorrat für die Messwerte|
# |Digital|Signale, die sowohl zeit-, als auch wertdiskret sind|
# |Deterministisch|Größe / Informationsparameter ist zu jedem Zeitpunkt eindeutig definiert|
# |Stochastisch|Größe unterliegt zufälligen Einflüssen. Eine Wertezuordnung ist nur über längere Betrachtung und statistischer Analyse möglich (Rauschen beispielsweise)|
# |Modulation|Informationssignal verändert ein Trägersignal in Amplitude, Frequenz oder Phase|
# |Demodulation|Einrichtung zur Rückgewinnung des Modulationssignals (Messinformation)|
# |Analog-Digital-Wandlung|Abbildung eines analogen Wertevorrats auf einen endlichen|
# |Aliasing|Möglicher Fehler bei der Digitalisierung bei Verletzung Nyquist-Shannon. Durch Aliasing kann ursprüngliche analoge Zeitfunktion nicht mehr rekonstruiert werden.|
# |Mittelwert|Nach vereinbarter Berechnungsvorschrift ermittelter repräsentativer Wert für ein zeitveränderliches Signa, der dieses Signal durch nur einen Zahlenwert beschreibt|
# |Periodisches Signal|Ein Signal, bei dem eine Wiederholung des Zeitverlaufs der Amplitude des Signals nach der Periodendauer T erkennbar ist|
# |Formfaktor|Quotient aus Effektivwert und Gleichrichtwert eines periodischen Signals|
# |Scheitelfaktor (Crestfaktor)|Quotient von Spitzenwert (Amplitude) und Effektivwert eines perdioschen Signals|
# |Effektivwert|Quadratischer Mittelwert, welcher zur Berechnung von Leistungen genutzt wird|
# |Gleichrichtwert|Gleichgerichteter Mittelwert für Einweg- oder Zweiweggleichrichtungen. Kann als Maß für die Amplitude genutzt werden|
# |Fourier-Reihen|Jedes periodische Signal kann als Summe von Sinus- und Cosinusfunktionen geschrieben werden|
# |Fourier-Koeffizienten|Geben an wie stark eine bestimmte Frequenz in einem persischem Signal vertreten ist|
# |Amplituden-/Betragsspektrum|Grafische Darstellung der Frequenzanteile in einem Amplituden-Frequenz-Diagram |
# |Fourier-Transformation|Spektrum eines aperiodischen Signals. Liefert anstelle eines Amplitudenspektrums ein Amplitudendichtespektrum|
# |Amplitudendichtespektrum|Normierung des Amplitudenspektrum mit der Abtastfrequenz. Einheit z.B. V/Hz|
