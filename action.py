# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 19:19:21 2020

@author: josse
"""

import random
import re


from psclib.diversifieur import get_syn
from psclib.diversifieur import cong



class Action :

  def getAvailable():
    return ["s'exercer", "decider", "payer", "choisir", "acheter", "faire a manger", "manger", "aller", "courir", "marcher", "attaquer", "tomber", "casser", "chanter", "parler", "regarder", "raconter", "voir", "ecrire", "boire",
            "crier", "sourir", "sauter", "ecouter", "dormir", "travailler", "trouver", "devenir", "balader", "ecraser", "rouler", "soigner", "aller voir", "se défouler","discuter","s'occuper","faire","tenir","livrer",
            "vendre","patrouiller","se balader","se reposer","forger","tanner","fabriquer","chasser","installer","traiter","s'informer","réparer","moudre","reporter","couper", "exercer","rencontrer", "battre","continuer","pêcher", "monter","scier"]

  def getAlike(s):
    """ Renvoie toutes les actions qui contiennent s dans leur nom"""
    liste = []
    for action in Action.getAvailable():
      if s in action:
        liste.append(action)
    return liste

  def __init__(self, lib = None, expressions = None, adverbes = [], name=None):

    if not(name is None):
      if not(name in Action.getAvailable()) : raise NameError('Il n\'y a pas d\'Action nommée ' + name)
      
      if name == "aller" : self = Action.__init__(self, "aller", [[1, "[aller]"]] )
      if name == "acheter" : self = Action.__init__(self, "acheter", [[1, "[(acheter)]"]] )
      if name == "attaquer" : self = Action.__init__(self, "attaquer", [[0.8,"[(attaquer)]"], [0.2,"[tomber] sur"]] )
      if name == "balader"  : self = Action.__init__(self, "balader", [[0.5, "[balader]"], [0.5, "[promener]"]])
      if name == "boire"  : self = Action.__init__(self, "boire", [[1, "[(boire)]"]])
      if name == "casser"  : self = Action.__init__(self, "casser", [[1, "[(casser)]"]])
      if name == "chanter" : self = Action.__init__(self, "chanter", [[1, "[(chanter)]"]])
      if name == "choisir" : self = Action.__init__(self, "choisir", [[1, "[choisir]"]] )
      if name == "courir": self = Action.__init__(self, "courir", [[1, "[(courir)]"]])
      if name == "crier"  : self = Action.__init__(self, "crier", [[1, "[(crier)]"]])
      if name == "decider" : self = Action.__init__(self, "décider", [[1, "[(décider)]"]])
      if name == "devenir" : self = Action.__init__(self, "devenir", [[1, "[(devenir)]"]])
      if name == "dormir"  : self = Action.__init__(self, "dormir", [[1, "[(dormir)]"]])
      if name == "ecouter" : self = Action.__init__(self, "écouter", [[1, "[(écouter)]"]])
      if name == "ecraser"  : self = Action.__init__(self, "ecraser", [[0.7, "[ecraser]"], [0.3, "[ecrabouiller]"]])
      if name == "ecrire"  : self = Action.__init__(self, "écrire", [[1, "[(écrire)]"]])
      if name == "manger": self = Action.__init__(self, "manger", [[1.0, "[(manger)]"], [0.0, "[se prendre] une part"], [0.0, "[casser] la croute"]])
      if name == "marcher" : self = Action.__init__(self, "marcher",[ [0.7,"[(marcher)]"], [0.3, "[aller] à pieds"]])
      if name == "parler"  : self = Action.__init__(self, "parler", [[1, "[(parler)]"]])
      if name == "payer"  : self = Action.__init__(self, "payer", [[1, "[(payer)]"]])
      if name == "raconter" : self = Action.__init__(self, "raconter", [[0.5, "[(raconter)]"], [0.2, "[(expliquer)]"], [0.3, "[(dire)]"]])
      if name == "regarder" : self = Action.__init__(self, "regarder", [[1, "[(regarder)]"]])
      if name == "rouler" : self = Action.__init__(self, "rouler", [[1, "[(rouler)]"]])
      if name == "sauter"  : self = Action.__init__(self, "sauter", [[1, "[(sauter)]"]])
      if name == "sourire"  : self = Action.__init__(self, "sourire", [[1, "[(sourire)]"]])
      if name == "tomber"  : self = Action.__init__(self, "tomber", [[1, "[(tomber)]"]] )
      if name == "travailler": self = Action.__init__(self, "travailler", [[0.8, "[(travailler)]"],[0.2, "[faire] un effort"]])
      if name == "trouver" : self = Action.__init__(self, "trouver", [[1, "[(trouver)]"]])     
      if name == "voir"   : self = Action.__init__(self, "voir",  [[0.8, "[(voir)]"],[0.2, "[prendre] conscience de"]])
      if name == "soigner"   : self = Action.__init__(self, "soigner",  [[0.8, "[(soigner)]"],[0.2, "[guérir]"]])
      if name == "aller voir"   : self = Action.__init__(self, "aller voir",  [[0.6, "[aller] voir"],[0.4, "[aller] consulter"]])
      if name == "se défouler"  : self = Action.__init__(self, "se défouler",  [[0.6, "[se défouler]"],[0.4, "[se dégourdir] les pattes"]])
      if name == "faire a manger"  : self = Action.__init__(self, "faire à manger",  [[0.6, "[faire] à manger"],[0.2, "[cuisiner]"], [0.2, "[préparer]"]])
      if name == "discuter"  : self = Action.__init__(self, "discuter", [[1, "[discuter]"]] )
      if name == "s'occuper"  : self = Action.__init__(self, "s'occuper", [[1, "[s'occuper]"]] )
      if name == "faire"  : self = Action.__init__(self, "faire", [[1, "[faire]"]] )
      if name == "tenir"  : self = Action.__init__(self, "tenir", [[1, "[tenir]"]] )
      if name == "livrer"  : self = Action.__init__(self, "livrer", [[1, "[(livrer)]"]] )
      if name == "patrouiller"  : self = Action.__init__(self, "patrouiller", [[1, "[(patrouiller)]"]] )
      if name == "se balader"  : self = Action.__init__(self, "se balader", [[1, "[se balader]"]] )
      if name == "se reposer"  : self = Action.__init__(self, "se reposer", [[1, "[se reposer]"]] )
      if name == "forger"  : self = Action.__init__(self, "forger", [[1, "[(forger)]"]] )
      if name == "tanner"  : self = Action.__init__(self, "tanner", [[1, "[(tanner)]"]] )
      if name == "fabriquer"  : self = Action.__init__(self, "fabriquer", [[1, "[(fabriquer)]"]] )
      if name == "chasser"  : self = Action.__init__(self, "chasser", [[1, "[(chasser)]"]] )
      if name == "installer"  : self = Action.__init__(self, "installer", [[1, "[(installer)]"]] )
      if name == "traiter"  : self = Action.__init__(self, "traiter", [[1, "[(traiter)]"]] )
      if name == "s'informer"  : self = Action.__init__(self, "s'informer", [[1, "[s'informer]"]] )
      if name == "réparer"  : self = Action.__init__(self, "réparer", [[1, "[(réparer)]"]] )
      if name == "moudre"  : self = Action.__init__(self, "moudre", [[1, "[(moudre)]"]] )
      if name == "reporter"  : self = Action.__init__(self, "reporter", [[1, "[(reporter)]"]] )
      if name == "couper"  : self = Action.__init__(self, "couper", [[1, "[(couper)]"]] )
      if name == "continuer"  : self = Action.__init__(self, "continuer", [[1, "[(continuer)]"]])
      if name == "exercer" : self = Action.__init__(self, "exercer", [[1, "[(exercer)]"]])
      if name == "pêcher"  : self = Action.__init__(self, "pêcher", [[1, "[(pêcher)]"]])
      if name == "rencontrer" : self = Action.__init__(self, "rencontrer", [[1, "[(rencontrer)]"]])
      if name == "battre"  : self = Action.__init__(self, "battre", [[1, "[(battre)]"]])
      if name == "monter" : self = Action.__init__(self, "monter", [[1, "[(monter)]"]])
      if name == "s'exercer" : self = Action.__init__(self, "s'exercer", [[1, "[(s'exercer)]"]])
      if name == "vendre" : self = Action.__init__(self, "vendre", [[1, "[(vendre)]"]])
      if name == "scier" : self = Action.__init__(self, "scier", [[1, "[(scier)]"]])
      
    else:
      self.lib = lib #str
      self.expressions = expressions #Liste couple [proba(float), string]
      self.adverbes = adverbes #Liste adverbes (liste str)
      
      
  def getGraphText(self):
      s = self.lib
      if len(self.adverbes) > 0:
          s += """</td></tr>\n"""
          s += """<tr><td align="left"><I>Adverbes:</I> """ + ', '.join(self.adverbes)
      return s
  

  def toText(self, mode, temps, personne, useTranslation=True, useCorrection=True):
    """
    - mode: str. ("indicatif", "imperatif", "subjonctif", "conditionnel", ...)
    - temps: str. ("présent", "imparfait", "futur", ...)
    - personne: int. (de 1 a 6)
    """

    # On choisit aléatoirement l'expressons qu'on va utiliser notée exp
    a = random.random()
    s = 0
    i = 0
    while i < len(self.expressions) and a > s:
      s += self.expressions[i][0]
      i += 1
    exp = self.expressions[i-1][1]

    # Il faut conjuguer et eventuellement chercher des synonymes
    # Voici la structure :
    # (xxx) :  xxx doit être conjugué
    # [yyy] : yyy peut être remplacé par un synonyme
    # C'est possible de faire ([zzz]) : pour conjuguer et utiliser les synonymes

    # Synonymes : pas fait encore
    c = re.search(r'\(.*\)', exp)
    while not(c is None):
      mot = c.group(0)[1:-1]
      syn = get_syn(mot)
      exp = exp.replace("(" + mot + ")", syn)
      c = re.search(r'\(.*\)', exp)

    # Conjuguaison
    c = re.search(r'\[.*\]', exp)
    while not(c is None):
      v = c.group(0)[1:-1]
      v_conj = cong(v, mode, temps, personne)
      exp = exp.replace("[" + v + "]", v_conj)
      c = re.search(r'\[[a-z]*\]', exp)

    # Adverbes
    if not(self.adverbes is None):
      for adv in self.adverbes:
        exp += " " + get_syn(adv) + " et"
      if len(self.adverbes) > 0:
        exp = exp[:-3]

    return exp