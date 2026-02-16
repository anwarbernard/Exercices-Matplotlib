# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 08:51:22 2026

@author: anwar
"""
import numpy as np
import matplotlib.pyplot as plt

# Exo 1

def dessin(x, taby, tablegende, tabcouleur, nomfic):
    fig, ax = plt.subplots()
    nby = len(taby)
    for i in range(nby):
        ax.plot(x, taby[i], label=tablegende[i])
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    #ax.set(xlim = (-5,2), ylim = (-10, 30))
    ax.legend(loc = 9, ncol = nby, labelcolor = tabcouleur, 
              bbox_to_anchor = (0.5,1.1), borderaxespad = 0)
    fig.savefig(nomfic+".jpg")
    
# x = np.linspace(-2,2,1000)
# y = [0,0,0,0]
# legende = ["$cos(40x)$","$exp(-x^2)$","$-exp(-x^2)$","$cos(40x)*exp(-x^2)$"]
# couleur = ["blue","blue","orange","green"]
# y[0] = np.cos(40*x)
# y[1] = np.exp(-x**2)
# y[2] = -np.exp(-x**2)
# #y[3] = np.cos(40*x)*np.exp(-x**2)
# y[3] = y[0]*y[1]
# dessin(x,y[1:],legende[1:],couleur[1:],"gex1")

# Exo 2

# avec les tableaux x et y de l'exercice précédent
# fig,ax = plt.subplots(nrows=2, ncols=3)
# i=1
# ax[0,0].plot(x,y[1])
# ax[0,0].plot(x,y[2])
# ax[0,0].plot(x,y[3])
# ax[0,1].plot(x,y[3])
# ax[0,2].plot(x,y[1])
# ax[0,2].plot(x,y[2])
# ax[1,0].plot(x,y[0])
# ax[1,1].plot(x,y[1])
# ax[1,2].plot(x,y[2])
# plt.show()
# fig.savefig("ggrille.jpg")

# Exo 3

# x = np.linspace(-2,2,100)
# y = np.linspace(-2,2,100)
# xx, yy = np.meshgrid(x, y, sparse = True)
# z = ((xx-yy)*(xx+yy)**2*(xx**2+yy))
# h = plt.contourf(x,y,z)
# plt.show()

# Exo 4

x = np.linspace(0,50,500)
y = [0,0,0]
legende = ["$sin(x)$","$exp(-x/10)$","$sin(x)*exp(-x/10)$"]
couleur = ["blue","blue","orange"]
y[0] = np.sin(x)
y[1] = np.exp(-x/10)
y[2] = y[0] * y[1]
dessin(x,y[1:],legende[1:],couleur[1:],"gex3")