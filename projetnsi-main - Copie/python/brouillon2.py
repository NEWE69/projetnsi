# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 11:55:48 2021

@author: dhem.romain
"""
import random
import sqlite3


def piece():
    
    t = ["Face","Pile"]
    r=random.choice(t)
    return r
    


def detectionpile():
    
    re = piece()
    print("La pièce est tombé sur",re)
    
    if re=="Pile":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        return("gagné")
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        return("perdu")
        
def detectionface():
    re = piece()
    
    print("La pièce est tombé sur",re)
    
    if re == "Face":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        return("gagné")
        
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        return("perdu")

    
conn = sqlite3.connect('SQL.db', timeout=10)
cur = conn.cursor()



print(detectionpile())
