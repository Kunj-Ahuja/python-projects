from termcolor import colored,cprint

def print_board(p1,p2):
    one =  colored('X', 'red') if '1' in p1 else (colored('O', 'blue') if ('1' in p2) else '1')
    two =  colored('X', 'red') if '2' in p1 else (colored('O', 'blue') if ('2' in p2) else '2')
    three =  colored('X', 'red') if '3' in p1 else (colored('O', 'blue') if ('3' in p2) else '3')
    four =  colored('X', 'red') if '4' in p1 else (colored('O', 'blue') if ('4' in p2) else '4')
    five =  colored('X', 'red') if '5' in p1 else (colored('O', 'blue') if ('5' in p2) else '5')
    six =  colored('X', 'red') if '6' in p1 else (colored('O', 'blue') if ('6' in p2) else '6')
    seven =  colored('X', 'red') if '7' in p1 else (colored('O', 'blue') if ('7' in p2) else '7')
    eight =  colored('X', 'red') if '8' in p1 else (colored('O', 'blue') if ('8' in p2) else '8')
    nine =  colored('X', 'red') if '9' in p1 else (colored('O', 'blue') if ('9' in p2) else '9')
    print(f'{one} | {two} | {three}')
    print('---------')
    print(f'{four} | {five} | {six}')
    print('---------')
    print(f'{seven} | {eight} | {nine}')

def check_wins(p1,p2):
    wins = [['1','2','3'], ['1','4','7'],['1','5','9'],['2','5','8'],['3','6','9'],['3','5','7'],['4','5','6'],['7','8','9']]
    for win in wins:
        checkP1 = all(item in p1 for item in win)
        checkP2 = all(item in p2 for item in win)
        if checkP1 == True:
            return 1
        if checkP2 == True:
            return 2
p1 = []
p2 = []
print_board(p1,p2)
def ttt(p1,p2):    
    mix = p1+p2
    p1Post = input("Enter your number 'X': ")
    while p1Post in mix:
        print('Wrong number of postion, try different')
        p1Post = input("Enter your number 'X': ")
    p1.append(p1Post)
    print_board(p1,p2)
    if check_wins(p1,p2) == 1:
        print("'X' wins!!")
        exit()
    
    p2Post = input("Enter your number 'O': ")
    while p2Post in mix:
        print('Wrong number of postion, try different')
        p2Post = input("Enter your number 'O': ")
    p2.append(p2Post)
    print_board(p1,p2)
    if check_wins(p1,p2) == 2:
        print("'O' wins!!")
        exit()

while len(p1+p2) < 9:
    if len(p1+p2) == 9:
        print('Draw!')
    ttt(p1,p2)