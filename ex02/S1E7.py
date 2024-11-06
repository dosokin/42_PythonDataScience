from S1E9 import Character


class Baratheon(Character):

    """Representing the Baratheon family"""

    def __init__(self, first_name, is_alive=True):
        """init Baratheon"""
        self.first_name = first_name
        self.is_alive = is_alive

        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def __str__(self):
        """human-readable display of elements in class"""
        return (f"First name => {self.first_name}"
                f"Alive      => {self.is_alive}"
                f"Family name=> {self.family_name}"
                f"Eyes       => {self.eyes}"
                f"Hairs      => {self.eyes}")

    def __repr__(self):
        """display of elements in class"""
        elements = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {elements}"


class Lannister(Character):

    """Representing the Lannister family"""

    def __init__(self, first_name, is_alive=True):
        """init Lannister"""
        self.first_name = first_name
        self.is_alive = is_alive

        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def __str__(self):
        """human-readable display of elements in class"""
        return (f"First name => {self.first_name}"
                f"Alive      => {self.is_alive}"
                f"Family name=> {self.family_name}"
                f"Eyes       => {self.eyes}"
                f"Hairs      => {self.eyes}")

    def __repr__(self):
        """display of elements in class"""
        elements = (self.family_name, self.eyes, self.hairs)
        return f"Vector: {elements}"

    def create_lannister(first_name: str, is_alive=True):
        """create a lannister"""

        return Lannister(first_name, is_alive)
