class Zombie:
    def __init__(self, health):
        self.health = health
        self.alive = 1
    def takeDamage(self, damage):
        self.health -= damage
        print "zombie takes %d damage" % damage
        if self.health <= 0:
            self.alive = 0
            print "zombie health = %d\nzombie killed" % self.health
        
            
zom1 = Zombie(50)
zom1.takeDamage(24)
zom1.takeDamage(27)











 
 
   
