  # if , elif , else

age = 18

if age > 20:
    print("you can drink")
else:
    print("you cannot drink")    

if age > 18:
    print("you can vote")
elif age == 18:
    print("you are just eligible to vote")
elif age < 18 and age > 0:
    print("you are still underage")    
else:
    print("you cannot vote")

