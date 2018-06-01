productId = 0
productDB = {}

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

def createProduct():
    productName = input("Enter name of product: ")
    productSize = input("Enter size of product in inches: ")
    productWeight = input("Enter weight of product in lbs: ")
    productPrice = input("Enter price of the product in $: ")
    global productId
    productId += 1
    newProd = {str(productId) : {'name' : productName, 'size' : productSize,
                            'weight' : productWeight, 'price' : productPrice}}
    return newProd
                            
while True:
    print("Retail Platform")
    print("1. Create a new product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        productDB.update(createProduct())
        print("New product created.\n")
        break
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        break
    else:
        print("Please choose a number between 1 and 4")