#big opertion-

import time 

def calculate_sum(n):
    sum = 0
    for numb in range(1, n+1):
        print(f"Sum ={sum} , num = {numb}")
        sum = sum + numb
        print(f"For {n}, sum is {sum}")
    return sum

#more efficiently
def claculate_sum2(n):
    return n * (n + 1) // 2 

start_time= time.time()
calculate_sum(100000)
end_time = time.time()
print(f"Time taken to calculate sum: {end_time - start_time} seconds")
