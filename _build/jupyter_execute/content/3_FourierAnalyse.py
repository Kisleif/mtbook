#!/usr/bin/env python
# coding: utf-8

# # Fourier-Analyse
# 
# ## Fourierreihen
# 
# Jeder periodische Signal kann als Summe von Sinus- und Cosinusfunktionen mit Frequenzen von ganzzahligen Vielfachen der Grundfrequenz des Signals beschrieben werden. Dies ist die sogenannten **Fourierreihe**, Fourierreihen-Entwicklung/oder -Zerlegung. Die **reelle Darstellung der Fourierreihe** sieht wiefolgt aus:
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
# Jedes Integral muss immer über eine Periode ausgeführt werden. Ob hier die Grenzen $\pm T/2$ gewählt werden, oder von 0 bis $T$ integriert wird, ist jedem selber überlassen. 
# 
# Es kann übrigens folgendes gezeigt werden, was für die Praxis oft sehr hilfreich ist, da es die Anzahl von Integralberechnungen reduziert:
# 
# * für **gerade** Funktionen, also wenn $x(t) = x(-t)$ gilt, dann sind alle $b_k = 0$ (es existieren nur noch Cosinus-Terme)
# * für **ungerade** Funktionen, also wenn $x(t) = -x(-t)$ gilt, dann sind alle $a_k = 0$ (es existieren nur noch Sinus-Terme)
# * einen Gleichanteil $x_0$ kann es folglich bei ungeraden FUnktionen *nicht* geben. 
# 
# Eine alternative Schreibweise ist die **komplexe Darstellung**. 
# 
# $$x(t) = \sum_{k=-\infty}^{\infty} \underline{c}_k \mathrm e^{j 2\pi k f_0 t}$$
# 
# Diese liefert den Vorteil, dass nur eine Art von Koeffizienten berechnet werden muss:
# 
# $$\underline {c}_k = \frac{1}{T}  \int_{-T/2}^{T/2} x(t) \mathrm e^{- j 2\pi k f_0 t} dt $$
# 
# Trotz der Rechnung mit komplexen Funktionen, anstelle von reellen Sinus- und Cosinus-Termen, handelt es sich immer noch um eine reelle Funktion. Für $k=0$ erhält man wieder den Gleichanteilm d.h.:
# 
# $$\underline c_0 = x_0$$
# 
# Außerdem sieht man, dass die Werte für $\underline {c}_{-k}$ und $\underline {c}_k$ zueinander komplex konjugiert sind:
# 
# $$\underline {c}_{-k} = \underline {c}_k^*$$
# 
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
# 
# ## Fourierreihe eines Rechteckpuls 
# <a id="SubSec-Bsp_Fourier_rechteck"></a>
# 
# Gucken wir uns im folgenden Code-Block mal einige Überlagerungen von Sinusschwingungen und wie dieser zum Rechteckpuls, der Signumsfumktion, führen.

# In[1]:


# Defintion der Rechteckfunktion
def rechteck(x):
    out = 0
    if x<0:
        out = -1
    if x>0:
        out = 1
    return out
sig = []   
x = np.linspace(-np.pi, np.pi, 1000)
for i in x:
    sig.append(rechteck(i))

plt.plot(x,sig, 'k')
plt.grid()
plt.xlabel('Zeit t')
plt.ylabel('Spannung U')
plt.show()


# In[ ]:


# Berechnung der Fourier-Koeffizienten für diesen Rechteckpuls

# Da die Funktion gerade ist sind alle Koeffzienten a_k = 0

# Berechnung der b_k:
def b(k):
    return 2/np.pi * (-1/k * np.cos(np.pi*k) + 1/k)

def fourier_reihe_rechteck(N,x):
    out = 0
    for i in range(1,N+1):
        out = out + b(i) * np.sin(i*x)
    return out

plt.plot(x,sig, 'k')
n = 5
plt.plot(x,fourier_reihe_rechteck(n,x), label = 'N = %d'%(n))
n = 10
plt.plot(x,fourier_reihe_rechteck(n,x), label = 'N = %d'%(n))
n = 20
plt.plot(x,fourier_reihe_rechteck(n,x), label = 'N = %d'%(n))
plt.grid()
plt.legend()
plt.xlabel('Zeit t')
plt.ylabel('Spannung U')
plt.show()

for i in range(1,n+1):
    plt.plot(x, b(i) * np.sin(i*x))
plt.grid()
plt.xlabel('Zeit t')
plt.ylabel('Spannung U')
plt.show()

for i in range(1,n+1):
    plt.plot(i, b(i),'o')
plt.grid()
plt.xlabel('Frequenz f')
plt.ylabel('Amplitude b_k')
plt.show()


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
# Ein Spektralanalyse, wie sie die Fouriertransformation durchführt, eigenet sich besonders gut zur Zustandüberwachung. Hier können Motoren, Turbinen, Sägen, Kugellager uvm, im Prinzip alles was rotiert, überwacht werden. Die spezifischen Frequenz jedes Kugellagers kann beispielsweise überwacht werden. Sollte sich die Amplitude über die Zeit verändert, kann dies ein Indiz dafür sein, dass eine Kugel ins Lager gefallen ist oder das Lager einen Schaden bekommen hat. Verschlechtert sich das Verhalten kann frühzeitig gegengewirkt werden, indem das Kugellager ausgetauscht wird. Das heißt auch Fehlerfrüherkennung, Fehlerdiagnose und Trendanalysen ("predictive maintenance") werden häufig im Frequenzraum durchgeführt. 
