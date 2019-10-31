#-------------------------------------------------------------------------------
# Name:        Supper Stuff
# Purpose:
#
# Author:      kenny.coons
#
# Created:     29/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Imports
#--------Lists---------------
supper = {}
#Supper Functions
def add_items_s(): #adds supper items
    stop = False
    while stop == False:
        items = input("what do you want to add to your supper list").lower()
        if items == "stop":
            stop = True
        elif items != "stop":
            value = input("how much of that would you like to add")
            print ("adding", value, items)
            supper[items] = value

def remove_items_s(): #removes supper items
    stop = False
    while stop == False:
        items = input("what would you like to remove from your supper list").lower()
    if items == "stop":
        stop = True
    elif items != "stop":
        if items in supper:
            print ("removing", items)
            del supper[items]

def view_items_s(): #supper function
    stop = False
    for(items, value) in supper.items():
        print ("You have", value, items, "in your list")

def stop_stuff(): #fumction for stoppuing
    stop = True

def main_s():  #main supper function
    play = 1
    print("Time to go shopping")
    while play == 1:
        choice = input("Would you like to add or remove items, view the list or stop?").lower()
        if choice == "add":
            add_items_s()
        elif choice == "remove":
            remove_items_s()
        elif choice == "view":
            view_items_s()
        elif choice == "stop":
            stop_stuff()
            play = 0
            print("onto dessert")
        else:
            print("i am sorry, i didn't understand that")