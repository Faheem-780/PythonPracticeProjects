import abc
import random

class Player(abc.ABC):
    """Abstract class defining the player."""
    def __init__(self) -> None:
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self) -> tuple:
        # 10. Use random.choice to get a random move
        move = random.choice(self.moves)
        
        # 11. Update position by adding move coordinates
        new_position = (self.position[0] + move[0], self.position[1] + move[1])
        self.position = new_position
        
        # 12. Append new position to path
        self.path.append(self.position)
        
        # 13. Return the updated position
        return self.position
    
    @abc.abstractmethod
    def level_up(self) -> None:
        pass

class Pawn(Player):
    def __init__(self):
        # 22. Call parent __init__ using super
        super().__init__()
        # 23. Set moves for up, down, left, right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # 25. Add diagonal movements
        self.moves += [(1, 1), (1, -1), (-1, -1), (-1, 1)]