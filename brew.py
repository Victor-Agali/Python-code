
import os
import csv
import sys
import itertools
import time
from functions import Order
from csv import reader

APP_NAME = 'br'
VERSION = '0.1'
MENU_TEXT = f'''\nWelcome to {APP_NAME} v{VERSION}!

Please, select an option by entering a number: 
[1] Get all people
[2] Get all drinks
[3] Add people to a list
[4] Add a drink to a list
[5] Set a favourite drink
[6] View favourites
[7] Order round
[8] Exit App

If you want to create a round for orders you can also type Create orders 
'''

under_18_people = ['Edward Cullen','Bella Swan','Jacob Black','Alice cullen','Esme Cullen','The volturi']
over_18_people = ['Peter Parker','Bruce banner','Nick Fury','Clint Barton','Steve Rodgers','Bruce Wayne']
non_alcoholic_drinks = ['Water','Coca-cola','Tea','Coffee','Schweppes','Lemonade','Smoothie','Cocktail','Apple juice','Coconut water']
alcoholic_drinks = ['Gin','Rum','Red bull','Smirnoff','Carling','Cider','Budweiser','Bulmers','Guiness','Heineken']
favourite_drinks ={}
favourite_drinks_file = 'favourites.csv'

def collect_data():
    user_menu_input = input( '---------------------------------------------------------------------------------------------\nTo view the menu, press * then select an option from the menu or type Exit to leave program\n--------------------------------------------------------------------------------------------\nEnter: ')
    print('+============================================================+')
    return user_menu_input

def to_view_menu(age,user):
    if user_age >= 18 and ask_user == 'iv':
        print('+============================================================+')
        for index,drink in enumerate(alcoholic_drinks, 1):
            print("{0} - {1}".format(index, drink))
        print('+============================================================+')

    elif user_age >= 18 and ask_user == 'v':
        print('+============================================================+')
        for index,drink in enumerate(non_alcoholic_drinks, 1):
            print("{0} - {1}".format(index, drink))
        print('+============================================================+')
    
    elif user_age < 18 and ask_user == 'iv':
        print('You are not allowed to view this menu, press # to return to main menu')

        while True:
            main_menu = input('Enter: ')
            if main_menu == '#':
                print(MENU_TEXT)
                break
            print('Error, please press # to return to menu')


    elif user_age < 18 and ask_user == 'v':
        print('+============================================================+')
        for index,drink in enumerate(non_alcoholic_drinks, 1):
            print("{0} - {1}".format(index, drink))
        print('+============================================================+')
        
def set_favourite_drink():
    if name_of_person in over_18_people:
        favourite_drinks[name_of_person] = name_of_drink

    elif name_of_person in under_18_people:
        favourite_drinks[name_of_person] = name_of_drink

    elif name_of_person not in over_18_people and name_of_person not in under_18_people:
        print('Error, this person is not in the menu, look at menu options to add this person\n')
        menu_return = input('Press # to return to menu\nEnter: ')

        if menu_return == '#':
            print(MENU_TEXT)

        else:
            print('Please type # to return to Menu')
            input('Enter: ')
            return menu_return

    elif name_of_drink not in alcoholic_drinks and name_of_drink not in non_alcoholic_drinks:
        print('Error, this drink is not in the menu, look at menu options to add this drink\n')
        menu_return = input('Press # to return to menu\nEnter: ')

        if menu_return == '#':
            print(MENU_TEXT)

        else:
            print('Please type # to return to Menu')
            input('Enter: ')
            return menu_return
    
    else:
        favourite_drinks[name_of_person] = name_of_drink

def add_drink_to_list():
    your_age = int(input('Your age: '))
    mature_menu = input('What menu would you like to add to?\nFor Alcoholic type A or to access the Soft drinks menu type S\nEnter: ')
    add_new_drink = input('What drink would you like to add?\nEnter: ')
    alcohol_test = input('Is it alcoholic?\nType Y/N\nEnter: ')

    if your_age >= 18 and mature_menu == 'A' or mature_menu == 'a':
        if alcohol_test == 'Y' or alcohol_test == 'y':
            alcoholic_drinks.append(add_new_drink)
            print('···························································')
            print('Your drink has been added to the alcoholic drink menu')
            print('···························································')

        elif alcohol_test == 'N' or alcohol_test == 'n':
            non_alcoholic_drinks.append(add_new_drink)
            print('···························································')
            print('Your drink has been added to the non-alcoholic drink menu')
            print('···························································')

    elif your_age < 18 and mature_menu =='S' or mature_menu == 's':
        if alcohol_test == 'N' or alcohol_test == 'n':
            non_alcoholic_drinks.append(add_new_drink)
            print('···························································')
            print('Your drink has been added to the non-alcoholic drink menu')
            print('···························································')
        
        elif alcohol_test == 'Y' or alcohol_test == 'y':
            print('·············································································')
            print('You cant access this menu, you will now be redirected to the main menu')
            print('·············································································')
            time.sleep(.700)
            print(MENU_TEXT)

    elif your_age < 18 and mature_menu == 'A' or mature_menu == 'a':
        if alcohol_test == 'Y' or alcohol_test == 'y':
            print('·············································································')
            print('Not allowed to join this list, you will now be redirected to the main menu')
            print('·············································································')
            time.sleep(.700)
            print(MENU_TEXT)

        elif alcohol_test == 'N' or alcohol_test == 'n':
            non_alcoholic_drinks.append(add_new_drink)
            print('···························································')
            print('Your drink has been added to the non-alcoholic drink menu')
            print('···························································')
            
        else:
            print(MENU_TEXT)



    # if your_age >= 18 and alcohol_test == 'Y' or alcohol_test == 'y':
    #     if mature_menu == 'Alcoholic' or mature_menu == 'alcoholic':
    #         alcoholic_drinks.append(add_new_drink)

    #     elif mature_menu == 'Non-alcoholic' or mature_menu == 'non-alcoholic':
    #         non_alcoholic_drinks.append(add_new_drink)

    
    # elif your_age < 18 and alcohol_test == 'N' or alcohol_test == 'n':
    #     if mature_menu == 'Non-alcoholic' or mature_menu == 'non-alcoholic':
    #         non_alcoholic_drinks.append(add_new_drink)
    #     else:
    #         print(MENU_TEXT)
    
    # elif your_age < 18 and alcohol_test == 'Y' or alcohol_test == 'y':
    #     if mature_menu == 'Alcoholic' or mature_menu == 'alcoholic':
    #         print('Not allowed to join this list')
    #         sys.stdout.flush()
    #         print(MENU_TEXT)
    #     else:
    #         print(MENU_TEXT)

