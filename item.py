# Define the Room class.

class Item:

    # Define the constructor. 
    def __init__(self, name, description, weight):
        self.name = name
        self.description = description
        self.weight = weight

    # The string representation of the command.
    def __str__(self):
         return  f"{self.name} : {self.description} ({self.weight} kg)"