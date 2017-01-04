import weapons 
import town 
import player
import Shop
shop1 = None
first_town = None
Player = None
Axe = None
def start_game():
	global shop1,first_town,Player,Axe
	Axe = weapons.Weapon('Axe',1,3,20,0)
	shop1 = Shop.CShop()
	first_town = town.Town(shop1)
	Player = player.CPlayer(first_town)
	print(Player,shop1,first_town)

