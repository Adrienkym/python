#like a constructor in js

#special methos in class(gets called automaticaly )
#initializer:  method is called whenever the blueprint is used to create an object
# method is a function inside a class
# (self) ->  as in this obect 

class Human():
    def __init__(self, gender, name):
        self.gender = gender
        self.name = name
        print("The initializer was called")
        print(self.gender)
        print(self.name)
        if self.gender == "male":
            self.ribs = 24
        else:
             self.ribs = 23    

    def another_one(self):
        print("This is the second one")  #not shown unless officialy called like on line 15

Kayeem=Human( name="kayeem", gender="male")  
# Kayeem.another_one()

eve=Human( name="eve", gender="female") 

print("", Kayeem.name)
print("", Kayeem.gender)
print("", Kayeem.ribs)
print('')
print("", eve.name)
print("", eve.gender)
print("", eve.ribs)


