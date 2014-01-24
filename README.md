python-cryptocoincharts.info-api
=========================

This is a python wrapper class for the cryptocoincharts.info api.

 http://www.cryptocoincharts.info/v2/tools/api
 
___________________________________________________

**Please donate to "DQ6mBVyuboTGwS8JYW11oHwXtxsjNAzkzi"** 

!["Dogecoin Donation QR-Code"](http://github.com/Dirrot/python-cryptocoincharts-api/blob/master/img/donation-qr-code.png?raw=true)

___________________________________________________
 
_Methods_
* listcoins - Use this function to list all coins with their data which are available on cryptocoincharts.
* tradingpair - Use this function to query price and volume data for ONE trading pair.
* tradingpairs - Use this function to query price and volume data for MANY trading pairs.

___________________________________________________

Here's an example:

```python
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
```
