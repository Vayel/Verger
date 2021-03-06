# Cartographie

## Objectifs :
Il nous faut générer une carte de préconisation du verger afin d'être en mesure, à
toute période de l'année, de déterminer quelle était la densité de floraison pour
une zone donnée.

Pour cela, il est en paticulier nécessaire d'être capable de positionner le tracteur 
dans le verger - i.e. sur la carte.

## Méthodes :
Les coordonnées GPS étant trop coûteuses et imprécises, l'idée serait de repérer 
le tracteur par rapport aux pommiers : le rang où il se situe est connu, donc si 
on le localise dans le rang, on connait sa position dans le verger et 
donc la région qu'il traite ; en se référant à la carte, on peut alors déterminer 
la dose à distribuer.

## Problèmes :
L'obstacle majeur est l'élaboration de la carte. Il nous faut, à partir d'images 
successives du rang, obtenir une vision globale de ce dernier. Comment, avec des 
clichés de parties de rang, construire une carte ?

Pour illustrer, il faudrait avoir la possibilité de rapetisser le rang puis de le 
photographier dans toute sa largeur pour aisément générer la portion de carte lui 
étant assignée.

## Pistes :
L'*image stitching* semble une piste intéressante. Afin de simplifier le *stitching*, 
ce dernier pourrait être fait sur les images binaires - après extraction du feuillage - 
et non sur les sources aux motifs complexes.

Une autre solution consisterait à effectuer le protocole suivant :
* Tracteur positionné entre les pommiers A et B
* Sélection de la photographie associée à cet intervalle
* Utilisation du tronc pour origine et de la vitesse pour connaître la distance 
parcourue
* Position exacte du tracteur connue

## Structure de la partie :
Rien pour l'instant.
