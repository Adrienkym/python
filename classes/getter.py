from datetime import datetime

def write_file(f_name, txt):
    with open(f_name, 'a') as file:
        file.write(f"{txt} \n")

class Human():
    def __init__(self, gender, name):
        self.gender = gender
        self._name = name  # recommended to change variable name by adding an (_) 
        print("The initializer was called")
        print(self.gender)
        print(self._name)
        if self.gender == "male":
            self.ribs = 24
        else:
             self.ribs = 23    

    def another_one(self):
        print("This is the second one")  #not shown unless officialy called like on line 15

    @property   #lets python know that the arguement in line 37 is function without using ()
    def get_name(self):
        #print('SOmebody is tring to get the name if a property')
        now = datetime.now()
        print('current time and', now)
        write_file(f_name="log.txt", txt=f"At {now} got name from Kayeem")
        return self._name

Kayeem=Human( name="kayeem", gender="male")  
# Kayeem.another_one()

# eve=Human( name="eve", gender="female") 

# print("", Kayeem.name)
# print("", Kayeem.gender)
# print("", Kayeem.ribs)
# print('')
# print("", eve.name)
# print("", eve.gender)
# print("", eve.ribs)

#getters & setters

print(Kayeem.get_name) # getting data or reading data(line 17 to 20)