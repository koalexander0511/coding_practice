import random
import os

random.seed();

count = [0,0,0,0,0,0,0,0,0,0];

for i in range(0,100000):
    count[int(random.random()*10)] += 1;
    print(count);
    os.system('clear');