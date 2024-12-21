class Unit:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def take_damage(self, damage):
        self.health -= damage

    
    def deal_damage(self, enemy):
        enemy.take_damage(self.damage)