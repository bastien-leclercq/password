import random
import hashlib
import json

Pass = input ("Entrez votre mot de passe : ")
historique = [ ]

def password(Pass):
    l = ["0","1","2","3","4","5","6","7","8","9"]
    n = 0
    for j in Pass:
        if j in l:
            n = 1
    x = ["@","!","?","-","_","#","[","]","{","}"]
    y = 0
    for j in Pass:
        if j in x:
            y = 1
    if len(Pass)<8:
        print("Entrez un mot de pass d'au moins 8 caractères")
    if Pass == Pass.lower():
        print("votre mot de passe doit contenir au moins une Majuscule")
    if Pass == Pass.upper():
        print("votre mot de passe doit contenir au moins une Minuscule")
    if n == 0:
        print("votre mot de passe doit contenir au moins un Chiffre")
    if y == 0:
       print("Votre mot de pass doit contenir au moins un Caractère Spéciale (@, !, ?, -, _, #, [, ], {, })")
    if len(Pass) >= 8 and Pass != Pass.lower() and Pass != Pass.upper() and n == 1 and y == 1:
        print("Mot de passe accpeté")
    h = hashlib.sha256(Pass.encode('utf-8'))
    historique.append (hashlib.sha256(Pass.encode('utf-8')))
    print(h.hexdigest())
    




password(Pass)