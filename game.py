# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions

class Game:

    # Constructor
    def __init__(self):
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
    
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
        
        # Setup rooms

        train = Room("train", "au train de l'infini.")
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
        arene = Room("arene", "à l'arène")
        self.rooms.append(arene)

        # Create exits for rooms

        train.exits = {"N" : None, "E" : None, "S" : village, "O" : None, "U" : ile_flottante, "D" : None}
        monastere.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : marche_souterrain}
        village.exits = {"N" : train, "E" : arene, "S" : None, "O" : monastere, "U" : None, "D" : None}
        foret.exits = {"N" : mine, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        ile_flottante.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : None, "D" : train}
        marche_souterrain.exits = {"N" : None, "E" : None, "S" : None, "O" : None, "U" : monastere, "D" : None}
        mine.exits = {"N" : village, "E" : None, "S" : None, "O" : None, "U" : None, "D" : None}
        arene.exits = {"N" : None, "E" : None, "S" : None, "O" : village, "U" : None, "D" : None}
        
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

    # Print the welcome message
    def print_welcome(self):
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        #
        print(self.player.current_room.get_long_description())
    

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
