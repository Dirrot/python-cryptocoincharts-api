'''
Created on 24.01.2014

@author: Dirk Rother
@contact: dirrot.dev@gmail.com
@license: GPL
@version: 0.2

'''

from urllib2 import Request, urlopen, URLError, HTTPError
from urllib import urlencode
from Models import Coin, TradingPair
import json

class API(object):
    '''
    This class is a wrapper class for the CryptoCoinCharts api.
    '''
    
    API_PATH = "http://api.cryptocoincharts.info/"
        
    def listcoins(self):
        '''
        Use this function to list all coins with their data which are available on cryptocoincharts.
        Usage: http://api.cryptocoincharts.info/listCoins
        '''
        url = self.API_PATH + 'listCoins'
        
        json_data = json.loads(self._getdata(url))
        
        coins = []
        for entry in json_data:
            coin = Coin()
            coin.id = entry['id']
            coin.name = entry['name']
            coin.website = entry['website']
            coin.price_btc = entry['price_btc']
            coin.volume_btc = entry['volume_btc']
            coins.append(coin)
        
        return coins
    
    def tradingpair(self, pair):
        '''
        Use this function to query price and volume data for ONE trading pair.
        A list with all coin currencies can be found by using the listcoins method.
        A example pair: currency1_currency2 = "doge_btc" 
        Usage: http://api.cryptocoincharts.info/tradingPair/[currency1_currency2]
        '''
        url = self.API_PATH + 'tradingPair/' + pair
        
        json_data = json.loads(self._getdata(url))
        
        tradingpair = TradingPair()
        tradingpair.id = json_data['id']
        tradingpair.price = json_data['price']
        tradingpair.price_before_24h = json_data['price_before_24h']
        tradingpair.volume_first = json_data['volume_first']
        tradingpair.volume_second = json_data['volume_second']
        tradingpair.volume_btc = json_data['volume_btc']
        tradingpair.best_market = json_data['best_market']
        tradingpair.latest_trade = json_data['latest_trade']

        return tradingpair
    
    def tradingpairs(self, pairs):
        '''
        Use this function to query price and volume data for MANY trading pairs.
        Usage: http://api.cryptocoincharts.info/tradingPairs/[currency1_currency2,currency2_currency3,...]
               A example pair: currency1_currency2 = "doge_btc"
                               currency2_currency3 = "btc_eur"
               http://api.cryptocoincharts.info/tradingPairs/"doge_btc,btc_eur"            
        '''
        url = self.API_PATH + 'tradingPairs/'
        data = { 'pairs':pairs }
        
        json_data = json.loads(self._getdata(url, data))
        
        tradingpairs = []
        for entry in json_data:
            tradingpair = TradingPair()
            tradingpair.id = entry['id']
            tradingpair.price = entry['price']
            tradingpair.price_before_24h = entry['price_before_24h']
            tradingpair.volume_first = entry['volume_first']
            tradingpair.volume_second = entry['volume_second']
            tradingpair.volume_btc = entry['volume_btc']
            tradingpair.best_market = entry['best_market']
            tradingpair.latest_trade = entry['latest_trade']
            tradingpairs.append(tradingpair)
        
        return tradingpairs
    
    def listofpairs(self):
        pass
    
    def _getdata(self, url, data = ""):
        '''
        Wrapper method
        '''
        request = Request(url)
        
        if data != "":
            request = Request(url, urlencode(data))
            
        try:
            response = urlopen(request)
        except HTTPError as e:
            print('The Server couldn\'t fulfill the request.')
            print('Error code: ', e.code)
        except URLError as e:
            print('We failed to reach a server.')
            print('Reason: ', e.code)
        else:
            # Everything is fine.
            return response.read()
            