from mongo_setup import user_db
import os
def switch(name,what):
    if what == 1:
        print('Sign up portal!!\n')
        name = input('Name: ')
        password = input('Password: ')
        signup(name,password)
    elif what == 2:
        print('Login portal!!\n')
        name = input('Name: ')
        password = input('Password: ')
        login(name,password)

def login(name,password):
    if user_db.find_one({'name':name}):
        if user_db.find_one({'name':name,'password':password}):
            a = user_db.find_one({'name':name,'password':password})
            return {'amount' : a['amount'], 'portfolio' : a['portfolio']}
        else:
            print('Wrong password!!')
            while not user_db.find_one({'name':name,'password':password}):
                print('Try again \n(or write "exit" to exit code and "signup" for signup page)')
                user_input = input()
                os.system('cls')
                if user_input == 'exit':
                    exit()
                elif user_input == 'signup':
                    switch(name,1)
                else:
                    password = user_input
    else:
        while not user_db.find_one({'name':name}):
            print(f'User with the name {name} not present in the database!!')
            print('Type "exit" to exit or "signup" to signup')
            user_input = input()
            os.system('cls')
            if user_input == 'exit':
                    exit()
            elif user_input == 'signup':
                switch(name,1)
            else:
                password = user_input

def signup(name,password):
    if not user_db.find_one({'name':name}):
        user_db.insert_one({'name':name,'password':password,'amount':10_000,'portfolio':{}})
        return {'amount' : 10_000, 'portfolio': {}}
    else:
        while not user_db.find_one({'name':name}):
            print('Use another name\n(or type "login" to login and "exit" to exit code)')
            user_input = input()
            os.system('cls')
            if user_input == 'exit':
                exit()
            elif user_input == 'login':
                switch(name,2)
            else:
                password = user_input

def update(amount,portfolio,name,password):
    odata = {'name' : name, 'password' : password}
    nData = {'amount' : amount, 'portfolio': portfolio}
    user_db.update_one(odata,{'$set': nData})