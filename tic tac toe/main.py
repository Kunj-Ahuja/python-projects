from termcolor import colored

#printing board using positions
def print_board(player1_postions,player2_postions):
    one =  colored('X', 'red') if '1' in player1_postions else (colored('O', 'blue') if ('1' in player2_postions) else '1')
    two =  colored('X', 'red') if '2' in player1_postions else (colored('O', 'blue') if ('2' in player2_postions) else '2')
    three =  colored('X', 'red') if '3' in player1_postions else (colored('O', 'blue') if ('3' in player2_postions) else '3')
    four =  colored('X', 'red') if '4' in player1_postions else (colored('O', 'blue') if ('4' in player2_postions) else '4')
    five =  colored('X', 'red') if '5' in player1_postions else (colored('O', 'blue') if ('5' in player2_postions) else '5')
    six =  colored('X', 'red') if '6' in player1_postions else (colored('O', 'blue') if ('6' in player2_postions) else '6')
    seven =  colored('X', 'red') if '7' in player1_postions else (colored('O', 'blue') if ('7' in player2_postions) else '7')
    eight =  colored('X', 'red') if '8' in player1_postions else (colored('O', 'blue') if ('8' in player2_postions) else '8')
    nine =  colored('X', 'red') if '9' in player1_postions else (colored('O', 'blue') if ('9' in player2_postions) else '9')
    print(f'{one} | {two} | {three}')
    print('---------')
    print(f'{four} | {five} | {six}')
    print('---------')
    print(f'{seven} | {eight} | {nine}')

#match again taking user input
def match_again(player1_postions,player2_postions):
    player1_postions.clear()
    player2_postions.clear()
    user_input = input("Want to play again (y/n): ")
    if user_input.capitalize() == 'Y':
        print_board(player1_postions,player2_postions)
        play_game(player1_postions,player2_postions)
    else: exit()

#checking win possebilites 
def check_wins(player1_postions,player2_postions):
    if len(player1_postions+player2_postions) == 9: #if moves are 9 its draw
        print('Draws')
        match_again(player1_postions,player2_postions)
    wins = [['1','2','3'], ['1','4','7'],['1','5','9'],['2','5','8'],['3','6','9'],['3','5','7'],['4','5','6'],['7','8','9']]
    for win in wins:
        checkplayer1_postions = all(item in player1_postions for item in win)
        checkplayer2_postions = all(item in player2_postions for item in win)
        if checkplayer1_postions == True:
            print('X wins!!') #if player1 positions are in wins
            match_again(player1_postions,player2_postions)
        if checkplayer2_postions == True:
            print('O wins!!') #if player2 postitions are in wins
            match_again(player1_postions,player2_postions)
player1_postions = []
player2_postions = []
print_board(player1_postions,player2_postions)
def play_game(player1_postions,player2_postions):    
    mix = player1_postions+player2_postions
    # X plays 
    player1_postionsPost = input("Enter your number 'X': ")
    while player1_postionsPost in mix or player1_postionsPost not in [1,2,3,4,5,6,7,8,9]:
        print('Wrong number of postion, try different')
        player1_postionsPost = input("Enter your number 'X': ")
    player1_postions.append(player1_postionsPost)
    print_board(player1_postions,player2_postions)
    check_wins(player1_postions,player2_postions)

    #O plays
    player2_postionsPost = input("Enter your number 'O': ")
    while player2_postionsPost in mix or player2_postionsPost not in [1,2,3,4,5,6,7,8,9]:
        print('Wrong number of postion, try different')
        player2_postionsPost = input("Enter your number 'O': ")
    player2_postions.append(player2_postionsPost)
    print_board(player1_postions,player2_postions)
    check_wins(player1_postions,player2_postions)

#looping till games end
while len(player1_postions+player2_postions) <= 9:
    play_game(player1_postions,player2_postions) 