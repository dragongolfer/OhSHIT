import random

class Player:
    #creates player object based on character specified by user input
    def __init__(self,name,character):
        self.health = 100

        #assigns name associated to new player
        self.name = name

        #initializes empty powerup list
        self.powerups = []

        #powerup count will count up to 3 and reset to 0 on three successful hits
        self.powerup_count = 0

        #assigns character entered by player
        self.character = character

        #generates weapon list
        self.weapons = self.get_character_weapons(character)
        
        #don't think we need the next three lines but there just in case we want to use.
        self.power_add = False
        self.increaseHit_add = False
        self.armor_add = False

        #next three values are true or false based on if they have been activated by player using powerup
        self.increaseHit_active = False
        self.armor_active = False
        self.power_active = False

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

    def get_weapons(self):
        return self.weapons
        
    def get_name(self):
        return self.name
    
    #updates the health to 100%.
    def setFullHealth(self):
        self.health  = 100
        return self.health

    #gets attack value based on character weapon choosen from dictionary(weapon_list)
    def get_attack_damage(self,weapon):
        ###Add stuff for checking if you have a powerUp
        weapon_attack = self.weapons[weapon][0]
        return weapon_attack

    #gets probability of success from character weapon choosen from dictionary(weapon_list)
    def get_attack_probability(self,weapon):
        ###Add stuff for checking if you have a powerUp
        weapon_prob = self.weapons[weapon][1]
        return weapon_prob


class Weapon:
	def __init__(self,name,attack,percent):
		self.name = name
		self.attack_value = attack
		self.percent = percent

    #toggles armor powerup to true or false based on previous value
    def change_armor(self):
        if self.armor_active == False:
            self.armor_active = True
        else:
            self.armor_active = False
    
    #toggles change_increase_hit powerup to true or false based on previous value
    def change_increase_hit(self):
        if self.increaseHit_active == False:
            self.increaseHit_active = True
        else:
            self.increaseHit_active = False

    #toggles update power powerup to true or false based on previous value
    def update_power(self):
        if self.power_active == False:
            self.power_active = True
        else:
            self.power_active = False
  
    #uses powerup and changes powerup status to active, else prints none available
    def use_power_up(self,powerup_choice):
        power_up_length = len(self.powerups)
        if power_up_length > 0:
            if powerup_choice == "Power":
                self.update_power()
            elif powerup_choice == "Armor":
                self.change_armor()
            else:
                self.change_increase_hit()
        else:
            print "No powerup available."

    #retrieves damage and probability potential of hit from weapon given
    #a random number is generated and if that number is less than the probability, a hit is awarded.
    #damage is then returned, else 0 damage is returned.
    def attack(self,weapon, powerUp):

        attack_damage = self.get_attack_damage(weapon)
        attack_probability = self.get_attack_probability(weapon)*100
        print "attack Probability", attack_probability
        attack_win = random.randrange(0,101)
        print "Attack Win", attack_win
        if attack_win < attack_probability:
            return attack_damage
        else:
            return 0
            
    def damagePlayer(self, amount):
        ###Add stuff for checking if you have an armor powerup
        self.health -= amount
        return


class Weapon:
    def __init__(self,name,attack,percent):
        self.name = name
        self.attack_value = attack
        self.percent = percent