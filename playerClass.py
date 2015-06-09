import random

class Player:
    #creates player object based on character specified by user input
    def __init__(self,character):
        self.health = 100
        #initializes empty powerup list
        self.powerups = []
        #powerup count will count up to 3 and reset to 0
        self.powerup_count = 0
        self.character = character
        #generates weapon list
        self.weapons = self.get_character_weapons(character)
        #self.power_add = False - don't need right now because of add_powerup_count()
        self.increaseHit_add = False
        self.armor_add = False
        self.armor_active = False

    #generates weapon list based on character selected. example: if character is granola then Ruler Slap will induce
    #20 damage points with a probability rate of 75%.
    def get_character_weapons(self,character):
        if self.character == "granola":
            weapon_list = {"Ruler Slap":[20,.75],"Rubber Band Shot":[5,.95],"Poison":[50,.25],"Catapult":[40,.50]}
            return weapon_list
        elif self.character == "notebook":
            weapon_list = {"Ruler Slap":[20,.75],"Rubber Band Shot":[5,.95],"Paper Cut":[50,.25],"Wire Skewer":[40,.50]}
            return weapon_list
        elif self.character == "backpack":
            weapon_list = {"Ruler Slap":[20,.75],"Rubber Band Shot":[5,.95],"Slam":[50,.25],"Strap Choke": [40,.50]}
            return weapon_list
        elif self.character == "computer":
            weapon_list = {"Ruler Slap":[20,.75],"Rubber Band Shot":[5,.95],"Self Destruct": [50,.25],"CD Launcher": [40,.50]}
            return weapon_list
        else:
            weapon_list =  {"Ruler Slap":[20,.75],"Rubber Band Shot":[5,.95]}
            return weapon_list

    #when called, will choose a power up and assign it to the player and reset variable to 0.
    def add_powerup_count(self):
        self.powerup_count = self.powerup_count + 1
        if self.powerup_count == 3:
            new_power_up = random.choice(["Armor", "Power", "Hit"])
            self.powerups.append(new_power_up)
            self.powerup_count = 0

    def get_health(self):
        return self.health

    def get_powerups(self):
        return self.powerups

    def get_weapons():
    	return self.weapons
    
    updates the health based on if damage is incurred or a power up is taken. damage keyword can be changed.
    def update_health(self,type_health,amount_health):
        if type_health == "damage":
    	    self.health -= amount_health
    	    return self.health
    	else:
    		self.health  = amount_health
    		return self.health

    #gets attack value based on character weapon choosen from dictionary(weapon_list)
    def get_attack_damage(self,weapon):
    	weapon_attack = self.weapons[weapon][0]
    	return weapon_attack
    #ets probability of success from character weapon choosen from dictionary(weapon_list)
    def get_attack_probability(self,weapon):
        weapon_prob = self.weapons[weapon][1]
        return weapon_prob

class Weapon:
	def __init__(self,name,attack,percent):
		self.name = name
		self.attack_value = attack
		self.percent = percent


#checking calls to see class is working properly
player1 = raw_input("Select a character: ")
player1 = Player(player1)
player1_weapons = []
for weapon in player1.weapons:
    player1_weapons.append(weapon)
print player1_weapons

player1.add_powerup_count()
player1.add_powerup_count()
player1.add_powerup_count()
print player1.get_health()
print player1.get_attack_damage("Ruler Slap")
print player1.get_attack_probability("Ruler Slap")