# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 08:38:00 2022

@author: yhvig
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


#Données du véhicule :

L = 1.3
v = 10 #mètre par seconde
x_y_r_circuit = np.loadtxt("x_y_r_nugaro.txt", delimiter=',')
x_circuit, y_circuit, r_circuit = x_y_r_circuit.T
distance_circuit = np.loadtxt("distance_nugaro.txt")
#Calcul du steering angle :
steering_angle = []
acceleration_laterale = []
#Condition de non basculement et vitesse max 
#m_tot*a_l*0,3 < 0,236*m_tot*g
g = 9.81
#Position du centre de gravité
m_totale = 90
h_g = 0.3
bras_levier = 0.236
moment_poids = m_totale * g * bras_levier
#On considère que l'accélération latérale s'applique à G (approximation)
v_max= np.zeros(len(r_circuit))
x_y_v_max = []
x_y_v_max_kmh = []
for i in range(len(r_circuit)):
    if r_circuit[i] == inf:
        acceleration_laterale += [0]
        v_max[i] = 35/3.6
    else:
        a_l = (v_max[i]**2/1.3)*np.arctan(1.3/r_circuit[i])
       
        while moment_poids > 0.3*a_l*m_totale and v_max[i] < 35/3.6:
            v_max[i] += 0.1
            a_l = (v_max[i]**2/1.3)*np.arctan(1.3/r_circuit[i])
            
        acceleration_laterale += [a_l]            
    x_y_v_max += [[x_circuit[i], y_circuit[i], round(v_max[i])]]
    x_y_v_max_kmh += [[x_circuit[i], y_circuit[i], round(v_max[i]*3.6)]]
    print('x = ',x_circuit[i], ' y = ',y_circuit[i],' r = ',r_circuit[i], 'Vitesse max = ', round(v_max[i]*3.6, 1))   
mat = np.array(x_y_v_max)
with open("v_max.txt", "w") as o:
     for line in mat:
         print("{},{},{}".format(line[0], line[1], line[2]), file=o)              
mat1 = np.array(x_y_v_max_kmh)
with open("v_max_kmh.txt", "w") as o:
     for line in mat1:
         print("{},{},{}".format(line[0], line[1], line[2]), file=o)  
#Longueur circuit et vitesse selon la distance
d_circuit = np.zeros(len(x_circuit))
d = 0
x = np.linspace(0, 3600, 1000)
y = np.linspace(0, 60, 1000)
X, Y = np.meshgrid(x,y)
fig, ax = plt.subplots()
for i in range(1,len(x_circuit)-1, 1):
    d_x = x_circuit[i+1] - x_circuit[i]
    d_y = y_circuit[i+1] - y_circuit[i]
    d = np.sqrt(d_x**2 + d_y**2)
    d_circuit[i] += d + d_circuit[i-1]
    
    # plt.plot(d_circuit[i], v_max[i]*3.6, '-o')
plt.scatter(d_circuit, v_max*3.6)
plt.plot(d_circuit,v_max*3.6, 'o')
plt.show()




