# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 16:00:45 2021

@author: equin
"""


from flask import Flask, render_template, request, redirect
import sqlite3
import random

app = Flask(__name__)

p = ""
sm = 0
tw = 0
tc = 0
un = 0
deux = 0
trois = 0
quatre = 0
cinq = 0



conn = sqlite3.connect('SQL.db', timeout=10, check_same_thread=False)
cur = conn.cursor()

liste = cur.fetchall()


@app.route('/login')
def login():
   return render_template("index1.html",data=liste)

@app.route('/dashboard', methods = ['POST', 'GET'])    
def log():
    global p, sm, tw, tc, un
    
    p = request.form['Pseudo']
    user_check = cur.execute("SELECT * FROM pseudo WHERE user = ?", (p,)).fetchone()
    if user_check == None:    
        cur.execute("INSERT INTO pseudo (user, score, win, coup, un, deux, trois, quatre, cinq) VALUES (?,?,?,?,?,?,?,?,?)", (p,0,0,0,0,0,0,0,0))
        conn.commit()
    
    lsm = cur.execute("SELECT score FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    sm = lsm[0][0]

    ltw = cur.execute("SELECT win FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tw = ltw[0][0]
    
    ltc = cur.execute("SELECT coup FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tc = ltc[0][0]    
    
    lun = cur.execute("SELECT un FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    un = lun[0][0]

    ldeux = cur.execute("SELECT deux FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    deux = ldeux[0][0]
    
    ltrois = cur.execute("SELECT trois FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    trois = ltrois[0][0]
    
    lquatre = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    quatre = lquatre[0][0]
    
    lcinq = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    cinq = lcinq[0]


    
    return render_template("index.html",data=liste,Pseudo = p, scoremax = sm, totalwin = tw, totalcoups = tc, un = un, deux = deux, trois = trois, quatre = quatre, cinq = cinq)

@app.route('/pile', methods = ['POST', 'GET'])    
def pile():
    
    
    t = ["Face","Pile"]
    re=random.choice(t)
    
    if re=="Pile":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1,
                         cinq = quatre,
                         quatre = trois,
                         trois = deux,
                         deux = un,
                         un = 1
                     WHERE user = ?''',(p,))
        conn.commit()
            
            
        res = "La pièce est tombé sur ",re, " gagné"
        
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1,
                         cinq = quatre,
                         quatre = trois,
                         trois = deux,
                         deux = un,
                         un = 0
                     WHERE user = ?''',(p,))
        conn.commit()
        res = "La pièce est tombé sur ",re, " perdu"
    
    lun = cur.execute("SELECT un FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    un = lun[0][0]

    ldeux = cur.execute("SELECT deux FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    deux = ldeux[0][0]
    
    ltrois = cur.execute("SELECT trois FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    trois = ltrois[0][0]
    
    lquatre = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    quatre = lquatre[0][0]
    
    lcinq = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    cinq = lcinq[0]

    lsm = cur.execute("SELECT score FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    sm = lsm[0][0]

    ltw = cur.execute("SELECT win FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tw = ltw[0][0]
    
    ltc = cur.execute("SELECT coup FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tc = ltc[0][0]    

    return render_template("index.html",data=liste, resultat=res, Pseudo = p, scoremax = sm, totalwin = tw, totalcoups = tc, un = un, deux = deux, trois = trois, quatre = quatre, cinq = cinq)

@app.route('/face', methods = ['POST', 'GET'])    
def face():
    
    t = ["Face","Pile"]
    re=random.choice(t)
    
    if re == "Face":
        conn.execute('''UPDATE pseudo
                     SET score= score + 1,
                         win = win + 1,
                         coup = coup + 1,
                         cinq = quatre,
                         quatre = trois,
                         trois = deux,
                         deux = un,
                         un = 0
                     WHERE user = ?''',(p,))
        conn.commit()
        res = "La pièce est tombé sur ",re, " gagné"
        
        
    else:
        conn.execute('''UPDATE pseudo
                     SET score= 0,
                         coup = coup + 1,
                         cinq = quatre,
                         quatre = trois,
                         trois = deux,
                         deux = un,
                         un = 0
                     WHERE user = ?''',(p,))
        conn.commit()
        res = "La pièce est tombé sur ",re, " perdu"
        
    lun = cur.execute("SELECT un FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    un = lun[0][0]

    ldeux = cur.execute("SELECT deux FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    deux = ldeux[0][0]
    
    ltrois = cur.execute("SELECT trois FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    trois = ltrois[0][0]
    
    lquatre = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    quatre = lquatre[0][0]
    
    lcinq = cur.execute("SELECT cinq FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    cinq = lcinq[0][0]
        
    lsm = cur.execute("SELECT score FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    sm = lsm[0][0]

    ltw = cur.execute("SELECT win FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tw = ltw[0][0]
    
    ltc = cur.execute("SELECT coup FROM pseudo WHERE user = ?", (p,)).fetchall()
    conn.commit()
    tc = ltc[0][0]    
    
        
    return render_template("index.html",data=liste, resultat=res, Pseudo = p, scoremax = sm, totalwin = tw, totalcoups = tc, un = un, deux = deux, trois = trois, quatre = quatre, cinq = cinq)

app.run(debug=True, use_reloader=False)
