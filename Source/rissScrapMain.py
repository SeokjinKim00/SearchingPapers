from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from rissScrap import *

from commonFunc import makeCSV

def runRISS(question):
    menu = textInput()

    opt = webdriver.ChromeOptions()
    opt.add_experimental_option('excludeSwitches', ['enable-logging'])
    path = 'WebDriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, options=opt)
    
    basicUrl = 'http://www.riss.kr'
    url = basicUrl+'/index.do'

    driver.get(url)
    time.sleep(4)

    menuLink = {1:'//*[@id="tabMenu"]/ul/li/div/ul/li[2]/a',
                2:'//*[@id="tabMenu"]/ul/li/div/ul/li[3]/a',
                3:'//*[@id="tabMenu"]/ul/li/div/ul/li[4]/a',
                4:'//*[@id="tabMenu"]/ul/li/div/ul/li[5]/a',
                5:'//*[@id="tabMenu"]/ul/li/div/ul/li[6]/a',
                6:'//*[@id="tabMenu"]/ul/li/div/ul/li[7]/a',
                7:'//*[@id="tabMenu"]/ul/li/div/ul/li[8]/a'}
    
    rissSearchPage(driver=driver, query=question)
    
    dataNumDict = checkDataNum(driver=driver)

    driver.find_element(By.XPATH, menuLink[menu]).click()
    #s1 = '//*[@id="divContent"]/div/div[2]/div/div[3]/div[3]/div[2]/div[3]/div[1]/label'
    #element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, s1)))
    #driver.find_element(By.XPATH, s1).click()
    #time.sleep(0.1)
    #s2 = '//*[@id="divContent"]/div/div[2]/div/div[3]/div[3]/div[2]/div[3]/div[2]/div/ul/li[5]/a'
    #driver.find_element(By.XPATH, s2).click()
    #time.sleep(0.1)
    #s3 = '//*[@id="divContent"]/div/div[2]/div/div[3]/div[3]/div[2]/button'
    #driver.find_element(By.XPATH, s3).click()
    #time.sleep(1)

    
    pageMax = dataNumDict[menu]//10
    
    titles, authors, links = rissGetData(driver=driver, lastPage=pageMax)

    data = {"Title": titles,
            "Author": authors,
            "Link": links}
    df = pd.DataFrame(data)
    name = 'RissPapers'+question
    makeCSV(df, name)
    
    driver.quit()