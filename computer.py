class Computer:

    # What attributes will it need? 
    
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive, memory, operating_system, year_made, price):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive = hard_drive
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

