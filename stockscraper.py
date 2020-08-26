import bs4
import requests
from bs4 import BeautifulSoup
import time
from collections import defaultdict

top_gainers = defaultdict(list)
def scan():
    r = requests.get('https://www.webull.com/quote/rankgainer')
    
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    
    arr = [' ', ' ', ' ', ' ', ' ']
    arr1 = [' ', ' ', ' ', ' ', ' ', ' ']
    arr2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    num = 20
    for stocks in range(num):
        ticker = soup.findAll('div', {'class' : 'jss47w31n'})[stocks].find('a').text
        for letter in range(len(ticker)):
            arr.remove(' ')
        if stocks == 0:
            i = 2
        else:
            i = 8
        price = soup.findAll('div', {'class' : 'jsso8a07n'})[0].findAll('span')[stocks*i + 2].text
        for letters in range(len(price)):
            arr1.remove(' ')
        perchange = soup.findAll('div', {'class' : 'jsso8a07n'})[0].findAll('span')[stocks*i + 4].text
        for letters in range(len(perchange)):
            arr2.remove(' ')
        volume = soup.findAll('div', {'class' : 'jsso8a07n'})[0].findAll('span')[stocks*i + 5].text
        str1 = ''.join(arr)
        str2 = ''.join(arr1)
        str3 = ''.join(arr2)
        if float(price) >= 2.0 and float(price) <= 50.0 and ('M' in volume or ('K' in volume and len(volume) > 6)):
            print(f'Ticker: {ticker}{str1}', f'|  Price: {price}{str2} | ', f'% Change: {perchange}{str3} | ',f'Volume: {volume}')
            top_gainers[ticker].append(price)
        for letter in range(len(ticker)):
            arr.append(' ')
        for letter in range(len(price)):
            arr1.append(' ')
        for letter in range(len(perchange)):
            arr2.append(' ')
    #for loops with arrs ensure equal spacing
    
def scan60(): #scans every minute and prints list of stocks
    while True:
        scan()
        print()
        time.sleep(60)

    

