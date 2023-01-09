from selenium import webdriver
import pandas as pd

from scholar import *
from commonFunc import makeCSV

def runScholar(question):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    path = 'WebDriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, options=opt)

    titles = []
    authors = []
    links = []
    page = 0
    while 1:
        url = getScholarURL(question, (page*10))
        
        driver.minimize_window()
        driver.get(url)
        if checkCAPTCHA(driver):
            print("Please check reCAPTCHA")
            print("If you're done, press Enter")
            print("Enter : ", end=' ')
            input()
        if checkNextPage(driver):
            break
        page += 1
        
        titles.extend(getScholarTitle(driver=driver))
        authors.extend(getAuthorScholar(driver=driver))
        links.extend(getScholarLink(driver=driver))

    data = {"Title": titles,
            "Author": authors,
            "Link": links}

    df = pd.DataFrame(data)
    df.to_csv('Data/ScholarPapers.csv')
    
    driver.quit()