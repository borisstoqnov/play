from os import listdir
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


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

#get data for all companies in a directory
def readcsvfromdirtopandas():
    filepathwindows = "F:\\stockcompanies\\"
    filepathlinux = "/home/bobi/stockcompanies/modified/"
    i = []
    existingfiles = [f for f in listdir(filepathwindows) if isfile(join(filepathwindows, f))]
    for file in existingfiles:
        with open(filepathwindows + file) as f:
            numberoflines = len(f.readlines())
            if numberoflines > 17:
                df = pd.read_csv(filepathwindows + file + "", skiprows=18)
                calculateavaragefromcsv(df)

#Get panda data for one company
def readcsvfiletopandas(filename):

    with open(filename) as f:
        numberoflines = len(f.readlines())
        if numberoflines > 17:
            df = pd.read_csv(filename, skiprows=18)
            return df

#Get the avarage sum
def calculateavaragefromcsv(df):
    numberoftrades = len(df.iloc[:, 1])
    summofnumber = sum(df.iloc[:, 1])
    print(float(summofnumber) / float(numberoftrades))

def liniarregression(df):
    X = df.iloc[:, 3].values
    y = df.iloc[:, 1].values
    X = np.array(X).reshape(-1,1)
    # y = np.array(y).reshape(1, -1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    print(X)
    print(y)

# Fitting Simple Linear Regression to the Training set
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

# Predicting the Test set results
    y_pred = regressor.predict(X_test)
    # plt.get_backend()
# Visualising the Training set results
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Open vs Close price (Training set)')
    plt.xlabel('Open')
    plt.ylabel('Close')
    plt.show()


# Visualising the Test set results
    plt.scatter(X_test, y_test, color = 'red')
    plt.plot(X_test, regressor.predict(X_test), color = 'blue')
    plt.title('Open vs Close price (Test set)')
    plt.xlabel('Open')
    plt.ylabel('Close')
    plt.show()


liniarregression(readcsvfiletopandas("/home/bobi/stockcompanies/modified/AMD.csv"))

