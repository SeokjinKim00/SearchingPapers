from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs


def textInput():
    print("Search Text")
    print("Enter : ", end='')
    searchTxt = input()

    print("Choice Menu")
    print("1.국내학술논문, 2.학위논문, 3.해외학술논문")
    print("4.학술지, 5.단행본, 6.연구보고서, 7.공개강의")
    print("Enter : ", end='')
    menuInput = int(input())
    return searchTxt, menuInput

def rissSearchPage(driver, query):
    element = driver.find_element(By.ID,'query')
    driver.find_element(By.ID,'query').click( )
    element.send_keys(query)
    element.send_keys(Keys.ENTER)

def checkDataNum(driver):
    html = driver.page_source
    soup = bs(html, 'html.parser')

    referNumDict = dict()
    num1 = soup.find_all('div', 'title')

    strDel1 = '[<span class="moreCnt">'
    strDel2 = ','
    strDel3 = '</span>]'

    for n, t in zip(range(1, 8), num1):
        referNum = str(t.select('h3 > span'))
        referNum = referNum.replace(strDel1, '').replace(strDel2, '').replace(strDel3, '')
        referNumDict[n] = int(referNum)

    return referNumDict

def rissGetData(driver, lastPage):
    titles = []
    authors = []
    links = []

    for page in range(2, lastPage + 1) :
        html = driver.page_source
        soup = bs(html, 'html.parser')
        element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CLASS_NAME, 'srchResultListW')))
        content = soup.find('div', 'srchResultListW').find_all('li')
        for con in content:
            con = con.find('div', 'cont ml60')
            try:
                title = con.find('p','title').get_text()
            except:
                continue
            else:
                titles.append(str(title))
                try:
                    author = con.find('p','etc').find("span", {"class":"writer"}).get_text()
                except:
                    author = 'No'
                authors.append(str(author))

                try:
                    link = con.find('p','title').find('a')
                    link = str(link).replace('<a href="', '').split('">')[0]
                    link = link.replace('amp;', '')
                    link = 'http://www.riss.kr/'+link
                except:
                    link = 'No'
                links.append(link)
            
        try :
            driver.find_element(By.LINK_TEXT ,str(page)).click()
        except :
            driver.find_element(By.LINK_TEXT, '다음 페이지로').click()

    return titles, authors, links