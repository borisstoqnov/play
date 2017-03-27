import requests
import csv
import time
from os import listdir
from os.path import isfile, join
from getsymbol import getsymbols

#Get the name of the files we have so far without the extension
existingfiles = [f for f in listdir('/home/bobi/stockcompanies/') if isfile(join('/home/bobi/stockcompanies/', f))]
lofstocks = []
for existingname in existingfiles:
    lofstocks.append(existingname.split(".")[0])

#get a list of all the companies
companies = getsymbols()

#make a final list with the missing ones
newcompanies = [item for item in companies if item not in lofstocks]

for stockquote in newcompanies:
    print(stockquote)
    filename = '/home/bobi/stockcompanies/'+stockquote+'.csv'
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stockquote+'/chartdata;type=quote;range=10y/csv'
    download = requests.get(url)
    decoded_content = download.content.decode('utf-8')
    with open(filename, 'w', newline='\n') as csvfile:
        csvfile.writelines(decoded_content)
        #time.sleep(1)

