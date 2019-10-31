#-------------------------------------------------------------------------------
# Name:        Lunch Stuff
# Purpose:
#
# Author:      kenny.coons
#
# Created:     29/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Imports
#-----------Lists------------------------
dinner = {}

#Dinner Functions
def add_items_d(): #dinner function to add items
    stop = False
    while stop == False:
        items = input("what do you want to add to your dinner list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            dinner[items] = value

def remove_items_d(): #dinner function to remove items
    stop = False
    while stop == False:
        items = input("what would you like to remove from your list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in dinner:
            print ("removing", items)
            del dinner[items]

def view_items_d(): #dinner function
    stop = False
    for(items, value) in dinner.items():
        print ("You have", value, items, "in your list")

def stop_stuff(): #function for stoppuing
    stop = True

def main_d(): #main dinner function
    play = 1
    print("Time to go shopping")
    while play == 1:
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_d()
        elif choice == "remove":
            remove_items_d()
        elif choice == "view":
            view_items_d()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("Onto supper")
        else:
            print("i am sorry, i didn't understand that")
