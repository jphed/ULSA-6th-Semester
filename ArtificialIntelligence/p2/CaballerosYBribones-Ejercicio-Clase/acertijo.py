from logic import *

# Definición de símbolos proposicionales
CaballeroA = Symbol("A es un Caballero")
BribonA = Symbol("A es un Bribon")

CaballeroB = Symbol("B es un Caballero")
BribonB = Symbol("B es un Bribon")

CaballeroC = Symbol("C es un Caballero")
BribonC = Symbol("C es un Bribon")

# Reglas generales: cada persona es caballero o bribón, pero no ambos
base_knowledge = And(
    Or(CaballeroA, BribonA),
    Not(And(CaballeroA, BribonA)),
    Or(CaballeroB, BribonB),
    Not(And(CaballeroB, BribonB)),
    Or(CaballeroC, BribonC),
    Not(And(CaballeroC, BribonC))
)

# Acertijo 0: A dice "Soy a la vez un caballero y un bribón"
knowledge0 = And(
    base_knowledge,
    Biconditional(CaballeroA, And(CaballeroA, BribonA))
)

# Acertijo 1: A dice "Los dos somos unos bribones". B no dice nada.
knowledge1 = And(
    base_knowledge,
    Biconditional(CaballeroA, And(BribonA, BribonB))
)

# Acertijo 2: A dice "Somos de la misma clase". B dice "Somos de distinta clase".
knowledge2 = And(
    base_knowledge,
    Biconditional(CaballeroA, Biconditional(CaballeroA, CaballeroB)),
    Biconditional(CaballeroB, Not(Biconditional(CaballeroA, CaballeroB)))
)

# Acertijo 3: 
# A dice "Soy un caballero" o "Soy un bribón"
# B dice "A dijo 'Soy un bribón'" y "C es un bribón"
# C dice "A es un caballero"
knowledge3 = And(
    base_knowledge,
    Biconditional(CaballeroA, Or(CaballeroA, BribonA)),
    Biconditional(CaballeroB, Biconditional(CaballeroA, BribonA)),
    Biconditional(CaballeroB, BribonC),
    Biconditional(CaballeroC, CaballeroA)
)

# Acertijo 4: 
# A dice "O yo soy un bribón, o tanto B como C son caballeros."
# B dice "Exactamente uno de nosotros es un bribón".
# C no dice nada.
knowledge4 = And(
    base_knowledge,
    Biconditional(CaballeroA, Or(BribonA, And(CaballeroB, CaballeroC))),
    Biconditional(CaballeroB, Or(And(CaballeroA, BribonC), And(BribonA, CaballeroC)))
)

# Acertijo 5:
# A dice "Si C es un caballero, entonces B es un bribón."
# B dice "A miente o yo soy un caballero".
# C dice "O todos nosotros somos bribones, o exactamente dos de nosotros son caballeros".
knowledge5 = And(
    base_knowledge,
    Biconditional(CaballeroA, Implication(CaballeroC, BribonB)),
    Biconditional(CaballeroB, Or(Not(CaballeroA), CaballeroB)),
    Biconditional(CaballeroC, Or(And(BribonA, BribonB, BribonC),
                                And(Or(CaballeroA, CaballeroB, CaballeroC), Not(And(CaballeroA, CaballeroB, CaballeroC)))))
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
