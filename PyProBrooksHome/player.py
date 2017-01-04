#this is the player class it has the players info and class stored here
from Con import *

class CPlayer():
    def __init__(self,t1):
        self.player_name = ''
        self.player_pos = 0
        self.Town = t1
        self.player_pos_list = [self.Town]
        self.gold = 300
        self.hp = 20
        self.max_hp = 20
        self.level = 1
        self.weapons = []
       
