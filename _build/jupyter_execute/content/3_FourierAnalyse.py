#!/usr/bin/env python
# coding: utf-8

# # Fourier-Analyse
# 
# ## Fourierreihen
# 
# Jedes periodische Signal kann als *Summe von Sinus- und Cosinusfunktionen* mit Frequenzen von ganzzahligen Vielfachen der Grundfrequenz des Signals beschrieben werden. Dies ist die sogenannten **Fourierreihe**, Fourierreihen-Entwicklung/oder -Zerlegung. Im folgenden Bild sehr ihr einen Rechteckpuls und die zugehörige Fourierreihe unter Einbeziehung verschiedener Anzahl von Sinus- bzw. Cosinusfunktionen. Je mehr Sinusfunktionen bei ganzzahligen Vielfachen der Grundfrequenz des Rectheckpulses miteinbezogen werden, desto genauer wird das ursprüngliche Rechtecksignal dargestellt.

# In[1]:


#Benötigte Libraries:
import numpy as np
import pandas as pd
from scipy import signal 
import scipy.integrate as spi
import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.tools as tls
import seaborn as sns
import time
import warnings
warnings.filterwarnings('ignore')

# MatplotLib Settings:
plt.style.use('default') # Matplotlib Style wählen
plt.figure(figsize=(10,6)) # Plot-Größe
plt.rcParams['font.size'] = 10; # Schriftgröße

T = 1
t_range = np.linspace(-2*T, 2*T, 1000, endpoint = True)

# Rechteckpuls:
f = lambda t: signal.square(2 * np.pi * 1/T * t)

y_true = f(t_range)

#function that computes the real fourier couples of coefficients (a0, 0), (a1, b1)...(aN, bN)
def compute_real_fourier_coeffs(func, N):
    result = []
    for n in range(N+1):
        an = (2./T) * spi.quad(lambda t: func(t) * np.cos(2 * np.pi * n * t / T), 0, T)[0]
        bn = (2./T) * spi.quad(lambda t: func(t) * np.sin(2 * np.pi * n * t / T), 0, T)[0]
        result.append((an, bn))
    return np.array(result)

#function that computes the real form Fourier series using an and bn coefficients
def fit_func_by_fourier_series_with_real_coeffs(t, AB):
    result = 0.
    A = AB[:,0]
    B = AB[:,1]
    for n in range(0, len(AB)):
        if n > 0:
            result +=  A[n] * np.cos(2. * np.pi * n * t / T) + B[n] * np.sin(2. * np.pi * n * t / T)
        else:
            result +=  A[0]/2.
    return result

maxN = 9
COLs = 3 #cols of plt
ROWs = 1 + (maxN-1) // COLs #rows of plt
plt.rcParams['font.size'] = 8
fig, axs = plt.subplots(ROWs, COLs)
fig.suptitle('Rechteckpuls')
#fig.tight_layout(rect=[0, 0, 1, 0.95], pad=3.0)

#plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
for N in range(1, maxN + 1):
    AB = compute_real_fourier_coeffs(f, N)
    #AB contains the list of couples of (an, bn) coefficients for n in 1..N interval.

    y_approx = fit_func_by_fourier_series_with_real_coeffs(t_range, AB)
    #y_approx contains the discrete values of approximation obtained by the Fourier series

    row = (N-1) // COLs
    col = (N-1) % COLs
    axs[row, col].set_title('N=' + str(N))
    axs[row, col].plot(t_range, f(t_range), color='k')
    axs[row, col].plot(t_range, y_approx, color='tab:blue')
plt.tight_layout()   
plt.show()


