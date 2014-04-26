# Modulation de dose de produits de traitement dans un verger

## Késako ?

Ce projet **expérimental**, mené en collaboration avec mon oncle agriculteur,
a pour objectif la modulation de dose de produits de traitement dans un verger.
Il nous faut donc être en mesure d'acquérir et d'analyser des clichés de pommiers
en fleurs afin de déterminer, pour des zones définies, une densité de floraison, 
puis de générer une carte pour être capable, à tout moment de l'année, de 
distribuer une quantité de produit adaptée à la région considérée : il est en
effet inutile de traiter une portion exempte de fruits.

Concrètement, chaque rang d'arbres est photographié, découpé en zones dont nous 
calculons la densité de floraison. Une carte est alors générée puis, lors des 
phases de traitement, nous déterminons la position du tracteur sur la carte afin 
de connaître la quantité de produit à distribuer, que nous distribuons. 

## Structure du dépôt

* Acquisition : dédié à la prise des clichés
    * img : contient les images
        * jour : photographies de jour
        * nuit : photographies de nuit
        
* Analyse : dédié à l'analyse des images

* Cartographie : dédié à la génération de la carte de densité

* Distribution : dédié à l'interface embarquée

## TODO
* Analyse : inversion de couleurs puis seuillage
* visionneuse.py
