from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):

    """representing the king"""

    def __init__(self, first_name: str, is_alive=True):
        """init king"""
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color: str):
        """change eyes color"""
        self.eyes = color

    def set_hairs(self, color: str):
        """change hairs color"""
        self.hairs = color

    def get_eyes(self):
        """get eye color"""
        return self.eyes

    def get_hairs(self):
        """get hair color"""
        return self.hairs
