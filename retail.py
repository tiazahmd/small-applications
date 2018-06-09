#! /usr/bin/python3.6

import shelve

class Product():
    def __init__(self, name, size, weight, price):
        self.name = name
        self.size = size
        self.weight = weight
        self.price = price
        
    def show_all_products(self):
        print("Name: " + self.name)
        print("Size: " + str(self.size))
        print("Weight: " + str(self.weight + "lbs"))
        print("Price: $" + str(self.price))
        print("\n")

def createProduct(productId):
    productName = input("Enter name of product: ")
    productSize = input("Enter size of product in inches: ")
    productWeight = input("Enter weight of product in lbs: ")
    productPrice = input("Enter price of the product in $: ")

    productObj = Product(productName, productSize, productWeight, productPrice)
    productId += 1
    newDictItem = {str(productId) : productObj}
    
    return newDictItem

def viewAllItems(dictionary):
    for values in dictionary.keys():
        tempObj = dictionary[values]
        print("\nProduct ID: " + values)
        print("Product Name: " + tempObj.name)
        print("Product Size: " + str(tempObj.size))
        print("Product Weight: " + str(tempObj.weight))
        print("Product Price: " + str(tempObj.price) + "\n")

def storeInDB(dictionary):
    shelfFile = shelve.open('database')
    shelfFile['db'] = dictionary
    shelfFile.close()

def retrieveDB():
    shelfFile = shelve.open('database')
    productDB = shelfFile['db']
    shelfFile.close()
    return productDB

def getProductId(dictionary):
    productId = len(dictionary)
    return productId

def deleteItem(deleteChoice):
    shelfFile = shelve.open('database')
    productDB = shelfFile['db']
    if deleteChoice in productDB.keys():
        del productDB[deleteChoice]
        print("Product Deleted")
    else:
        print("Product ID does not exist")
    shelfFile['db'] = productDB
    shelfFile.close()

def changeSize(productID, newSize):
    db = retrieveDB()
    db[productID].size = newSize
    storeInDB(db)

def changeWeight(productID, newWeight):
    db = retrieveDB()
    db[productID].size = newWeight
    storeInDB(db)

def changePrice(productID, newPrice):
    db = retrieveDB()
    db[productID].size = newPrice
    storeInDB(db)

def updateProduct():
    while True:
        pID = input("Enter product ID: ")
        print("What do you want to update?")
        print("1. Size\n2. Weight\n3. Price")
        updateChoice = input("Enter choice: ")
        if updateChoice == "1":
            newSize = input("Enter new size: ")
            changeSize(pID, newSize)
            print("Product Updated.")
            break
        elif updateChoice == "2":
            newWeight = input("Enter new weight: ")
            changeWeight(pID, newWeight)
            print("Product Updated.")
            break
        elif updateChoice == "3":
            newPrice = input("Enter new price: ")
            changePrice(pID, newPrice)
            print("Product Updated.")
            break
        else:
            print("Pleae only enter 1, 2 or 3")

while True:
    print("Retail Platform")
    print("1. Create a new product")
    print("2. View all products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        productDB = retrieveDB()
        productId = getProductId(productDB)
        productDB.update(createProduct(productId))
        storeInDB(productDB)
        print("New product created.\n")
    elif choice == "2":
        productDB = retrieveDB()
        viewAllItems(productDB)
    elif choice == "3":
        updateProduct()
    elif choice == "4":
        deleteChoice = input("Enter Product Id to delete: ")
        deleteItem(deleteChoice)
    elif choice == "5":
        break
    else:
        print("Please choose a number between 1 and 4")