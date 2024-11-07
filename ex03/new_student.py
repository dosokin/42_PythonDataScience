import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name, surname) -> str:
    return "".join([name[0], surname])


@dataclass
class Student:
    name: str
    surname: str

    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        self.login = generate_login(self.name, self.surname)
