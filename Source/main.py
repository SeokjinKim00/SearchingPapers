from scholarMain import runScholar

if __name__ == '__main__':
    print("--- Please enter a search term ---")
    print("Input : ", end='')
    question = input()

    print("--- Please Check Site ---")
    print("1. Google Scholar")
    print("Input : ", end='')
    siteCheck = input()

    if siteCheck == '1':
        question.replace(' ', '+')
        runScholar(question=question)
