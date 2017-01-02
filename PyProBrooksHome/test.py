import pygame



##########################################################
intro = 'Welcome to Rust! A world of endles posabilaties and YOU are the center of it.'
print(intro)
player_name = input('Now, tell me what is your name?')
print('Ok then %s.today is your first day in Rust so get out there and do want you want.If you need me just call.' % (player_name))
option_list = []
##########################################################
class Help():
    def __init__(self,player_name):
        self.call_name = 'help'
        self.options = [self.name_change]
#////////////////////////////////////////////////////////////#
    def run(self):
        num = 1
        for x in self.options:
            print('%s. %s'% (num,x))
            num += 1
        print('%s. exit' % (num))    
        com = input('What can I help you with %s' % (player_name))
        com = int(com)
        com -= 1
        num -= 1
        if com == num:
            print('Ok. Bye.')
        else:
            self.options[com]()
#////////////////////////////////////////////////////////////#
    def name_change(self):
        global player_name
        print(player_name)
        com = input('Would you like to change your name %s?(y/n)' % (player_name))
        if com == 'y' or com == 'yes':
            player_name = input('Ok. What do you want your new name to be?')
            print("I'll call you %s from now on"% (player_name))
        else:
            print('Ok.Bye')



        
call_help = Help(player_name)
option_list.append(call_help)
##########################################################
def menu():
    num = 1
    for x in option_list:
        print('%s. %s'% (num,x.call_name))
        num += 1
    print('%s. exit' % (num))    
    com = input('What would you like to do?')
    com = int(com)
    com -= 1
    num -= 1
    if com == num:
        print('Ok. Bye.')
    else:
        option_list[com].run()
##########################################################

menu()

