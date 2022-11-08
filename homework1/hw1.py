class Hero:
    Head = 1
    Ability = True

    def __init__(self, name, nickname, hp, damage):
        self.name = name
        self.nickname = nickname
        self.hp = hp
        self.damage = damage

    def heal(self):
        self.hp += 100

    def two_damage(self):
        self.damage *= 2

    def greetins(self):
        print('my name is', self.name)

    def brand_phrase(self):
        print('good will win')


hero1 = Hero('Kudret', 'no name', 100, 60)
hero2 = Hero('Asyl', 'asyl312', 58, 24)
hero3 = Hero('Stas', 'zodiak', 120, 40)
hero4 = Hero('Andrey', 'ZaDyRa321', 120, 40)

hero1.heal()
hero2.two_damage()
hero3.greetins()
hero4.brand_phrase()