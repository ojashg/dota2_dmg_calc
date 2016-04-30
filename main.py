#Importing the reqired files
print "\nimporting files(formula.py, hero.py)..."
import formula
import hero
print "importing is now complete!\n"

#############################################  CLASS DEFINATIONS  #############################################################

class DotaStats(object):
	pass

	
class HeroStats(DotaStats):
	''' Initializes all the basic hero stats; not inclusive of hero spells; not inclusive of item builds 
		The said stats can be grouped into two types:
			1. The default fixed stats that can be found in the hero profile wiki page. Eg. BAT, Base MS
			2. Variable stats such as Level, stats upgrade which require user input '''
			
	#golbal variables that still needs to be added
	#hero armor type
	
	t1_tower_armor = 1
	t2_tower_armor = 3
	
	
	
	def __init__(self, hero_name, level = 1, stat_points = 0.0, enemy_dmg_block = 0, enemy_armor = 0,\
				enemy_armor_type = 0, dd_rune = False, haste_rune = False, tower_tier = 0, fountain_regen = False):
		#initializing the User initiated stats
		
		self.hero_name = hero_name
		self.level = level 	
		self.stats = stat_points
		self.dd_rune = dd_rune
		self.haste_rune = haste_rune				
		self.fountain_regen = fountain_regen
		self.enemy_dmg_block = enemy_dmg_block
		self.enemy_armor = enemy_armor
		self.enemy_armor_type = enemy_armor_type
		
		#tower tier is inputed as 1,2,3 or 4 representing t1, t2, t3 and t4 towers respectively
		if tower_tier == 1:						
			self.tower_armor = t1_tower_armor
		elif tower_tier == 0:
			self.tower_armor = 0
		else:
			self.tower_armor = t2_tower_armor
			
		
	def import_hero_database(self, import_file):
		'''IMPORTANT----REQUIRES CALLING TO USE OTHER MODULES IN THIS CLASS--------'''
		#importing the hero database from another file and initializing it
		
		f = import_file 					#imp: the passed import_file should be import from hero.py where the dict is saved
		self.type = f['type']				#main attribute (agi, str or int)
		self.bat = f['bat']					#base attack time
		self.base_dmg = f['dmg']			#base damage (not inclusive of main stat attribute)
		self.base_ms = f['ms']				#base movement speed
		self.base_hp = f['b_health']		#base hp exclusive of base strength stat
		self.base_hp_regen = f['h_regen']	#base hp regen exclusive of base strength stat
		self.base_mana_regen = f['m_regen']
		self.base_mana = f['mana']
		self.base_magic_resis = f['magic_resis']

		self.base_agi = f['b_agi']
		self.base_str = f['b_str']
		self.base_int = f['b_int']
		self.agi_gain = f['agi_gain']
		self.str_gain = f['str_gain']
		self.int_gain = f['int_gain']
		
		if self.type == 'agi':
			self.prime_attr_dmg = f['b_agi'] 		#dmg which depends on hero primary attribute type
			self.prime_attr_gain = f['agi_gain']
		elif self.type == 'str':
			self.prime_attr_dmg = f['b_str']
			self.prime_attr_gain = f['str_gain']
		elif self.type == 'int':
			self.prime_attr_dmg = f['b_int']
			self.prime_attr_gain = f['int_gain']
		else:
			print "illegal input detected"

	'''  NEED TO MODIFY FUNCTION NAMES OF FORMULA.PY; CHANGE HOW LVL -1 IS CALCULATED; AND CHANGE PASSED VARIABLE NAMES IN THE FORMULA FUNCT.'''	
	
	def get_attack_speed(self):
		'''Note need to change program if import file name changes; uses formula. to gain access to formula'''
		#gets attack_speed without items and spells. 
		self.attack_speed = formula.attack_speed(self.base_agi, 0, self.bat, self.level, self.agi_gain, self.stats)
		return self.attack_speed
		
	def get_main_phy_dmg(self):
		#returns main damage without considering items and spells.(main dmg is total dmg from attributes; excludes bonus dmg )
		self.main_phy_dmg = formula.main_dmg(self.base_dmg, self.prime_attr_dmg, 0, self.level , self.prime_attr_gain, self.stats)
		return self.main_phy_dmg
	
	def get_physical_dmg(self):
		#total physical dmg before reductions
		if self.dd_rune == True:
			self.physical_dmg = self.main_phy_dmg * 2
		else:
			self.physical_dmg = self.main_phy_dmg
		return self.physical_dmg
	
	def get_final_phy_dmg(self):
		#total physical dmg dealt to enemy after reductions
		if self.dd_rune == True:
			self.final_phy_dmg = formula.final_attack_dmg(self.main_phy_dmg, 0, self.main_phy_dmg, self.enemy_dmg_block,\
								 self.enemy_armor, self.enemy_armor_type) #main_phy_dmg is passed twice, 1 for the bonus dmg from dd rune.
		else:
			self.final_phy_dmg = formula.final_attack_dmg(self.main_phy_dmg, 0, 0, self.enemy_dmg_block, self.enemy_armor)
		return self.final_phy_dmg
			
	def get_ms(self):
		#returns total movement speed; excludes item and skill bonus
		if self.haste_rune == False:
			self.ms = formula.move_speed(self.base_ms)
		else: 
			self.ms = 522.0
		return self.ms
	
	def get_hp_pool(self):
		#returns the total hp pool; excludes item and skill bonus
		self.hp_pool = formula.hp_pool(self.base_str, 0, 0, self.base_hp, self.level, self.str_gain, self.stats)
		return self.hp_pool
		
	def get_hp_regen(self):
		#returns the total hp regen; excludes item and skil bonus
		
		if self.fountain_regen == True:
			bonus_regen = (0.4/100.0) * self.hp_pool * 10
			self.hp_regen = formula.hp_regen(self.base_str, 0, self.level, self.str_gain, self.stats, bonus_regen, 0, self.base_hp_regen)
		else:
			self.hp_regen = formula.hp_regen(self.base_str, 0, self.level, self.str_gain, self.stats, 0, 0, self.base_hp_regen)
		return self.hp_regen
		
	def get_mana_pool(self):
		#returns the total mana pool; excludes item and skill bonus
		self.mana_pool = formula.mana_pool(0, self.base_int, 0, self.level, self.int_gain, self.stats, self.base_mana)
		return self.mana_pool
		
	def get_mana_regen(self):
		#returns total mana regen; excludes item and skill bonus
		if self.fountain_regen == False:
			self.mana_regen = formula.mana_regen(0, self.base_int, self.level, self.int_gain, self.stats, self.base_mana_regen)
		else:
			bonus_regen = ((0.4/100.0) * self.mana_pool + 1.4)* 10
			self.mana_regen = formula.mana_regen(0, self.base_int, self.level, self.int_gain, self.stats, self.base_mana_regen, bonus_regen)
		return self.mana_regen
		
	def get_armor(self):
		#returns total armor value without reductions; excludes item and skills
		self.armor = formula.armor_pool(0, self.base_agi, self.level, self.agi_gain, self.stats, 0, self.tower_armor)
		return self.armor
		
	def get_armor_resistance(self):
		#returns the percentage of incoming physical dmg taken after armor calculation.
		self.armor_resistance = formula.armor_reduction(self.armor)
		return self.armor_resistance
		
	def get_magic_resistance(self):
		#returns the percentage of incoming magic dmg taken
		self.magic_resistance = formula.magic_resistance(self.base_magic_resis)
		return self.magic_resistance
			
