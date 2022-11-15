import numpy as np
Vinit = 25.0;


def Simu(Vinitiale):
    Moteur = 1; #1 valant moteur_on, 0 moteur_off
    compt = 0;
    V=[35.0,32.0,27.0,22.0,34.0];
    Vitesse = 0;
    M = np.zeros ((25,2));
    
    M[0][0] = Vinit; #M[ligne][colonne]
    M[0][1] = Moteur ; 
    
    i=0;
    while compt < 5 : #dans réalité 144 : 3600/25[notre intervalle]
    
        if i%2 == 0 :
            Moteur = 1;
        else:
            Moteur = 0;
            
            
        Vitesse = V[i];
        
        i = i + 1;
    
        #Vitesse = Sortie AppelDymola(M[i-1][1]Moteur)
        if Vitesse <35.0 and Vitesse >23.0 :
            M[i][1] = Moteur;
            M[i][0] = Vitesse;
    
        compt = compt + 1; # +25 dans réalité car c'est notre intervalle de distance
    M = M[~np.all(M == 0, axis=1)]
    print (M);

Simu(Vinit);

