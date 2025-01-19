from item import Item
"""
Module beamer

Ce module contient la méthode d'un item capable de nous téléporter

Chaque méthode d'action prend les paramètres suivants :
- 'game': L'objet représentant l'état actuel du jeu.
- 'list_of_words': La liste des mots constituant la commande saisie.
- 'number_of_parameters': Le nombre de paramètres attendu pour la commande.

Les méthodes vérifient si le nombre de paramètres est correct et effectuent une action
appropriée dans le jeu (par exemple, déplacer le joueur, prendre un objet, ou quitter le jeu).

Messages d'erreur :
- Les messages pour les erreurs de paramètres sont stockés dans les constantes 'MSG0' et 'MSG1'.

Classes :
- 'Actions': Contient toutes les méthodes statiques pour exécuter les commandes du joueur.

Constantes :
- 'MSG0': Message d'erreur pour les commandes ne prenant pas de paramètres.
- 'MSG1': Message d'erreur pour les commandes prenant exactement un paramètre.
"""

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
