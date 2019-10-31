#-------------------------------------------------------------------------------
# Name:        Dessert Stuff
# Purpose:
#
# Author:      kenny.coons
#
# Created:     29/10/2019
# Copyright:   (c) kenny.coons 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
dessert = []
#Dessert Functions
def choose_dessert():  #Allows the user to add or remove from the shopping list they have for desserts, an then view the length of the lis
    dessert_list = input("You have already added ice cream, pie and cheesecake, would you like to add or delete an item").lower
    if dessert_list == "add":
        added_dessert = input("what you like to add").lower
        append.added_dessert
    elif dessert_list == "delete":
        removed_dessert = input("what desert would you like to remove?").lower
        if removed_dessert == "cheesecake":
            dessert_list.remove("cheesecake")
        elif removed_dessert == "ice cream":
            dessert_list.remove("ice cream")
        elif removed_dessert == "pie":
            dessert_list.remove("pie")
    print(dessert_list)
