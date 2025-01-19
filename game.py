"""
Module contenant la classe Game.

La classe Game représente le moteur principal du jeu d'aventure textuel.
Elle configure les éléments du jeu, traite les commandes des joueurs
et gère la boucle principale de jeu.
"""
# Import modules
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from beamer import Beamer
from character import Character
from debug import DEBUG

class Game:
    """
    Classe principale pour gérer le jeu.

    Attributs:
        finished (bool): Indique si le jeu est terminé.
        rooms (list[Room]): Liste des salles disponibles dans le jeu.
        commands (dict): Dictionnaire des commandes disponibles.
        player (Player): Instance représentant le joueur.
        items (list[Item]): Liste des objets du jeu.
        characters (list[Character]): Liste des personnages non-joueurs.
    """
    # Constructor
    def __init__(self):
        """
        Initialise les attributs de la classe Game.
        """
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []

    # Setup the game
    def setup(self):
        """
        Configure les éléments nécessaires au jeu, tels que :
        - Les commandes disponibles.
        - Les objets présents dans les salles.
        - Les salles et leurs sorties.
        - Les personnages non-joueurs.
        - L'état initial du joueur.
        """
        # Setup commands
        help = Command("help", " : afficher cette aide", Actions.help, 0)
        self.commands["help"] = help
        quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
        self.commands["quit"] = quit
        go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
        self.commands["go"] = go
        back = Command("back", " : revenir au lieu précédent", Actions.back, 0)
        self.commands["back"] = back
        history = Command("history", " : affiche l'historique des lieux visités", Actions.history, 0)
        self.commands["history"] = history
        look = Command("look", " : regarder les objets dans la pièce", Actions.look, 0)
        self.commands["look"] = look
        take = Command("take", " <objet> : prendre un objet", Actions.take,1)
        self.commands["take"] = take
        drop = Command("drop", " <objet> : reposer un objet", Actions.drop,1)
        self.commands["drop"] = drop
        check = Command("check", " : affiche l'inventaire", Actions.check, 0)
        self.commands["check"] = check
        use = Command("use", " : utilise un item de ton inventaire", Actions.use, 1)
        self.commands["use"] = use
        charge = Command("charge", " : charger un Beamer avec la salle actuelle", Actions.charge, 1)
        self.commands["charge"] = charge
        talk = Command("talk", " : interagir avec un pnj de la meme piece", Actions.talk, 1)
        self.commands["talk"] = talk
        # Setup rooms
        gant_force = Item("gant_force", "des gants donnant une force herculéenne", 10)
        self.items.append(gant_force)
        train = Room("train", "dans le train de l'infini.")
        self.rooms.append(train)
        deguisement = Item("deguisement", "un deguisement rouge et blanc",20)
        self.items.append(deguisement)
        monastere = Room("monastere", "dans un monastère.",deguisement)
        self.rooms.append(monastere)
        village = Room("village", "dans un village.")
        self.rooms.append(village)
        foret = Room("foret", "dans une fôret.")
        self.rooms.append(foret)
        ile_flottante = Room("ile_flottante", "dans une île flottante.")
        self.rooms.append(ile_flottante)
        marche_souterrain = Room("marche_souterrain", "dans un marché souterrain.")
        self.rooms.append(marche_souterrain)
        mine = Room("mine", "dans un champ de mines.")
        self.rooms.append(mine)
        arene = Room("arene", "dans une arène.")
        self.rooms.append(arene)

        # Create exits for rooms
        train.exits = {"N" : None, "E" : None, "S" : village, "O" : None, "U" : ile_flottante, "D" : None}
        monastere.exits = {"N" : None, "E" : village, "S" : None, "O" : None, "U" : None, "D" : marche_souterrain}
        village.exits = {"N" : train, "E" : arene, "S" : None, "O" : monastere, "U" : None, "D" : None}
        foret.exits = {"N" : mine, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        ile_flottante.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : train}
        marche_souterrain.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : monastere, "D" : None}
        mine.exits = {"N" : village, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        arene.exits = {"N" : None, "E" : None, "S" : None, "O" : village, "U" : None, "D" : None}
        # Setup items
        sword = Item("sword", "une épée au fil tranchant comme un rasoir", 3)
        self.items.append(sword)
        foret.inventory.add(sword)
        lampe_torche = Item("lampe_torche", "une lampe torche permettant de voir dans l'obscurité", 1)
        self.items.append(lampe_torche)
        mine.inventory.add(lampe_torche)
        arene.inventory.add(gant_force)
        boite_cle_serrage = Item("boite_cle_serrage", "une boite de clé de serrage",20)
        self.items.append(boite_cle_serrage)
        train.inventory.add(boite_cle_serrage)
        beamer = Beamer("beamer", "Un appareil magique pour se téléporter", 25)
        self.items.append(beamer)
        village.inventory.add(beamer)
        henoch = Item("henoch", "mon petit frère",0)
        self.items.append(henoch)
        marche_souterrain.inventory.add(henoch)
        hercule = Item("hercule", "mon grand frère",0)
        self.items.append(hercule)
        arene.inventory.add(hercule)
        maman = Item("maman", "ma mère",0)
        self.items.append(maman)
        ile_flottante.inventory.add(maman)

        # Setup characters (PNJ)
        marchand = Character("marchand", "un marchand", village, ["Approche, voyageur ! Je t'offre une cape bénie protége ton âme et guideront tes pas !"])
        village.characters[marchand.name] = marchand
        religieux = Character("religieux", "un religieux vêtu d'une longue robe rouge recouvrant le corps jusqu'aux pieds et d'une capuche blanche", monastere, ["Laisse-moi faire ma prière"])
        monastere.characters[religieux.name] = religieux
        ravisseur = Character("ravisseur", "personnage très menaçante", mine, ["ARRETE TOI","Un seul cri, et tu regretteras d’être encore en vie."])
        mine.characters[ravisseur.name] = ravisseur
        villageois = Character("villageois", "Informateur", village, ["Ta famille a été kidnappé !","Henoch se trouve près du monastère et Hercule à l'arène"])
        village.characters[villageois.name] = villageois

        # Setup player and starting room
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = foret


    # Play the game
    def play(self):
        """
        Démarre et gère la boucle principale du jeu.
        Le joueur peut entrer des commandes jusqu'à ce que le jeu soit terminé.
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
            self.endgame()
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Traite une commande saisie par le joueur.

        Args:
            command_string (str): La commande saisie par le joueur.
        """
        #Affiche rien lorsque le joueur tape "entrer"
        if command_string=='':
            return

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")

        command_word = list_of_words[0]

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)
            if command_word != "quit":
                    self.move_characters()
                    pass
    # Print the welcome message
    def print_welcome(self):
        """
        Affiche un message de bienvenue et une introduction au jeu.
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("\nVotre famille ont disparu. Partez à leurs recherches.")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())

    def move_characters(self):
        """
        Déplace aléatoirement un liste de pnj
        """
        for room in self.rooms:
            # Créer une copie de la liste des personnages dans la pièce
            # Liste des personnages à déplacer
            characters_to_move = list(room.characters.values())
            for character in characters_to_move:
                if character.name =="ravisseur" and not character.has_moved:
                    character.move_character()
                    character.has_moved = True
        for room in self.rooms:
            for character in room.characters.values():
                character.has_moved = False

    def endgame(self):
        """
        Conditions de victoire et de défaites
        """
        if self.player.current_room.name == "ile_flottante" and all(item in self.player.inventory for item in ["henoch", "hercule", "maman"]):
            self.finished = True
            print("Vous avez retrouvé votre famille")
            return True
        if self.player.tentative == 2 and not any(item =="deguisement" for item in self.player.inventory):
            self.finished = True
            print("Ta profanation sera lavée dans ton propre sang.")
            return True
        if self.player.move_count > 31 :
            self.finished = True
            print("Le ravisseur vous a kidnappé\n")
            return True
        return False

def main():
    """
    Point d'entrée principal pour exécuter le jeu.
    """
    # Create a game object and play the game
    Game().play()
if __name__ == "__main__":
    main()
