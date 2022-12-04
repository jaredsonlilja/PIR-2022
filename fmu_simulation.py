
# On simule un appel à la fmu
#d_init= 0 m
#v_init = 25

v0= 25
import random
speeds= []
cons = []
while len(speeds)<1:
    v1=random.randint(15,35)
    c1= random.random()
    if v1 > v0 and c1 > 0:
        speeds+= [v1]
        cons+= [c1]
while len(speeds)!=2:
    v2=random.randint(15,35)
    c2=0
    if v2 <v0:
        speeds+= [v2]
        cons+= [c2]


print(speeds)
print(cons)