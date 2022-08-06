#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Crear distribución gaussiana de 10.000 puntos con  media 3 y desviación estándar 1.5.


# In[11]:


# Obtener el rango en el que se encuentran el 95% de nuestros valores.


# In[12]:


import numpy as np


# In[13]:


array_gaus = np.random.normal(3,1.5,10000)


# In[14]:


array_gaus


# In[ ]:


# Cálculo de la media


# In[21]:


media = np.mean(array_gaus)


# In[ ]:


# Cálculo de la desviación estándar


# In[22]:


desv_est = np.std(array_gaus)


# In[28]:


# Cálculo del rango


# In[23]:


rango_95 = [media - 2*desv_est, media + 2*desv_est]


# In[24]:


rango_95


# In[27]:


import matplotlib.pyplot as plt
import scipy.stats as stats
plt.scatter(array_gaus, stats.norm.pdf(array_gaus, media, desv_stand))


# In[18]:





# In[ ]:




