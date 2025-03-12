import termcolor
from logic import *

personas = [
    Symbol('Doctor Verde'),
    Symbol('Miss Scarlet'),
    Symbol('Profesor Mostaza'),
    Symbol('Sra. Blanco'),
    Symbol('Coronel Mostaza'),
    Symbol('Sra. Púrpura'),
    Symbol('Señorita Rosa'),
    Symbol('Señor Azul'),
    Symbol('Sr. Marrón'),
    Symbol('Capitán Naranja')
]

lugares = [
    Symbol('Salón'),
    Symbol('Cocina'),
    Symbol('Biblioteca'),
    Symbol('Comedor'),
    Symbol('Jardín'),
    Symbol('Pasillo'),
    Symbol('Vestíbulo'),
    Symbol('Estudio'),
    Symbol('Sala de Música'),
    Symbol('Invernadero')
]

armas = [
    Symbol('Cuchillo'),
    Symbol('Pistola'),
    Symbol('Cuerda'),
    Symbol('Veneno'),
    Symbol('Revolver'),
    Symbol('Bate'),
    Symbol('Hacha'),
    Symbol('Pica'),
    Symbol('Llave'),
    Symbol('Candelabro')
]

simbolos = personas + lugares + armas

def check_knowledge(knowledge):
    for simbolo in simbolos:
        if model_check(knowledge, simbolo):
            termcolor.cprint(f"{simbolo}: Yes", 'green')
        elif not model_check(knowledge, Not(simbolo)):
            termcolor.cprint(f"{simbolo}: Maybe", 'yellow')

knowledge = And(
    Or(*personas),
    Or(*lugares),
    Or(*armas),
)

knowledge.add(Not(personas[0]))  # Doctor Verde no es el culpable
knowledge.add(Not(lugares[0]))   # Salón no fue el escenario
knowledge.add(Not(armas[0]))     # Cuchillo no fue el arma utilizada

knowledge.add(Or(
    Not(personas[0]),
    Not(lugares[1]),
    Not(armas[1]),
))

knowledge.add(Or(
    Not(personas[1]),
    Not(lugares[2]),
    Not(armas[2]),
))

knowledge.add(Or(
    Not(personas[2]),
    Not(lugares[3]),
    Not(armas[3]),
))

knowledge.add(Or(
    Not(personas[3]),
    Not(lugares[4]),
    Not(armas[4]),
))

knowledge.add(Or(
    Not(personas[4]),
    Not(lugares[5]),
    Not(armas[5]),
))

knowledge.add(Or(
    Not(personas[5]),
    Not(lugares[6]),
    Not(armas[6]),
))

knowledge.add(Or(
    Not(personas[6]),
    Not(lugares[7]),
    Not(armas[7]),
))

knowledge.add(Or(
    Not(personas[7]),
    Not(lugares[8]),
    Not(armas[8]),
))

knowledge.add(Or(
    Not(personas[8]),
    Not(lugares[9]),
    Not(armas[9]),
))

knowledge.add(Or(  
    And(personas[0], lugares[1], armas[2]),
    And(personas[1], lugares[3], armas[4]),
    And(personas[2], lugares[5], armas[6]),
    And(personas[3], lugares[6], armas[7]),
    And(personas[4], lugares[7], armas[8]),
))

knowledge.add(Or(  
    Not(personas[5]),  # Sra. Púrpura no estuvo en la Cocina
    Not(lugares[1]),
    Not(armas[0]),
))

knowledge.add(Or(  
    Not(personas[6]),  # Señorita Rosa no estuvo en el Estudio
    Not(lugares[7]),
    Not(armas[3]),
))

knowledge.add(Or(  
    Not(personas[7]),  # Señor Azul no estuvo en el Vestíbulo
    Not(lugares[6]),
    Not(armas[4]),
))

knowledge.add(Or(  
    Not(personas[8]),  # Sr. Marrón no estuvo en la Biblioteca
    Not(lugares[2]),
    Not(armas[5]),
))

knowledge.add(Or(  
    Not(personas[9]),  # Capitán Naranja no estuvo en el Comedor
    Not(lugares[3]),
    Not(armas[6]),
))

print(knowledge.formula())

check_knowledge(knowledge)
