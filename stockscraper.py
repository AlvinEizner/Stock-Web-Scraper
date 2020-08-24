import bs4
import requests
from bs4 import BeautifulSoup
import time
from collections import defaultdict
#from flask import Flask

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
            #top_gainers[ticker] = price
            top_gainers[ticker].append(price)
            #if ticker in top_gainers:
                #top_gainers[ticker].append[price]
            #else:
                #top_gainers[ticker] = [price]
        for letter in range(len(ticker)):
            arr.append(' ')
        for letter in range(len(price)):
            arr1.append(' ')
        for letter in range(len(perchange)):
            arr2.append(' ')
    #for loops with arrs ensure equal spacing
    
def scan60():
    while True:
        scan()
        print()
        #print(top_gainers)
        time.sleep(60)
    
def scan300():
    count = 0 
    while True:
        scan()
        #print(top_gainers)
        for k in top_gainers:
            #print(f'{k}: {top_gainers[k]}')
            if count == 7:
                #print(top_gainers[k][8])
                if top_gainers[k][count] > top_gainers[k][count-1] and top_gainers[k][count-1] < top_gainers [k][count-4] and top_gainers[k][count-7] < top_gainers[k][count-5] and top_gainers[k][count-7] < top_gainers[k][count-1]:
                    print(f'{k}!!!!!')
                    print()
                    print()
            if count == 8:
                #print(top_gainers[k][8])
                if top_gainers[k][count] > top_gainers[k][count-1] and top_gainers[k][count-1] < top_gainers [k][count-4] and top_gainers[k][count-8] < top_gainers[k][count-5] and top_gainers[k][count-8] < top_gainers[k][count-1]:
                    print(f'{k}!!!!!')
                    print()
                    print()
            if count == 9:
                #print(top_gainers[k][8])
                if top_gainers[k][count] > top_gainers[k][count-1] and top_gainers[k][count-1] < top_gainers [k][count-4] and top_gainers[k][count-9] < top_gainers[k][count-5] and top_gainers[k][count-9] < top_gainers[k][count-1]:
                    print(f'{k}!!!!!')
                    print()
                    print()
                
            #for x in top_gainers[k]:
                #print(f'{k}: {x}')
        count += 1
        print(count)
        time.sleep(300)

scan300()
#app = Flask(__name__)
#@app.route("/webull-scraper", methods=['GET'])
#def webull_scraper():
    #scan()
    #return "Done"
    

