"""
Description: Les modules d'actions.

Le module d'actions contient les fonctions appelées lorsqu'une commande est exécutée.

Chaque fonction prend 3 paramètres :
    -game : l'objet représentant le jeu
    -list_of_words : la liste des mots dans la commande
    -number_of_parameters : le nombre de paramètres attendus par la commande

Les fonctions retournent True si la commande a été exécutée avec succès, ou False dans le cas contraire.
Les fonctions affichent un message d'erreur si le nombre de paramètres est incorrect.
Le message d'erreur varie en fonction du nombre de paramètres attendus par la commande.

Le message d'erreur est stocké dans les variables MSG0 et MSG1, et formaté avec la variable command_word, qui correspond au premier mot de la commande.
La variable MSG0 est utilisée lorsque la commande ne prend aucun paramètre.
"""
# Import modules
from beamer import Beamer

MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"

class Actions:
    """
    Actions contient les méthodes statiques qui définissent les actions réalisables
    dans le jeu en fonction des commandes saisies par le joueur.
    """
    @staticmethod
    def go(game, list_of_words, number_of_parameters):
        """
        Move the player in the direction specified by the parameter.
        The parameter must be a cardinal direction (N, E, S, O).

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Exemples:
        
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game, ["go", "N"], 1)
        True
        >>> go(game, ["go", "N", "E"], 1)
        False
        >>> go(game, ["go"], 1)
        False

        """
        player = game.player
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Toutes les directions valides
        directions= {
            "N": "N", "NORD": "N",
            "S": "S", "SUD": "S",
            "E": "E", "EST": "E",
            "O": "O", "OUEST": "O",
            "U": "U", "UP": "U",
            "D": "D", "DOWN": "D",
            }
        # Get the direction from the list of words.
        direction = list_of_words[1]

        #Convertir la direction en majuscule
        direction = direction.upper()
        # Move the player in the direction specified by the parameter.
        if direction in directions:
            direction = directions[direction]
            player.move(direction,player)
        else:
            print(f"Direction '{direction}' non reconnue.")
        return True

    @staticmethod
    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    @staticmethod
    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.
        
        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True
    @staticmethod
    def history(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des déplacements du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        game.player.get_history()
    @staticmethod
    def back(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des déplacements du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        return game.player.back()
    @staticmethod
    def look(game, list_of_words, number_of_parameters):
        """
        Affiche les objets et personnages dans la pièce actuelle.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # If the number of parameters is incorrect, print an error message and return False.
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(game.player.current_room.get_inventory())

    @staticmethod
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de prendre un objet dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        item_name = list_of_words[1].lower()
        total_weight = 0
        for poids in player.inventory.values() :
            total_weight += poids.weight
        for item in player.current_room.inventory :
            if item_name == item.name :
                total_weight += item.weight
                if total_weight > player.max_weight :
                    print("\nLimite d'objet atteinte, il faut deposer un objet avant d'en prendre un nouveau.\n")
                    return True
                player.inventory[item.name]=item
                player.current_room.inventory.remove(item)
                print(f"\nVous avez pris l'objet : '{item.name}'.\n")
                return True
        if item_name in player.inventory:
            print(f"\nL'objet '{item_name}' se trouve deja dans votre inventaire.\n")
        else :
            print(f"\nL'objet '{item_name}' n'est pas dans cet endroit.\n")
        return True
    @staticmethod
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        player = game.player
        item_name = list_of_words[1].lower()

        if item_name in player.inventory :
            item = player.inventory.pop(item_name)
            player.current_room.inventory.add(item)
        else :
            print(f"\nVous ne possedez pas cet objet : '{item_name}'.\n")
        return True
    @staticmethod
    def check(game, list_of_words, number_of_parameters):
        """
        Vérifie l'inventaire du joueur.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        print(f"\n{game.player.get_inventory()}")
    @staticmethod
    def use(game, list_of_words, number_of_parameters):
        """
        Permet d'utiliser le beamer.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        if item_name in game.player.inventory:
            if isinstance(item,Beamer):
                return item.use(game)
        else:
            print(f"L'objet '{item_name}' n'est pas utilisable ou n'est pas un Beamer.")
            return False

    @staticmethod
    def charge(game, list_of_words, number_of_parameters):
        """
        Créer l'emplacement de téléportation.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        item_name = list_of_words[1]
        item = game.player.inventory.get(item_name, None)
        print(item_name)
        if item_name in game.player.inventory:
            item.charge(game.player.current_room)
            return True
        print(f"L'objet '{item_name}' ne peut pas être chargé ou n'est pas un Beamer.")
        return False
    @staticmethod
    def talk(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de parler à un personnage dans la pièce.

        Args:
            game (Game): L'objet représentant le jeu.
            list_of_words (list): Liste des mots constituant la commande.
            number_of_parameters (int): Nombre de paramètres attendus pour la commande.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        if len(list_of_words) != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        if len(game.player.current_room.characters) >= 1:
            character_name = list_of_words[1].lower()
            character = game.player.current_room.get_character(character_name)
            if character is not None:
                print(character.get_msg())
                if character_name == "marchand":
                    for item in game.items :
                        if item.name == "deguisement":
                            game.player.inventory[item.name]=item
            else:
                print(f"Il n'y a pas ce PNJ {character_name} dans cette pièce")
        else:
            print("Il n'y a aucun PNJ dans cette pièce")
        return True
