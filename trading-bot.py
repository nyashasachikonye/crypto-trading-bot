import time
import sys, getopt
import datetime
import requests
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
	for item in data:
		if item in currentHoldings:
			percentChange = data[item]["percentChange"]
			if (percentChange > 0):
				print "currency_pair:",item
				print "lastPrice:",data[item]["last"]
				print "% change",data[item]["percentChange"],"\n"

if __name__ == "__main__":
	main(sys.argv[1:])
