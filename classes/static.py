from datetime import datetime

def write_file(f_name, txt):
    with open(f_name, 'a') as file:
        file.write(f"{txt} \n")

class Human():

    species= "H.sapiens"
    genus="HOmo"            # static => non changing
    count=0

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

        Human.count=Human.count+1       # line 11 

    def another_one(self):
        print("This is the second one")  #not shown unless officialy called like on line 15

# getters
    @property   # lets python know that the argument in line 37 is function without using ()
    def name(self):
        now = datetime.now()
        print('current time and', now)
        write_file(f_name="log.txt", txt=f"At {now} got name from Kayeem")
        return self._name

# setter
    @name.setter
    def name(self,new_name):
        # data integrity
        if not isinstance(new_name,str):
            print("Failed to update name")
            return
        #new_name is astring
        now = datetime.now()
        print("Curreent date and time",now)
        write_file(f_name="log.txt",txt=f"At {now} Name changed from {self._name} to {new_name}")
        self._name=new_name
        return new_name

    # classmethods
    @classmethod
    def gen_class_method(cls):   
      print("Species", cls.species)
      print ("Genus", cls.genus)
      print("Total Humans", cls.count)

   

Kayeem=Human( name="kayeem", gender="male")  
# Kayeem.another_one()
eve=Human( name="eve", gender="female") 

# print("", Kayeem.name)
# print("", Kayeem.gender)
# print("", Kayeem.ribs)
# print('')
# print("", eve.name)
# print("", eve.gender)
# print("", eve.ribs)


#print(Kayeem.name) # getting data or reading data(line 17 to 20)

#print("species", Kayeem.species)
#print("class property", Human.species)

#print("Total HUmans", Human.count)

Human.gen_class_method()  # calling class method