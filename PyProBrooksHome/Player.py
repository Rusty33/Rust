#this is the player class it has the players info and class stored here
from Town import *
from Shop import *
shop = Shop()
class Player():
    def __init__(self):
        self.player_name = ''
        self.player_pos = 0
        self.Town = Town(shop)
        self.player_pos_list = [self.Town]
        self.gold = 300
        self.hp = 20
        self.max_hp = 20
        self.level = 1
        self.weapons = []
       
