from os import listdir
from os import listdir
from os.path import isfile, join
import pandas as pd

def getsymbolsbycsv():
    filepathwindows = "F:\\stockcompanies\\twofortest\\"
    filepathlinux = "/home/bobi/stockcompanies/modified/"
    existingfiles = [f for f in listdir(filepathwindows) if isfile(join(filepathwindows, f))]
    lofstocks = []
    for existingname in existingfiles:
        lofstocks.append(existingname.split(".")[0])
    return lofstocks

# def removefirstseventeenlines():
#     existingfiles = [f for f in listdir('/home/bobi/stockcompanies/modified') if isfile(join('/home/bobi/stockcompanies/modified', f))]
#     for file in existingfiles:
#         lines = open('textfile.txt').readlines()
#         open('newfile.txt', 'w').writelines(lines[17:])


def readcsvfromdirtopandas():
    filepathwindows = "F:\\stockcompanies\\twofortest\\"
    filepathlinux = "/home/bobi/stockcompanies/modified/"
    i = []
    existingfiles = [f for f in listdir(filepathwindows) if isfile(join(filepathwindows, f))]
    for file in existingfiles:
        with open(filepathwindows + file) as f:
            numberoflines = len(f.readlines())
            if numberoflines > 17:
                df = pd.read_csv(filepathwindows + file + "", skiprows=18)
                numberoftrades = len(df.iloc[:, 1])
                summofnumber = sum(df.iloc[:, 1])
                print(float(summofnumber)/float(numberoftrades))

def readcsvfiletopandas(filename):

    with open(filename) as f:
        numberoflines = len(f.readlines())
        if numberoflines > 17:
            df = pd.read_csv(filename, skiprows=18)
            numberoftrades = len(df.iloc[:, 1])
            summofnumber = sum(df.iloc[:, 1])
            print(float(summofnumber)/float(numberoftrades))

readcsvfiletopandas("F:\\stockcompanies\\twofortest\\AMD.csv")