def add_round():
    owner = input('Whos round is it?\nEnter: ')
    print(owner)
    round = Order(owner)
    if owner in under_18_people:
        for names in under_18_people:
            drink_input = input(f'Please input what drink does {names} want: ') 
            round.add_to_order(names, drink_input)
        round.print_order()
        round.save_rounds_to_file()  

    elif owner in over_18_people:
        for names in over_18_people:
            drink_input = input(f'Please input what drink does {names} want: ') 
            round.add_to_order(names, drink_input)
        round.print_order()
        round.save_rounds_to_file() 

    elif owner not in under_18_people and owner not in over_18_people:
        print('This user is not in any menu press any number to return to main menu')
        back = int(input('Enter: '))
        print()
        if 0 <= back <=10:
            print(MENU_TEXT)
        else:
            print(MENU_TEXT) 

print(MENU_TEXT)
while True:
    user_menu_input = collect_data()

    if user_menu_input == '*':
        print(MENU_TEXT)

# Print menu from all lists
    elif user_menu_input == '1':
        view_people = input('What list of people do you want to see?\n..........................................................\n\nFor minors type [i]\nFor adults type [ii]\nTo see all type [iii]\n\n..........................................................\nEnter: ')
        print('-----------------------------------------------------------')

        if view_people == 'i':
            print('+=========================================================+')
            for index,person in enumerate(under_18_people, 1):
                print("{0} - {1}".format(index, person))
            print('+=========================================================+')
                
        elif view_people == 'ii':
            print('+=========================================================+')
            for index,person in enumerate(over_18_people, 1):
                print("{0} - {1}".format(index, person))
            print('+=========================================================+')

        elif view_people == 'iii':
            full_list = under_18_people + over_18_people
            print('Under-18 list')
            print('_________________')
            for index,person in enumerate(under_18_people, 1):
                print("{0} - {1}".format(index, person))
            print('------------------')
            print('Over-18 list')
            print('_________________')
            for index,person in enumerate(over_18_people, 1):
                print("{0} - {1}".format(index, person))
            print('_________________')
            # print('+=========================================================+')
            # for index,people in enumerate(full_list, 1):
            #     print("{0} - {1}".format(index, people))
            # for p1,p2 in itertools.zip_longest(under_18_people,over_18_people):
            #     print(f"Under aged drinkers:\n{p1}\nOther drinkers:\n{p2}\n")
            print('+=========================================================+')

    elif user_menu_input == '2':
        user_age = int(input('How old are you?\nEnter: '))
        ask_user = input('-----------------------------------------------------------\nWhat drink menu would you like to view?\n..........................................................\nFor alcoholic type [iv] or for non-alcoholic type [v]\n..........................................................\nEnter: ')
        to_view_menu(user_age,ask_user)


    elif user_menu_input == '3':
        add_people_to_list = input('Who would you like to add to the list?\nEnter name: ')
        add_age = int(input('What is their age?\nEnter: '))

        if add_age < 18:
            under_18_people.append(add_people_to_list)
            print('················································')
            print(f"{add_people_to_list} has been added to the list of minors")
            print('················································')
        elif add_age >= 18:
            over_18_people.append(add_people_to_list)
            print('················································')
            print(f"{add_people_to_list} has been added to the list of over-18s")
            print('················································')

    elif user_menu_input == '4':
        add_drink_to_list()

    elif user_menu_input == '5':
        name_of_person = input(f"Choose a person's name \n Enter: ")
        name_of_drink = input('What is their favourite drink? ')
        print('+============================================================+')
        set_favourite_drink()
        

    elif user_menu_input == '6':
        for x,y in favourite_drinks.items():
            print(x, '-', y)
            print('+============================================================+')

    elif user_menu_input == '7' or user_menu_input == 'Create orders':
        add_round()
    
    elif user_menu_input == '8' or user_menu_input == 'Exit':
        # favourite_drinks_file = open('favourites.csv', 'w')
        
        # write_favourites = csv.writer(favourite_drinks_file)
        # for key, value in favourite_drinks.items():
        #     write_favourites.writerow([key,value])
        # favourite_drinks_file.close()
        print('Thanks for coming!')
        print('+============================================================+')
        exit()