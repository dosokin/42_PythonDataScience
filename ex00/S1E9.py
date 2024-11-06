from abc import ABC, abstractmethod


class Character(ABC):

    """Character class, instanciate with *first_name*"""

    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """init a character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """make the character die"""
        if self.is_alive:
            self.is_alive = False
            return f"{self.first_name} is now dead."
        return f"{self.first_name} is already dead."


class Stark(Character):

    """Stark, just a kind of character"""

    def __init__(self, first_name, is_alive=True):
        """init stark"""
        Character.__init__(self, first_name, is_alive)
