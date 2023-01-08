from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def checkCAPTCHA(driver):
    checkStr = '사용자가 로봇이 아니라는 확인이 필요합니다.'
    try:
        check = driver.find_element(By.ID, 'gs_captcha_f')
        if checkStr == str(check.text):
            return 1
    except:
        return 0

def checkNextPage(driver):
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'gs_n')))
    try:
        link = driver.find_element(By.XPATH, '//*[@id="gs_n"]/center/table/tbody/tr/td[12]/a/b')
        return 0
    except:
        return 1

def getScholarURL(question, page):
    urlBefore = 'https://scholar.google.co.kr/scholar?start='
    searchQuery = '&q='+question
    urlAfter = '&hl=ko&as_sdt=0,5'
    url = urlBefore + str(page) + searchQuery + urlAfter
    return url

def getScholarTitle(driver):
    titleList=list()
    title = driver.find_elements(By.CLASS_NAME, 'gs_rt')
    for i in title:
        if i is not None:
            titleList.append(str(i.text))
    
    return titleList

def getAuthorScholar(driver):
    authorList=list()
    author=driver.find_elements(By.CLASS_NAME, 'gs_a')
    for i in author:
        if i is not None:
            authorList.append(str(i.text))
    return authorList

def getScholarLink(driver):
    linkList=list()
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'gs_rt')))
    link = driver.find_elements(By.CLASS_NAME, 'gs_rt')
    for i in link:
        if i is not None:
            try:
                href = i.find_element(By.TAG_NAME, 'a').get_attribute('href')
                linkList.append(href)
            except:
                linkList.append('None')
    return linkList

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