import Con


class CShop():
    def __init__(self):
        stock = [Con.Axe]
        self.stock = stock
        self.name = 'Johns'
    def run(self):
        print("Welcome to %s's shop. What can i do for you?")
        num = 1
        self.options = [self.buy]
        self.options_name = ['Buy']
        for x in self.options_name:
            print('%s. %s'% (num,x))
            num += 1
        print('%s. exit' % (num))
        com = input('What are you looking to do?' )
        com = int(com)
        com -= 1
        num -= 1
        if com == num:
            print('Ok. Bye.')
        else:
            self.options[com]()
    def buy(self):
        global Player
        num = 1
        for x in self.stock:
            print('%s. %s'% (num,x.name))
            num += 1
        com = input('What will it be?' )
        com = int(com)
        com -= 1
        num -= 1
        if com == num:
            print('Ok. Mabey next time.')
        else:
            Con.Player.weapons.append(self.stock[com])
            print(Con.Player.weapons[0].name)
