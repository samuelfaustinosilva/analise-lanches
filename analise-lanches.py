#!/usr/bin/env python
# coding: utf-8

# ### Bibliotecas

# In[1]:


import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import seaborn as sns 


# ### Importando dados

# In[2]:


lanches = pd.read_csv('lanches.csv')


# In[3]:


lanches


# ### Analisando

# In[5]:


lanches[lanches.Lanche == 'MISTO QUENTE']


# In[21]:


lanches_misto = lanches[lanches.Lanche == 'MISTO QUENTE']


# In[22]:


lanches_misto


# In[23]:


lanches_misto_turno = lanches_misto = lanches_misto[lanches_misto.Turno == 'TARDE']


# In[24]:


lanches_misto_turno


# In[28]:


lanches_misto_turno.reset_index()


# In[29]:


lanches_1 = lanches[lanches.Dia == 1]


# In[30]:


lanches_1


# In[33]:


sns.catplot(x=lanches_1.Lanche, y=lanches_1.Turno)
plt.xlabel("Período do Dia")
plt.ylabel("Tempo de espera (minutos)")
plt.title("Diferença de tempo (Dia 1)")
plt.show()


# In[34]:


lanches[lanches.Turno == 'NOITE']


# In[35]:


contagem_vendas = lanches.groupby(['Lanche', 'Turno', 'Dia']).size().reset_index()


# In[36]:


contagem_vendas


# In[40]:


contagem_vendas[contagem_vendas.Turno == 'NOITE']


# In[38]:


contagem_vendas.describe()


# In[47]:


contagem_vendas[contagem_vendas.Turno == 'TARDE']


# In[48]:


contagem_vendas = lanches.groupby(['Lanche', 'Turno', 'Dia']).size().reset_index()


# In[49]:


contagem_vendas


# In[52]:


contagem_vendas[contagem_vendas.Dia == 2]


# In[ ]:




