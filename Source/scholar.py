def getScholarURL(question, page):
    urlBefore = 'https://scholar.google.co.kr/scholar?start='
    searchQuery = '&q='+question
    urlAfter = '&hl=ko&as_sdt=0,5'
    url = urlBefore + str(page) + searchQuery + urlAfter
    return url
