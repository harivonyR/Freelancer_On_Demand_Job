# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:44:36 2025

@author: harivonyR
"""


"""
Search Parameter : 
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
        

"""

def frelancer_query_builder():
    """
        build a correct string to search
    """

    Returns
    -------
    None.

    """
    pass


"""
flow :

    build search param -> API request -> get page number () -> loop over page -> scrape job listing 


"""

