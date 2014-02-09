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

    print '*list of all coins*\n'
    
    listcoins = api.listcoins()
    for coin in listcoins:
        print coin
        print '\tid:', coin.id
        print '\tname:', coin.name
        print '\twebsite:', coin.website
        print '\tprice_btc:', coin.price_btc
        print '\tvolume_btc:', coin.volume_btc
        print '------------------------------'
        
    print '\n\n*a single tradingpair*\n'    
    
    pair = 'doge_btc'
    tradingpair = api.tradingpair(pair)
    print tradingpair
    print '\tid:', tradingpair.id
    print '\tprice:', tradingpair.price
    print '\tprice_before_24h:', tradingpair.price_before_24h
    print '\tvolume_first:', tradingpair.volume_first
    print '\tvolume_second:', tradingpair.volume_second
    print '\tvolume_btc:', tradingpair.volume_btc
    print '\tbest_market:', tradingpair.best_market
    print '\tlatest_price:', tradingpair.latest_trade
    print '------------------------------'
                     
    print '\n\n*list of specific tradingpairs*\n'                 
                                                                                       
    pairs = 'doge_btc,btc_usd,btc_eur'
    tradingpairs = api.tradingpairs(pairs)
    for tradingpair in tradingpairs:
        print tradingpair
        print '\tid:', tradingpair.id
        print '\tprice:', tradingpair.price
        print '\tprice_before_24h:', tradingpair.price_before_24h
        print '\tvolume_first:', tradingpair.volume_first
        print '\tvolume_second:', tradingpair.volume_second
        print '\tvolume_btc:', tradingpair.volume_btc
        print '\tbest_market:', tradingpair.best_market
        print '\tlatest_price:', tradingpair.latest_trade
        print '------------------------------'
