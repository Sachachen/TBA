"""
Module représentant la classe Character.

Ce module définit la classe 'Character', qui représente un personnage dans le jeu.
Un personnage peut se déplacer entre différentes salles, interagir avec le joueur
et réagir en fonction de son inventaire.

Classes :
     Character : Représente un personnage avec des messages et des objets spécifiques.
"""
import random
from player import Player
from debug import DEBUG

# Description class character
class Character(Player):
    """
    Représente un personnage dans le jeu.

    Attributs :
        name (str) : Le nom du personnage.
        description (str) : Une description du personnage.
        current_room (Room) : La salle où se trouve actuellement le personnage.
        msgs (list[str]) : Une liste de messages que le personnage peut dire.
        item_required (Item) : Un objet requis pour interagir avec le personnage (optionnel).
        item_gift (Item) : Un objet que le personnage peut offrir au joueur (optionnel).
    """
    def __init__(self, name, description, current_room, msgs, item_requis=None):
        """
        Initialise un objet Character.

        Args :
            name (str) : Le nom du personnage.
            description (str) : Une description du personnage.
            room (Room) : La salle initiale où se trouve le personnage.
            msgs (list[str]) : Les messages que le personnage peut dire.
            item (Item, optionnel) : L'objet requis pour interagir avec le personnage.
            gift (Item, optionnel) : L'objet offert par le personnage en échange.
        """
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.item_required = item_requis
        self.has_moved = False

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du personnage.

        Returns :
            str : Une description formatée du personnage.
        """
        return f" {self.name} : {self.description}"
    def move_realisable(self):
        """
        Retourne un résultat.

        Returns :
            bool : True si le personnage se déplace dans une autre salle, False sinon.
        """
        result = random.choice([True, False])
        return result

    def move_character(self):
        """
        Déplace le personnage aléatoirement dans une salle adjacente, si possible.
        1 chances sur 2 de déplacement.

        Le personnage reste dans la salle actuelle ou se déplace vers une salle
        adjacente choisie aléatoirement si des sorties sont disponibles.

        Returns :
            bool : True si le personnage se déplace dans une autre salle, False sinon.
        """
        if self.move_realisable():
            excluded_rooms = {"ile_flottante"}
            direction = random.choice([key for key, value in self.current_room.exits.items() if value is not None and value.name not in excluded_rooms])
            next_room = self.current_room.exits[direction]

            if self.name in self.current_room.characters:
                del self.current_room.characters[self.name]
                next_room.characters[self.name] = self
                self.current_room = next_room
                if DEBUG:
                    print(f"{self.name} a été déplacé vers {next_room.name}")
            return True  # Le mouvement a eu lieu
            # print(f"{self.name} n'a pas bougé.")
        return False

    def get_msg(self):
        """
        Récupère un message du personnage en fonction de l'inventaire du joueur.

        Si le personnage est un "Chomeur" et qu'il nécessite un objet pour interagir,
        la réponse varie en fonction de la possession ou non de l'objet requis.
        Sinon, les messages standards du personnage sont renvoyés de manière cyclique.

        Args :
            player (Player) : Le joueur interagissant avec le personnage.

        Returns :
            str : Le message que le personnage dit.
        """
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg

    