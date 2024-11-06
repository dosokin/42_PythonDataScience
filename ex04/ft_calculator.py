class calculator:

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        print(f"Dot product is: {sum(map(lambda a, b: a * b, V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Add Vector is: {[a + b for a, b in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        print(f"Sous Vector is: {[a - b for a, b in zip(V1, V2)]}")

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)