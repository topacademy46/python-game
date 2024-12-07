from unit import *
 
class Hero (Unit):
    def __init__(self, name, health = 100, damage = 1, armor = 1, evasion = 1):
        super().__init__(name, health, damage, armor)
        self.evasion = evasion