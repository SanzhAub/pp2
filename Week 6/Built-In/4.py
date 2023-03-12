import math
import time 
def func():
    x = int(input())
    seconds = int(input())
    time.sleep(seconds/1000)
    result = math.sqrt(x)
    print("Square root of" , x , "after", seconds ,"miliseconds is ", result )
func()
