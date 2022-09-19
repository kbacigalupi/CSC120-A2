from computer import Computer 
from typing import Dict

class ResaleShop:
    # constructor of the resale shop-uses same dictionary method as procedural code 
    def __init__(self):
        """ inventory: a dictionary where we'll store our inventory
    The key is an int representing the item number
    The value is an object of type Computer containing all the information about the computer
    """
        self.itemID = 0
        self.inventory : Dict[int, Computer] = {}
        
    #takes the instance and a computer and adds the itemID as a key and computer as the corresponding element to the shop's dictionary
    def buy_computer(self, computer):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        print("Buying computer", self.itemID)
        return self.itemID

    #removes the key and entry from the resale shop's dictionary with the given itemID
    def sell_computer(self, itemID):
        print("Selling computer", itemID)
        if itemID in self.inventory:
            del self.inventory[itemID]
            print("Item", itemID, "sold!\n")
        else: 
            #If the item was already sold/not in the dictionary tells the user so
            print("Item", itemID, "not found. Please select another item to sell.\n")

    #Prints all of the attributes of each computer instance in the resale shop's dictionary 
    def print_inventory(self):
        print("Checking inventory...")
        if self.inventory:
            for c in self.inventory:
                item = self.inventory[c]
                print(item.description, item.processor_type, item.hard_drive, item.memory, item.operating_system, item.year_made, item.price)
        else:
            #If the dictionary is empty, the program tells the user there are no computers
            print("No inventory to display :(")
        print("Done checking inventory.\n")
    
    #Takes the itemID and the new OS that the computer is being upgraded to & refurbishes the computer
    #Same tests (year made) is used to determine new price
    def refurbish_computer(self, itemID, new_os):
        print("Updating inventory...")
        print("Refurbishing Item ID:", itemID, "updating OS to", new_os)
        if itemID in self.inventory:
            c = self.inventory[itemID] # locate the computer
            if int(c.year_made) < 2000: 
                c.price = 0 # too old to sell, donation only
            elif int(c.year_made) < 2012:
                c.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(c.year_made) < 2018:
                c.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                c.price = 1000 # recent stuff
            if new_os is not None:
                c.operating_system = new_os # update details after installing new OS
                print(c.operating_system)
            else:
                #if not given a new OS tells the user so
                print("No New OS found \n")
        else:
            #If given an itemID that isn't in the inventory tells the user so
            print("Item not found. Please select another item to refurbish\n")
        

        
