# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 19:24:38 2025

@author: harivonyR
"""

from script.freelancer import build_freelancer_query,get_total_result,extract_job_list
from script.piloterr import website_crawler
from math import ceil

# Set Search Parameters (filters)
param = {
    "keyword":"script python",
    "fixed":True,
    "fixed_min":0,
    "fixed_max":10000,
    "languages":['en','fr','pt']}

# Build Query (With Pagination PlaceHolder)
query = build_freelancer_query(**param)                       # list like ['en', 'fr']

# Get The Page Limit
result_len =  get_total_result(query.replace("{page}","2"))   # can only get a reliable result count on page2
page_len   =  ceil(result_len / 50)                           # each page contain 50 results

# Loop Over Pages
jobs = []

print("> freelancer scraping started !")
for i in range(1, page_len + 1):
    
    res = website_crawler(query.replace("{page}", str(i)))
    jobs.extend(extract_job_list(res))
    
    print(f"page {i} scraped !")
    
"""
    Exporting Data

"""

# Display the first 5 scraped jobs as a sample
import pandas as pd
from datetime import datetime

jobs_df = pd.DataFrame(jobs)
now = datetime.now()
date_str = now.strftime("%d_%m_%y")

# 2. Construct the new file path with the keyword and the date
# The resulting filename will be like: "output/TechJobs-29_10_25.csv"
keyword = param['keyword']
filename = f"output/{keyword}-{date_str}.csv"
jobs_df.to_csv(filename,sep=",")
