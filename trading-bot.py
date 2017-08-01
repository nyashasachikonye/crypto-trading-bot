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

def main(argv):
	print "Hello World. Welcome to Trading Assistant"
	ret = urllib2.urlopen(urllib2.Request('https://poloniex.com/public?command=returnTicker'))
	data = json.loads(ret.read())

	currentHoldings = ["BTC_AMP","BTC_BLK","BTC_BTC","BTC_BTS","BTC_DGB","BTC_ETC","BTC_ETH","BTC_GAME","BTC_LTC","BTC_NAUT","BTC_SYS","BTC_XRP"]
	fh = open("database.txt", "a")
	for item in data:
		if item in currentHoldings:
			percentChange = data[item]["percentChange"]
			if (percentChange > 0):
				fh.write("currency_pair: ")
				fh.write(item)
				fh.write("\n lastPrice: ")
				fh.write(data[item]["last"])
				fh.write("\n % change ")
				fh.write(data[item]["percentChange"])
				fh.write("\n")
	fh.close

if __name__ == "__main__":
	main(sys.argv[1:])
