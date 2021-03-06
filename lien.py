# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 00:24:13 2020

@author: josse
"""

COMPLEMENT = 0
COMPLEMENT_LIEU = 1
COMPLEMENT_TEMPS = 2
COMPLEMENT_MANIERE = 3
OBJECTIF = 4
CAUSE = 5
CONSEQUENCE = 6
AJOUT = 7
SUITE = 8
LOINTAIN = 9


class Lien :

  def __init__ (self, coeur = None, typeLien = None, importance = 1):
    self.coeur = coeur # Objet Coeur vers lequel le lien pointe : ??? -> lien -> coeur
    self.typeLien = typeLien # Entier identifiant le type de lien (CAUSE = 1, CONSEQUENCE = 2, SUITE = 3)
    self.importance = max(0.000001,importance)
    

  def getGraphText(self):
      dict_liens = {COMPLEMENT: "Complément", COMPLEMENT_LIEU: "Lieu", COMPLEMENT_TEMPS: "Moment", COMPLEMENT_MANIERE: "Manière",
                    OBJECTIF: "Objectif", CAUSE: "Cause", CONSEQUENCE: "Conséquence", AJOUT: "Ajout", SUITE: "Suite", LOINTAIN: "Lointain"}
      s = """<table border="0" cellborder="0" cellspacing="0">\n"""
      s+= """   <tr><td align="center"><I>""" + dict_liens[self.typeLien] + "</I></td></tr>\n"
      s+= """   <tr><td align="center">""" + str(self.importance) + "</td></tr>\n"
      s+= "</table>"
      return s