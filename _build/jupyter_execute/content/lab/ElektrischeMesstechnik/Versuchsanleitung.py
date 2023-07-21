#!/usr/bin/env python
# coding: utf-8

# # Grundlagen der elektrischen Messtechnik

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from IPython.display import Image
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 10),
          'axes.labelsize': 'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}
plt.rcParams.update(params)


# ## UI Kennline Widerstand

# In[2]:


figure(figsize=(3.5,3))
R = 10000
U = np.arange(0,4,0.1)
plt.plot(U, U/R*1000, lw = '3')
plt.grid()
plt.xlim([0,4])
plt.ylim([0,0.4])
plt.xlabel('Spannung (V)')
plt.ylabel('Stromstärke (mA)')
plt.savefig('UI.pdf',bbox_inches="tight")
plt.show()


# ## Kondensatorentladung

# In[3]:


tau = 0.05
I_0 = 1.0
t = np.arange(0,0.4,0.001)
def I(t):
    return I_0 * np.exp(-t/tau)

figure(figsize=(3.5,3))
plt.plot(t, I(t), lw = '3')
plt.grid()
plt.xlim([0,0.25])
plt.ylim([0,1.1])
plt.axhline(np.exp(-1), color = 'tab:gray', ls = ':')
plt.axvline(0.05, color = 'tab:gray', ls = ':')
plt.text(0.12,0.4, r'$\mathrm{e}^{-1} \approx 0.36787$', color = 'tab:gray', fontsize = '12')
plt.xlabel('Zeit (s)')
plt.ylabel(r'Spannung $U_\mathrm{C}$ (V)')
plt.savefig('Entladung_C.pdf',bbox_inches="tight")
plt.show()


# In[4]:


print(np.exp(-1))


# In[ ]:




