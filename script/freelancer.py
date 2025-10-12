# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:44:36 2025

@author: harivonyR
"""

"""
Search Parameters : 
    key word : "python script"
    eg : https://www.freelancer.com/jobs/?keyword=python%2520script
    
    location (hard with few advantages) : "United States"
    eg : https://www.freelancer.com/jobs/?vic=United%20States&country=United%20States&lat=38.7945952&lon=-106.5348379&local=true
    
    Fixed price :
        True
        eg : https://www.freelancer.com/jobs/?fixed=true
    
        Price Min Max : 10, 100
        eg : https://www.freelancer.com/jobs/?fixed_min=10&fixed_max=100
    
    Hourly Project (*con't be combine with Fixed price param'): 
        True
        eg : https://www.freelancer.com/jobs/?hourly=true
    
        Hourly Min & Max : 20, 50
        eg : https://www.freelancer.com/jobs/?hourly_min=20&hourly_max=50
        
        Hourly Duration : 
            1 : Less than 1 week,
            2 : 1 to 4 weeks,
            3 : 1 to 3 months,
            4 : 3 to 6 months,
            5 : Over 6 month
            eg : https://www.freelancer.com/jobs/?hourly_duration=5
    
    Contest : 
        TRUE 
        eg : https://www.freelancer.com/jobs/?contest=true
        
        Min Max
        eg : https://www.freelancer.com/jobs/?contest_min=10&contest_max=15
        
    Language (separtor "%C"):
        en : English
        es : Spanish
        de : German
        fr : French
        pt : Portuguese
    
        eg : https://www.freelancer.com/jobs/?languages=en%2Ces%2Cde%2Cfr%2Cpt
    
    Job State :
        All Job, open and closed
        https://www.freelancer.com/jobs/?status=all
    
"""

from bs4 import BeautifulSoup
from urllib.parse import urlencode
from script.piloterr import website_crawler
from math import ceil

def build_freelancer_query(
    keyword=None,
    fixed=False,
    fixed_min=None,
    fixed_max=None,
    hourly=False,
    hourly_min=None,
    hourly_max=None,
    hourly_duration=None,
    contest=False,
    contest_min=None,
    contest_max=None,
    languages=None,       # list like ['en', 'fr']
    status=None          # set to "all" to display closed job
):
    base_url = "https://www.freelancer.com/jobs/{page}/?"
    params = {}

    # --- 1. Keyword ---
    if keyword:
        params["keyword"] = keyword.replace(" ", "%20")
        
    # --- 2. Handle exclusivity ---
    mode_count = sum([fixed, hourly, contest])
    
    if mode_count > 1:
        raise ValueError(" [incorrect] Parameters 'fixed', 'hourly', and 'contest' are mutually exclusive")

    # --- 3. Fixed Price ---
    if fixed:
        params["fixed"] = "true"
        if fixed_min and fixed_max:
            params.update({
                "fixed_min": fixed_min,
                "fixed_max": fixed_max
            })

    # --- 4. Hourly Project ---
    if hourly:
        params["hourly"] = "true"
        if hourly_min and hourly_max:
            params.update({
                "hourly_min": hourly_min,
                "hourly_max": hourly_max
            })
        if hourly_duration:
            params["hourly_duration"] = hourly_duration

    # --- 5. Contest ---
    if contest:
        params["contest"] = "true"
        if contest_min and contest_max:
            params.update({
                "contest_min": contest_min,
                "contest_max": contest_max
            })

    # --- 6. Languages ---
    if languages:
        params["languages"] = "%2C".join(languages)

    # --- 7. Job status ---
    if status:
        params["status"] = "all"

    # --- 8. Return full query ---
    return base_url + urlencode(params, doseq=True)

def get_total_result(query: str) -> int:
    """
    Extract total number of results from HTML.
    bug : the total number of page is stuck on 5000
    """
    html = website_crawler(query)
    
    soup = BeautifulSoup(html, "html.parser")
    total_result = soup.select_one("span#total-results")  # correction du sélecteur
    
    if not total_result:
        return 0  # sécurité si l'élément n'existe pas

    # extraction et conversion en entier
    text = total_result.get_text(strip=True)
    digits = ''.join(filter(str.isdigit, text))  # garde uniquement les chiffres
    
    return int(digits) if digits else 0

def extract_job_list(html: str):
    soup = BeautifulSoup(html, "html.parser")
    
    # Sélecteur CSS : il manquait un point pour indiquer la classe
    items = soup.select(".JobSearchCard-item")
    
    job_lists = []
    
    for item in items:
        job = {
            # Sélection par attribut data-qtsb-label
            "title": item.select_one('[data-qtsb-label="link-project-title"]').get_text(strip=True) if item.select_one('[data-qtsb-label="link-project-title"]') else None,
            
            # Sélection du paragraphe de description
            "description": item.select_one("p.JobSearchCard-primary-description").get_text(strip=True) if item.select_one("p.JobSearchCard-primary-description") else None
        }
        
        job_lists.append(job)
    
    return job_lists

if __name__ == "__main__" :
    # BUILD A QUERY
    query = build_freelancer_query(
        keyword="script python",
        fixed=True,
        fixed_min=0,
        fixed_max=10000,
        contest=False,
        languages=['en','fr','pt'])       # list like ['en', 'fr']
    
    # ONE INSTANCE SCRAPING
    res = website_crawler(query.replace("{page}","1"))
    jobs = extract_job_list(res)
    
    # COUNT RESULT and PAGE NUMBER
    #result_len =  get_total_result(query.replace("{page}","2"))       # can only get result on page number 2
    #page_len = ceil(result_len / 50)                                  # there is 50 results each page