# ### Reelle Fourierreihe
# 
# Die **reelle Darstellung der Fourierreihe** für eine Funktion $x(t)$ sieht wiefolgt aus:
# 
# $$x(t) = x_0 + \sum_{k=1}^{\infty} a_k \cos(2\pi k f_0 t) + \sum_{k=1}^{\infty} b_k \sin(2\pi k f_0 t)$$
# 
# $x_0$ ist hierbei der Gleichanteil (Mittelwert) des Signals, der sich wieder über den arithmetischen Mittelwert berechnet:
# 
# $$x_0 = \frac{1}{T} \int_{-T/2}^{T/2} x(t) dt = \frac{a_0}{2}$$
# 
# Die (reellen) Koeffizienten $a_k$ und $b_k$ nehmen für jedes Messsignal eine anderen Wert an und berechnen sich über:
# 
# $$a_k = \frac{2}{T}  \int_{-T/2}^{T/2} x(t) \cos(2\pi k f_0 t) dt $$
# 
# und 
# 
# $$b_k = \frac{2}{T}  \int_{-T/2}^{T/2} x(t) \sin(2\pi k f_0 t) dt$$
# 
# Jedes Integral muss immer über eine Periode ausgeführt werden. Ob hier die Grenzen $\pm T/2$ gewählt werden, oder von $0$ bis $T$ integriert wird, ist jedem selber überlassen. 
# 
# Die Koeffizienten geben die Amplitude der Sinus- bzw. Cosinusfunktionen an, aus denen ein periodisches Signal rekonstruiert wird. Dargestellt über die Frequenz ergibt sich folgendes Bild, aus dem ersichtlich wird, dass für eine Rechtackfunktion auch noch bis zu 19. Harmonischen relevante Frequenzanteile zu erkennen sind. Bei einem Dreickecksignal sieht das anders aus.
# 
# `````{admonition} Aufgabe
# :class: tip
# Woran könnte es liegen, dass das Rechtecksignal höhere Harmonische benötigt als das Dreiecksignal? Im Python-Code könnt ihr die Flanke des Dreicksignals ändern indem ihr in `f = lambda t: signal.sawtooth(2 * np.pi * 1/T * t, 0.5)`den letzten Parameter, die 0.5, entfernt. Was ändert sich jetzt?
# `````

# In[2]:


maxN = 20
plt.rcParams['font.size'] = 10

# Rechteckpuls:
f = lambda t: signal.square(2 * np.pi * 1/T * t)

#plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
i = []
for N in range(1, maxN + 1):
    i.append(N)
    AB = compute_real_fourier_coeffs(f, N)
    #AB contains the list of couples of (an, bn) coefficients for n in 1..N interval.

    y_approx = fit_func_by_fourier_series_with_real_coeffs(t_range, AB)
    #y_approx contains the discrete values of approximation obtained by the Fourier series

plt.figure(figsize=(8,4)) # Plot-Größe

plt.subplot(1,2,1)
plt.title('N=' + str(N))
plt.plot(t_range, f(t_range), color='k')
plt.plot(t_range, y_approx, color='tab:blue')
plt.xlabel('Zeit')
plt.ylabel('Signalamplitude')

plt.subplot(1,2,2)
plt.plot(abs(AB[:,0]), 'o', label = '|a_k|')
plt.plot(abs(AB[:,1]), 'o', label = '|b_b|')
plt.legend()
plt.xlabel('Vielfache der Grundfrequenz')
plt.ylabel('Reelle Amplitude der Fourierreihe')
plt.xticks(i)
plt.suptitle('Reelle Fourierkoeffizienten für einen Rechteckpuls')
plt.tight_layout()
plt.show()


# In[3]:


# Dreieckfunktion:
f = lambda t: signal.sawtooth(2 * np.pi * 1/T * t, 0.5)

maxN = 10
plt.rcParams['font.size'] = 10

#plot, in the range from BT to ET, the true f(t) in blue and the approximation in red
i = []
AB = []
for N in range(1, maxN + 1):
    i.append(N)
    AB = compute_real_fourier_coeffs(f, N)
    #AB contains the list of couples of (an, bn) coefficients for n in 1..N interval.

    y_approx = fit_func_by_fourier_series_with_real_coeffs(t_range, AB)
    #y_approx contains the discrete values of approximation obtained by the Fourier series

plt.figure(figsize=(8,4)) # Plot-Größe

plt.subplot(1,2,1)
plt.title('N=' + str(N))
plt.plot(t_range, f(t_range), color='k')
plt.plot(t_range, y_approx, color='tab:blue')
plt.xlabel('Zeit')
plt.ylabel('Signalamplitude')

