#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import pandas as pd
from bs4 import BeautifulSoup 
import datetime
import os


# In[27]:


URL = "https://www.fnbzambia.co.zm/Controller?nav=rates.forex.list.ForexRatesList"
Headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "DNT": "1",
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
 }

page = requests.get(URL , headers = Headers)
soup = BeautifulSoup(page.content, "html.parser")
#print (soup)
scrape_time = datetime.date.today()

table = soup.find("tr", class_="tableBorder")

rows=[]

for tr in soup.find_all("tr"):
    td = tr.find_all("td")
    if len(td) == 5:
        Description = td[0].get_text(strip = True)
        code = td[1].get_text(strip = True)
        selling = td[2].get_text(strip = True)
        buying_tt = td[3].get_text(strip = True)
        buying_notes = td[4].get_text(strip = True)
        
        rows.append([Description, code, selling, buying_tt, buying_notes,scrape_time])

df =pd.DataFrame(rows, columns = ["Description", "Code", "Selling", "Buying_TT", "Buting_Notes", "Scrape_time"])

file_name = "Zambian_fx.csv"

if os.path.exists(file_name):
    df_old = pd.read_csv(file_name)
else:
    df_old = pd.DataFrame(columns=df.columns)

df_combined = pd.concat([df_old, df], ignore_index=True)
df_clean = df_combined.drop_duplicates(subset=["Code", "Scrape_time"], keep="first")

df_clean.to_csv(file_name, index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




