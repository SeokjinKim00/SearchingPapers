from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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