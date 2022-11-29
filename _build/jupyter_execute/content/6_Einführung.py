#!/usr/bin/env python
# coding: utf-8

# # Einführung

# Bei der Messtechnik geht es darum physikalische Messgrößen aus dem Umwelt zu beobachten und diese mithilfe einer Messkette / einem Messsystem zugänglich zu machen. Im vorangegangenen Abschnitt haben wir uns mit dem Messsystem selber beschäftigt und wie elektrische Größen gemessen werden können. In diesem Abschnitt wollen wir nicht-elektrische Messgrößen mithilfe von Sensoren messbar machen. 
# Sensoren wandeln eine nicht-elektrische Messgröße in eine elektrische um, wodurch anschließend die Kenntnisse der vorangeganenen Kapitel wieder angewendet werden können. 
# 
# :::{figure-md} messgroesse1
# <img src="draw/messgroesse.jpg" alt="messgroesse1" width="600px" label = messgroesse1>
# 
# Darstellung der Messkette.
# :::
# 
# 1. Die Messgröße wird mittels Sensor aufgenommen in ein elektrisches Signal gewandelt (ggf. wird es noch zusätzlich gefiltert und gegen äußerliche Störgrößen abgeschirmt).
# 2. Das Messsignal wird mittels Multiplexer ausgewhält.
# 3. Der Pegel des Messsignals wird an das Messsystem angepasst, also ggf. verstärkt oder abgeschwächt.
# 4. Das Messsignal wird abgetastet, z.B. über Sample & Hold. Es liegt  liegt also zeitdiskret vor.
# 5. Das Messsignal wird digitalisiert mittels Analog-Digital-Umwandler (ADU). Es liegt jetzt also wertediskret vor.
# 6. Das Messsignal wird angezeigt und wird ggf. weitergeleitet (z.B. an eine Steuerungseinheit für Regelaufgaben und Automatisierungstechnik).
# 
# ## Äußere Störeinflüsse
# Wie schon unter 1. erwähnt, muss sicher gestellt sein, dass wirklich nur die gewünschte physikalische Messgröße vom Sensor aufgenommen wird und keine, oder nur wenig, Störungen wir elektromagnetische Verträglichkeit (EMV), hochfrequente Störwellen (WLAN, GHz) aus der Umgebung einkoppeln. Hierfür werden die Kabel abgeschirmt. Je höher die Übertragungsrate (Frequenz), desto mehr Störungen sind möglich. 
# 
# Moderne elektronische Schaltungen werden immer minimaler und die Bauteile liegen mitunter sehr dicht beinander. Durch diese kompakte Bauweise können mehr elektro-magnetische Kopplungen, Schwingungen und Störsignale in die Messung einkoppeln. 
# 
# ## Filtern von Störeinflüssen
# Zur Vermeidung und Reduzierung von Störeinflüssen werden Filter verwendet, die Störsignale mit Frequenzen außerhalb des Nutzsignalbereichs unterdrücken. 
# Vorrangig dienen hierzu analoge Filter 1. und 2. Ordnung. Bei Filtern höherer Ordnung muss die *Welligkeit* der Filter berücksichtigt werden. Diesen werden beispielsweise eingesetzt um Netzbrummen zu reduzieren. 
# 
# Rundfunksender oder Mobilfunknetze produzieren Störsignale bei hohen Frequenzen. Um diese zu Unterdrücken werden **Tiefpass-Filter** eingesetzt. **Bandpass-Filter** können benutzt werden um die Nutzbandbreite einzugrenzen und somit das Signal-Rausch-Verhältnis zu verbssern. 
# 
# ## Verarbeitung eines Messsignals
# Häufig werden rauscharme und sehr leistungsfähige **Operationsverstärker** benutzt, bei denen über Widerstände (im einfachsten Fall lediglich 2 Widerstände) die **Verstärkung** eingestellt werden kann. 
# 
# Damit Sensor und Messsignalverarbeitung möglichst rückwirkungsfrei sind, werden **Impedanzwandler** eingesetzt. 

# In[ ]:




