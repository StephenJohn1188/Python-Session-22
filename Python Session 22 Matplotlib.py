#!/usr/bin/env python
# coding: utf-8

# # Data Visualization using Matplotlib

# In[3]:


import matplotlib.pyplot as plt
import numpy as np


# In[5]:


a=np.array([12,35,45,48,86,75,59])
b=np.array([78,95,48,62,15,35,48])


# In[8]:


plt.title('Linear Line')
plt.xlabel('a')
plt.ylabel('b')
plt.plot(a,b)
plt.show()


# In[9]:


g=np.array([10,20,30,40,50,60,70])
h=np.array([99,88,77,66,55,44,33])
plt.title('Linear Line')
plt.xlabel('g')
plt.ylabel('h')
plt.plot(g,h)
plt.show()


# In[13]:


#Brokenline
plt.plot(g,h, '--g')


# In[16]:


a=np.array([12,35,45,48,86,75,59])
b=np.array([78,95,48,62,15,35,48])
plt.title('Bar Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.bar(a,b)
plt.show()


# In[20]:


g=np.array([10,20,30,40,50,60,70])
h=np.array([99,88,77,66,55,44,33])
plt.title('Bar Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.bar(g,h)
plt.show()


# In[21]:


g=np.array([10,20,30,40,50,60,70])
h=np.array([99,88,77,66,55,44,33])
plt.title('Bar Graph')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.bar(g,h, color='g', align='center')
plt.show()


# Histogram

# In[22]:


import matplotlib.pyplot as plt
import numpy as np


# In[23]:


a=np.array([24,5,48,7,65,5,98,9,66,5,6,45,12,75,84,23,77,36,15,1,45,7,9,63,14,12])
plt.hist(a,bins=[0,20,40,60,80,100])
plt.title('Histogram')
plt.show()


# In[28]:


import pandas as pd
df=pd.read_csv('student_marks.csv')
print(df)
df.columns


# In[26]:


plt.hist(df['Maths'],bins=10)
plt.title('Maths Histogram')
plt.show()


# In[27]:


plt.hist(df['English'],bins=10)
plt.title('English Histogram')
plt.show()


# In[29]:


plt.boxplot(df['Maths'])


# In[30]:


plt.boxplot(df['Chemistry'])


# In[31]:


plt.violinplot(df['Maths'])


# In[32]:


plt.violinplot(df['English'])


# In[33]:


plt.violinplot(df['Chemistry'])


# In[35]:


a=np.array([12,35,45,48,86,75,59, 68,66,78,96,85,74,41,52,63,44,46])
b=np.array([78,95,48,62,15,35,48,12,19,18,17,49,43,61,67,59,53,33])
plt.title('scatter plot')
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.scatter(a,b)
plt.show()


# In[37]:


x=df['Maths']
y=df['English']
plt.scatter(x,y)
plt.xlabel('Maths')
plt.ylabel('English')
plt.show()


# # Seaborn Visualization Library

# In[39]:


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as snt
import warnings
warnings.filterwarnings('ignore')


# In[40]:


x=['Sunday','Monday','Tuesday','Wednesday','Thursday']
y=[4,5,6,7,8]


# In[41]:


snt.stripplot(x,y)


# In[43]:


ds=pd.read_csv('emptest.csv')
print(ds)
print(ds.head())

snt.violinplot(x='Salary',data=ds)
plt.show()


# In[44]:


ds=pd.read_csv('emptest.csv')
print(ds)
print(ds.head())

snt.violinplot(x='Age',data=ds)
plt.show()


# In[ ]:




