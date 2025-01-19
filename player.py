"""
Module représentant la classe Player.

Ce module définit la classe `Player`, qui représente le joueur dans le jeu. 
Le joueur peut se déplacer, suivre son historique de déplacements et gérer 
son inventaire.

Classes :
    - Player : Représente un joueur avec un nom, une position actuelle, un inventaire
               et un historique de déplacements.
"""
class Player():
    """
    Représente un joueur dans le jeu.

    Attributs :
        name (str) : Le nom du joueur.
        current_room (Room) : La salle actuelle où se trouve le joueur.
        history (list[Room]) : L'historique des salles visitées par le joueur.
        inventory (dict) : L'inventaire du joueur, contenant des objets (Item).
        max_weight (float) : Le poids maximum transportable par le joueur.
    """
    # Define the constructor.
    def __init__(self, name):
        """
        Initialise un joueur.

        Args :
            name (str) : Le nom du joueur.
        """
        self.name = name
        self.history = []
        self.current_room = None
        self.inventory = {}
        self.max_weight = 30
        self.move_count = 0
        self.tentative = 0
    # Define the move method.
    def move(self, direction, player):
        """
        Permet au joueur de se déplacer dans une direction donnée.

        Args :
            direction (str) : La direction dans laquelle le joueur souhaite se déplacer.
            player (Player) : Le joueur effectuant le déplacement.

        Returns :
            bool : True si le déplacement est réussi, False sinon.
        """
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits[direction]
        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        item = next_room.item_required
        if item and item not in player.inventory:
            if next_room.name == "train":
                print("\nVous avez besoin d'un item qui vous donne de la force\n")
                return False

        # Set the current room to the next room.
        self.history.append(self.current_room)
        self.current_room = next_room
        self.move_count += 1
        print(self.current_room.get_long_description())
        if self.current_room.name == "monastere":
            if self.current_room.item_required not in player.inventory:
                print("Seuls les élus peuvent franchir ce seuil. Tourne les talons, impur! La prochaine fois je te sévirais.")
                self.tentative +=1
            else:
                print("Bienvenue, frère dans la foi. Que ta dévotion illumine ces lieux sacrés.")
        self.get_history()
        print(f"Nombre de déplacement : {self.move_count}")
        return True
    # Retoure les lieux visités
    def get_history(self):
        """
        Retourne une chaîne décrivant l'historique des lieux visités par le joueur.

        Returns :
            str : Une liste des salles précédemment visitées.
        """
        try:
            if len(self.history) >= 1:
                print("\nVous avez déjà visité les pièces suivantes:")
                for room in self.history:  # Exclut la pièce actuelle de l'historique affiché
                    print(f"    - {room.description[5:-1]}")
            else:
                print("\nVous n'avez visité aucune autre pièce.")
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors de l'affichage de l'historique : {e}")

    # Define the back method.
    def back(self):
        """
        Permet au joueur de revenir à la salle précédente.

        Returns :
            bool : True si le retour est effectué avec succès, False sinon.
        """
        try:
            if len(self.history) >= 1:
                # Set the current room to the previous room
                self.current_room = self.history.pop()
                print(self.current_room.get_long_description())
                self.get_history()
                return True
            print("\nVous ne pouvez pas revenir en arrière !\n")
            return False
        except Exception as e:
            print(f"\nUne erreur inattendue s'est produite lors du retour en arrière : {e}")
            return False

    def get_inventory(self):
        """
        Retourne une chaîne décrivant le contenu de l'inventaire du joueur.

        Returns :
            str : Une liste des objets dans l'inventaire, ou un message indiquant que
                  l'inventaire est vide.
        """
        if not self.inventory:
            return "\nVotre inventaire est vide."
        inventory_contents = "\nVous disposez des items suivants :"
        for item in self.inventory.values():
            inventory_contents += f"\n  - {item}"
        return inventory_contents
