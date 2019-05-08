# ----------------------------------------------------------
# Cassebriques
# Gamebuino Academy Workshop
# 
# This is a CircuitPython port of the original C++ code
# Maybe not the more pythonic, but as close as possible
# to the original to be able to understand
# Original workshop: https://gamebuino.com/fr/academy/workshop/casse-briques/premiere-etape-titre-a-trouver
# ----------------------------------------------------------
# Author: TitiMoby
# Date: May 2019
# ----------------------------------------------------------

import gamebuino_meta as gb
from random import randint

def entrees():
    if (gb.buttons.repeat(gb.buttons.LEFT, 1) and raquette['X'] > 0):
        raquette['X'] -= 3
    elif (gb.buttons.repeat(gb.buttons.RIGHT, 1) and raquette['X'] < gb.display.width() - raquette['LARGEUR']):
        raquette['X'] += 3

def miseAJour():
    # MAJ Balle
    balle['X'] += balle['VX']
    balle['Y'] += balle['VY']
    
    # Collisions avec les murs
    if (balle['X'] < 0 or balle['X'] > gb.display.width() - balle['TAILLE']):
        balle['VX'] *= -1
    
    if (balle['Y'] < 0):
        balle['VY'] *= -1
    elif (balle['Y'] > gb.display.height()):
        reinitialiser()
        
    # Collision avec la raquette
    if (gb.collide.rectRect(balle['X'], balle['Y'], balle['TAILLE'], balle['TAILLE'], raquette['X'], raquette['Y'], raquette['LARGEUR'], raquette['HAUTEUR'])):
        balle['VY'] = -1 # Haut

def reinitialiser():
    balle['X'] = randint(0, gb.display.width() - balle['TAILLE'])
    balle['Y'] = raquette['Y'] - balle['TAILLE'] - 1 # Juste au dessus de la raquette
    balle['VX'] = 1  # Droite
    balle['VY'] = -1  # Haut

def affichage():
    gb.display.clear()
    
    # Raquette
    gb.display.fillRect(raquette['X'], raquette['Y'], raquette['LARGEUR'], raquette['HAUTEUR'])
    
    # Balle
    gb.display.fillRect(balle['X'], balle['Y'], balle['TAILLE'], balle['TAILLE'])

# Caractéristiques de la raquette
raquette = {
    'X': 40,
    'Y': 58,
    'LARGEUR': 10,
    'HAUTEUR': 2
}

# Caractéristiques de la balle
balle = {
    'X': 40,
    'Y': 60,
    'VX': 0,
    'VY': 0,
    'TAILLE': 3
}

reinitialiser()

while True:
  gb.waitForUpdate()
  # INPUTS
  entrees()
  # LOGIC
  miseAJour()
  # DRAW
  affichage()
