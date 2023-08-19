#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np


# In[7]:


my_lst = [1,2,3,4]
arr = np.array(my_lst)
print (my_lst)


# In[8]:


type (arr)


# In[10]:


arr.shape


# In[13]:


my_lst1 = [1,2,3,4]
my_lst2 = [4,5,6,7]
my_lst3 = [7,8,9,10]
arr=np.array([my_lst1, my_lst2, my_lst3])


# In[14]:


arr


# In[16]:


arr.shape


# In[17]:


arr.reshape(3,4)


# In[18]:


arr


# In[19]:


print(arr)


# In[20]:


arr[2]


# In[22]:


arr[0:,:]


# In[23]:


arr[1:,2:]


# In[24]:


newarr = np.arange(1,300, step = 2)
print (newarr)


# In[25]:


arr1 = newarr.copy()


# In[26]:


print(arr1)


# In[29]:


val = 200
arr1[arr1<val]


# In[30]:


arr1*3


# In[34]:


np.ones(4)
np.ones((2,5),dtype=float)


# In[33]:


np.random.rand(5,3)


# In[42]:


np.random.randint(0,100, 9).reshape(3,3)


# In[ ]:





# In[ ]:




