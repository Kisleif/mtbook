#!/usr/bin/env python
# coding: utf-8

# # Übertragungsfunktion

# In diesem Kapitel gucken wir uns dynamische Messsysteme nur noch im Frequenzraum an. Im letzten Kapitel haben wir schon gesehen, dass wir DGL's benutzen können um das Verhalten von Messsystemen auf bestimmte Anregungsfunktionen vorhersagen zu können. Außerdem haben wir gesehen, dass das Lösen von DGL's im Frequenzraum einfacher und schneller geht. 
# Die DGL im Frequenz- oder Laplaceraum kann direkt benutzt werden, um die sogenannte **Übertragungsfunktion** zu berechnen. Dies ist eines der wichtigsten Funktionen um Messsysteme zu charakterisieren.
# 
# * Die Übertragungsfunktion ist das Verhältnis von Ausgangs- zu Eingangssinal. 
# * Die Übertragungsfunktion kann aus der DGL im Frequenzraum bestimmt werden.
# * Die Übertragungsfunktion kann außerdem experimentell bestimmt werden, sodass keine theoretischen Herleitungen nötig sein.
# * Mittels Faltung kann die Übertragung von beliebigen Messsignalen vorhergesagt werden.
# 
# Zur Erinnerung schreiben wir hier noch mal die Integrale, die für die Umrechnung benutzt werden:
# 
# * Fourier-Transformation: 
# 
#     $$\mathcal F(x(t)) = X(j\omega) = \int_{-\infty}^{\infty} x(t) \mathrm e^{-j \omega t} dt$$
# 
# * Laplace-Transformaton, mit der komplexen Frequenz $s = \sigma + j\omega$: 
# 
#     $$\mathcal L(x(t)) = X(s) = \int_{0}^{\infty} x(t) \mathrm e^{-st} dt$$
# 
# Wenn $x(t)$ das Eingangssignal im Zeit-Raum ist, dann bezeichnen wir mit $X(j \omega)$, bzw. $X(s)$ das Eingangssignal im Frequenz- bzw. Laplaceraum. Hier ist $j$ wieder die komplexe Zahl. Das Ausgangssignal $y(t)$ wird analog dazu mit $Y(j \omega)$ bzw. $Y(s)$ bezeichnet. Es hat sich eingebürgert, dass Zeitsignale mit kleinen Buchstaben, $x$, bezeichnet werden und Signale im Frequenzbereich mit großen Buchstaben, $X$. 
# 
# :::{figure-md} zeit-f-block
# <img src="draw/zeit-f-block.jpg" alt="zeit-f-block" class="bg-primary mb-1" width="600px" label = zeit-f-block>
# 
# Signale und Messsystem im Zeit- bzw. Frequenzraum.
# :::
# 
# {numref}`strommesseingang`
# 
# Die Übertragungsfunktion eines Messsystems, $G(j \omega)$ bzw. $G(s)$, kann also wiefolgt aus den Fourier-Transformierten der Ein- und Ausgangssignale ausgedrückt werden:
# 
# $$G(j \omega) = \frac{Y(j \omega)}{X(j \omega)}$$
# 
# bzw. im Laplaceraum:
# 
# $$G(s) = \frac{Y(s)}{X(s)}$$
# 
# Im Folgenden werden wir zwischen Fourier- und Laplaceraum nicht unbedingt unterscheiden. Die Herleitung der Übertragungsfunktion, Amplitudengang und Phasengangs sind für beide Räume die gleiche, lediglich die Variable ändert sich von $j \omega$ zu $s$. 
# Im Allgmeinen gilt:
# 
# * Die **Fourier-Transformation (FT)** wird bei **kontinuierlichen Signalen** verwendet.Für eine FT muss das Signal **integrierbar** sein, was für einen Sprung, Rampe z.B. nicht gilt, wo das Integral gegen unendlich läuft.
# * Die **Laplace-Transformation** wird bei Reaktionen auf **diskrete Funktionen** verwendet, wie z.B. Stufenfunktion, Impulsfunktion, Delta-Dirac-Puls, die mittels FT nicht anlysiert werden können. 

# ## Herleitung der Übertragungsfunktion
# 
# Anhand unseres Beispiels, dem **Tiefpass 1. Ordnung**, wollen wir die Übertragungsfunktion einmal herleiten. Dazu gibt es verschiedene Ansätze. 
# 
# ### Mittels Differentialgleichung
# 
# Eine Möglichkeit die Übertragungsfunktion zu bestimmen, ist es die DGL aus dem vorherigen Kapitel in den Frequenzraum zu transformieren, wie wir es bereits in [Differentialgleichung](5_DGL.ipynb) gemacht machen. Aus
# 
# $$\tau \frac{du_\mathrm a (t)}{dt} + u_\mathrm a (t) = u_\mathrm e (t)$$
# 
# und dem Einsetzen von $u_\mathrm e (t) \rightarrow U_e(j \omega)$, $u_\mathrm a (t) \rightarrow U_a(j \omega)$ und $\dot u_\mathrm a (t) \rightarrow j \omega U_a(j \omega)$ wird
# 
# $$\tau j \omega U_\mathrm a(j \omega) + U_\mathrm a (j \omega) = U_\mathrm e (j \omega)$$
# 
# Die DGL wird nach $U_\mathrm a(j \omega) / U_\mathrm e(j \omega)$ umgestellt, um die Übertragungsfunktion zu erhalten.
# 
# $$G(j \omega) = \frac{U_\mathrm a(j \omega)}{U_\mathrm e(j \omega)} = \frac{1}{1+\tau j \omega}$$
# 
# ### Mittels komplexen Widerständen
# 
# Sollte die DGL (noch) nicht bekannt sein, kann die Übertragungsfunktion auch direkt über die komplexen Widerstände bestimmt werden. Bei dem **Tiefpass 1. Ordnung** handelt es sich um die Reihenschaltung von Widerstand und Kondensator. 
# 
# Die komplexe Ausgangsspannung wird über dem Kondensator abgegriffen, das heißt es gilt das ohm'sche Gesetz für komplexe Zahlen. $\underline Z_C = \frac{1}{j\omega C}$ ist die Impedanz des Kondensators mit Kapazität $C$ und $\underline I$ der Strom. 
# 
# $$\underline U_\mathrm a = \underline Z_C \cdot \underline I$$
# 
# Die komplexe Eingangsspannung liegt an kompletten Messsystem, also der Reihenschaltung an, d.h. es gilt
# 
# $$\underline U_\mathrm a = (R+ \underline Z_C) \cdot \underline I$$
# 
# Die Division der beiden Spannungen führt abermals zur der gesuchten Übertragungsfunktion:
# 
# $$G(j \omega) = \frac{\underline U_\mathrm a}{\underline U_\mathrm e} = \frac{1/(j\omega C)}{R + 1/(j\omega C)} = \frac{1}{1+RC j \omega}$$
# 
# Die Zeitkonstante $\tau = RC$ könnte nun noch in die Gleichung eingesetzt werden.

# ## Darstellung: Bode Diagramm
# 
# Nachdem wir nun die Übertragungsfunktion hergeleitet haben, wollen wir wissen, was wir aus dieser Funktion ableiten, bzw. von ihr lernen können. 
# Wir verwenden wieder das Beispiels eines Tiefpasses. Zunächst einmal sehen wir, dass es sich bei $G$ um eine komplexe Zahl handelt. Wie für jede andere komplexe Zahl können wir hier Amplitude und Phase bestimmen. Dazu formen wir $G$ in die typische Schreibe einer komplexen Zahl um, sodass Real- ($\mathrm{Re}$) und Imaginärteil ($\mathrm{Im}$) direkt abgelesen werden können. Hierfür erweitern wir $G$ typischer mit dem komplex Konjugierten:
# 
# $$
# \begin{align}
# G(j \omega) &= \frac{1}{1+RC j \omega} \\
# &= \frac{1}{1+RC j \omega} \cdot \frac{1-RC j \omega}{1-RC j \omega}\\
# &= \frac{1-RC j \omega}{1- (RC \omega)^2} \\
# &= \frac{1}{1- (RC \omega)^2} - j\frac{ RC \omega}{1- (RC \omega)^2}
# \end{align}
# $$
# 
# Die **Amplitude** wird wiefolgt berechnet, wobei $\tau = RC =: 1/\omega_0$. Die Einheit beträgt typischerweise dB.
# 
# $$G(\omega) = \sqrt{\mathrm{Re}^2 + \mathrm{Im}^2} = \frac{1}{\sqrt{1+\left(\frac{\omega}{\omega_0}\right)^2}}$$
# 
# 
# Die **Phase** wird wiefolgt berechnet, wobei $\tau = RC =: 1/\omega_0$. Die Einheit beträgt typischerweise Grad. 
# 
# $$\phi(\omega) = \arctan\left(\frac{\mathrm{Im}}{\mathrm{Re}}\right) = \arctan\left(-\frac{\omega}{\omega_0}\right)$$
# 
# Sowohl Amplitude als auch Phase hängen von der Frequenz $\omega$ des eingehenden Signals ab! Daher nennt man die Fuktionen für Amplitude und Phase auch **Amplitudengang** bzw. **Phasengang**. Beide zusammengenommen bilden den **Frequenzgang** eines Systems und werden häufig zusammen geplottet, im sogenannten **Bode-Diagramm**. 
# 
# * Die Übertragungsfunktion wird für eine Impulsanregung berechnet.
# * Das Bode-Diagramm bietet eine einfache Darstellungsweise der Frequenzantwort eines Messsystems
# * Das Bode-Diagramm ist ein Werkzeug um die Stabilitätseigenschaften von Kontrollsystemem zu analysieren.
# 
# Eine solche Darstellung ist im folgenden Bild gezeigt. Rechts ist zum Vergleich noch einmal die Sprungantwort im Zeitbereich gezeigt.

# In[1]:


import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.xkcd()
plt.rcParams['axes.grid']= True     # defaults to False but xkcd() makes it False
plt.rcParams['grid.linewidth']= 0.8  # defaults to 0.8
plt.rcParams['font.size'] = 10; # Schriftgröße

# Transfer Funktion Tiefpass:
num = np.array([1])
den = np.array([1 , 1])
H = signal.TransferFunction(num , den)
num = np.array([1])
den = np.array([2 , 1])
H2 = signal.TransferFunction(num , den)

# Bode-Plot:
w, mag, phase = signal.bode(H)
w2, mag2, phase2 = signal.bode(H2)

# Plotting
# Supplot2grid approach
fig, ax = plt.subplots(figsize=(10,5))
ax1 = plt.subplot2grid((2,2), (0,0)) # topleft
ax3 = plt.subplot2grid((2,2), (0,1), rowspan=2)            # right
ax2 = plt.subplot2grid((2,2), (1,0))                       # bottom left

ax1.semilogx(w, mag, color='tab:blue', label = r'$G_1(s) = \frac{1}{s+1} \rightarrow \tau_1 = 1\, s $')
ax1.semilogx(w2, mag2, color='tab:red', label = r'$G_2(s) = \frac{1}{2s+1} \rightarrow \tau_2 = 2\, s $')

ax1.axhline(y = -3, color='k', ls = '--', lw = 1)
ax1.axvline(x = 1, color='tab:blue', ls = '--', lw = 1)
ax1.axvline(x = 0.5, color='tab:red', ls = '--', lw = 1)
ax1.set_xticks([1e-2, 1e-1, 0.5, 1, 10], labels = [r'$10^{-2}$', r'$10^{-1}$', '0.5', '1', '10'])
ax1.set_title("Bode Plot")
ax1.grid(True, lw=0.5, zorder=0, ls = '--', which='major', axis='both')
ax1.grid(True, lw=0.5, zorder=0, ls = '--', which='minor', axis='both')
ax1.set_ylabel("Amplitude (dB)")
ax1.legend()


# Plotting
ax2.semilogx(w, phase, color='tab:blue')
ax2.semilogx(w2, phase2, color='tab:red')
ax2.axhline(y = -45, color='k', ls = '--', lw = 1)
ax2.axvline(x = 1, color='tab:blue', ls = '--', lw = 1)
ax2.axvline(x = 0.5, color='tab:red', ls = '--', lw = 1)
ax2.set_yticks([0,-45,-90])
ax2.set_xticks([1e-2, 1e-1, 0.5, 1, 10], labels = [r'$10^{-2}$', r'$10^{-1}$', '0.5', '1', '10'])
ax2.grid(True, lw=0.5, zorder=0, ls = '--', which='minor', axis='both')
ax2.grid(True, lw=0.5, zorder=0, ls = '--', which='major', axis='both')
ax2.set_xlabel("Frequenz (Hz)")
ax2.set_ylabel('Phase (deg)')


# Sprungantwort:
t, y = signal.step(H)
t2, y2 = signal.step(H2)

# Plotting
ax3.plot(t, y, color='tab:blue', label = r'$\frac{u_a(t)}{u_0} = 1- e^{-\left(\frac{t}{\tau = 1\, s}\right)}$')
ax3.plot(t2, y2, color='tab:red', label = r'$\frac{u_a(t)}{u_0} = 1- e^{-\left(\frac{t}{\tau = 2\, s}\right)}$')
ax3.axhline(y = 1.0, color='k', ls = '--', lw = 1)
ax3.axhline(y = 0.63, color='k', ls = '--', lw = 1)
ax3.axvline(x = 1, color='tab:blue', ls = '--', lw = 1)
ax3.axvline(x = 2, color='tab:red', ls = '--', lw = 1)
ax3.set_yticks([1.0, 0.63])
ax3.set_yticklabels(['100%', '63%'])
ax3.set_xticks([1,2])
ax3.set_xticklabels([r'$\tau_1$',r'$\tau_2$'])
ax3.set_title("Sprungantwort eines Tiefpasses")
ax3.set_xlabel("Zeit t")
ax3.set_ylabel(r'$u_a(t)/u_0$')
ax3.grid(True, lw=0.5, zorder=0, ls = '--', which='minor', axis='both')
ax3.grid(True, lw=0.5, zorder=0, ls = '--', which='major', axis='both')
ax3.legend()

fig.tight_layout()


# Auch hier kann man, wie schon bei der Interpretation der Sprungantwort, Kenngrößen ablesen. 
# 
# Bei der **Grenzfrequenz (Bandbreite, cut-off Frequenz)** $\omega_0 = 1/\tau$ fällt die Amplitude auf $1/\sqrt{2} = 0,707 = -3\,\mathrm{dB}$ ab. Häufig werden Systeme anhand der Grenzfrequenz charakterisiert. Man sollte aber nicht vergessen, dass bei Signalen mit diesen Frequenzanteilen bereits signifikante Verluste in Höhe von 29% zu erwarten sind, die eigentlich nicht tolerierbar sind. Je höher die Frequenz, desto höher die Verluste (bei dem hier dargestellten Tiefpassfilter!). Das heißt der Fehler, der bei einer Messung gemacht wird, ist frequenzabhängig!
# 
# In der Akustik kann man damit leben, da man kaum einen Unterschied hört. 
# In der Messtechnik bei der Überwachung von schwingenden Maschinenteilen oder der Ermittlung von Rundlaufabweichungen von drehenden Wellen ist solch ein Ampitudenabfall meist nicht zu akzeptieren.
# Üblicherweise sollte man andere Grenzfrequenzen separat angeben, die 90% oder 99% der Signalstärke durchlassen. 
# 
# Sind die zeitbestimmenden Glieder (R und C) des Tiefpasses bestimmt, können wir daraus die Grenzfrequenz bestimmen und somit den Verlust abschätzen. 
# 
# Im Folgenden Bild grafisch dargestellt, wie verschiedene Signale durch einen **Tiefpass** mit der Übertragungsfunktion 
# 
# $$G(s) = \frac{1}{s+1}$$
# 
# verfälscht werden können, in dem hohe Frequenzanteile abgeschwächt werden. Auch hier erkennt man wieder einen Zusammenhang zu den Fourierreihen, wenn man sich das Rechtecksignal ansieht. Eine Reihe von Rechteckpulsen benötigt eine hohe Anzahl von Sinusfunktionen bei höheren harmonischen der Grundfrequenz, um möglichst steile Flankenübergänge zu erhalten. Eine Filterung dieser hohen Frequenzanteile sorgt für eine deutliche Verzerrung des Signals. Bei sinusförmirgen Signalen hingegen wird nur die Amplitude abgeschwächt und es findet zusätzlich, je nach Frequenz, eine zeitlich Verzögerung statt, d.h. die Signale sind phasenverschoben um bis zu -90°. 
# 
# * Je größer $\tau$, desto langsamer ist das System
# * Je kleiner $\tau$, desto schneller ist das System

# In[2]:


from scipy import signal

SAMPLE_RATE = 100.0  # Hertz
DURATION = 10  # mSeconds
t = np.linspace(0, DURATION, int(SAMPLE_RATE * DURATION), endpoint=False)
u = 1.0

# tiefpass Filter wie oben:
order = 1
Wn = 1
b, a = signal.butter(order, Wn, 'low', analog=True)
sos = signal.butter(order, Wn, 'low', fs = SAMPLE_RATE, output='sos')
w, h = signal.freqs(b, a)

# 0.2 Hz Sinus Signal + Gefiltert
ff = 0.2
y_sin1 = u * np.sin(2 * np.pi * ff * t)
y_sin1_filt = signal.sosfilt(sos, y_sin1)

# 2 Hz Sinus Signal + Gefiltert
ff = 2.
y_sin2 = u * np.sin(2 * np.pi * ff * t)
y_sin2_filt = signal.sosfilt(sos, y_sin2)

# 0.4 Hz Rechteck Signal + Gefiltert
ff = 0.4
y_rect1 = signal.square(2 * np.pi * ff * t)
y_rect1_filt = signal.sosfilt(sos, y_rect1)

# 2x Sinus Signal + Gefiltert
ff = 0.2
y_sin3 = 0.7 * np.sin(2 * np.pi * ff * t) + 0.3 * np.sin(40 * 2 * np.pi * ff * t)
y_sin3_filt = signal.sosfilt(sos, y_sin3)


# Plotting
# Supplot2grid approach
fig, ax = plt.subplots(figsize=(10,6))
ax3 = plt.subplot2grid((4,3), (0,0), colspan=1) # topleft
ax1 = plt.subplot2grid((4,3), (0,1), rowspan=2)            # right
ax2 = plt.subplot2grid((4,3), (2,1), rowspan=2)            # right
ax4 = plt.subplot2grid((4,3), (1,0))                       # bottom left
ax5 = plt.subplot2grid((4,3), (2,0))                       # bottom left
ax6 = plt.subplot2grid((4,3), (3,0))                       # bottom left
ax7 = plt.subplot2grid((4,3), (0,2))                       # bottom left
ax8 = plt.subplot2grid((4,3), (1,2))                       # bottom left
ax9 = plt.subplot2grid((4,3), (2,2))                       # bottom left
ax10= plt.subplot2grid((4,3), (3,2))                       # bottom left

# Bode Plot:
ax1.semilogx(w, 20 * np.log10(abs(h)))
ax1.axhline(y = -3, color='k', ls = '--', lw = 1)
ax1.axvline(x = 1, color='tab:blue', ls = '--', lw = 1)
ax1.axvline(x = 0.2, color='tab:red', ls = '--', lw = 1)
ax1.axvline(x = 2.0, color='tab:orange', ls = '--', lw = 1)
ax1.axvline(x = 8.0, color='tab:olive', ls = '--', lw = 1)
ax1.axvline(x = 0.4, color='tab:green', ls = '--', lw = 1)
ax1.set_xticks([1e-2, 1e-1, 0.5, 1, 10], labels = [r'$10^{-2}$', r'$10^{-1}$', '0.5', '1', '10'])
ax1.set_title("Tiefpass: Bode Plot")
ax1.grid(True, lw=0.5, zorder=0, ls = '--', which='major', axis='both')
ax1.grid(True, lw=0.5, zorder=0, ls = '--', which='minor', axis='both')
ax1.set_ylabel("Amplitude (dB)")

