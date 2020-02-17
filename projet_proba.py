#Projet proba 

#Chargement de dépendances
import numpy as np
import matplotlib.pyplot as plt
#Discrétisation
A=0
B=500
N=101 #Nombre de points de discrétisation
Delta = (B-A)/(N-1)
discretization_indexes = np.arange(N)
discretization = discretization_indexes*Delta
#Paramètres du modèle
mu=-5
a = 50
sigma = 12
#Données
observation_indexes = [0,20,40,60,80,100]
depth = np.array([0,-4,-12.8,-1,-6.5,0])
#Indices des composantes correspondant aux observations et aux componsantes non observées
18
unknown_indexes=list(set(discretization_indexes)-set(observation_indexes))

###

#QUESTION 1
# Correspond à la fonction C(h) donnée dans l'énoncé. cov_1 ne marche pas avec une matrice, mais cov si.
def cov_1(dist, a, sigma):
    return sigma**2 * np.exp(-dist/a)

cov = np.vectorize(cov_1)

#QUESTION 2
# Calcul de la matrice de distance 
M_dist = np.array([[Delta*abs(i-j) for i in range(N)] for j in range (N)])

#QUESTION 3
# On passe la matrice des distances par la fonction cov pour obtenir la matrice de covariance
M_cov = cov(M_dist, a, sigma)

#QUESTION 4
# Pour la matrice de cov des observations, il suffit d'extraire les éléments d'indices dans la liste observation_indexes
M_cov_obs = np.array([[M_cov[i, j] for i in observation_indexes] for j in observation_indexes])


#M_cov_inc


#QUESTION 8
# Calcule la longueur du câble avec en argument le vecteur des profondeurs depth et le pas de discrétisation Delta
def long_cable(depth, Delta) :
    S = 0
    for i in range(len(depth)-1):
        S += np.sqrt(Delta**2 + (depth[i+1] - depth[i])**2)
    return S
        
        

        
        