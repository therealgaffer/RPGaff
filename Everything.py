import random
import weakref

class Creature:

    creatures = set()
    name = None

    def __init__(self, name, race, max_health, attack, defence):
        self.name = name
        self.race = race
        self.max_health = max_health
        self.attack = attack
        self.defence = defence
        self.creatures.add(weakref.ref(self))

    def attack_target(self, target):

        # Calculate the chance of attacker hitting the defender
        def calculate_hit(attacker, defender):

            # Formula for deciding hit chance
            hit_percent = round((attacker.attack / (attacker.attack + defender.defence * 0.25) * 0.95) * 100, 1)
            print (
                "{}'s attack is {} and {}'s defence is {} meaning a {}% chance to hit".format(
                    attacker.name, attacker.attack, defender.name, defender.defence, hit_percent
                )
            )

            # Roll a random integer between 1-100, success if integer is within chance to hit %
            randint = random.randint(1, 100)
            print ("Random roll = {}".format(randint))
            if randint < hit_percent:
                print ("{} sucessfully lands a hit on {}!".format(attacker.name, defender.name))
            else:
                print ("{} misses their swing at {}!".format(attacker.name, defender.name))

        #When attacking, attacker needs a target:
        self.target = target

        # Calculate attack and then counter-attack
        print ("{} attacks {}!".format(self.name, target.name))
        calculate_hit(self, target)

        print ("{} counter-attacks!".format(target.name))
        calculate_hit(target, self)


def name_yourself():
    self_name = raw_input("What is your name?")
    print ("Your name is now {}".format(self_name))
    return self_name

def pick_race():

    while True:
        answer = raw_input("What race are you? [H, O, E, D]")
        if answer not in ("H", "O", "E", "D"):
            print ("{} Is not an available race. Please pick again".format(answer))
        else:
            break
    if answer == "H":
        return "Human"
    elif answer == "O":
        return "Orc"
    elif answer == "E":
        return "Elf"
    elif answer == "D":
        return "Dwarf"

races = ["Human", "Orc", "Elf", "Dwarf"]

PC = Creature(name_yourself(), pick_race(), random.randint(80, 120), random.randint(20, 30), random.randint(20, 30))
NPC = Creature("Nameless NPC", random.choice(races), random.randint(80, 120), random.randint(1, 20), random.randint(1, 15))

print ("Player race: {} attack:{} defence:{}".format(PC.race, PC.attack, PC.defence))
print ("Monster race: {} attack:{} defence:{}".format(NPC.race, NPC.attack, NPC.defence))

PC.attack_target(NPC)
