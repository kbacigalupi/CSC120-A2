# Import a few useful containers from the typing module
from calendar import c
import random
from typing import Dict, Union
from procedural_resale_shop import buy, print_inventory, sell, refurbish
from computer import Computer
from oo_resale_shop import ResaleShop


#Main 2 is the OOP version
def main2():
    #First, let's make a computer
    computer1 = Computer("Mac Pro (Late 2013)",  "3.5 GHc 6-Core Intel Xeon E5", 1024, 64,"macOS Big Sur", 2013, 1500)
    #Let's start our resale shop
    my_shop = ResaleShop()
    
    # Print a little banner with the store
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    #Checks inventory & prints what is in the inventory or that there is no inventory
    my_shop.print_inventory()

    # Adds computer to the resale store's inventory using the ResaleShop method.
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_id = my_shop.buy_computer(computer1)
    print("Done.\n")

    # Makes sure computer was added by checking inventory
    my_shop.print_inventory()

    #sell our one computer
    my_shop.sell_computer(1)

    #print our empty inventory
    my_shop.print_inventory()
    

    #Making some computers
    comp2 = Computer("Macintosh Plus (1999)", "Something extremely old", 256, 64, "macOS 7.5", 1999, 20)
    comp3 = Computer("Mac Air 2018", "1.2GHz quad core Intel Core i7", 1024, 128, "macOS 12", 2018, 1000)
    comp4 = Computer("Mac Pro 2014", "Intel core i5", 1024, 128, "macOS 10", 2014, 1250)
    comp5 = Computer("Fairytale Computer 2004", "Unicorns and Rainbows", 2048, 256, "Marshmallows infinity", 2021, 1800)
    comp6 = Computer("Microsoft Surface 8", "Intel Atom 612E", 2048, 128, "Windows 11",  2020, 1500)
    
    # Makes list of computers
    comps = [comp2, comp3, comp4, comp5, comp6]

    print("Adding 6 new computers to inventory")
    #adds all of the computers to my resale shop
    for i in comps:
        my_shop.buy_computer(i)
    
    print("\n")
    #prints updated inventory
    my_shop.print_inventory()    

    #Attempts to refurbish computer 1, but computer 1 has already been sold. 
    #prints appropriate error message
    new_OS = "MacOS Monterey"
    my_shop.refurbish_computer(1, new_OS)
    
    #Refurbishes Macintosh Plus 1999
    print("Computer 2 Current Price:", comp2.price)
    my_shop.refurbish_computer(2, new_OS)
    print("Computer 2 New price:", comp2.price, '\n')
    
    #tries to sell computer 1 but computer 1 has already been sold   
    my_shop.sell_computer(1)

    print("Thanks for visiting the OOP shop today!")

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""

def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    # First, let's make a computer
    computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

# Calls the main2() function (OOP methods) when this file is run
if __name__ == "__main__": main2()
