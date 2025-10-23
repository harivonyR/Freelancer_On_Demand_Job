# Freelancer On-Demand Job Scraping

**Freelancer On-Demand Job Scraping** is a Python project that automates data collection from [Freelancer.com](https://www.freelancer.com) using the **Piloterr API**.  
It allows you to extract real-time job listings, analyze market trends, and explore in-demand freelance skills.

---

## 🚀 Features

Build dynamic search queries with filters (keyword, language, price range, etc.)  
Handle anti-bot protection seamlessly through **Piloterr API**  
Collect structured job data directly from Freelancer.com pages  
Easily extend for trend analysis, NLP, or machine learning  

---

## 💡 Use Cases

- Analyze **freelance market trends** and **in-demand skills**  
- Identify **niche opportunities** and **pricing benchmarks**  
- Train **machine learning** models with real-world job data  
- Optimize **freelancer profiles for SEO**  

---

## Get Started

### 1. Clone the repository
```bash
git clone https://github.com/harivonyR/Freelancer_On_Demand_Job
cd Freelancer_On_Demand_Job
```

### 2. Install dependecies
```bash
$ pip install requests beautifulsoup4
```

### 3. Configure your API key:  
Copy credential
```bash
$ cp credential.example.py credential.py
```

Open `credential.py` and paste your API key inside:  
```python
x_api_key = "YOUR API KEY HERE!"
```

---

## RUN THE SCRIPT

Open `main.py` and set search parameters

```python
param = {
    "keyword":"script python",
    "fixed":True,
    "fixed_min":0,
    "fixed_max":10000,
    "languages":['en','fr','pt']}
```

Run the main script to start Freelancer.com job listings:  
```bash
$ python main.py
```

This will:  
- Build a search query 
- Scrape over page listing 
- Build dataset

---