ax2.semilogx(w, np.arctan2(np.imag(h),np.real(h))*180/np.pi, color='tab:blue')
ax2.axhline(y = -45, color='k', ls = '--', lw = 1)
ax2.axvline(x = 1, color='tab:blue', ls = '--', lw = 1)
ax2.axvline(x = 0.2, color='tab:red', ls = '--', lw = 1)
ax2.axvline(x = 2.0, color='tab:orange', ls = '--', lw = 1)
ax2.axvline(x = 8.0, color='tab:olive', ls = '--', lw = 1)
ax2.axvline(x = 0.4, color='tab:green', ls = '--', lw = 1)

ax2.set_yticks([0,-45,-90])
ax2.set_xticks([1e-2, 1e-1, 0.5, 1, 10], labels = [r'$10^{-2}$', r'$10^{-1}$', '0.5', '1', '10'])
ax2.grid(True, lw=0.5, zorder=0, ls = '--', which='minor', axis='both')
ax2.grid(True, lw=0.5, zorder=0, ls = '--', which='major', axis='both')
ax2.set_xlabel("Frequenz (Hz)")
ax2.set_ylabel('Phase (deg)')

ax3.set_title('Originalsignal')
ax3.plot(t,y_sin1, color = 'tab:red', label = '0.2Hz')
ax3.legend(loc = 1)
ax3.set_ylim(-1.2,1.2)
ax7.set_title('Gefiltertes Signal')
ax7.plot(t,y_sin1_filt, color = 'tab:red')
ax7.set_ylim(-1.2,1.2)

ax4.plot(t,y_sin2, color = 'tab:orange', label = '2.0Hz')
ax4.set_ylim(-1.2,1.2)
ax4.legend(loc = 1)
ax8.plot(t,y_sin2_filt, color = 'tab:orange')
ax8.set_ylim(-1.2,1.2)

ax6.plot(t,y_rect1, color = 'tab:green', label = '0.4Hz')
ax6.set_ylim(-1.2,1.2)
ax6.legend(loc = 1)
ax10.plot(t,y_rect1_filt, color = 'tab:green')
ax10.set_ylim(-1.2,1.2)

ax5.plot(t,y_sin3, color = 'tab:olive', label = '0.2Hz & 8Hz')
ax5.set_ylim(-1.2,1.2)
ax5.legend(loc = 1)
ax6.set_xlabel('Zeit (s)')
ax9.plot(t,y_sin3_filt, color = 'tab:olive')
ax9.set_ylim(-1.2,1.2)
ax10.set_xlabel('Zeit (s)')

fig.tight_layout()


# ## Kombination von Übertragungsfunktionen: Faltung im Frequenzraum
# <a id="SubSec-kombi_bandpass"></a>
# 
# Auch das hintereinanderschalten von Messsystemen ist im Frequenzraum viel einfacher zu berechnen als im Zeitraum. Eine Hintereinanderschaltung bedeutet allgemein nichts anderes, als die Faltung von Übertragungsfunktionen der jeweiligen Messsysteme. Im Zeitbereich müsste man hierzu das Faltungsintegral lösen. Im Frequenzraum ist die Faltung lediglich eine Multiplikation der Übertragungsfunktionen. 
# 
# Als Beispiel soll uns ein Bandpass dienen, der aus der Hintereinanderschaltung eines Hoch- und Tiefpasses realisiert werden kann. Im Folgenden Bild sind die Komponenten des Tiefpasses (TP) blau dargestellt, die des Hochpasses (HP) rot dargestellt. Der Tiefpass lässt tiefe Frequenzen bis zu seiner Grenzfrequenz passieren (bis auf die 71% Signalverlust) und der Hoch lässt hohe Frequenzen bis zu seiner Grenzfrequenz passieren. Wir wählen C und R der beiden elektronischen Schaltungen so, dass die Grenzfrequenz der Hochpasses unterhalb der des Tiefpasses liegt, also $f_\mathrm HP < f_\mathrm{TP}$. Der Amplitudengang ist rechts im folgenden Bild geplottet:
# 
# ![Bild](pictures/bandpass.png)
# 
# Wie eben schon beschrieben, können im Zeitraum die Übertragungsfunktionen der Einzel-Systeme (hier also Hochpass und Tiefpass) einfach multipliziert werden und man erhält die kombinierte Übertragungsfunktion des resultierenden Bandpasses. Wird die Übertragungsfunktionen in Einheiten von dB gezeichnet, also logarithmisch aufgetragen, so ergibt sich eine weitere grafische Vereinfachung bei der Kombination: In logarithmischen Einheiten können die einzelnen Übertragungsfunktionen in einem Amplitudengangs-Plot addiert (!) statt multipliziert werden. 

