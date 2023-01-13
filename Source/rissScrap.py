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