plt.subplot(1,2,2)
plt.plot(abs(AB[:,0]), 'o', label = '|a_k|')
plt.plot(abs(AB[:,1]), 'o', label = '|b_k|')
plt.legend()
plt.xlabel('Vielfache der Grundfrequenz')
plt.ylabel('Reelle Amplitude der Fourierreihe')
plt.xticks(i)
plt.suptitle('Reelle Fourierkoeffizienten für ein Dreicksignal')
plt.tight_layout()
plt.show()


# Es kann übrigens folgendes gezeigt werden, was für die Praxis oft sehr hilfreich ist, da es die Anzahl von Integralberechnungen reduziert:
# 
# * für **gerade** Funktionen, also wenn $x(t) = x(-t)$ gilt, dann sind alle $b_k = 0$ (es existieren nur noch Cosinus-Terme)
# * für **ungerade** Funktionen, also wenn $x(t) = -x(-t)$ gilt, dann sind alle $a_k = 0$ (es existieren nur noch Sinus-Terme)
# * einen Gleichanteil $x_0$ kann es folglich bei ungeraden FUnktionen *nicht* geben. 
# 
# Das ist in den obigen Darstellungen bereits zu sehen. Für den Rechteckpuls sind die $a_k = 0$, während für das Dreiecksignal die $b_k = 0$ sind. 

# ### Komplexe Fourierreihe
# Eine alternative Schreibweise ist die **komplexe Darstellung**. 
# 
# $$x(t) = \sum_{k=-\infty}^{\infty} \underline{c}_k \mathrm e^{j 2\pi k f_0 t}$$
# 
# Diese liefert den Vorteil, dass nur eine Art von Koeffizienten berechnet werden muss:
# 
# $$\underline {c}_k = \frac{1}{T}  \int_{-T/2}^{T/2} x(t) \mathrm e^{- j 2\pi k f_0 t} dt $$
# 
# Trotz der Rechnung mit komplexen Funktionen, anstelle von reellen Sinus- und Cosinus-Termen, handelt es sich immer noch um eine reelle Funktion. Für $k=0$ erhält man wieder den Gleichanteil:
# 
# $$\underline c_0 = x_0$$
# 
# Außerdem sieht man, dass die Werte für $\underline {c}_{-k}$ und $\underline {c}_k$ zueinander komplex konjugiert sind:
# 
# $$\underline {c}_{-k} = \underline {c}_k^*$$
# 
# ### Umrechnung zwischen reellen und komplexen Fourier-Koeffizienten
# Mittels der Euler-Formel
# 
# $$e^{j\omega t} = \cos(\omega t) + j \sin(\omega t)$$
# 
# lassen sich die Koeffizienten aus reeller Fourierreihen-Entwicklung und komplexer Darstellung ineinander umformen. Durch die Addition eines zueinander komplex konjugierten Koeffizientenpaares lässt sich der reelle Koeffizient $a_k$ bestimmen:
# 
# $$a_k = \underline{c}_{k} + \underline{c}_{-k}$$
# 
# und analog fällt bei der Subtraktion der Realteil weg, sodass nach zusätzliche Multiplikation mit $j$ $b_k$ berechnet wird:
# 
# $$b_k = j (\underline{c}_{k} - \underline{c}_{-k})$$
# 
# Andersherum können aus den reellen Koeffizienten auch die komplexen Koeffizienten berechnet werden:
# 
# $$\underline c_k = \frac{1}{2} (a_k - j b_k)$$
# 
# $$\underline c_{-k} = \frac{1}{2} (a_k + j b_k) = \underline c_k^*$$
# 
# An dieser Stelle wollen wir noch mal festhalten, dass die Koeffizienten der Fourierreihe eine Schwingung oder ein Messsignal im Frequenzbereich eindeutig beschreibt. In Ihrer Gesamtheit stellen diese Koeffizienten das **Spektrum** des Signals dar. Dies ist zumindest wahr für die hier dargestellte mathematische Betrachtung mittels Fourier-Transformation. Ein Spektrumanalysator wertet hingegen bei der jeder Einzelmessung in einem begrenzten Bereich Frequenzbereich das Signal aus, was häufig noch durch einen Bandpassfilter geschleust wurde. Dabei gehen Informationen über die Phasenlage verloren. 

