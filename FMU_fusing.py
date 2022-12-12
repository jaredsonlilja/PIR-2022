
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


# my code
samplenode3 = [25, 30, 22, 32, 31.9]
samplecons3 = [0.8, 0, 0.2, 0]

#we will have a list “nodes” that is updated continuously instead
#same for cons, this is updated after each FMU

position_list = []
for i in range(1, len(samplenode3)):
   if i > len(samplenode3):
       break
   elif abs(samplenode3[i] - samplenode3[i-1]) <= 0.1: #compare
       position_list.add(i)
       position_list.add(i-1) #add both positions to list for next loop

for i in range(1, len(samplecons3)):
    if i > len(samplecons3):
        break
    elif (samplecons3[i-1] <= samplecons3[i-2]):
            samplecons3.remove(samplecons3[i-2])
            samplenode3.remove(samplenode3[i-1])
    else:
            samplecons3.remove(samplecons3[i-1])
            samplenode3.remove(samplenode3[i])

print(samplenode3)
print(samplecons3)
