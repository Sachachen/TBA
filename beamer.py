# beamer.py

from item import Item

class Beamer(Item):
    def __init__(self, name, description, weight, teleport_room=None):
        super().__init__(name, description, weight)
        self.teleport_room = teleport_room  # La salle où le Beamer peut téléporter

    def use(self, game):
        """
        Utiliser le Beamer pour téléporter le joueur.
        """
        if self.teleport_room:
            print(f"Vous êtes téléporté dans la salle : {self.teleport_room.name}.")
            game.player.current_room = self.teleport_room
            game.player.history.append(game.player.current_room)
            print(game.player.current_room.get_long_description())
            game.player.get_history()
            return True
        else:
            print("Le Beamer n'est pas chargé avec une destination.")
            return False

    def charge(self, current_room):
        """
        Charger le Beamer avec la salle actuelle.
        """
        self.teleport_room = current_room
        print(f"Le Beamer est maintenant chargé avec la salle : {current_room.name}.")