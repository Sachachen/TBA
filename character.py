import random
from player import Player
from debug import DEBUG

class Character(Player):

    def __init__(self, name, description, current_room, msgs):
        self.name = name
        self.description = description
        self.current_room = current_room
        self.msgs = msgs
        self.has_moved = False

    def __str__(self):
        return f" {self.name} : {self.description}"  
    
    def move_realisable(self):
        result = random.choice([True, False])
        return result

    def move(self):  
        if self.move_realisable():
            direction = random.choice([key for key, value in self.current_room.exits.items() if value is not None])
            next_room = self.current_room.exits[direction]

            if self.name in self.current_room.characters:
                del self.current_room.characters[self.name]
                next_room.characters[self.name] = self
                self.current_room = next_room
                if DEBUG:
                    print(f"{self.name} a été déplacé vers {next_room.name}")           
            return True  # Le mouvement a eu lieu
        else:
            print(f"{self.name} n'a pas bougé.")
         
    def get_msg(self):
        msg = self.msgs.pop(0)
        self.msgs.append(msg)
        return msg
    