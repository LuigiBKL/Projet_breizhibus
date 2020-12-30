# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:57:57 2020

@author: utilisateur
"""

import mysql.connector as mysqlpyth

class Connexion :    
    
    def __init__ (self):
        
         self.bdd = mysqlpyth.connect(
            host="localhost",
            port="3306",
            user="root", 
            password="root", 
            database="breizhibus")
         self.cursor = self.bdd.cursor()

#recherche des arrêts en fonciton des lignes 

    def recherche (self,numero_ligne):
        
        ligne_bus = []
        stockage = []
        arrets = {}
        
        self.cursor.execute(f"SELECT  id_ligne, nom FROM arrets_lignes JOIN arrets on arrets.id_arret = arrets_lignes.id_arret WHERE id_ligne ={numero_ligne}")
        curseur = self.cursor.fetchall()
        
        for id_ligne, id_arret in curseur:
            ligne_bus =[(id_ligne,id_arret)]
            stockage = stockage + ligne_bus
        for key, value in stockage:    
            arrets.setdefault(key,[]).append(value)
        
        self.cursor.close()
        self.bdd.close()
    
        return arrets

#récupération des lignes de bus    

    def recup_ligne_bus (self):
        
        self.cursor.execute("SELECT id_ligne FROM lignes")
        self.id_ligne = [ i[0] for i in self.cursor.fetchall()]
        
        return self.id_ligne
    
#récupération de tous les bus    

    def recup_infos_bus (self):
        
        self.cursor.execute("SELECT *FROM bus")
        self.bus = self.cursor.fetchall()
        
        return self.bus

#récupération des numéros de bus
    
    def recup_numero_bus (self):
        
        self.cursor.execute("SELECT numero from bus")
        self.immatriculation_bus = [ i[0] for i in self.cursor.fetchall()]
        return self.immatriculation_bus
 
#récupération des immatriculations de bus        
 
    def recup_immatriculation_bus (self):
        
        self.cursor.execute("SELECT immatriculation from bus")
        self.numero_bus = [i[0] for i in  self.cursor.fetchall()]
        return self.numero_bus

###################################################################################################

#Fonction propres à la console interne 

#Fonction permettant d'ajouter un bus
    
    def ajout_bus (self):

        self.immatriculation_bus = Connexion().recup_immatriculation_bus()
        self.numero_bus = Connexion().recup_numero_bus()
        self.ligne_bus = Connexion().recup_ligne_bus()
        
        print("Bus déjà existant(s)",self.numero_bus)
        
        self.numero = str(input("Entrer un numéro de bus (4 caractères maximum): "))
        self.numero = self.numero.upper()
        
        
#Cette instruction permet d'éviter les doublons dans la liste des bus de la base donnée

        if self.numero in  self.numero_bus:
            
            print ("Bus déjà existant")
        
        else:
        
            print("Voici la liste des immatricualtions déjà existantes",self.immatriculation_bus)
            self.immatriculation = str(input("Saisissez une immatriculation  (7 caractères maximum) :"))
            self.immatriculation = self.immatriculation.upper()
            
            if self.immatriculation in self.immatriculation_bus:
                print("Immatricualtion déjà existante")
            else:
                
                self.nbre_place = (input("Veuillez saisir le nombre de place :"))
                
                print("numéro de ligne disponible:",self.ligne_bus)
                self.numero_ligne = int(input("A Quelle ligne désirez-vous l'assignez ?: "))
                
# Permet d'éviter de créer une nouvelle ligne de bus 
                
            if self.numero_ligne in self.ligne_bus : 
               
                try:
                    self.cursor.execute ("INSERT INTO bus(numero, immatriculation, nombre_place,id_ligne) VALUES (%s,%s,%s,%s)",(self.numero,self.immatriculation,self.nbre_place,self.numero_ligne))
                    self.bdd.commit()
                    print ("Ajout Terminé avec succès")
                except: 
                    
                    print("Cette ligne de bus n'existe pas")
                
        self.cursor.close()
        self.bdd.close()
                
    def modification_bus (self):
        
        self.immatriculation_bus = Connexion().recup_immatriculation_bus()
        self.numero_bus = Connexion().recup_numero_bus()
        print("Voici la liste des numéros de bus modifiables:",self.numero_bus)
        
        self.numero = (input("Quel numero de bus souhaitez-vous modifier?:"))
        self.numero = self.numero.upper()

#Cette instruction permet d'éviter les doublons dans la liste des bus de la base donnée
            
        if self.numero in self.numero_bus:
            print("Voici la liste des immatricualtions déjà existantes",self.immatriculation_bus)
            self.immatriculation = (input("Saisissez une immatriculation (7 caractères maximum) :"))
            self.immatriculation = self.immatriculation.upper()
            self.nbre_place = (input("Veuillez saisir le nombre de place: "))
            self.numero_ligne = int(input("A Quelle ligne désirez-vous l'assignez ? (lignes disponibles : 13,14,15): "))
            self.ligne_bus = Connexion().recup_ligne_bus()

# Permet d'éviter de créer une ligne de bus inexistante     
            
            if self.numero_ligne  in self.ligne_bus :
               self.cursor.execute("UPDATE bus SET immatriculation = '%s', nombre_place=%s, id_ligne = %s WHERE numero = '%s'"%(self.immatriculation, self.nbre_place, self.numero_ligne, self.numero))
               self.bdd.commit()
               print ("Modification Terminée avec succès")
            else:
               
                print ("Ligne inexistante")
        else:
           
            print("Numéro de bus inexistant")
        
        self.cursor.close()
        self.bdd.close()
        
    def suppression_bus (self):
   
        self.numero_bus = Connexion().recup_numero_bus()
        print("Voici la liste des numéros de bus déjà existants:",self.numero_bus)
        
        self.numero = (input("Quel numero de bus souhaitez-vous supprimer?:"))
        
        if self.numero in self.numero:
            
            self.cursor.execute(f"DELETE FROM bus WHERE numero = '{self.numero}'")
            self.bdd.commit()
            print ("Suppression  Terminée avec succès")
        else:
            
            print("Numéro de bus inexistant")
        
        self.cursor.close()
        self.bdd.close()

    # Fonction propres à tkinter 

    def ajout_bus_tkinter (self,numero,immatriculation,nbre_place,numero_ligne):
    
        self.immatriculation_bus = Connexion().recup_immatriculation_bus()
        self.numero_bus = Connexion().recup_numero_bus()
        self.ligne_bus = Connexion().recup_ligne_bus()
        
        #print("Bus déjà existant(s)",self.numero_bus)
        
        numero = (numero)
        numero = numero.upper()
        
        
#Cette instruction permet d'éviter les doublons dans la liste des bus de la base donnée

        if numero in  self.numero_bus:
            
            print ("Bus déjà existant")
        
        else:
        
            #print("Voici la liste des immatricualtions déjà existantes",self.immatriculation_bus)
            immatriculation = (immatriculation)
            immatriculation = immatriculation.upper()
            
            if immatriculation in self.immatriculation_bus:
                print("Immatricualtion déjà existante")
            else:
                
                nbre_place = (nbre_place)
                
                
                numero_ligne = (numero_ligne)
                
# Permet d'éviter de créer une nouvelle ligne de bus 
                
            if numero_ligne in self.ligne_bus : 
               
                try:
                    self.cursor.execute ("INSERT INTO bus(numero, immatriculation, nombre_place,id_ligne) VALUES (%s,%s,%s,%s)",(numero,immatriculation,nbre_place,numero_ligne))
                    self.bdd.commit()
                    print ("Ajout Terminé avec succès")
                except: 
                    
                    print("Cette ligne de bus n'existe pas")
                
        self.cursor.close()
        self.bdd.close()

    def modification_bus_tkinter (self,numero,immatriculation,nbre_place,numero_ligne):
            
        self.immatriculation_bus = Connexion().recup_immatriculation_bus()
        self.numero_bus = Connexion().recup_numero_bus()
        print("Voici la liste des numéros de bus modifiables:",self.numero_bus)
        
        numero = str(numero)
        numero = numero.upper()

#Cette instruction permet d'éviter les doublons dans la liste des bus de la base donnée
            
        if numero in self.numero_bus:
            print("Voici la liste des immatricualtions déjà existantes",self.immatriculation_bus)
            immatriculation = str(immatriculation)
            immatriculation = immatriculation.upper()
            nbre_place = int(nbre_place)
            numero_ligne = int(numero_ligne)
            self.ligne_bus = Connexion().recup_ligne_bus()

# Permet d'éviter de créer une ligne de bus inexistante     
            
            if numero_ligne  in self.ligne_bus :
               self.cursor.execute("UPDATE bus SET immatriculation = '%s', nombre_place=%s, id_ligne = %s WHERE numero = '%s'"%(immatriculation, nbre_place, numero_ligne, numero))
               self.bdd.commit()
               print ("Modification Terminée avec succès")
            else:
               
                print ("Ligne inexistante")
        else:
           
            print("Numéro de bus inexistant")
        
        self.cursor.close()
        self.bdd.close()
        
    def suppression_bus_tkinter (self,numero):
   
        self.numero_bus = Connexion().recup_numero_bus()
       
        
        if numero in self.numero_bus:
            
            self.cursor.execute(f"DELETE FROM bus WHERE numero = '{numero}'")
            self.bdd.commit()
        
        else:
            
            print("Numéro de bus inexistant")
        
        self.cursor.close()
        self.bdd.close()
