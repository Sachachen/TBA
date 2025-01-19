"""
Module représentant la classe Iventory.

Ce module définit la classe `Iventory`, qui représente un objet pouvant être
utilisé ou transporté dans le jeu.

Classes :
    - Inventory : Représente un objet avec un nom, une description et un poids.
"""
class Inventory:
    """
    Représente un objet dans le jeu.

    Attributs :
        name (str) : Le nom de l'objet.
        description (str) : Une description de l'objet.
        weight (float) : Le poids de l'objet en kilogrammes.
    """
    def __init__(self):
        """
        Initialise un objet Item.

        Args :
            inventory (set) : Item.
            poids (float) : Notre poids.
            weight (float) : Le poids de l'objet en kilo.
        """
        self.inventory = set()
        self.poids = 0
        self.max_weight = 5000

    def add(self, item):
        """
        Ajouter un objet.
        """
        if self.poids + item.weight <= self.max_weight:
            self.inventory[item.name] = item
            self.poids += item.weight
            print(f"{item.name} a été ajouté à l'inventaire.")
            return True
        print(f"Vous ne pouvez pas ajouter {item.name}, poids maximum dépassé.")
        return False

    def remove(self, item_name):
        """
        Retirer un objet.
        """
        if item_name in self.inventory:
            item = self.inventory.pop(item_name)
            self.poids -= item.weight
            print(f"{item_name} a été retiré de l'inventaire.")
        else:
            print(f"{item_name} n'est pas dans l'inventaire.")

    def get_inventory(self):
        """
        Regarder si un objet est présent dans la pièce.
        """
        if len(self.inventory) > 0:
            print("\nLa pièce contient :")
            for name, item in self.inventory.items():
                print(f"    - {name} : {item.description} ({item.weight} g)")
        else:
            print("\nIl y a rien ici.")
