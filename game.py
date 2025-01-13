# Description: Game class

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

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.items = []
    
    # Setup the game
    def setup(self):

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

        train = Room("train", "dans le train de l'infini.")
        self.rooms.append(train)
        monastere = Room("monastere", "dans un monastère.")
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
        arene = Room("arene", "dans une arène")
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
        gant_force = Item("gant_force", "des gants donnant une force herculéenne", 10)
        self.items.append(gant_force)
        arene.inventory.add(gant_force)
        boite_cle_serrage = Item("boite_cle_serrage", "une boite de clé de serrage",20)
        self.items.append(boite_cle_serrage)
        train.inventory.add(boite_cle_serrage)
        deguisement = Item("deguisement", "un deguisement rouge et blanc",20)
        self.items.append(deguisement)
        village.inventory.add(deguisement)
        beamer = Beamer("beamer", "Un appareil magique pour se téléporter", 25)
        self.items.append(beamer)
        village.inventory.add(beamer)

        # Setup characters (PNJ)
        marchand = Character("marchand", "un marchand", village, ["Approche, voyageur ! Mes capes bénies protégeront ton âme et guideront tes pas !"])
        village.characters[marchand.name] = marchand
        religieux = Character("religieux", "un religieux vêtu d'une longue robe rouge recouvrant le corps jusqu'aux pieds et d'une capuche blanche", monastere, ["Seuls les élus peuvent franchir ce seuil. Tourne les talons, impur !", "Ta profanation sera lavée dans ton propre sang.", "Bienvenue, frère dans la foi. Que ta dévotion illumine ces lieux sacrés."])
        monastere.characters[religieux.name] = religieux
        Henoch = Character("Henoch", "mon petit frère", monastere, ["Merci grand frère, tu m'as retrouvé"])
        marche_souterrain.characters[Henoch.name] = Henoch
        Hercule = Character("Hercule", "mon grand frère", arene, ["HAHAHA, merci petit frère"])
        arene.characters[Hercule.name] = Hercule
        maman = Character("maman", "ma mère", ile_flottante, ["Mes enfants vous êtes sain et sauf, malheureusement votre père n'est plus là..."])
        ile_flottante.characters[maman.name] = maman
        ravisseur = Character("ravisseur", "personnage très menaçante", mine, ["ARRETE TOI","Un seul cri, et tu regretteras d’être encore en vie."])
        mine.characters[ravisseur.name] = ravisseur

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = foret


    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:

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
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())

    def move_characters(self):
        for room in self.rooms:
            # Créer une copie de la liste des personnages dans la pièce
            characters_to_move = list(room.characters.values())  # Liste des personnages à déplacer
            for character in characters_to_move:
                if character.name =="ravisseur" and not character.has_moved:
                    character.move()
                    character.has_moved = True

        for room in self.rooms:
            for character in room.characters.values():
                character.has_moved = False

    # def some_function():
    #     if DEBUG:
    #         print("DEBUG: Message de débogage dans some_function()")
    #     print("Message normal pour l'utilisateur")
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