# ## Anlegen von Testfunktionen
# <a id="SubSec-freq_test"></a>
# 
# Nicht nur im Zeitraum können Sprünge oder Impulse angelegt werden. Für diese Testfunktionen können auch die Laplace, bzw. Fourier-Transformierten berechnet werden. Auch dies ist im Frequenzraum häufig einfacher, da die Testfunktionen, wie es in der Tabelle im folgenden Bild zu erkennen ist, sehr einfach sind. 
# 
# Um das Verhalten unseres eben diskutierten Bandpasses auf verschiedene Eingangssignale zu untersuchen, können wir die gleichung der Übertragungsfunktion einfach nach $U_\mathrm a$ auflösen. Das liefert uns im allgemeinen Fall eine Gleichung für das zu erwartende Ausgangssignal:
# 
# $$U_\mathrm a = G(s) \cdot U_\mathrm e(s)$$
# 
# Wählen wir als Eingangssignal einen Dirac-Puls, $\delta(t)$, um die Impulsantwort zu berechnen, so erhalten wir diese in dem wir für $U_\mathrm e(s) = 1$. Dies ist einfach die Laplace-Transformierte eines Delta-Peaks. 
# 
# Wählen wir als Eingangssignal einen Sprung, möchten also die Sprungantwort bestimmen, so setzen wir in die Gleichung $U_\mathrm e(s) = 1/s$, die Laplace-Transformierte einer Sprungfunktion. 
# 
# Auch hierbei handelt es sich wieder um Faltungen im Frequenzraum, deren Berechnungen im Zeitbereich sehr viel komplizierter wären. 
# 
# aus Übertragungsfunktionen können noch weitere Eigenschaften von Messsystemen abgeleitet werden, auf die wir hier nicht näher eingehen können. Aus den Nullstellen und Polstellen kann aber abgelesen werden, ob das System stabil ist, sprungfähig ist oder eher ein integrales Verhalten aufweist. 
# 
# ![Bild](pictures/bandpass_laplace.png)

