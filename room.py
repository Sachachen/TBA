# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description, item_requis=None):
        self.name = name
        self.description = description
        self.exits = {}
        self.inventory = set()
        self.characters = {}
        self.item_required = item_requis
    
    # Define the get_exit method.
    def get_exit(self, direction):

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string
         
    def get_inventory(self):
        if not self.inventory and not self.characters:
            return "\nIl n'y a rien ici."
        else:
            inventory_contents = "\nOn voit :"
            for item in self.inventory:
                inventory_contents += f"\n  - {item}"
            for character in self.characters.values():
                inventory_contents += f"\n  -{character}"
            return inventory_contents
    
    def get_character(self, name):               
        for key in self.characters.keys():
            if key.lower() == name_lower:
                return self.characters[key]
        return None
        
    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
