#Text based adv, broad plan to have 6 factions with 7 territories

class Character:
    def __init__(self, heart, strength, dexterity, charisma, wit, spirit, arcane, age, relation="Neutral"):
        self.heart = heart
        self.strength = strength
        self.dexterity = dexterity
        self.charisma = charisma
        self.wit = wit
        self.spirit = spirit
        self.arcane = arcane

        self.age = age
        self.relation = relation

class Player(Character):
    def __init__(self, heart, strength, dexterity, charisma, wit, spirit, arcane, name, occupation, reputation, origin, age):
        self.heart = heart
        self.strength = strength
        self.dexterity = dexterity
        self.charisma = charisma
        self.wit = wit
        self.spirit = spirit
        self.arcane = arcane

        self.name = name
        self.occupation = occupation
        self.reputation = reputation
        self.origin = origin
        self.age = age




def create_pc():
    print("Fearful")

    player_char = Player()