
def creep_gold (number):
    avg = (38 * 3 + 44)/4.0
    print "gold: ", number * avg
    
def creep_exp (number):
    avg = (45 * 3 + 90)/4.0
    print "exp: ", number * avg
    
def neutral_gold (rounds):
    small_camp = (68 + 71 + 74 + 75 + 78 + 86)/6.0
    medium_camp = (94 + 89 + 92 + 110 + 116) / 5.0
    large_camp = (116 + 130 + 132+ 112 + 135) / 5.0
    total = small_camp + medium_camp *2 + large_camp * 2
    print "total gold: ", total
    
    
    
creep_gold (13)
creep_exp (4)
neutral_gold (1)

