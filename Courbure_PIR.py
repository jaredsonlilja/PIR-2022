# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 16:57:58 2022

@author: yhvig
"""


from math import *
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd
import json

#

#Coordonnées du circuit de circuit from txt 

x_y_circuit = np.loadtxt("nugaro.txt", delimiter=',')
x_circuit, y_circuit = x_y_circuit.T



# Fonction pour trouver le meilleur cercle qui fit le mieux pour 3 points

def findCircle(x1, y1, x2, y2, x3, y3) :
    global r;
    global h;
    global k;
    x12 = x1 - x2;
    x13 = x1 - x3; 
    y12 = y1 - y2;
    y13 = y1 - y3;
    y31 = y3 - y1;
    y21 = y2 - y1;
    x31 = x3 - x1;
    x21 = x2 - x1;
	# x1^2 - x3^2
    sx13 = pow(x1, 2) - pow(x3, 2);
	# y1^2 - y3^2
    sy13 = pow(y1, 2) - pow(y3, 2);
    sx21 = pow(x2, 2) - pow(x1, 2);
    sy21 = pow(y2, 2) - pow(y1, 2);
    f = (((sx13) * (x12) + (sy13) *
		(x12) + (sx21) * (x13) +
		(sy21) * (x13)) // (2 *
		((y31) * (x12) - (y21) * (x13))));
    g = (((sx13) * (y12) + (sy13) * (y12) +
		(sx21) * (y13) + (sy21) * (y13)) //
		(2 * ((x31) * (y12) - (x21) * (y13))));
    c = (-pow(x1, 2) - pow(y1, 2) -
		2 * g * x1 - 2 * f * y1);
    #Coordonnées du centre (h, k)
    h = -g;
    k = -f;
    sqr_of_r = h * h + k * k - c;
	# r le rayon
    r = round(sqrt(sqr_of_r), 5);
    # print("Centre = (", h, ", ", k, ")");
    # print("Radius = ", r);
    return r,k,h


#Boucle calcul courbure sur tout le circuit
circles = []
all_circles = []
x_circles = []
y_circles = []

r_max_admis = 1000  #Rayon de courbure max pris en compte
for i in range(len(x_y_circuit)-2):
    
    x1 = x_circuit[i-1]
    x2 = x_circuit[i]
    x3 = x_circuit[i+1]
    y1 = y_circuit[i-1]
    y2 = y_circuit[i]
    y3 = y_circuit[i+1]
   
    findCircle(x1, y1, x2, y2, x3, y3)
    all_circles = all_circles + [[h, k ,r]]
    if r < r_max_admis :
        circle_admis = [h, k, r]
        circles = circles + [circle_admis]
        x_circles = x_circles + [circle_admis[0]]   #Extraction des x pour les cercles admis
        y_circles = y_circles + [circle_admis[1]]   #Extraction des y pour les cercles admis
        
   
#print(circles)
print('Combien de cerles ? ',len(circles))


#Tracé de tous les cercles + circuit

#Mettre en limite la valeur max et min du x et du y du circuit

x_circles_max=max(x_circles)
y_circles_max=max(y_circles)
x_circles_min=min(x_circles)
y_circles_min=min(y_circles)
x_circuit_min=min(x_circuit)
y_circuit_min=min(y_circuit)
x_circuit_max=max(x_circuit)
y_circuit_max=max(y_circuit)
if x_circles_min < x_circuit_min:
    x_min = x_circles_min
else:
    x_min = x_circuit_min      
if x_circles_max > x_circuit_max:
    x_max = x_circles_max
else:
    x_max = x_circuit_max            
if y_circles_min < y_circuit_min:
    y_min = y_circles_min
else:
    y_min = y_circuit_min            
if y_circles_max > y_circuit_max:
    y_max = y_circles_max
else:
    y_max = y_circuit_max

x = np.linspace(x_min-r_max_admis, x_max+r_max_admis, 1000)
y = np.linspace(y_min-r_max_admis, y_max+r_max_admis, 1000)
X, Y = np.meshgrid(x,y)
fig, ax = plt.subplots()
plt.gca().set_aspect('equal', adjustable='box') #Same scale on x & y

for i in range(len(circles)):
    circle_admis = circles[i]
    x_circle = circle_admis[0]
    y_circle = circle_admis[1]
    r_circle = circle_admis[2]
    F = (X-x_circle)**2 + (Y-y_circle)**2 - r_circle**2  
    ax.contour(X,Y,F,[0], colors="r")
#plot_circuit = plt.scatter(x_circuit, y_circuit, s=5)
plt.plot(x_circuit, y_circuit, '-o', markersize=2)



plt.title('Radius max : ' + str(r_max_admis) + "m")
plt.show()



#Association des rayons de courbure à chaque point
#On considère que le rayon de courbure associé au point x_i est celui calculé 
#avec x_i-1, x_i et x_i+1

x_y_r = []

#Faire une boucle pour le 1er et Dernier point du circuit

for i in range(len(x_y_circuit)-1):
    
    x1 = x_circuit[i-1]
    x2 = x_circuit[i]
    x3 = x_circuit[i+1]
    y1 = y_circuit[i-1]
    y2 = y_circuit[i]
    y3 = y_circuit[i+1]
   
    findCircle(x1, y1, x2, y2, x3, y3)

    
    
    if r < r_max_admis :
        print('Point',i, ' : x = ', x_circuit[i], ', y = ', y_circuit[i], ', r = ', r)
        plt.plot(x_circuit[i],y_circuit[i], 'o', markersize=3, color='r')
        x_y_r = x_y_r + [[x_circuit[i], y_circuit[i], r]]
            
    else :
        x_y_r = x_y_r + [[x_circuit[i], y_circuit[i], inf]]
        print('Point',i, ' : x = ', x_circuit[i], ', y = ', y_circuit[i], ', r = ', inf)

    

mat = np.array(x_y_r)

with open("x_y_r_nugaro.txt", "w") as o:
    for line in mat:
        print("{},{},{}".format(line[0], line[1], line[2]), file=o)












