#this has the town class
from Player import *
from Shop import *
shop = Shop()
class Town():
    def __init__(self,shop):
        self.name = 'Town'
        self.shops = [shop]
    def run(self):
        self.num = 1
        self.options = [self.shop]
        self.options_name = ['shop']
        for x in self.options_name:
            print('%s. %s'% (self.num,x))
            self.num += 1
        print('%s. exit' % (self.num))    
        com = input('What can I help you with ' )
        com = int(com)
        com -= 1
        self.num -= 1
        if com == self.num:
            print('Ok. Bye.')
        else:
            self.options[com]()
    def shop(self):
        self.num = 1
        self.options_name = [shop.name]
        for x in self.options_name:
            print('%s. %s'% (self.num,x))
            self.num += 1
        print('%s. exit' % (self.num))    
        com = input('What can I help you with ')
        com = int(com)
        com -= 1
        self.num -= 1
        if com == self.num:
            print('Ok. Bye.')
        else:
            self.shops[com].run()
        
