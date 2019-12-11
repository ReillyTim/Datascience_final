#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib as plt


# In[6]:


file = pd.read_csv("stand.csv")
info = file['Info']
src = file['Source']
print(info, src)


# In[ ]:


with open('badsites.txt') as bad:
    lines = bad.read().splitlines()
hits = 0
for i in range(len(info)):
    for l in range(len(lines)):
        if lines[l] in info[i]:
            print('found', src[i], 'reaching', lines[l])
            hits+=1
if hits == 0:
    print('All good')


# In[4]:


with open('slackingatwork.txt') as bad:
    lines = bad.read().splitlines()
hits = dict()
for i in range(len(info)):
    for l in range(len(lines)):
        if lines[l] in info[i]:
            print('found', src[i], 'connecting to', lines[l])
            if lines[l] in hits:
                hits[lines[l]] += 1
            else:
                hits[lines[l]] = 1
print(hits)


# In[ ]:





# In[ ]:




