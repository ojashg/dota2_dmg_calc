print "\nimporting files(formula.py, hero.py)..."

import formula
import hero

print "importing is now complete!\n"


#global variable to take#
############################################

hero_data = hero.jug
hero_name = 'juggernaut'
type = 'agi'
lvl = 10
stats = 0
###########################################
bat = hero_data['bat']
base_dmg = hero_data['dmg']
base_ms = hero_data['ms']
base_hp = hero_data['b_health']
hp_regen = hero_data['h_regen']
mana_regen = hero_data['m_regen']
base_mana = hero_data['mana']
base_magic_resis = hero_data['magic_resis']

base_agi = hero_data['b_agi']
base_str = hero_data['b_str']
base_int = hero_data['b_int']

agi_gain = hero_data['agi_gain']
str_gain = hero_data['str_gain']
int_gain = hero_data['int_gain']

item_agi = 0.0				#affected by agi
item_str = 0.0				#affected by str
item_int = 0.0

ms_boost = 0.0
percent_boost = 0.0
item_hp_pool = 0.0
item_mana_pool = 0.0
item_regen = 0
skill_regen = 0
item_armor = 0
magic_dmg_1 = 0
magic_dmg_2 = 0
magic_dmg_3 = 0
magic_dmg_4 = 0
magic_resis_1 = 0
magic_resis_2 = 0  #negative value for resistance decrease

bonus_dmg = 0
enemy_armor = 3
base_dmg_mult = 0
enemy_dmg_block = 0
armor_peirce = 100
gen_dmg_mult = 0
crit_mult = 0



if type == 'agi':
	base_attribute_dmg = hero_data['b_agi'] #depends on hero attribute type
	item_attribute = item_agi
	lvl_gain = hero_data['agi_gain']
elif type == 'str':
	base_attribute_dmg = hero_data['b_str']
	item_attribute = item_str
	lvl_gain = hero_data['str_gain']
elif type == 'int':
	base_attribute_dmg = hero_data['b_int']
	item_attribute = item_int
	lvl_gain = hero_data['int_gain']






def jug_starting_stats ():
	print "These are the the starting stats for %s:\n" % hero_name
	attack_speed = formula.attack_speed(base_agi,item_agi,bat, lvl, agi_gain, stats)
	print "%-20s %.3f" % ('Attack Speed:', attack_speed)
	main_dmg = formula.main_dmg(base_dmg, base_attribute_dmg, item_attribute, lvl , lvl_gain, stats)
	print "%-20s %.3f" % ('Main dmg:', main_dmg)
	phy_dmg = main_dmg + bonus_dmg
	print "%-20s %.1f" % ('Physical dmg:', phy_dmg)
	tot_dmg = formula.final_attack_dmg(main_dmg, base_dmg_mult, bonus_dmg, enemy_dmg_block, enemy_armor, armor_peirce, gen_dmg_mult, crit_mult)
	print "%-20s %.3f" % ('Final phy dmg: ', tot_dmg)
	move_speed = formula.move_speed(base_ms, ms_boost, percent_boost)
	print "%-20s %.3f" % ('Move speed:', move_speed)
	hp_pool = formula.hp_pool(base_str,item_str, item_hp_pool,base_hp, lvl, str_gain, stats)
	print "%-20s %.3f" % ('Hp pool:', hp_pool)
	health_regen = formula.hp_regen(base_str, item_str, lvl, str_gain, stats, item_regen, skill_regen, hp_regen)
	print "%-20s %.3f" % ('Hp regen:', health_regen)
	mana_pool = formula.mana_pool (item_int, base_int, item_mana_pool, lvl, int_gain, stats, base_mana)
	print "%-20s %.3f" % ('Mana pool:', mana_pool)
	m_regen = formula.mana_regen ( item_int, base_int, lvl, int_gain, stats, mana_regen, item_regen, skill_regen)
	print "%-20s %.3f" % ('Mana regen:', m_regen)
	tot_armor = formula.armor_pool ( item_agi, base_agi, lvl, agi_gain, stats, item_armor)
	print "%-20s %.3f" % ('Total armor:', tot_armor)
	armor_def = formula.armor_reduction (tot_armor)
	print "%-20s %.1f" % ('% phy dmg taken:', armor_def*100)
	mag_resis = formula.magic_resistance(base_magic_resis, magic_resis_1, magic_resis_2)
	print "%-20s %.3f" % ('% Magic resistance: ', mag_resis)
	mag_dmg = formula.magic_dmg(magic_dmg_1, base_int, item_int, lvl, int_gain, stats, magic_dmg_2, magic_dmg_3, magic_dmg_4)
	print "%-20s %.3f" % ('Total magic dmg: ', mag_dmg)
	
	

jug_starting_stats()
raw_input("\npress any key to continue...\n>")

