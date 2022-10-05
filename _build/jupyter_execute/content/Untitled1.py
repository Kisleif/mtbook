#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
V = 1
R = 1e6
P_ref = 1e-3
P = V**2/(8*R)
print(P)
print(10*np.log10(P/P_ref))


# In[ ]:




