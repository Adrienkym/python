#practice

#add
def add(a, b):
    return a + b
result = add(3, 5)
print(result)



#check if even
def check_even_odd(numb):
    remainder =  numb % 2

    if remainder == 0:
        print(f"{numb} is even")
    else:
        print(f"{numb} is odd")    
check_even_odd(5)    




#find largest number
def find_largest():
    numbers = [10, 25, 17, 50]
    if not numbers:
        largest_number = None
    else:
        largest_number = numbers[0] # at first assume the numb at index 0 is the largest numb  
        for number in numbers:
            if number > largest_number:
                largest_number = number
    print(largest_number)                 
    
find_largest()    
        # ussing the max() method to find the largest
def find_largest_numb():   
    numbs = [10, 30, 41, 6]     
    largest_numb = max(numbs)
    print(largest_numb)
find_largest_numb()    




#count the number of vowels in a word
def count_vowels(word):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']  # list the vowels
    for i in range(len(word)):          # every letter in the word from index 0
        if word[i] in vowels:           # if any i in the word is in the vowel list
            count = count + 1           # the count goes up by one
    print(count)        
count_vowels("banana")    





#check the gcf
def Division(num1,num2):
# check if both numbers are in the range of 1 to 1000
    if not (1 <= num1 <= 10**3 and 1 <= num2 <= 10**3):
        raise ValueError ("Both numbers must be in the range of 1 to 10^3.")
  
    while num2 != 0:
      num1, num2 = num2, num1 % num2
    return num1  

# keep this function call here 
print(Division(82, 48))

#
#SELECT
 # e.Position,
 # e.FirstName,
 # e.LastName,
 # m.Position AS ReportsToPosition
#FROM
 # main_table_29UAQ AS e
#JOIN
 # main_table_29UAQ AS m ON CONCAT(m.FirstName, ' ', m.LastName) = e.ReportsTo
#ORDER BY
 # ReportsToPosition ASC,
  #Position ASC;





#this function updates a shopping cart based on the given action
def update_shopping_cart(cart, action):
  product_id = action.get("product_id") # get the product id from the action dictionary
  action_type = action.get("type") # get the action type from the action dictionary
  if action_type == "add":
    quantity = action.get("quantity", 0) # get the quantity from the action dictionary, default to 0 if not provided
    if product_id in cart:
        cart[product_id] += quantity # if the product is already in the cart, increase its quantity
    else:
        cart[product_id] = quantity # if the product is not in the cart, add it with the specified quantity

  elif action_type == "remove" :
    if product_id in cart:
        del cart[product_id] # if the product is in the cart, remove it

  elif action_type == "change":
    quantity = action.get("quantity", 0) # get the new quantity from the action dictionary, default to 0 if not provided
    if quantity > 0:
        cart[product_id] = quantity # if the new quantity is greater than 0, update the product's quantity
    else:
        if product_id in cart:
            del cart[product_id] # if the new quantity is 0 or less, remove the product from the cart

  return  cart                                

# do not modify the values below(example for testing)
print(update_shopping_cart({ "product_A": 4, "product_B": 3, "product_C": 1 }, { "type": "change", "product_id": "product_B", "quantity": 2 }))

# Steps of the function:
# 1. Get product_id and action_type from the action dictionary.
# 2. If action_type is "add":
#    - Get the quantity (default 0 if not given).
#    - If product already in cart → increase its quantity.
#    - Else → add product with given quantity.
# 3. If action_type is "remove":
#    - If product is in cart → delete it.
# 4. If action_type is "change":
#    - Get the new quantity (default 0 if not given).
#    - If quantity > 0 → update product with new quantity.
#    - Else if quantity <= 0 → remove product from cart (if it exists).
# 5. Return the updated cart.
