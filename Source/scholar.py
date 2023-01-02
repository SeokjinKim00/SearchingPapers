from selenium.webdriver.common.by import By

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