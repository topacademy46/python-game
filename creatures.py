from unit import *
import random
 
class Dragon(Unit):
    def __init__(self, name, health, damage, armor, crit_counter):
        super().__init__(name, health, damage, armor)
        self.crit_counter = 0
        self.crit_counter = crit_counter
        self.crit_counter += 1
        if self.crit_counter == 3:
            Dragon.deal_damage(self.damage * 1.5)
            self.crit_counter = 0
 
 
 
class Ogre(Unit):
    def __init__(self, name, health, damage, armor, evasion):
        super().__init__(name, health, damage, armor)
        self.evasion = evasion

class Rat(Unit):
    def __init__(self, name, health, damage, armor, block):
        super().__init__(name, health, damage, armor)
        self.block = block

    def take_damage(self, damage):
        if random.randint (1, 100) >= 33:
            self.health -= damage