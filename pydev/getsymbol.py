import csv

def getsymbols():
    stock = []
    with open ('/home/bobi/Downloads/companylist.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stock.append(row['Symbol'])
    return stock

print(getsymbols())