'''
Created on 24.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

from CryptoCoinChartsApi import API

if __name__ == '__main__':
    
    api = API()

    listcoins = api.listcoins()
    print 'ListCoins: ', listcoins
    
    pair = 'doge_btc'
    tradingpair = api.tradingpair(pair)
    print 'TradingPair: ', tradingpair
    
    pairs = 'doge_btc,btc_eur'
    tradingpairs = api.tradingpairs(pairs)
    print 'TradingPairs: ', tradingpairs
