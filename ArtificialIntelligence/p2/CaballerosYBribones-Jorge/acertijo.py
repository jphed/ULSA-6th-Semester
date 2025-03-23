from logic import *

CaballeroA = Symbol("A es un Caballero")
BribonA = Symbol("A es un Bribon")

CaballeroB = Symbol("B es un Caballero")
BribonB = Symbol("B es un Bribon")

CaballeroC = Symbol("C es un Caballero")
BribonC = Symbol("C es un Bribon")

# Acertijo 0
#  A dice: "Soy a la vez caballero y bribón".
knowledge0 = And(
    Or(CaballeroA, BribonA),
    Not(And(CaballeroA, BribonA)),
    Implication(CaballeroA, And(CaballeroA, BribonA)),
    Implication(BribonA, Not(And(CaballeroA, BribonA)))
)

# Acertijo 1: A dice "Los dos somos unos bribones". B no dice nada.
knowledge1 = And(
    Or(CaballeroA, BribonA),
    Or(CaballeroB, BribonB),
    Not(And(CaballeroA, BribonA)),
    Not(And(CaballeroB, BribonB)),
    Implication(CaballeroA, And(BribonA, BribonB)),
    Implication(BribonA, Not(And(BribonA, BribonB)))
)

# Acertijo 2: A dice "Somos de la misma clase". B dice "Somos de distinta clase".
knowledge2 = And(
    Or(CaballeroA, BribonA),
    Or(CaballeroB, BribonB),
    Not(And(CaballeroA, BribonA)),
    Not(And(CaballeroB, BribonB)),
    Implication(CaballeroA, Or(And(CaballeroA, CaballeroB), And(BribonA, BribonB))),
    Implication(BribonA, Not(Or(And(CaballeroA, CaballeroB), And(BribonA, BribonB)))),
    Implication(CaballeroB, Or(And(CaballeroA, BribonB), And(BribonA, CaballeroB))),
    Implication(BribonB, Not(Or(And(CaballeroA, BribonB), And(BribonA, CaballeroB))))
)

# Acertijo 3
# A dice "Soy un caballero" o  "Soy un bribón", pero no sabes cuál.
# B dice "A dijo “Soy un bribón” y "C es un bribón".
# C dice "A es un caballero.""
knowledge3 = And(
    Or(CaballeroA, BribonA),
    Or(CaballeroB, BribonB),
    Or(CaballeroC, BribonC),
    Not(And(CaballeroA, BribonA)),
    Not(And(CaballeroB, BribonB)),
    Not(And(CaballeroC, BribonC)),
    Implication(CaballeroA, Or(CaballeroA, BribonA)),
    Implication(BribonA, Not(Or(CaballeroA, BribonA))),
    Implication(CaballeroB, BribonA),
    Implication(BribonB, Not(BribonA)),
    Implication(CaballeroB, BribonC),
    Implication(BribonB, Not(BribonC)),
    Implication(CaballeroC, CaballeroA),
    Implication(BribonC, Not(CaballeroA))
)

# Acertijo 4
# A dice: "O yo soy un bribón, o tanto B como C son caballeros.""
# B dice: "Exactamente uno de nosotros es un bribón"
# C no dice nada.
knowledge4 = And(
    Or(CaballeroA, BribonA),
    Or(CaballeroB, BribonB),
    Or(CaballeroC, BribonC),
    Not(And(CaballeroA, BribonA)),
    Not(And(CaballeroB, BribonB)),
    Not(And(CaballeroC, BribonC)),
    Implication(CaballeroA, Or(BribonA, And(CaballeroB, CaballeroC))),
    Implication(BribonA, Not(Or(BribonA, And(CaballeroB, CaballeroC)))),
    Implication(CaballeroB, Or(And(CaballeroA, BribonB), And(BribonA, CaballeroB))),
    Implication(BribonB, Not(Or(And(CaballeroA, BribonB), And(BribonA, CaballeroB))))
)

# Acertijo 5:
# A dice "Si C es un caballero, entonces B es un bribón."
# B dice "A miente o yo soy un caballero".
# C dice "O todos nosotros somos bribones, o exactamente dos de nosotros son caballeros".
knowledge5 = And(
    Or(CaballeroA, BribonA),
    Or(CaballeroB, BribonB),
    Or(CaballeroC, BribonC),
    Not(And(CaballeroA, BribonA)),
    Not(And(CaballeroB, BribonB)),
    Not(And(CaballeroC, BribonC)),
    Implication(CaballeroA, Implication(CaballeroC, BribonB)),
    Implication(BribonA, Not(Implication(CaballeroC, BribonB))),
    Implication(CaballeroB, Or(Not(CaballeroA), CaballeroB)),
    Implication(BribonB, Not(Or(Not(CaballeroA), CaballeroB))),
    Implication(CaballeroC, Or(And(BribonA, BribonB, BribonC), And(CaballeroA, CaballeroB, Not(CaballeroC)))),
    Implication(BribonC, Not(Or(And(BribonA, BribonB, BribonC), And(CaballeroA, CaballeroB, Not(CaballeroC)))))
)

def main():
    simbolos = [CaballeroA, BribonA, CaballeroB, BribonB, CaballeroC, BribonC]
    acertijos = [
        ("Acertijo 0", knowledge0),
        ("Acertijo 1", knowledge1),
        ("Acertijo 2", knowledge2),
        ("Acertijo 3", knowledge3),
        ("Acertijo 4", knowledge4),
        ("Acertijo 5", knowledge5)
    ]
    for acertijo, knowledge in acertijos:
        print(acertijo)
        if len(knowledge.conjuncts) == 0:
            print("    No implementado.")
        else:
            for simbolo in simbolos:
                if model_check(knowledge, simbolo):
                    print(f"    {simbolo}")


if __name__ == "__main__":
    main()