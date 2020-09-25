

import sys
import os


####### DO THESE THINGS ONE AT A TIME
# 1. Add a person - Check your understanding
# 2. Add a drink - This is very similar to adding a person
# 3. Add favourite drink
    # Get a name from the user
    # Get a drink from the user
    # Store them in the dictionary favourites[name] = drink
####### FOR LATER!!
# Before menu loop - load everything from files and store in people_list and drink_list
# Have an exit option
# Before you exit - save people_list and drink_list to a file

# CLI menu
APP_NAME = 'BrIW'
VERSION = '0.1'
MENU_TEXT = f'''
Welcome to {APP_NAME} v{VERSION}!
Please, select an option by entering a number:
[1] Get all people
[2] Get all drinks
[3] Add a person
[4] Add a drink
[5] Set a favourite drink
[6] View favourites
[7] Exit

If you want to create a round for orders please press Confirm
'''

peoples_list = ['Johnny', 'Anissa', 'Giles', 'Saeed', 'Stuart']
drinks_list = ['coca-cola', 'Scwheppes', 'Sprite', 'Coffee', 'Cold Water']
favourite_drinks = {}
favourite_drinks_file = './favourites.txt'

def collect_data():
    user_menu_input = input(
        'Hi, welcome, what would you like to view? the menu??\n -------------------------\n Enter: ')
    print('+==================+')
    return user_menu_input

def add_person():
    new_person = input('Please add a new person: ')
    print(new_person)
    peoples_list.append(new_person)

def add_drink():
    new_drink = input('Please add a new drink: ')
    print(new_drink)
    drinks_list.append(new_drink)

def person_favourite():
    if name_of_person not in peoples_list:
        peoples_list.append(name_of_person)

    elif name_of_person in peoples_list:
        favourite_drinks[name_of_person] = name_of_drink

# def save_data():
#     # Save people
#     with open(PEOPLE_FILE_PATH, 'w') as file:
#         file.writelines([f'{person}\n' for person in people])


print(MENU_TEXT)

def round_order():
    while True:
        user_option = input('Do you want to get an order? ')

        if user_option == 'Yes' or user_option == 'Yes please':
            get_order_from_user()

        elif user_option == 'No':
            back_to_menu = input('Type enter to return to Menu ')
            if back_to_menu == 'Enter':
                print(MENU_TEXT)
            elif back_to_menu != 'Enter':
                print('Error')
            continue




def get_order_from_user():
    order = place_order()
    user_name = input('Please enter name of person trying to place an order ')
    drink_name = input(f'{user_name} wants to order a ..............')
    
    order.place_an_order(user_name, drink_name)

    if drink_name in drinks_list:
        f = open('./favourites.txt', 'w')
        f.write(f"{user_name} - {drink_name}")
        f.close()
        print('Thank you, your order has been saved')

class place_order:
    def __init__(self):
        self.order = {}

    def place_an_order(self, name, drink=None):
        if drink:
            self.order[name] = drink
        elif name in favourite_drinks:
            self.order[name] = favourite_drinks[name]
        else:
            print(f'Order not available, please try again')

#Create new menu option to ask for order class and save



while True:
    user_menu_input = collect_data()

    if user_menu_input == '1':
        for person in peoples_list:
            print(person)

    elif user_menu_input == '2':
        global drink
        for drink in drinks_list:
            print(drink)

    elif user_menu_input == '3':
        add_person()

    elif user_menu_input == '4':
        add_drink()

    elif user_menu_input == '5':
        name_of_person = input('Please enter a name: ')
        name_of_drink = input('What is their favourite drink? ')

    elif user_menu_input == '6':
        person_favourite()
        global y
        for x, y in favourite_drinks.items():
            print(x, ' - ', y)
            favourite_drinks_file = open('./favourites.txt', 'w')
            favourite_drinks_file.write(f'{x} - {y}')
            favourite_drinks_file.close()

    elif user_menu_input == '7':
        print('Thanks for coming! ')
        print('+==================+')

        exit()

    elif user_menu_input == 'Confirm' or user_menu_input == 'confirmed':
        round_order()

