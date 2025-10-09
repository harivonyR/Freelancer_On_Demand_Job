# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 19:24:38 2025

@author: harivonyR
"""

from script.piloterr import website_rendering


url = "https://www.upwork.com/nx/search/talent/"
res = website_rendering(url,wait_in_seconds=10)