class ItemStats(DotaStats):
	pass

############################################  MAIN PROGRAM ######################################################################



def jug_starting_stats():
	#prints the starting stats of jugg at lvl 1.
	jug = HeroStats('jug', 1)
	jug.import_hero_database(hero.jug)
	print "These are the the starting stats for %s:\n" %jug.hero_name
	print "%-20s %.3f" % ('Attack Speed:', jug.get_attack_speed())
	print "%-20s %.3f" % ('Main dmg:', jug.get_main_phy_dmg())
	print "%-20s %.1f" % ('Physical dmg:', jug.get_physical_dmg())
	print "%-20s %.3f" % ('Final phy dmg: ', jug.get_final_phy_dmg())
	print "%-20s %.3f" % ('Move speed:', jug.get_ms())
	print "%-20s %.3f" % ('Hp pool:', jug.get_hp_pool())
	print "%-20s %.3f" % ('Hp regen:', jug.get_hp_regen())
	print "%-20s %.3f" % ('Mana pool:', jug.get_mana_pool())
	print "%-20s %.3f" % ('Mana regen:', jug.get_mana_regen())
	print "%-20s %.3f" % ('Total armor:', jug.get_armor())
	print "%-20s %.1f" % ('% phy dmg taken:', jug.get_armor_resistance())
	print "%-20s %.3f" % ('% Magic resistance: ', jug.get_magic_resistance())
	
jug_starting_stats()	
	

