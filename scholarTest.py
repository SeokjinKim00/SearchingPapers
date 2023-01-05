from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import pandas as pd
import datetime
import os
import getpass
from scholar import *


if __name__ == '__main__':
    print("--- Please enter a search term ---")
    print("Input : ", end='')
    question = input().replace(' ', '+')
        
    path = 'WebDriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path)
    pageNum = 0
    titles = []
    authors = []
    links = []
    try:
        for page in range(99):
            url = getScholarURL(question, (page*10))
            
            driver.minimize_window()
            driver.get(url)
            checkCAPTCHA(driver)
            titles.extend(getScholarTitle(driver=driver))
            authors.extend(getAuthorScholar(driver=driver))
            links.extend(getScholarLink(driver=driver))
    except:
        print("Scrap End")
        
        # print(titles)
    data = {"Title": titles,
            "Author": authors,
            "Link": links}

    df = pd.DataFrame(data)
    df.to_csv('Data/Papers.csv')
    
    driver.quit()