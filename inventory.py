class Inventory:

    def __init__(self):
        self.inventory = set()
        self.poids = 0
        self.max_weight = 5000

    def add(self, item):
        if self.poid + item.weight <= self.max_weight:
            self.inventory[item.name] = item
            self.poid += item.weight
            print(f"{item.name} a été ajouté à l'inventaire.")
            return True
        else:
            print(f"Vous ne pouvez pas ajouter {item.name}, poids maximum dépassé.")
            return False

    def remove(self, item_name):
        if item_name in self.inventory:
            item = self.inventory.pop(item_name)
            self.poids -= item.weight
            print(f"{item_name} a été retiré de l'inventaire.")
        else:
            print(f"{item_name} n'est pas dans l'inventaire.")

    def get_inventory(self):
        if len(self.inventory) > 0:
            print("\nLa pièce contient :")
            for name, item in self.inventory.items():
                print(f"    - {name} : {item.description} ({item.weight} g)")
        else:
            print("\nIl y a rien ici.")