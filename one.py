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