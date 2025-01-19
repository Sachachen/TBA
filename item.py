"""
Module représentant la classe Item.

Ce module définit la classe `Item`, qui représente un objet pouvant être
utilisé ou transporté dans le jeu.

Classes :
    - Item : Représente un objet avec un nom, une description et un poids.
"""
class Item:
    """
    Représente un objet dans le jeu.

    Attributs :
        name (str) : Le nom de l'objet.
        description (str) : Une description de l'objet.
        weight (float) : Le poids de l'objet en kilogrammes.
    """
    # Désactivation de la règle "trop peu de méthodes publiques"
    # pylint: disable=too-few-public-methods

    # Define the constructor.
    def __init__(self, name, description, weight):
        """
        Initialise un objet Item.

        Args :
            name (str) : Le nom de l'objet.
            description (str) : Une description de l'objet.
            weight (float) : Le poids de l'objet en grammes.
        """
        self.name = name
        self.description = description
        self.weight = weight

    # The string representation of the command.
    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'objet.

        Returns :
            str : Une description formatée de l'objet, incluant son nom, sa description
                  et son poids.
        """
        return f"{self.name} : {self.description} ({self.weight} kg)"
