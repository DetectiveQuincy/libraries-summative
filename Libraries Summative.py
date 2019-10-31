#-------------------------------------------------------------------------------
# Name:        Libraries Summative
# Author:      kenny.coons
# Created:     29/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Imports
from Other import Breakfast_stuff, Lunch_stuff, Supper_stuff, Dessert_stuff

def eating_time(): #New function that prints all the items
    print ("you have eaten", breakfast, "for breakfast")
    print ("you have eaten", dinner, "for dinner")
    print ("you have eaten", supper, "for supper")
    dessert_time = input("What would you like to have for dessert you can choose anything from", dessert_list)

Breakfast_stuff.main_b()
print (Breakfast_stuff.breakfast)
Lunch_stuff.main_d()
print(Lunch_stuff.lunch)
Supper_stuff.main_s()
print(Supper_stuff.supper)
Dessert_stuff.choose_dessert()
print(Dessert_stuff.dessert)
eating_time()
