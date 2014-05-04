# Analyse - images aériennes

## Objectifs :
Il nous faut, à partir d'images aériennes, extraire les rangs de pommiers du sol 
afin d'analyser la densité de floraison en toute quiétude.

## Méthodes :
Une fois l'arbre découpé, un simple passage en N&B puis un seuillage devraient 
nous donner avec précision la densité de fleurs.

Par contre, l'extraction représente un obstacle non négligeable.

## Problèmes :
TODO

## Structure de la partie :
Chaque sous-partie est consacrée à une variété particulière et est elle-même partagée en 
plusieurs dossiers dédiés chacun à une image source.

Chaque sous-sous-partie contient un fichier .json apportant plus de détails sur 
le déroulement des analyses : date, source, opérations effectuées... Le fichier 
../gimp.json décrit ces dernières avec précision.
