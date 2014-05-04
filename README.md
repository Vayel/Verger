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
* Acquisition : dédié à la prise des clichés des pommiers
    * sol : images prises du sol
        * img : contient les images
            * nuit : photographies de nuit
    * ciel : images aériennes
        * img : contient les images       
        
* Analyse : dédié à l'analyse des images pour déterminer la densité de floraison
    * sol : analyse des images prises du sol
    * ciel : analyse des images aériennes
    
* Cartographie : dédié à la génération de la carte de densité et à son utilisation

* Distribution : dédié à l'interface embarquée employée pour distribuer le produit

## Pour ne pas s'ennuyer
* Beaucoup d'analyses
* Eclairage de nuit pour atténuer le ciel ?
