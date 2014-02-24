python-cryptocoincharts-api [![Build Status](https://travis-ci.org/Dirrot/python-cryptocoincharts-api.png?branch=master)](https://travis-ci.org/Dirrot/python-cryptocoincharts-api) [![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/Dirrot/python-cryptocoincharts-api/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
=========================

This is a python wrapper class for the cryptocoincharts.info api.

 http://www.cryptocoincharts.info/v2/tools/api
 

___________________________________________________
 
_Methods_
* listcoins - Use this function to list all coins with their data which are available on cryptocoincharts.
* tradingpair - Use this function to query price and volume data for ONE trading pair.
* tradingpairs - Use this function to query price and volume data for MANY trading pairs.

___________________________________________________

_Install_
```bash
sudo pip install CryptoCoinChartsApi
```

___________________________________________________

Here's an example:

```python
from CryptoCoinChartsApi import API

if __name__ == '__main__':
    
    api = API()
    
    print '*list of all coins*'
    
    listcoins = api.listcoins()
    for coin in listcoins:
        print coin
        print 'id:', coin.id
        print 'name:', coin.name
        print 'website:', coin.website
        print 'price_btc:', coin.price_btc
        print 'volume_btc:', coin.volume_btc
        
    print '*a single tradingpair*'
    
    pair = 'doge_btc'
    tradingpair = api.tradingpair(pair)
    print tradingpair
    print 'id:', tradingpair.id
    print 'price:', tradingpair.price
    print 'price_before_24h:', tradingpair.price_before_24h
    print 'volume_first:', tradingpair.volume_first
    print 'volume_second:', tradingpair.volume_second
    print 'volume_btc:', tradingpair.volume_btc
    print 'best_market:', tradingpair.best_market
    print 'latest_price:', tradingpair.latest_trade
                     
    print '*list of specific tradingpairs*'                 
                                                                                       
    pairs = 'doge_btc,btc_usd,btc_eur'
    tradingpairs = api.tradingpairs(pairs)
    for tradingpair in tradingpairs:
        print tradingpair
        print 'id:', tradingpair.id
        print 'price:', tradingpair.price
        print 'price_before_24h:', tradingpair.price_before_24h
        print 'volume_first:', tradingpair.volume_first
        print 'volume_second:', tradingpair.volume_second
        print 'volume_btc:', tradingpair.volume_btc
        print 'best_market:', tradingpair.best_market
        print 'latest_price:', tradingpair.latest_trade

```

___________________________________________________

**Please donate to "DQ6mBVyuboTGwS8JYW11oHwXtxsjNAzkzi" [DOGECOIN]** 

!["Dogecoin Donation QR-Code"](http://github.com/Dirrot/python-cryptocoincharts-api/blob/master/img/donation-qr-code.png?raw=true)


