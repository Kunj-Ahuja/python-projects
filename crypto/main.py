from mongo_setup import crypto_db
from user_functions import login, signup, update
import api_work
import os
user_function = int(input('''What do you want to do?
1. Login
2. Signup
Reply in 1 or 2:\n\n'''))
while not user_function in [1,2]:
    print('Wrong funtion\nEnter again')
    user_function = int(input())
name = input('Name: ')
password = input('Password: ')
data = {}
os.system('cls')
if user_function == 1:
    data = login(name,password)
elif user_function == 2:
    data = signup(name,password)

os.system('cls')
amount = data['amount']
portfolio = data['portfolio']

print(f'You have currently ${amount} in your account\n')

current_crypto = []
for i in crypto_db.find():
    current_crypto.append({'Name' : i['name'], 'Price': i['price']})
print('Current crypto prices are as follows: \n')
for i in current_crypto:
    print(f"{current_crypto.index(i)+1}) {i['Name']} - {i['Price']}\n")

crypto_input = int(input('\n\nIn which Crypto u wanted to invest (1,2,3,4): \n\n'))-1

while not crypto_input in [0,1,2,3]:
    print('Wrong selection!!')
    crypto_input = int(input('\n\nIn which Crypto u wanted to invest (1,2,3,4): \n\n'))-1
os.system('cls')
selected_crypto = current_crypto[crypto_input]
crypto_name = selected_crypto["Name"]
crypto_price = selected_crypto['Price'] 
number_coins_buy = amount//crypto_price
number_coins_have = 0 if crypto_name not in portfolio.keys() else portfolio[crypto_name]
print(f'So, u selected {crypto_name}\n')
print(f'You have {number_coins_have} {crypto_name} coins\n')
print(f'Currently u can buy {number_coins_buy} {crypto_name} coins\n')
print('''
1. Buy 
2. Sell
3. Exit
''') 

user_input = int(input())
while not user_input in [1,2,3]:
    print('Wrong input!!')
    user_input = int(input())
os.system('cls')
match user_input:
    case 1:
        print(f'You can buy {number_coins_buy} {crypto_name} coins')
        buy_amount = int(input('Number of coins u want to buy: '))
        if buy_amount > number_coins_buy:
            print('You dont have enough balance to buy')
        else:
            amount = amount-(crypto_price*buy_amount)
            print(f'Successfully bought {buy_amount} {crypto_name} coins worth {crypto_price*buy_amount}')
            portfolio.update({crypto_name:number_coins_have+buy_amount})
    case 2:
        print(f'You can sell {number_coins_have} {crypto_name} coins')
        sell_amount = int(input('Number of coins u want to sell: '))
        if sell_amount > number_coins_have:
            print('You cant sell coins which u dont have')
        else: 
            amount = amount + (crypto_price*sell_amount)
            print(f'Successfully sold {sell_amount} {crypto_name} coins worth {crypto_price*sell_amount}')
            portfolio.update({crypto_name:number_coins_have-sell_amount})
    case 3:
        exit()

update(amount,portfolio,name,password)