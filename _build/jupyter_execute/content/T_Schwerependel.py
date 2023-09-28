#!/usr/bin/env python
# coding: utf-8

# # Schwerependel

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Messung der Periodendauer aus der Vorlesung:

# In[2]:


T = 1.3


# ## Schrecksekunde - Statistische Messunsicherheit
# 
# Erstelle ein Array oder ein DataFrame deiner persönlichen Messdaten um die Schrecksekunde zu ermitteln.

# In[3]:


T_schrecksekunde = np.array([5.1, 5.4, 4.9, 5.0, 4.9, 5.1])
T_schrecksekunde_df = pd.DataFrame(T_schrecksekunde)
print(T_schrecksekunde_df)


# Berechne Standardabweichung dieser Messreihe um die Messunsicherheit einer Zeit-Einzelmessung zu erhalten. 
# Achtung, bei der Standardabweichung musst du aufpassen ob das Programm die empirische (durch n-1 geteilt) oder die arithmetische (durch n geteilt) berechnet. Während die Funktion für dataframes bereits die gewünschte empirische berechnet, muss das für numpy arrays explizit über `ddof=1` mitangegeben werden (dof: degree of freedom). 

# In[4]:


print('Standardabweichung (DataFrame)', T_schrecksekunde_df.std())
print('Standardabweichung (Numpy ohne ddof1)', T_schrecksekunde.std())
print('Standardabweichung (Numpy mit ddof1)', T_schrecksekunde.std(ddof=1))

u_T =T_schrecksekunde.std(ddof=1) # DataFrame 


# In[5]:


print('Damit beträgt die Messunsicherheit deiner persönlichen Zeitmessung: ',u_T , 's' )


# ## Pendellänge

# In[6]:


l = 42e-2 # in m
u_l = 1e-3 # in m


# ## Bestimmung der Erdbeschleunigung
# 
# Der Wert der Erdbeschleunigung für $g$ wird aus den besten Schätzwerten (= Mittelwerten) bestimmt:
# 
# $$g = \left(\frac{2\pi}{\overline T}\right)^2 \overline l$$

# In[7]:


def g(T,l): # Definition der Funktion für g
    return (2*np.pi/T)**2 * l

g = g(T, l)
print('Die Schwerebeschleunigung ist', g, 'm/s^2')


# Bestimmung der Messunsicherheit von $g$ erfolgt durch Fehlerfortpflanzung nach Gauß. 

# In[8]:


pip install sympy

