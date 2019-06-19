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

        if self.race == "Orc":
            self.max_health *= 1.5
            self.attack *= 1.8
            self.defence *= 0.6
        elif self.race == "Elf":
            self.max_health *= 0.8
            self.attack *= 1.6
            self.defence *= 1.6
        elif self.race == "Human":
            self.max_health *= 1
            self.attack *= 1.2
            self.defence *= 1.0
        elif self.race == "Dwarf":
            self.max_health *= 1.8
            self.attack *= 0.7
            self.defence *= 1.8

        self.current_health = self.max_health


    def attack_target(self, target):

        # Roll damage and apply to targets health
        def take_health(x):
            damage = random.randint(1, 20)
            x.current_health -= damage
            print("{} is it for {}. Remaining health: {}".format(x.name, damage, x.current_health))

        # Calculate the chance of attacker hitting the defender
        def calculate_hit(attacker, defender):

            # Formula for deciding hit chance
            hit_percent = round((attacker.attack / (attacker.attack + defender.defence * 0.25) * 0.8) * 100, 1)
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
                take_health(defender)
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
names = ["Barry", "Luke", "Mike"]

# Make a couple of characters
PC = Creature(
    name_yourself(),
    pick_race(),
    float(random.randint(80, 100)),
    float(random.randint(30, 50)),
    float(random.randint(30, 50))
)
NPC = Creature(
    "{} the NPC".format(random.choice(names)),
    random.choice(races),
    float(random.randint(80, 100)),
    float(random.randint(30, 50)),
    float(random.randint(30, 50))
)

print ("Player race: {} attack:{} defence:{} hp:{}/{}".format(PC.race, PC.attack, PC.defence, PC.max_health, PC.current_health))
print ("Monster race: {} attack:{} defence:{} hp:{}/{}".format(NPC.race, NPC.attack, NPC.defence, NPC.max_health, NPC.current_health))

# Game Loop
while True:

    while True:
        answer = raw_input("Would you like to Attack, or Quit? [A, Q]")
        if answer not in ("A", "Q"):
            print ("Please answer A or Q")
        else:
            break

    if answer == "A":
        PC.attack_target(NPC)

        print ("{} hp:{}/{}".format(PC.name, PC.current_health, PC.max_health))
        print ("{} hp:{}/{}".format(PC.name, NPC.current_health, NPC.max_health))

    else:
        print ("Alright FINE, BYE")
        break