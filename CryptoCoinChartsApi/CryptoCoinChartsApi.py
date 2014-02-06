'''
Created on 24.01.2014

@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

from urllib2 import Request, urlopen, URLError, HTTPError
from urllib import urlencode

class API(object):
    '''
    This class is a wrapper class for the CryptoCoinCharts api.
    '''
    
    API_PATH = "http://www.cryptocoincharts.info/v2/api/"
        
    def listcoins(self):
        '''
        Use this function to list all coins with their data which are available on cryptocoincharts.
        Usage: http://www.cryptocoincharts.info/v2/api/listCoins
        '''
        url = self.API_PATH + 'listCoins'
        return self._getdata(url)
    
    def tradingpair(self, pair):
        '''
        Use this function to query price and volume data for ONE trading pair.
        A list with all coin currencies can be found by using the listcoins method.
        A example pair: currency1_currency2 = "doge_btc" 
        Usage: http://www.cryptocoincharts.info/v2/api/tradingPair/[currency1_currency2]
        '''
        url = self.API_PATH + 'tradingPair/' + pair
        return self._getdata(url)
    
    def tradingpairs(self, pairs):
        '''
        Use this function to query price and volume data for MANY trading pairs.
        Usage: http://www.cryptocoincharts.info/v2/api/tradingPairs/[currency1_currency2,currency2_currency3,...]
               A example pair: currency1_currency2 = "doge_btc"
                               currency2_currency3 = "btc_eur"
               http://www.cryptocoincharts.info/v2/api/tradingPairs/"doge_btc,btc_eur"            
        '''
        url = self.API_PATH + 'tradingPairs/'
        data = { 'pairs':pairs }
        return self._getdata(url, data)
    
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
            print 'The Server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        except URLError as e:
            print 'We failed to reach a server.'
            print 'Reason: ', e.code
        else:
            # Everything is fine.
            return response.read()
