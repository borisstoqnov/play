from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir('/home/bobi/stockcompanies/') if isfile(join('/home/bobi/stockcompanies/', f))]
stocks = []
for i in onlyfiles:
    stocks.append(i.split(".")[0])

#print(onlyfiles)
print(stocks)