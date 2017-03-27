from os import listdir
from os import listdir
from os.path import isfile, join
import pandas as pd

def getsymbolsbycsv():
    existingfiles = [f for f in listdir('/home/bobi/stockcompanies/') if isfile(join('/home/bobi/stockcompanies/', f))]
    lofstocks = []
    for existingname in existingfiles:
        lofstocks.append(existingname.split(".")[0])
    return lofstocks

# def removefirstseventeenlines():
#     existingfiles = [f for f in listdir('/home/bobi/stockcompanies/modified') if isfile(join('/home/bobi/stockcompanies/modified', f))]
#     for file in existingfiles:
#         lines = open('textfile.txt').readlines()
#         open('newfile.txt', 'w').writelines(lines[17:])


def readcsvtopandas():
    filepath = "/home/bobi/stockcompanies/modified/"
    i = []
    existingfiles = [f for f in listdir(filepath) if isfile(join(filepath, f))]
    for file in existingfiles:
        with open(filepath + file) as f:
            numberoflines = len(f.readlines())
            if numberoflines > 17:
                df = pd.read_csv(filepath + file + "", skiprows=17)
                print(df)

readcsvtopandas()