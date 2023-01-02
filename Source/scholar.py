from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def checkCAPTCHA(driver):
    checkStr = '사용자가 로봇이 아니라는 확인이 필요합니다.'
    try:
        check = driver.find_element(By.ID, 'gs_captcha_f')
        if checkStr == str(check.text):
            print("Please check reCAPTCHA")
            print("If you're done, press Enter")
            print("Enter : ", end=' ')
            input()
    except:
        pass

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