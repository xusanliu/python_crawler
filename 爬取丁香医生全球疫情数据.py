#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json


# In[2]:


url='http://ncov.dxy.cn/ncovh5/view/pneumonia'
html=requests.get(url).content.decode('utf-8')
data=re.findall('getListByCountryTypeService2true = (.*?)}catch',html)[0]
data=json.loads(data)
data


# In[3]:


needed_data=[{
    'continents':country['continents'],
    'country_name':country['provinceName'],
    'current_confirmed_count':country['currentConfirmedCount'],
    'confirmed_count':country['confirmedCount'],
    'cured_count':country['curedCount'],
    'dead_count':country['deadCount'],
    'dead_rate':country['deadRate']
    }for country in data]
data=pd.DataFrame(needed_data)
data


# In[4]:


data=data.sort_values(by='dead_count',ascending=False)
data


# In[5]:


grouped_data=data.groupby('continents')
data=grouped_data.sum()
data


# In[ ]:




