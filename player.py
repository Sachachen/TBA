# Define the Player class.
class Player():

    # Define the constructor.
    def __init__(self, name):
        self.name = name
        self.history = []
        self.current_room = None
    
    # Define the move method.
    def move(self, direction):
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False

        # Set the current room to the next room.
        self.current_room = next_room
        self.history.append(current_room)
        print(self.current_room.get_long_description())
        self.get_history()
        return True
    
    # Retoure les lieux visités
    def get_history(self):
        try:
            if len(self.history) >= 1:
                print("\nVous avez déjà visité les pièces suivantes:")
                for room in self.history:  # Exclut la pièce actuelle de l'historique affiché
                    print(f"    - {room.description}")
            else:
                print("\nVous n'avez visité aucune autre pièce.")
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors de l'affichage de l'historique : {e}")

    # Define the back method.
    def back(self):
        try:
            if len(self.history) >= 1:
                # Set the current room to the previous room
                self.current_room = self.history.pop()
                print(self.current_room.get_long_description())
                self.get_history()
                return True
            else:
                print("\nVous ne pouvez pas revenir en arrière !\n")
                return False
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors du retour en arrière : {e}")
            return False