# ## Verhalten von Systemen 2. Ordnung
# <a id="SubSec-2ndorder_freq"></a>
# 
# Der Vollständigkeitshalber wollen wir uns noch ganz kurz die Bode-Diagramme von Systemen 2. Ordnung ansehen. Auf eine mathematische Beschreibung wollen wir an dieser Stelle aber verzichten. 
# 
# Bei Systemen 1. Ordnung handelt es sich um Systeme mit Energiespeicher, also alle Systeme die irgendwie warm werden. Bei Systemen 2. Ordnung hat man zwei gekoppelte Energiespeicher, die Energie unter Umständen periodisch austauschen können. Hier findet man dann immer einen zusätzlichen Term in der DGL der die Dämpfung des Systems beschreibt. 
# 
# Um ein System 1. Ordnung von einem System 2. Ordnung zu unterscheiden, kann man sich das Bode-Diagramm (links im nachfolgenden Bild) ansehen. Bei Systemen 1. Ordnung fällt die Amplitude innerhalb einer Frequenzdekade (also ein Faktor 10) um -20 dB ab, bei Systemen 2. Ordnung  um -40 dB (*Übung: Warum?*). Auch die zeitliche Verzögerung, also die Phase des Eingangssignals, erfährt ebenfalls einen steileren Abfall.  
# 
# Rechts im Bild ist das Zeitliche Verhalten einer Sprungantwort dargestellt. Je nach Dämpfung erhält man ein Überschwingen, ein langsames Annähern (aperiodische Einstellung in b)) oder sogar ein oszillierendes Verhalten (schwingende Einstellung in a)) des Ausgangssignals um das Endsignal. Aufgrund dieser Dynamik entstehen Fehler und es ist ratsam eine gewisse Zeit zu warten, bis der Endwert auch hier ein 1% Toleranzband erreicht, ähnlich wie bei Systemen 1. Ordnung. Hieraus kann man außerdem schlussfolgern, dass man in der Tat immer eine gewisse Dämpfung haben möchte, damit die Oszillationen frühzeitig abklingen. Eine zu hohe Dämpfung verursacht jedoch lange Wartezeiten, bis das Ausgangssignal sich dem endgültigem Wert endlich angenähert hat. 
# 
# ![Bild](pictures/TP_2ndorder.png)
# 
# Einige Beispiele zu Systemen mit Verzögerungs, Dämpfungs bzw. auch integrierendem Verhalten sind in nachfolgender Tabelle dargestellt. In der Literatur findet man häufig diese tabellarischen Zusammenfassungen verschiedener Messsysteme inklusive Übertragungsfunktion und Bode-Diagramm, damit die DGL nicht jedes mal neu hergeleitet werden müssen. Die Hintereinanderschaltung einzelner Komponenten kann auch hier wieder ganz einfach im logarithmischen Bode-Diagramm per Addition der Übertragungsfunktionen abgeschätzt werden. 
# 
# ![Bild](pictures/wichtigste_regelkreisglieder.png)

# ## Zusammenfassung
# <a id="Sec-Zusammenfassung"></a>
# 
# Bevor wir zu der Zusammenfassung kommen, soll im folgenden Bild noch einmal dargestellt werden, welche Trick und Tips man sich im Frequenzraum noch von Nutzen machen kann, solange es sich um ein LZI System handelt!
# 
# * Mittels Fourier-Transformation kann ich jederzeit in den Frequenzraum wechseln und mittels Rücktransformation zu gehen. Egal ob es sich um ein Signal oder ein System (hier wird häufig der Laplace-Raum verwendet) handelt.
# * Die Ableitung der Sprunganregung ist eine Dirca-Funktion (Impulsanregung). Die Ableitung der Sprung*antwort* ergibt die Impuls*antwort*. Die gilt sowohl im Zeit- wie auch im Frequenzraum. (*Frage: Was sieht die zeitliche Ableitung der Fourier-Transformierten 1/s?)
# * Lösen von DGLs im Laplace-Raum ist eine algebraische Umformung der Gleichung
# * Lösen von DGLs im Zeitraum benötigt einen Lösungsansatz, eine homogene Lösung, eine spezielle Lösung und verschiedene Schritte inkl. Anfangsbedingungen um die Lösung zu finden.
# * Die Faltung im Laplace-Raum ist eine Multiplkation
# * Die Faltung im Zeitraum ist ein Integral
# * Die Faltung ist generell ein hilfreiches Werkzeug um...
#     * Systeme hintereinanderzuschalten und die Gesamt-Übertragungsfunktion zu berechnen (Faltung der beiden Systeme berechnen)
#     * Die Antwort auf ein beliebiges Eingangssignal mittels Impulsantwort zu bestimmten (Faltung von beliebigem Eingangssignal mit Impulsantwort liefert Antwort des Systems auf das beliebige Eingangssignal)
#     * Die Faltung hilft bei allen drei Problemen: System-Indentifizierungsproblem, Simulationsproblem und Kontrollproblem
#     
# ![Bild](pictures/t_s_draw.png)
