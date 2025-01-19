#import os
#from bs4 import BeautifulSoup
#import sqlite3
#import matplotlib.pyplot as plt
#import seaborn as sns
import requests
import time

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue#google_vignette"
html_data = requests.get(url, time.sleep(10)).text

# If no information is extracted, then connect as anonymous
if "403 Forbidden" in html_data:
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
    request = requests.get(url, headers = headers, timeout=10)
    time.sleep(10)
    html_data = request.text

html_data