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
    if (gb.collide.rectRect(balle['X'], balle['Y'], balle['TAILLE'], balle['TAILLE'], \
        raquette['X'], raquette['Y'], raquette['LARGEUR'], raquette['HAUTEUR'])):
        balle['VY'] = -1 # Haut
    
    # Collision avec les briques
    for rangee in range(0, briques['GRILLE_TAILLE']):
        for colonne in range(0, briques['GRILLE_TAILLE']):
            if (briques['grille'][rangee][colonne] == 0):
                # Ignorer les briques nulles
                pass  # 'pass' force la boucle à passer a recommencer (et donc incrémenter)
            
            briqueX = colonne * (briques['BRIQUE_LARGEUR'] + 2) + 1
            briqueY = rangee * (briques['BRIQUE_HAUTEUR'] + 2) + 1
            if (gb.collide.rectRect(balle['X'], balle['Y'], balle['TAILLE'], balle['TAILLE'], \
                briqueX, briqueY, briques['BRIQUE_LARGEUR'], briques['BRIQUE_HAUTEUR'])):
                balle['VY'] *= -1
                briques['grille'][rangee][colonne] = 0 # Détruire la brique
                # Verifier qu'il reste encore des briques
                encoreDesBriques = False  # Si ce booléen reste faux, alors il n'y a plus de briques
                for x in range(0, briques['GRILLE_TAILLE']):
                    for y in range(0, briques['GRILLE_TAILLE']):
                        if (briques['grille'][x][y] == 0):
                            # On a trouver une brique!
                            encoreDesBriques = True  # Il reste encore au moins une brique
                
                if (encoreDesBriques == False):
                    # S'il n'y a plus de briques
                    reinitialiser()

def reinitialiser():
    balle['X'] = randint(0, gb.display.width() - balle['TAILLE'])
    balle['Y'] = raquette['Y'] - balle['TAILLE'] - 1 # Juste au dessus de la raquette
    balle['VX'] = 1  # Droite
    balle['VY'] = -1  # Haut
    for rangee in range(0, briques['GRILLE_TAILLE']):
        for colonne in range(0, briques['GRILLE_TAILLE']):
            briques['grille'][rangee][colonne] = 3 # Faire réapparaitre toutes les briques


def affichage():
    gb.display.clear()
    
    # Raquette
    gb.display.fillRect(raquette['X'], raquette['Y'], raquette['LARGEUR'], raquette['HAUTEUR'])
    
    # Balle
    gb.display.fillRect(balle['X'], balle['Y'], balle['TAILLE'], balle['TAILLE'])

    # Briques
    arcEnCiel = [gb.color.WHITE, gb.color.PURPLE, gb.color.RED, gb.color.YELLOW, gb.color.LIGHTGREEN, gb.color.GREEN, gb.color.DARKBLUE, gb.color.BLUE]

    for rangee in range(0, briques['GRILLE_TAILLE']):
        for colonne in range(0, briques['GRILLE_TAILLE']):
            if (briques['grille'][rangee][colonne] != 0):
                    gb.display.setColor(arcEnCiel[ briques['grille'][rangee][colonne] - 1 ]);
                    briqueX = colonne * (briques['BRIQUE_LARGEUR'] + 2) + 1
                    briqueY = rangee * (briques['BRIQUE_HAUTEUR'] + 2) + 1
                    gb.display.fillRect(briqueX, briqueY, briques['BRIQUE_LARGEUR'], briques['BRIQUE_HAUTEUR'])

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

# Briques. Chaque entier correspond à une couleur
briques = {
    'GRILLE_TAILLE': 8,
    'BRIQUE_HAUTEUR': 3
}
briques['grille']=[x[:] for x in [[0] * briques['GRILLE_TAILLE']] * briques['GRILLE_TAILLE']] # Tableau 2D
briques['BRIQUE_LARGEUR'] = gb.display.width() // briques['GRILLE_TAILLE'] - 2 

reinitialiser()

while True:
  gb.waitForUpdate()
  # INPUTS
  entrees()
  # LOGIC
  miseAJour()
  # DRAW
  affichage()
