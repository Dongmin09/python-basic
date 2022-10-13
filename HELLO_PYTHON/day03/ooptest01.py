

class Animal:

    def __init__(self):
        self.hungry =5
        
    def timegoby(self):
        if self.hungry >0:
            self.hungry -= 1

    def manttang(self):
        self.hungry = 10
        
        
class Human(Animal):
    def __init__ (self):
        super().__init__()
        self.skill_lang = 0
    
    def monstouch(self, stroke):
        self.skill_lang += stroke
        
hum = Human()
print(hum.skill_lang)

print(hum.hungry)
hum.manttang()
hum.monstouch(11)
print(hum.skill_lang)
        
