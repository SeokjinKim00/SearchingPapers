from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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