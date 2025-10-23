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
query = build_freelancer_query(**param)                     # list like ['en', 'fr']

# Get The Page Limit
result_len =  get_total_result(query.replace("{page}","2")) # can only get a reliable result count on page2
page_len   =  ceil(result_len / 50)                         # each page contain 50 results

# Loop Over Pages
jobs = []

print("> freelancer scraping started !")
for i in range(1, page_len + 1):
    
    res = website_crawler(query.replace("{page}", str(i)))
    jobs.extend(extract_job_list(res))
    
    print(f"page {i} scraped !")