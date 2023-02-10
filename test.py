from random import random
from Vec import Vec

# Nn = Vec(1, 0, 0)
# Nn.rotate((0.5-random())*0.004)


for i in range(100):
    Nn = Vec(1, 0, 0)
    Nn.rotate((0.5-random())*4)
    print(Nn)