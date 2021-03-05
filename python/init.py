# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:00:45 2021

@author: equin
"""


from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)


conn = sqlite3.connect('SQL.db', timeout=10, check_same_thread=False)
cur = conn.cursor()

liste = cur.fetchall()


def piece():
    
    t = ["Face","Pile"]
    r=random.choice(t)
    return r
    


def detectionpile():
    
    re = piece()
    
    if re=="Pile":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        resultat = "La pièce est tombé sur ",re, " gagné"
        return(resultat)
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        resultat = "La pièce est tombé sur ",re, " perdu"
        return(resultat)
        
def detectionface():
    re = piece()
    
    if re == "Face":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        resultat = "La pièce est tombé sur ",re, " gagné"
        return(resultat)
        
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1
                     WHERE user = "ewen"''')
        conn.commit()
        resultat = "La pièce est tombé sur ",re, " perdu"
        return(resultat)


@app.route('/login')
def login():
   return render_template("index1.html",data=liste)

@app.route('/dashboard', methods = ['POST', 'GET'])    
def log():
    p = request.form['Pseudo']
    user_check = cur.execute("SELECT * FROM pseudo WHERE user = ?", (p,)).fetchone()
    if user_check == None:    
        cur.execute("INSERT INTO pseudo (user, score, win, coup) VALUES (?,?,?,?)", (p,0,0,0))
        conn.commit()
    
    return render_template("index.html",data=liste,Pseudo = p)

@app.route('/dashboard', methods = ['POST', 'GET'])    
def game():
    
    return render_template("index.html",data=liste)

app.run(debug=True, use_reloader=False)
