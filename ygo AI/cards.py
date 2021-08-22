class crystal_clear_wing_synchro_dragon():
    def __init__ (self):
        self.kind = "monster"
        self.name = "crystal clear wing synchro dragon"
        self.ATK = 3000
        self.DEF = 2500
        self.level = 10
        self.type = "synchro"
        self.race = "dragon" 
        self.effect = True
        self.attribute = "wind"
        self.summoned = None
        self.speed = 2
        self.numEffects = 2

        self.image = "1.jpg"
 
        #add this part according to the avaivle effects in the decks
        self.effected = True


    def summon_condition(self, position,Tuner,nonTuner):
        if (Tuner.type == "synchro") and ("clear wing" in nonTuner.name) and (Tuner.level + nonTuner.level == 10):
            if position == "attack":
                self.summoned = "attack"
            elif position == "defense":
                self.summoned = "defense"
            return True
        else:
            print("Cant summon")
            return False

    def effect1(self,monster_effect_activate,playing_time,resolve):
        if playing_time <= 2:
            self.effected = False
            self.ATK += monster_effect_activate.ATK
            return True
        else:
            return False

    def effect2(self,card_activted,playing_time,resolve):
        if playing_time <= 2:
            if card_activted.kind == "monster":
                card_activted.summoned = None
            else:
                card_activted.played = False
            resolve == False
            return True
        else:
            return False

    def effect(self):
        pass
                

    


