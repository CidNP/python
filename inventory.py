print("What do you like to purchase: ")
search = input()
itemList=["Dalmot", "Chauchau", "Chips","Juice"]
itemPrice = {'Dalmot' :100, 'Chauchau' :20, 'Chips':50, 'Juice':100 }


if search in itemList:
    print("Available")
    print("Price of: " + search + " is " + str(itemPrice[search]))
else:
    print("Sorry! Not Available")
