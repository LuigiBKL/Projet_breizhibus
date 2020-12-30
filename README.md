# Projet_breizhibus
Projet visant à gérer (ajouter/supprimer/modifier) une base de données de bus  à l'aide d'un script python ou d'une interface graphique faite par nos soins

Pour ce qui est de l'organisation j'ai décidé de programmer en orienté objet pour m'exercer , et donc on distingue 3 principaux fichiers à savoir:

## Connexion_Breizhibus_po.py 

Ce fichier va nous permettre: 

-de nous connecter à la base de donnée déjà existante (breizhibus.sql)

-de nous afficher les différents arrêts en fonction des lignes 

-d'effectuer différentes opérations à savoir récupérer les informations dont à besoin (ajouter un bus,modiffier un  bus,supprimer un bus). J'ai décidé de de créer deux types de fonctions : en premier les fonctions propres à la console interne sans passer par tkinter  (visual code, python) qui permet d'effectuer les opérations que l'on veut , et en deuxième partie les fonctions qui seront utilisées par tkinter (l'interface graphique créee par mes soins ).


Je me suis assuré lors de l'ajout ou de la modification d'un bus que l'on n'ait pas de doublons de bus, de numéro de d'immatricualtion, et que l'on ne puisse pas creer de nouvelles lignes


### Programme_Principal.py

Ce fichier permet d'executer directement tous les opérations citées plus haut juste en appelant les fonctions servant à executer les tâches désirées


### Tkinter_Breizhibus.py

Dans ce fichier, on retrouve toute la partie graphique tkinter avec les différentes fonctions necessaires 

