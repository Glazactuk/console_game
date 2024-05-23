#imagine being horny like goofy aaaaah
import random
import time


def abs(x):
    return (x*x)**0.5


x = 0.05
for i in range(random.randint(50, 75)):
    in_txt = "Пожалуйста, введите новую задачу:"
    for i in in_txt:
        print(i, end="")
        time.sleep(x)
    x= abs(x-0.0025)

