class Character():
    def __init__(self):
        self.name = "Link"
        self.sex = "male"
        self.max_hit_points = 50
        self.current_hit_points = 50
        self.max_speed = 10
        self.armor_amount = 8

character = Character()
print("My name is %s! I'm a %s." % (character.name, character.sex))