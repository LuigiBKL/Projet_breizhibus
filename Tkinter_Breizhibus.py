# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:48:40 2020

@author: utilisateur
"""

from tkinter import*
from tkinter import ttk
from Connexion_Breizhibus_po import Connexion

class Breizhibus:

    def __init__(self):
        
        self.breizhibus = Tk()

#Fonction permettant d'afficher les arrets demandés par l'utilisateur à l'aide la combobox        
    def affichage_arret_ligne (self):
        
        self.selected_item = self.listeCombo.get()
        self.resultat = Connexion().recherche(self.selected_item)
        self.monAffichage.configure(text =  self.resultat)
        return self.selected_item

#Fonction permettant d'afficher les arrets demandés par l'utilisateur à l'aide la combobox        
    def affichage_info_bus (self):
        
        self.liste = []
        self.recupinfo = Connexion().recup_numero_bus()
        j = 1
        for i in  self.recupinfo:
            self.p = ("Bus",j,":",i)
            self.liste.append(self.p)
            j += 1 
        self.monAffichage5.configure(text = self.liste )
        
    
    def suppression_bus (self) :
        
        self.selected_item = self.listeCombo1.get()
        Connexion().suppression_bus_tkinter (self.selected_item)
    
    def ajout_bus (self):
        
        self.entree = self.entree.get()
        self.entree1= self.entree1.get()
        self.entree2 = self.entree2.get()
        self.entree3 = self.entree3.get()
        Connexion().ajout_bus_tkinter(self.entree,self.entree1,self.entree2,self.entree3)
    
    def modification_bus (self):
            
        self.entree = self.entree.get()
        self.entree1= self.entree1.get()
        self.entree2 = self.entree2.get()
        self.entree3 = self.entree3.get()
        Connexion().modification_bus_tkinter(self.entree,self.entree1,self.entree2,self.entree3)
    
    def construction(self):
        self.liste_bus = []
        #titre fenêtre principale
        self.breizhibus.title = ("Breizhibus")
        #largeur fenêtre
        self.breizhibus.geometry = ("900x700")
        #largeur minimale
        self.breizhibus.minsize(800,600)
        #changement du logo de fenetre_principale
        #self.breizhibus.iconbitmap("Breizhibus.ico")
        #couleur de fond
        self.breizhibus.config(background="#55557f")
        #titre dans la fenêtre
        self.breizhibus_titre = Label(self.breizhibus,text="Breizhibus", font=("Bradley Hand ITC",30),bg= "#55557f",fg="white")
        #copyrigth
        self.breizhibus_copyrigth = Label(self.breizhibus,text="Breizhibus by Luigi Bokalli", font=("Bradley Hand ITC",8),bg= "#55557f",fg="white")
        #création 1ère frame
        self.frame = Frame (self.breizhibus,bg="#55557f",bd=0,relief=SUNKEN)
        #titre dans la frame
        self.titre_frame = Label(self.frame,text= "Quelle ligne désirez-vous?", font=("Bradley Hand ITC",10),bg= "#55557f",fg="white")
        #création de la combobox
        self.liste_ligne_bus = ["13","14","15"]
        self.listeCombo = ttk.Combobox(self.frame,values =self.liste_ligne_bus)
        self.listeCombo.current(0)
        self.liste_bus = Connexion().recup_numero_bus()
        self.listeCombo1 = ttk.Combobox(self.frame,values =self.liste_bus)
        self.listeCombo1.current(0)
        self.bouton1 = Button ( self.frame , text = "Afficher les arrets de ligne" , font = ( "Algerian", 11 ), bg = "#55557f", fg= "white" , height = 1, width = 25,command= lambda: self.affichage_arret_ligne())
        self.bouton4 = Button ( self.frame , text = "Afficher la liste des bus" , font = ( "Algerian", 11 ), bg = "#55557f", fg= "white" , height = 1, width = 33,command= lambda: self.affichage_info_bus())
        self.monAffichage5= Label(self.frame,bg = "#55557f" , fg = "White", text = "",height = 1, width=100)
        self.bouton2 = Button (self.frame ,text = "Ajouter", font = ( "Algerian", 11 ), bg = "#55557f" , fg = "White" , height = 1 , width = 12)
        self.monAffichage= Label(self.frame,bg = "#55557f" , fg = "White", text = "", width=50)
        self.bouton2 = Button (self.frame ,text = "Ajouter Bus", font = ( "Algerian", 11 ), bg = "#55557f" , fg = "White" , height = 1 , width =18, command = lambda: self.ajout_bus())
        self.bouton3 = Button (self.frame ,text = "Modifier Bus", font = ( "Algerian", 11 ), bg = "#55557f" , fg = "White" , height = 1 , width = 18, command = lambda: self.modification_bus())
        self.bouton5 = Button (self.frame ,text = "Supprimer Bus", font = ( "Algerian", 11 ), bg = "#55557f" , fg = "White" , height = 1 , width = 18, command = lambda: self.suppression_bus())
        self.monAffichage1 = Label(self.frame,bg = "#55557f" , fg = "White", text = "Entrer un numéro de bus (4 caractères maximum", width=50)
        self.entree =  Entry(self.frame,  width=20)
        self.monAffichage2 = Label(self.frame,bg = "#55557f" , fg = "White", text = "Entrer une immatriculation  de bus (7 caractères maximum)", width=50)
        self.entree1 =  Entry(self.frame,  width=20)
        self.monAffichage3 = Label(self.frame,bg = "#55557f" , fg = "White", text = "Entrer le nombre de places", width=30)
        self.entree2 =  Entry(self.frame,  width=20)
        self.monAffichage4 = Label(self.frame,bg = "#55557f" , fg = "White", text = "A quelle ligne voulez-vous assigner ce bus ?", width=50)
        self.entree3 =  Entry(self.frame,  width=20)
        
        
        ##########################################################
       
        
       
       
        #affichage du titre principal     
        self.breizhibus_titre.pack()
        #affichage titre dans la frame
        self.titre_frame.pack()
        self.listeCombo.pack()
        #self.listeCombo.bind("<<ComboboxSelected>>",recuperer)
        self.bouton1.pack()
        self.monAffichage.pack()
        self.bouton4.pack()
        self.monAffichage5.pack()
        self.bouton2.pack(side = "left",pady = 5)
        self.bouton3.pack(side = "right",pady = 5)
        self.monAffichage1.pack(pady= 10)
        self.entree.pack(padx=5, pady=5)
        self.monAffichage2.pack()
        self.entree1.pack(padx=5, pady=0)
        self.monAffichage3.pack()
        self.entree2.pack(padx=5, pady=0)
        self.monAffichage4.pack()
        self.entree3.pack(padx=5, pady=0)
        
        self.listeCombo1.pack(pady = 5)
        self.bouton5.pack(pady = 5)
        #expansion de la frame
        self.frame.pack(side = TOP)
        #affichage du copyrigth  
        self.breizhibus_copyrigth.pack(side=BOTTOM)
        #affichage de la fenêtre
        self.breizhibus.mainloop()
    
        
   
        

#Breizhibus().construction()

        
        
        