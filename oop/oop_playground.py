
class Character(object):
    def __init__(self, char_class, attack_power, hit_points):
        self.char_class = char_class
        self.attack_power = attack_power
        self.hit_points = hit_points

    def take_damage(self, damage):
        self.hit_points = self.hit_points - damage

    def gain_health(self, health):
        self.hit_points = self.hit_points + health

    def attack(self, target: object):
        target.take_damage(self.attack_power)


mage = Character("mage", 30, 150)
knight = Character("mage", 40, 200)

# Mage attacks Knight
print(knight.hit_points)
mage.attack(knight)
print(knight.hit_points)



