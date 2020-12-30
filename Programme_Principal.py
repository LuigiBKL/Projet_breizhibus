# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:43:24 2020

@author: utilisateur
"""
from Connexion_Breizhibus_po import Connexion

from Tkinter_Breizhibus import Breizhibus

"""
Affichage des lignes et des différents arrêts dans une interface graphique (Tkinter)
"""
Breizhibus().construction()

"""
ajouter un bus 
"""
#Connexion().ajout_bus()


"""
modifier  un bus 
"""
#Connexion().modification_bus()


"""
supprimer un bus 
"""
#Connexion().suppression_bus()