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
        self.armor_active = False #not using anymore in the game but again here in case we want to change how armor operates
        self.increase_chance_active = False

    #generates weapon list based on character selected. example: if character is granola then Ruler Slap will induce
    #10 damage points with a probability rate of 75%.
    def get_character_weapons(self,character):
        if self.character == "granola":
            weapon_list = {"Ruler Slap":[10,.75],"Rubber Band Shot":[5,.95],"Poison":[50,.20],"Catapult":[25,.50]}
            return weapon_list
        elif self.character == "notebook":
            weapon_list = {"Ruler Slap":[10,.75],"Rubber Band Shot":[5,.95],"Paper Cut":[50,.20],"Wire Skewer":[25,.50]}
            return weapon_list
        elif self.character == "backpack":
            weapon_list = {"Ruler Slap":[10,.75],"Rubber Band Shot":[5,.95],"Slam":[50,.20],"Strap Choke": [25,.50]}
            return weapon_list
        elif self.character == "computer":
            weapon_list = {"Ruler Slap":[10,.75],"Rubber Band Shot":[5,.95],"Self Destruct": [50,.20],"CD Launcher": [25,.50]}
            return weapon_list
        else:
            weapon_list =  {"Ruler Slap":[10,.75],"Rubber Band Shot":[5,.95]}
            return weapon_list

    #when called, will update the powerup count and if it equals two, will give the player a powerup and reset count to 0.
    def add_powerup_count(self):
        self.powerup_count = self.powerup_count + 1
        if self.powerup_count == 2:
            new_power_up = random.choice(["Armor", "Hit","Health","Increase Chance"])
            self.powerups.append(new_power_up)
            self.powerup_count = 0
    
    #returns health value for player
    def get_health(self):
        return self.health

    #returns list of powerups for player available
    def get_powerups(self):
        return self.powerups
    
    #returns list of weapons available for player
    def get_weapons(self):
        return self.weapons
    
    #returns name of player 
    def get_name(self):
        return self.name
    
    #updates the health to 100%
    def setFullHealth(self):
        self.health  = 100
        return self.health
    
    #updates the health to 100% based on if a powerup is used and removes from powerup list.
    def useHealth():
        self.health = 100
        self.powerups.remove("Health")
        return self.health
    
    #updates the health by 50 points based on if Armor is used and removes from powerup list.
    def use_armor(self):
        self.health += 50
        self.powerups.remove("Armor")
        return self.health

    #gets attack value based on character weapon choosen from dictionary(weapon_list) and if an additional hit value power up is used.
    #value will increase by a factor of 2 if it is.
    def get_attack_damage(self,weapon):
        weapon_attack = self.weapons[weapon][0]
        if self.increaseHit_active == True:
            weapon_attack = weapon_attack * 2
            self.change_increase_hit()
        return weapon_attack

    #gets probability of success from character weapon choosen from dictionary(weapon_list) and if an additional probability power up
    #is used. probablity will increase by 50%.
    def get_attack_probability(self,weapon):
        weapon_prob = self.weapons[weapon][1]
        if self.increaseHit_active == True:
            weapon_prob = weapon_prob * 1.5
            self.change_increase_chance()
        return weapon_prob

    #toggles armor powerup to true or false based on previous value
    def change_armor(self):
        if self.armor_active == False:
            self.armor_active = True
            self.powerups.remove("Armor")
        else:
            self.armor_active = False
            
    
    #toggles change_increase_hit powerup to true or false based on previous value.
    #if true removes "Hit" from list.
    def change_increase_hit(self):
        if self.increaseHit_active == False:
            self.increaseHit_active = True
            self.powerups.remove("Hit")
        else:
            self.increaseHit_active = False
            

    #toggles update power powerup to true or false based on previous value - power value not used.
    def change_increase_chance(self):
        if self.perfect_chance == False:
            self.perfect_chance = True
            self.powerups.remove("Increase Chance")
        else:
            self.perfect_chance = False
            

    #uses powerup and changes powerup status to active, else prints none available
    def use_power_up(self,powerup_choice):
        power_up_length = len(self.powerups)
        if power_up_length > 0:
            if powerup_choice == "Armor":
                self.use_armor()
            elif powerup_choice == "Health":
                self.setFullHealth()
            elif powerup_choice == "Increase Chance":
                self.change_perfect_chance()
            else:
                self.change_increase_hit()
        else:
            print "No powerup available."

    #retrieves damage and probability potential of hit from weapon given
    #a random number is generated and if that number is less than the probability, a hit is awarded.
    #damage is then returned, else 0 damage is returned.
    def attack(self,weapon):
        attack_damage = self.get_attack_damage(weapon)
        attack_probability = self.get_attack_probability(weapon)*100
        attack_win = random.randrange(0,101)
        if attack_win < attack_probability:
            self.add_powerup_count()
            return attack_damage
        else:
            return 0
    
    #removes damage amount from player.       
    def damagePlayer(self, amount):
        self.health -= amount
        return


class Weapon:
    def __init__(self,name,attack,percent):
        self.name = name
        self.attack_value = attack
        self.percent = percent