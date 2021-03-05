# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:55:48 2021

@author: dhem.romain
"""
import random



def piece():
    
    t = ["Face","Pile"]
    r=random.choice(t)
    return r
    


def detectionpile():
    
    re = piece()
    print("La pièce est tombé sur",re)
    
    if re=="Pile":
        return("gagné")
        #inserer base de donnée
    else:
        return("perdu")
        
def detectionface():
    re = piece()
    
    print("La pièce est tombé sur",re)
    
    if re == "Face":
        return("gagné")
    else:
        return("perdu")
        


print(detectionpile())

