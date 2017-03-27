import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import urllib
import numpy as np
import csv
from getsymbol import getsymbols


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)

    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def graph_data(company):

    stock_data = []
    print('Currently polling', company)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    source_code = urllib.request.urlopen(url).read().decode()
    print("This is the url", url)
    split_source=source_code.split('\n')
    for each_line in split_source:
        split_line=each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    return(stock_data)

stock = input("Get data for which stock:")
#print(graph_data(stock))

with open('/home/bobi/stockcompanies/' + stock + '.csv', 'w', newline='\n') as csvfile:
    stockwriter = csv.writer(csvfile, delimiter=' ')
    stockwriter.writerow(graph_data(stock))


