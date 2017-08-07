import time
import sys, getopt
import datetime
#import requests
import urllib
import urllib2
import json
import time
import hmac,hashlib
from poloniex import poloniex

def percentageChange(lastPrice,coinPurchasePrice):
   p_change = ((lastPrice)-(coinPurchasePrice))/(coinPurchasePrice)*100
   p_change = float(p_change)
   return p_change

 # print "Menu"
 # print "Please Select Option
 # 1. View Portfolio
 # 	** Value Of Holdings: ?? USD / BTC**
 #
 # 	Coin 1, Price
 # Coin 2, Price
 # .
 # .
 # Coin n, Price
 # 2. Edit Portfolio
 # 1. Coin 1
 # 	1. Edit Purchase Price
 # 	2. Delete Coin
 # 2. Coin 2
 # 	1. Edit Purchase Price
 # 	2. Delete Coin
 # .
 # .
 # .
 # n. Coin n
 # 	1. Edit Purchase Price
 # 	2. Delete Coin

# '''
# open the portolio file
# format: coin,purchase_price
# eg. BTC_AMP,0.0000700
# '''

def readFile():
	file = open("portfolio.txt","r")
	portfolio = {}
	for line in file.readlines():
		line = line.strip()
		#add new coin, price to portfolio
		portfolio[line.split(",")[0]] = float(line.split(",")[1])
	return portfolio

def welcomeBanner():
	print "\n*********************************************"
	print "* Hello World. Welcome to Trading Assistant * "
	print "********************************************* \n"
	print ("Please Enter The alt-Coins In Portfolio:\n")


def main(argv):
	#declaration of variables
	count = 1
	userInput = []

	#print welcome message
	welcomeBanner()

	if(raw_input("Manual Entry: y?: ") == "y"):
		while True:
			print "\n",count,":",
			coinCode = raw_input()
			if (coinCode == ""):
				break
			userInput.append("BTC_"+coinCode.upper())
			count = count + 1
		currentHoldings = userInput

		userInput = []
		print ("Please Enter The Purchase Price For The alt-Coins In Portfolio: \n \n")
		for coin in currentHoldings:
			#request each coins purchase price
			coinPurchasePrice = raw_input(coin+": ")
			if (coinPurchasePrice == ""):
					break
			#turn the input to a float
			coinPurchasePrice = float(coinPurchasePrice)
	else:
		#import previous portfolio
		portfolio = readFile()

	#fetch data from poloniex
	ret = urllib2.urlopen(urllib2.Request('https://poloniex.com/public?command=returnTicker'))
	#add data to a dictionary
	data = json.loads(ret.read())

	fh = open("database.txt", "w")

	#display header material for table
	print "{:^10} {:^15} {:^10}".format("Coin", "Purchase Price", "% Change")
	print "------------------------------------------"

	#display coin data
	for item in portfolio:
		coinPurchasePrice = portfolio[item]
		lastPrice = float(data[item]["last"])
		print '{: <10}'.format(item),": ",
		print '{: <15}'.format('{:.8f}'.format(coinPurchasePrice)),
		print '{: <10}'.format('{:.2f}'.format(percentageChange(lastPrice,coinPurchasePrice)),"%")

	print "\n Statistics:"
	print "# of Coins:",len(portfolio)
	fh.close

if __name__ == "__main__":
	main(sys.argv[1:])
