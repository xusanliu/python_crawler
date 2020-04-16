#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}



# In[3]:


def detail_url(url):
    result=[]
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    title=soup.title.text
    result.append(title)
    academic=soup.select('.job_academic')[0].text
    result.append(academic)
    company_name=soup.select('.com_intro .com-name')[0].text
    company_name=company_name.replace('\n','')
    result.append(company_name)
    return result
def get_urls(url):
    a=[]
    b=[]
    c=[]
    html=requests.get(url,headers=headers)
    soup=BeautifulSoup(html.text,'lxml')
    offers=soup.select('.intern-wrap.intern-item')
    for offer in offers:
        url=offer.select('.f-l.intern-detail__job a')[0]['href']
        a.append(detail_url(url)[0])
        b.append(detail_url(url)[1])
        c.append(detail_url(url)[2])
    result={'title':a,
           'academic':b,
           'company_name':c}
    return result
url='https://www.shixiseng.com/interns?page=1&keyword=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E5%AE%9E%E4%B9%A0%E7%94%9F'
print(get_urls(url))


# In[4]:


data=pd.DataFrame(get_urls(url))
data













