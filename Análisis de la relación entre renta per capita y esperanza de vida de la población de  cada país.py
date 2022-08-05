#!/usr/bin/env python
# coding: utf-8

# # Análise de la relación entre renta per capita y la esperanza de vida de la población de cada país

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# # Preguntas norteadoras

# In[ ]:


# Hay correlacción entre la renta per capita y la esperanza de vida de la población de cada país?
# De qué manera se dá esta correlacción?
# El tamaño de la población impacta, de alguna manera, a la Esperanza de vida?


# # Carga y manipulación

# In[7]:


df = pd.read_csv(r'C:\Users\Thais\Desktop\Curso Python\Datasets+Data+Science+con+Python+-+Pandas\1.3\Info_pais.csv',encoding="ISO-8859-1",delimiter=";",)


# In[8]:


df.head(20)


# In[9]:


df_order = df.sort_values("Esperanza de vida",ascending=True)


# In[10]:


df_order.head()


# # Visualización 

# In[12]:


plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"])
plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")


# In[14]:


df_order["Pobl_norm"] = df_order["Poblacion"]/max(df_order["Poblacion"]/10000)


# In[15]:


df_order.head()


# In[23]:


plt.scatter(df_order["Renta per capita"],df_order["Esperanza de vida"],s=df_order["Pobl_norm"],c=df_order["Pobl_norm"])
plt.title("Renta per capita vs Esperanza de vida")
plt.xlabel("Renta per capita")
plt.ylabel("Esperanza de vida")

# aumentando el tamaño del gráfico:

fig = plt.gcf()
fig.set_size_inches(14.5,10)

#etiquetando los países:

for i in range(1,10):
    plt.annotate(df_order["País"][i], (df_order["Renta per capita"][i],df_order["Esperanza de vida"][i]))
    
#ordenando los puntos del eje y (que de los 120 países, aparezcan de 10 en 10, del primero al último):

plt.yticks(ticks=range(1,120,10))


# 
# # Conclusiones

# In[24]:


# Sí, hay correlacción entre la renta per capita y la esperanza de vida de la población.
# Son directamente proporcionales, es decir, conforme la renta per capita aumenta, así también ocurre con la esperanza de vida.
# Impacta el tamaño de la población a la Esperanza de vida? Es necesário evaluar con más profundidad el gráfico y algunos de sus patrones.


# In[ ]:




