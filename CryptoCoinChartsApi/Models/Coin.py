'''
@author: Dirk Rother
@contact: dirrot@web.de
@license: GPL
@version: 0.1

'''

class Coin(object):
    '''
    This is a model for a Coin object.
    '''
    
    def __init__(self, id = "", name = "", website = "", price_btc = "", volume_btc = ""):
        '''
        Simple constructor for a Coin.
        '''
        self.id = id
        self.name = name
        self.website = website
        self.price_btc = price_btc
        self.volume_btc = volume_btc
        
    def __repr__(self):
        '''
        The typ representation of a Coin.
        '''
        return "Coin"
    
    def __str__(self):
        '''
        The string representation of a Coin.
        '''
        return "Coin: [" + self.id + '/' + self.name + "] - " + self.price_btc
    