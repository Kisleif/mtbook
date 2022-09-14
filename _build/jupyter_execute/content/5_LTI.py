#!/usr/bin/env python
# coding: utf-8

# # Linear zeitinvariante (LZI) Systeme 
# <a id="Sec-LZI_system"></a>
# 
# LTI Systeme sind wichtig, da sie zwar sehr vereinfacht sind, aber gut zu lösen sind. Sie sind in der Tat die einzigen Systeme, die wir lösen können (mittels Differentialgleichungen). 
# 
# Für ein LTI System können Ausgangssignale vorhergesagt werden, die man für ein bestimmtes Eingangssignale erwarten würde. Das gleiche gilt auch für *Veränderungen* von Eingangssignalen. 
# 
# ## Eigenschaften
# 
# Das liegt daran, dass LTIs bestimmte Eigenschaften haben: *Superposition, Homogenität und Zeitinvarianz*.
# Im Folgenden sei $h$ ein Operator, der eine lineare Abbildung zwischen Eingangsvektor $x(t)$ und dem Ausgang eines Systems, Vektor $y(t)$, darstellt. 
# Für ein **lineares System** gelten allgemein folgende Eigenschaften:
# * **Homogenität**: Wenn $x(t)$ mit Faktor $a$ skaliert wird, dann wird $y(t)$ ebenso skaliert
#     * Ein Sprung der Größe $A$ produziert eine Schwingung mit Größe $B$
#     * Da h(x) linear ist, wird ein verdoppelter Sprung am Eingang, also $2A$ zu einer Verdopplung am Ausgang, $2B$, führen
# * **Superposition** bedeutet Additivität: Addiere zwei Eingangssignale, $A$ und $B$ zusammen, sprich $A+B$, dann ist die Antwort des linearen Systems auch die Summe der individuellen Ausgänge ($a$ und $b$), also $a+b$. 
# * **Zeitinvariant**: Das Systeme verhält sich immer gleich, egal wann in der Zeit es durchgeführt wird.
#     * Wird das Eingangssignal $$x(t) um $T$ verschoben, dann ist auch das Ausgangssignal um $T$ verschoben.
# 
# In Realität gibt es fast immer Abweichungen von diesen Idealvorstellungen. D.h. wir können mit LTIs Eingänge eines Signals skalieren, verschieben und summieren, aber sie entsprechen niemals einem realen System. Warum sind sie dann so wichtig? Richard Feynman sagte damals: „Linear Systems are important, because we can solve them“. 
# Selbst wenn LTI nicht real ist, so können wir reale Probleme sehr gut *annähern* indem wir LTI Analysen durchführen.
# Das heißt, stell immer sicher, dass dein System für einen bestimmten Bereich linear funktioniert. 
# 
# ![Bild](pictures/LZI.png)

# ## System-Identifizierung
# <a id="Sec-System-Identifizierung"></a>
# 
# Jedes Messsystem hat eine spezifische Übertragungsfunktion $h(t)$, welche, angewendet auf ein Eingangssignal $x(t)$, ein Ausgangssignal $y(t)$ liefert. Im Allgemeinen kann man drei Probleme in der Praxis erkennen, jenachdem welche Informationen einem vorliegen:
# 
# 1. $x(t)$ und $h(t)$ sind gegeben -> $y(t)$ ist gesucht: Dies ist das **Simulationsproblem**
#     * Anhand von Simulationen kann der Ausgang eines Systems vorhergesagt werden.
# 2. $h(t)$ und $y(t)$ sind gegeben -> $x(t)$ ist gesucht: Dies ist das **Kontrollproblem**
#     * Dieses Problem wird man in der Regelungstechnik häufig antreffen, wo eine Regelgröße am Eingang des Mess- bzw. Regelsystems gesucht wird um einen stabilen Zustand zu erreichen.
# 3. $u(t)$ und $y(t)$ gegeben -> $h(t)$ ist gesucht: Dies ist das **System-Identifizierungsproblem**
#     * Hier wollen wir das Messsystem charaktisieren, was unter anderem durch 2 Methoden möglich ist: Mittels Messungen der Eingangs- und Ausgangsgröße, oder mittels Aufstellen von Differentialgleichungen (Systemtheorie).
#     
# Während Problem 1 und 2 Bestandteil anderer Vorlesungen oder Themengebiete ist, wollen wir uns im Folgenden mit dem Problem 3 befassen. Hier wollen wir im Folgenden zwei Möglichkeiten betrachten, mittels welcher $h(t)$ bestimmt werden kann. Die beiden Methoden werden im folgenden mit **black box** und **white box** bezeichnet. 
# 
# In allen Kapiteln wird der Inhalt am Beispiel eines Tiefpasses 1. Ordnung noch einmal konkreter erläutert.
# 
# ![Bild](pictures/3probleme.png)
