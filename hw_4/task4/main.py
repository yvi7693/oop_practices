from hw_4.task4.model.constants import *
from hw_4.task4.model.entities import *

expelliarmus = Spell("Expelliarmus", DISARMAMENT, 5)
stupefy = Spell("Stupefy", STUN, 15)
avada_kedavra = Spell("Avada Kedavra", DEAD, 30)
protego = Spell("Protego", SHIELD, 5)

harry = HogwartsStudent("Harry Potter", "Gryphendor", [expelliarmus, stupefy, avada_kedavra, protego])
drako = HogwartsStudent("Drako Malfoy", "Slizering", [expelliarmus, stupefy, avada_kedavra, protego])

hogwarts = Hogwarts([harry, drako], [expelliarmus, stupefy, avada_kedavra, protego])
hogwarts.simulate_duel(harry, drako)

if harry.mana <= 0:
    print("Выиграл Драко")

else:
    print("Выиграл Гарри")