import requests
import csv
import time
from os import listdir
from os.path import isfile, join
from .getsymbol import getsymbols

def getallcompaniesquote(directory,range):
#Get the name of the files we have so far without the extension
    existingfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    lofstocks = []
    for existingname in existingfiles:
        lofstocks.append(existingname.split(".")[0])

    #get a list of all the companies
    companies = getsymbols()

    #make a final list with the missing ones
    newcompanies = [item for item in companies if item not in lofstocks]

    for stockquote in newcompanies:
        print(stockquote)
        filename = directory + stockquote + '.csv'
        url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stockquote+'/chartdata;type=quote;range=' + range + '/csv'
        download = requests.get(url)
        decoded_content = download.content.decode('utf-8')
        with open(filename, 'w', newline='\n') as csvfile:
            csvfile.writelines(decoded_content)
            #time.sleep(1)

