import pandas as pd
import os

def createDir(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except:
        print('Creating Directory Error')

def makeCSV(df, name):
    createDir('Data')
    fileName = 'Data/'+name+'.csv'
    df.to_csv(fileName)