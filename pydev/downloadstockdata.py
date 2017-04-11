import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np
import csv
import os
from .getallcompaniesquote import getallcompaniesquote

allcompanychecker = False
dirforfiles = '/home/bobi/stockcompanies/'

def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)

    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter


def store_data(stock,range):

    stock_data = []
    print('Currently polling', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range='+range+'/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    print("This is the url", url)
    split_source=source_code.split('\n')
    for each_line in split_source:
        #split_line=each_line.split(',')
        stock_data.append(each_line)

    return(stock_data)

def inputdataparameters():
    range = input("What range do you want?(2 years period has more granularity")
    stock = input("Which company?(type all for all)")
    directory = input("Which direcotry?(default="+dirforfiles+"")
    if not os.path.isdir(directory):
        print("Not a directory")
        return 1
    if stock == "all":
        getallcompaniesquote(directory,range)
    else:
        getdataforonecompany(directory,stock,range)



#print(graph_data(stock))
def getdataforonecompany(directory,stock,range):
    with open(directory + stock + '.csv', 'w', newline='\n') as csvfile:
        stockwriter = csv.writer(csvfile, delimiter=' ')
        stockwriter.writerow(store_data(directory,stock,range))


