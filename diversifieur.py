# -*- coding: utf-8 -*-
"""diversifieur.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11t7W3Yq_CmjJPF6BOIuwwbEWl80s0qiV
"""

"""
!pip install verbecc
!pip install google_trans_new
"""

from verbecc import Conjugator
from google_trans_new import google_translator

cg = Conjugator(lang='fr')
useTranslation = True

ts = None
if useTranslation:
  ts = google_translator()



def cong(s, mode, temps, personne):
  """
  Fonction qui conjugue

  Arguments :
  - s: str (verbe à conjuguer)
  - mode: str. ("indicatif", "imperatif", "subjonctif", "conditionnel", ...)
  - temps: str. ("present", "imparfait", "futur", ...)
  - personne: int. (de 1 a 6)

  Renvoie :
  - c: str (verbe conjugué)
  """
  global cg
  conjugation = cg.conjugate(s)
  c = conjugation['moods'][mode][temps][personne-1]
  return c



def get_syn(s):
  """
  Fonction qui renvoie des synonymes de s
  NOT IMPLEMENTED YET

  Arguments :
  - s: str. (le mot)

  Renvoie:
  - syn: str. (Un synonyme choisi aléatoirement)
  """

  return s



def correct(s):
  """
  Fonction qui corrige un morceau de phrase avec le double traducteur

  Arguments :
  - s: str. (le mot)

  Renvoie:
  - s2: str. (Un synonyme choisi aléatoirement)
  """
  global useTranslation, ts

  if not(useTranslation):
    return s

  s1 = ts.translate(s, lang_src="fr", lang_tgt="en")
  if type(s1) == list:
    s1 = s1[0]
  s2 = ts.translate(s1, lang_src="en", lang_tgt="fr")
  #s1 = ts.translate(s, lang_tgt="en")
  #s2 = ts.translate(s1, lang_tgt="fr")

  if type(s2) == list:
    s2 = s2[0]
  return s2



def diversifier(s):
  """
  Fonction qui diverifie un morceau de phrase avec le traducteur en apssant aps plusieurs languages

  Arguments :
  - s: str. (l'expression)

  Renvoie:
  - s2: str. (l'expression diversifiée)
  """
  global useTranslation, ts

  if not(useTranslation):
    return s
    
  return correct(s)

  l = ["en"]
  nb_langues = 1

  langues = []
  for i in range(nb_langues):
    index = random.randint(0,len(l)-1)
    langues.append(l[index])
    l = l[:index] + l[index+1:]

  #s2 = ts.translate(s, lang_src="fr", lang_tgt=langues[0])[1]
  s2 = ts.translate(s, lang_tgt=langues[0])
  for i in range(1, len(langues)):
    #s2 = ts.translate(s2, lang_src=langues[i-1], lang_tgt=langues[i])[1]
    s2 = ts.translate(s2, lang_tgt=langues[i])
  #s2 = ts.translate(s2, lang_src=langues[-1], lang_tgt="fr")[1]
  s2 = ts.translate(s2, lang_tgt="fr")
  return s2