# ## Fourier-Transformation 
# <a id="Sec-FFT"></a>
# 
# Die Fourier-Transformation ist Teil der Spektralanalyse in der Messtechnik. Sie basiert auf der Grundidee, dass, wie wir eben gesehen haben, sich jede periodische Funktion aus Sinus- und Cosinusfunktionen schreiben lässt. Das Ziel ist es, die Anteile dieser Schwingungen sichtbar zu machen. Die Fourier-Transformation ist eine mathematische Methode mit der nun auch aperiodische Signale in ein kontinuierliches Spektrum zerlegt werden. 
# 
# Die **diskrete Fourier-Transformation** (z.B. auf digitalisierte, abgetastete Messwerte angewendet) entspricht der Fourierreihen:
# 
# $$X_\mathrm d (k \Delta f) = \sum_{i = 0}^{N-1} x(i\Delta t) \mathrm e^{-j 2\pi  k \Delta f i \Delta t}$$
# 
# wobei $\Delta f = 1/T$ mit der Periode $T = N\cdot \Delta T$, $N$ ist die Anzahl der Samples. 
# 
# Die **kontinuierliche Fourier-Transformation** ist für beliebige Funktionen $f(t)$ definiert, d.h. die Periode kann unendlich lang werden und die Funktion kann aperiodisches Verhalten aufweisen:
# 
# $$\mathcal F(x(t)) = X(j\omega) = \int_{-\infty}^{\infty} x(t) \mathrm e^{-j \omega t} dt$$
# 
# Die Rücktransformation ist wiefolgt definiert: 
# 
# $$x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(j\omega) \mathrm e^{j \omega t} d\omega$$
# 
# Der Vollständigkeitshalber soll an dieser Stelle auch noch die **Laplace-Transformation** erwähnt werden, die sich wiefolgt berechnen lässt:
# 
# $$\mathcal L(x(t)) = X(s) = \int_{0}^{\infty} x(t) \mathrm e^{-st} dt$$
# 
# mit der Rücktransformation
# 
# $$x(t) = \frac{1}{2\pi}\int_{0}^{\infty} X(s) \mathrm e^{st} ds$$
# 
# Hierbei ist $s= \sigma + j\omega$ eine komplexe Zahl (anstelle von $\omega$) und wird für dynamische Messsysteme wichtig werden.  
# 
# ### Eigenschaften
# <a id="SubSec-Eigenschaften_FFT"></a>
# 
# Jeder Fourier-Transformation hat folgende wichtige **Eigenschaften**, die das Leben und Rechnen im Frequenzraum erheblich erleichtern können:
# 
# * **Linearität**: $\mathcal F(ax_1 + bx_2) = a\mathcal F(x_1)+ b \mathcal F(x_2)$
# * **Ableitung**: $\mathcal F(\dot x) = j\omega \cdot \mathcal F(x)$
# * **Faltung**:$ \mathcal F(x_1*x_2) = \mathcal F(x_1) \cdot \mathcal F(x_1)$
#     * Faltung im Zeichbereich ist zum Vergleich sehr kompliziert: $(x_1 \ast x_2)(t) = \int_{-\infty}^{\infty} x_1(\tau)x_2(t-\tau) \mathrm{d}\tau$
# * **Zeitverschiebung**: $\mathcal F(x(t-\tau)) = \mathcal F(x(t)) \cdot \mathrm e^{-j\omega \tau}$
# 
# ### Anwendung
# <a id="SubSec-Anwendung_FFT"></a>
# 
# Ein Spektralanalyse, wie sie die Fouriertransformation durchführt, eignet sich besonders gut zur Zustandsüberwachung. Hier können Motoren, Turbinen, Sägen, Kugellager uvm, im Prinzip alles was rotiert, überwacht werden. Die spezifischen Frequenz jedes Kugellagers kann beispielsweise überwacht werden. Sollte sich die Amplitude über die Zeit verändert, kann dies ein Indiz dafür sein, dass eine Kugel ins Lager gefallen ist oder das Lager einen Schaden bekommen hat. Verschlechtert sich das Verhalten kann frühzeitig gegengewirkt werden, indem das Kugellager ausgetauscht wird. Das heißt auch Fehlerfrüherkennung, Fehlerdiagnose und Trendanalysen ("predictive maintenance") werden häufig im Frequenzraum durchgeführt. 
