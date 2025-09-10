import sys
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity): #Initialize class
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        pass

    def get_cost(self): 
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self): #Converting into string for later use in functions
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


#=============Shoe list===========

shoe_list = [] #store objects 


#==========Functions outside the class==============
def read_shoes_data(shoes, file): #Take input from text file and set as separate objects and put into shoe_list
    try:
        with open(file, 'r') as f:
            for line in f:
                try:
                    data = line.strip().split(',')
                    att1 = data[0]
                    att2 = data[1] 
                    att3 = data[2]
                    att4 = int(data[3])
                    att5 = int(data[4])
                    obj = Shoe(att1, att2, att3, att4, att5)
                    shoes.append(obj)
                except:
                    pass #passes the first line of the text file and any others that may not be able to fit as an object
    except:
        print("inventory.txt not found")
        sys.exit()
    return shoes

def capture_shoes(shoes): #add a new shoe to the list
    att1 = input("Enter the country: ")
    att2 = input("Enter the code: ")
    att3 = input("Enter the product: ")
    try:
        att4 = int(input("Enter the cost: "))
        att5 = int(input("Enter the quantity: "))
    except:
        return print("Enter a valid number")
    obj = Shoe(att1, att2, att3, att4, att5)
    shoes.append(obj)
    print("Shoe successfully added!")
    return shoes

def view_all(shoes):
    return print([str(item) for item in shoes])

def re_stock(shoes, file): #Sort list by lowest quantity, then add to that quantity
    n = len(shoes)
    for i in range(n): #Sorting algorithm for the list
        swapped = False
        for j in range(0, n-i-1):
            if shoes[j].quantity > shoes[j+1].quantity:
                shoes[j], shoes[j+1] = shoes[j+1], shoes[j]
                swapped = True
        if not swapped:
            break

    stock = input(f"Would you like to increase the quantity for the lowest stocked shoe? ({shoes[0]}) Respond using 'y' or 'n' ")
    if stock.lower() == "y":
        try:
            stock_amount = int(input("How much would you like to add to this shoe? "))
        except:
            print("Enter a valid number")
            return

        shoes[0].quantity = stock_amount + shoes[0].quantity
        with open(file, 'r') as f: #Change value in the text file
            lines = f.readlines()

        for i, line in enumerate(lines):
            data = line.strip().split(',')
            if data[1] == shoes[0].code:  
                data[4] = str(shoes[0].quantity) 
                lines[i] = ",".join(data) + "\n"  

        with open(file, 'w') as f: #Write to text file
            f.writelines(lines)

    return shoes



def search_shoe(shoes): #Find specific shoe from code
    index = input("Enter the code of the shoe you would like to find: ")
    for shoe in shoes:
        if shoe.code == index:
            return print(str(shoe))
        else:
            return print("Code given does not match any codes in the inventory.")



def value_per_item(shoes): #Find total value for each item
    for shoe in shoes:
        total = shoe.quantity * shoe.cost
        print(f"The total value for {shoe.product}, {shoe.code} is {total}")
    return



def highest_qty(shoes): #Find the highest quantity shoe and set it for sale
    n = len(shoes)
    for i in range(n): #Same sorting algorithm used earlier except change ">" to "<"
        swapped = False
        for j in range(0, n-i-1):
            if shoes[j].quantity < shoes[j+1].quantity:
                shoes[j], shoes[j+1] = shoes[j+1], shoes[j]
                swapped = True
        if not swapped:
            break
    return print(f"{shoes[0].product}, {shoes[0].code} is the highest quantity with {shoes[0].quantity} shoes in stock and is thus for sale")


#==========Main Menu=============
read_shoes_data(shoe_list, "inventory.txt")
while True: #Loop through the menu
    choice = int(input("----------------------------------------------------------------------------------------------------------\n"
          "Welcome to the inventory program! What would you like to do? (Type the number corresponding to the option) \n"
          "1) Add new shoe to inventory\n"
          "2) View all shoes?\n"
          "3) Restock the lowest quantity shoe?\n"
          "4) Search for a specific shoe in the inventory?\n"
          "5) See the total value for each shoe in the inventory?\n"
          "6) Set the highest quantity shoe in the inventory for sale?\n"
          "7) Exit the program?\n "
          "----------------------------------------------------------------------------------------------------------\n"))

    if choice == 1:
        capture_shoes(shoe_list)
    elif choice == 2:
        view_all(shoe_list)
    elif choice == 3:
        re_stock(shoe_list, "inventory.txt")
    elif choice == 4:
        search_shoe(shoe_list)
    elif choice == 5:
        value_per_item(shoe_list)
    elif choice == 6:
        highest_qty(shoe_list)
    elif choice == 7:
        break
    else:
        print("Type a valid response")