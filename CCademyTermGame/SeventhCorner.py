from datetime import datetime
from pydantic import BaseModel, PositiveInt
#Text based adv, broad plan to have 6 factions with 7 territories

class Character():
    def __init__(self, statline, age, name='Vagrant'):
        self.strength = statline['Strength']
        self.dexterity = ['Dexterity']
        self.resolve = statline['Resolve']
        self.charisma = statline['Charisma']
        self.wit = statline['Wit']
        self.composure = statline['Composure']
        self.arcane = statline['Arcane']

        self.age = age
        self.name = name

        self.skills = []

    def add_skill(self, new_skill): #new_skill should be in the form of dictionary, to match other key value pairs
        if new_skill not in self.skills:
            self.skills.append(new_skill)
        elif new_skill[0] != self.skills[new_skill]:
            self.skills[new_skill] = new_skill[0]
        


class Player(Character):
    def __init__(self, statline, name, occupation, reputation, origin, age):
        self.strength = statline['Strength']
        self.dexterity = statline['Dexterity']
        self.resolve = statline['Resolve']
        self.charisma = statline['Charisma']
        self.wit = statline['Wit']
        self.composure = statline['Composure']
        self.arcane = statline['Arcane']

        self.name = name
        self.occupation = occupation
        self.reputation = reputation
        self.origin = origin
        self.age = age

        self.skills = []

    def add_skill(self, new_skill):
        Character.add_skill(self, new_skill)


class Enemy(Character):
    def __init__(self, statline, name, specialization):
        self.strength = statline['Strength']
        self.dexterity = statline['Dexterity']
        self.resolve = statline['Resolve']
        self.charisma = statline['Charisma']
        self.wit = statline['Wit']
        self.composure = statline['Composure']
        self.arcane = statline['Arcane']

        self.name = name
        self.specialization = specialization

        self.skills = []
#----------------------------------------------------------
# Functions
#----------------------------------------------------------

def create_pc():
    print('Fearful of the world? Or too busy justifying its grace? Or rather, do you favor the antiquity of it all?')
    #First line is corny, but I hope to implement it to help choose between 3 ways of deciding stats:
    #Fearful aligns with wanting random choice, Justifying will be set by player, either via rolls or manually.
    #Antiquity will be preset builds that MAY have certain unique bonuses, in some way functioning as challenge runs?
    statline = {'Strength': 0, 'Dexterity': 0 ,'Resolve': 0, 'Charisma': 0, 'Wit': 0, 'Composure': 0, 'Arcane': 0}

    while True:
        try:
            for i in statline:
                statline[i] = int(input('Enter your ' + i + ': '))

            #All "pc" inputs stand for player character
            pc_name = input('And your name? ')
            pc_occupation = input('What is your place in this world? ') #Phrasing this oddly cause I hope to have options rather than free input later
            pc_reputation = 0 #0 is neutral, negative is disliked, positive is liked
            pc_origin = input('Your mind floods in with memories of your past, tell me about them. ') #Again, multiple choice question for later.
            pc_age = int(input('How old are you? ')) #No cap on the number here, but obviously i plan to have one later.
            print('Anything')

            main_pc = Player(statline, str(pc_name), str(pc_occupation), int(pc_reputation), str(pc_origin), int(pc_age))
            main_pc.add_skill('win_button')

            return main_pc
        except ValueError:
            print("Enter a number 0-99, start over.")
        except Exception as e:
            print(e)

        

def create_end_condition():
    statline = {'Strength': 0, 'Dexterity': 0 ,'Resolve': 0, 'Charisma': 0, 'Wit': 0, 'Composure': 0, 'Arcane': 0}
    enemy_name = 'Gatekeeper'

    available_specs = {'Spellsword': ['slash', 'fireball', 'kick']}
    spec_info_list = available_specs['Spellsword'] #Adding more specs later, only basic spellsword setup available for now

    enemy_pc = Enemy(statline, enemy_name, spec_info_list)

    enemy_pc.add_skill('mock')

    return enemy_pc #Currently only setting this up as a function to randomize the end game condition, will add different conditions later

def battle(o_char, d_char): #o_char standing for offensive char, the character that began the engagement. d_char meaning defending character, on the other end of the interaction
    print(o_char.__class__.__name__ + " is engaged with " + d_char.name + ".")

    
def world_draft():
    print('There you were, in battle with your greatest foe that we can conjure at this moment')
    print('There is no other challenge, only that across from you')

    mc = create_pc() #mc meaning main character

    print('Now that you have physical form, escape limbo by force.')

    ec = create_end_condition() #ec meaning end condition

    print('Your opponent is ' + ec.__class__.__name__ + ', simply win the fight.')

    world_begin(mc, ec)

def world_begin(player, end_condition):
    game_state = 'explore'
    while game_state == 'explore':
        player_action = input('What would you like to do? ') 

        #if player_action is in ____ #this will later function as a check on document with listed options for exploring actions, similar to skillset actions

        #for now, change game state to end
        game_state = 'end_condition_win'
    
    print('You have reached the end, will you be remembered?') #Choice, later on, given here will allow the player to select yes or no, and have something be left behind by their character

#----------------------------------------------------------
# Run
#----------------------------------------------------------

world_draft()

