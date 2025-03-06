import termcolor
from logic import *

mostaza = Symbol('Mostaza')
moradillo = Symbol('Moradillo')
escarlata = Symbol('Escarlata')

personajes = [mostaza, moradillo, escarlata]

billar = Symbol('Billar')
cocina = Symbol('Cocina')
biblioteca = Symbol('Biblioteca')

lugares = [billar, cocina, biblioteca]

llave = Symbol('Llave')
cuchillo = Symbol('Cuchillo')
pistola = Symbol('Pistola')

armas = [llave, cuchillo, pistola]

simbolos = personajes + lugares + armas

def check_knowledge(knowledge):
    for simbolo in simbolos:
        if model_check(knowledge, simbolo):
            termcolor.cprint(f"{simbolo}: Yes", 'green')
        elif not model_check(knowledge, Not(simbolo)):
            termcolor.cprint(f"{simbolo}: Maybe")

knowledge = And(
    Or(mostaza, moradillo, escarlata),
    Or(billar, cocina, biblioteca),
    Or(llave, cuchillo, pistola),
)

knowledge.add(Not(mostaza))
knowledge.add(Not(cocina))
knowledge.add(Not(pistola))

knowledge.add(Or(
    Not(mostaza),
    Not(biblioteca),
    Not(llave),
))

knowledge.add(Or(
    Not(moradillo),
    Not(billar),
    Not(cuchillo),
))

knowledge.add(Or(
    Not(escarlata),
    Not(billar),
    Not(cuchillo),
))

knowledge.add(Or(  
    And(moradillo, billar, llave),
    And(escarlata, cocina, cuchillo)
))

print(knowledge.formula())

check_knowledge(knowledge)
