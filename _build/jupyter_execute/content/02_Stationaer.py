#!/usr/bin/env python
# coding: utf-8

# # Stationäre Messsysteme
# 
# Wir benutzen Messsysteme, um eine Messgröße in einen Messwert umzuführen. Hierbei werden wir den realen, echten Wert der Messgröße jedoch nie erfahren (Damit befassen wir uns im Kapitel  [Messunsicherheiten](1_Messunsicherheiten.ipynb)). 
# Ein Messwert kann direkt vom Messgerät angezeigt werden, beispielsweise über ein Display, oder er steht als Datenwert in analoger oder digitaler Form zur Verfügung, welcher mit entsprechenden Geräten oder Algorithmen weiterverarbeitet werden muss. 
# 
# In diesem Kapitel wollen wir uns mit den Begrifflichkeiten und Kenngrößen eines Messsystems befassen. Hierbei nehmen wir vorerst an, dass sich die Messwerte über die Zeit während des Messprozesses nicht ändern. Diese Art von Messsystemen werden *statische Messsysteme* genannt. 
# 
# ```{tableofcontents}
# ```

# ## Zusammenfassung
# 
# | Begriff | Beschreibung |
# |:--------------------|:----------------------------------------|
# |Empfindlichkeit | Das Verhältnis von Änderung der Ausgangsgröße zu der sie verursachenden Änderung der Eingangsgröße wird als Empfindlichkeit bezeichnet.|
# | Übertragungsfaktor | Er berechnet sich aus dem Quotienten von Ausgangsgröße zu Eingangsgröße eines Übertragungssystems (Definition der Empfindlichkeit für ideale Kennlinien). |
# | Kennlinie | Über den gesamten Eingangsbereich der Messeinrichtung wird der Übertragungsfaktor durch die statische Kennlinie beschrieben.|
# | Ideale Kennlinie | Lineare, statische Kennlinie |
# | Messbereich (engl. range) | Garantierter Bereich, in dem das Messgerät gemäß Spezifikation korrekt arbeitet |
# | Spanne (engl. span) | Differenz zwischen Messbereichsende und Messbereichsbeginn |
# | Vollbereichssignal (engl. full scale output) | Ausgang, der mit der „Spanne“ der Messwerteingänge korreliert |
# | Kenngröße, statisch / stationär | Kenngrößen, die im eingeschwungenen Zustand einer Übertragungseinrichtung wirksam sind. |
# | Kenngröße, dynamisch | Kenngrößen, die das zeitabhängige Übertragungsverhalten beschreiben.|

# In[ ]:




