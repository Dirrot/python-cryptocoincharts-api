'''
@author: Dirk Rother
@contact: dirrot.dev@gmail.com
@license: GPL
@version: 0.2

'''
    
class TradingPair(object):
    '''
    This is a model for a TradingPair object.
    '''
    
    def __init__(self, id = "", price = "", price_before_24h = "", volume_first = "", volume_second = "", volume_btc = "", best_market = "", latest_trade = ""):
        '''
        Simple constructor for a Coin.
        '''
        self.id = id
        self.price = price
        self.price_before_24h = price_before_24h
        self.volume_first = volume_first
        self.volume_second = volume_second
        self.volume_btc = volume_btc
        self.best_market = best_market
        self.latest_trade = latest_trade
        
    def __repr__(self):
        '''
        The typ representation of a TradingPair.
        '''
        return "TradingPair"
    
    def __str__(self):
        '''
        The string representation of a TradingPair.
        '''
        return "TradingPair: [" + self.id + "] - " + self.price 
    