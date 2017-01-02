from Player import *
Player = Player()

##########################################################
intro = 'Welcome to Rust! A world of endles posabilaties and YOU are the center of it.'
print(intro)
Player.player_name = input('Now, tell me what is your name?')
print('Ok then %s.today is your first day in Rust so get out there and do want you want.If you need me just call.' % (Player.player_name))
##########################################################
option_list = []
game = True
##########################################################
class Help():
    def __init__(self):
        self.name = 'help'
        self.options = [self.name_change,self.get_pos]
        self.options_name = ['Change name','Get your pos']
#////////////////////////////////////////////////////////////#
    def run(self):
        num = 1
        for x in self.options_name:
            print('%s. %s'% (num,x))
            num += 1
        print('%s. exit' % (num))    
        com = input('What can I help you with %s' % (Player.player_name))
        com = int(com)
        com -= 1
        num -= 1
        if com == num:
            print('Ok. Bye.')
        else:
            self.options[com]()
#////////////////////////////////////////////////////////////#
    def name_change(self):
        print(Player.player_name)
        com = input('Would you like to change your name %s?(y/n)' % (Player.player_name))
        if com == 'y' or com == 'yes':
            Player.player_name = input('Ok. What do you want your new name to be?')
            print("I'll call you %s from now on"% (Player.player_name))
        else:
            print('Ok.Bye')
#////////////////////////////////////////////////////////////#
    def get_pos(self):
        print(Player.player_pos_list[Player.player_pos].name)
        



        
call_help = Help()
option_list.append(call_help)
option_list.append(Player.player_pos_list[Player.player_pos])
##########################################################
def menu():
    global game
    num = 1
    for x in option_list:
        print('%s. %s'% (num,x.name))
        num += 1
    print('%s. exit' % (num))    
    com = input('What would you like to do?')
    com = int(com)
    com -= 1
    num -= 1
    if com == num:
        print('Ok. Bye.')
        game = False
    else:
        option_list[com].run()
##########################################################
while game:
    menu()
                    

