
###		OFFENSIVE CAPABILITIES		###

#need hero input ie hero's BAT #this is not marginal attack_speed but total attack_speed at a given BAT

def attack_speed (base_agi, item_agi = 0, BAT = 1.7, lvl = 0, agi_gain = 0, stats = 0):
    if lvl > 0: lvl -= 1
    attack_speed = ((100 + item_agi + base_agi + stats*2.0 + lvl*agi_gain ) * 0.01) / BAT
    return attack_speed
             
def main_dmg( base_dmg, base_attribute_dmg = 0, item_attribute = 0, lvl = 0, lvl_gain = 0, stats = 0):
    if lvl > 0: lvl -= 1	
    total = base_dmg + base_attribute_dmg + item_attribute + lvl*lvl_gain + stats * 2
    return total

def final_attack_dmg (main_dmg, percent_attack_mod = 0, bonus_dmg = 0, block_dmg = 0, enemy_armor = 0, armor_type = 100.0, general_multi =0, crit_multi =0):
    dmg = 	(main_dmg * (1 + percent_attack_mod/100.0) + bonus_dmg - block_dmg)*(armor_reduction(enemy_armor))\
			* (armor_type/100.0) *(1 + general_multi/100.0) * (1 + crit_multi /100.0)
    return dmg
    
    
def magic_dmg (source1, base_intel = 0, item_intel = 0, lvl = 0, lvl_gain = 0, stats = 0, source2 = 0, source3 = 0, source4 = 0):
    if lvl > 0: lvl -= 1
    intel = base_intel + item_intel + lvl*lvl_gain + stats*2
    magic_dmg = (source1 + source2 + source3 + source4) * (1 + (intel * 1/1600.0))
    return magic_dmg
    
def move_speed (base_ms, ms_boost= 0, percent_boost =0):
    speed = (base_ms + ms_boost) * ( 1 + percent_boost/100.0)
    return speed
   
   
    
###		DEFENSIVE CAPABILITIES		###

def hp_pool (base_strength,item_str = 0, item_hp_pool = 0.0, base_hp = 0, lvl = 0, str_gain = 0, stats=0):
    if lvl > 0: lvl -= 1
    hp =(item_str + base_strength + stats*2 + lvl*str_gain)* 20.0 + item_hp_pool + base_hp
    return hp

def hp_regen (base_strength, item_str = 0, lvl = 0, str_gain = 0, stats = 0, item_regen = 0.0, skill_regen = 0.0, base_regen = 0):
    #Includes life steal + natural regen
    if lvl > 0: lvl -= 1
    strength = (base_strength + item_str + lvl*str_gain + stats*2)
    hp_regen = (strength * 0.03) + item_regen + skill_regen + base_regen
    return hp_regen
    
def mana_pool (item_int, base_int = 0.0, item_mana_pool = 0.0, lvl = 0, int_gain = 0, stats= 0, base_mana = 0):
    if lvl > 0: lvl -= 1
    mana = (item_int + base_int + lvl * int_gain + stats * 2) * 12.0 + item_mana_pool + base_mana
    return mana
    
def mana_regen (item_int, base_int = 0, lvl= 0, int_gain = 0, stats= 0, base_regen = 0, item_regen= 0, skill_regen = 0):
    if lvl > 0: lvl -= 1
    intel = item_int + base_int + lvl*int_gain + stats*2
    intel_based = intel * 0.04
    return base_regen + item_regen + skill_regen + intel_based
        
def armor_pool (item_agi, base_agi = 0, lvl = 0, agi_gain = 0, stats = 0, item_armor = 0.0, tower_bonus = 0,reduction = 0.0):
    if lvl > 0: lvl -= 1
    agility = item_agi + base_agi + stats*2 + lvl * agi_gain
    armor = agility * 0.14
    total_armor = armor +  item_armor - reduction + tower_bonus
    return total_armor
    
def armor_reduction (armor):
    if armor >= 0:
        reduction = 1- (0.06 * armor)/ (1 +(0.06 * armor))
    else:
        reduction = 1- (0.06 * armor)/ (1 +(0.06 * -armor))
    return reduction 
    
def magic_resistance (base, source1 = 0.0, source2 = 0.0):
    #magic resistance, enter all in percent
    resistance = 1 -((1- base/100.0)*(1- source1/100.0)*(1- source2/100.0))
    return resistance * 100
    






