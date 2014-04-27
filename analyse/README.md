# Analyse

## Objectifs :
Il nous faut déterminer à partir d'images la densité de floraison de la zone 
considérée.

De plus, il est nécessaire d'être capable de mesurer le volume du feuillage 
(fleurs + feuilles + branches) puisque la densité de floraison sera calculée 
comme cela :  (quantité de fleurs)/(quantité de feuillage)

## Méthodes :
L'analyse des images se fera avec OpenCV ou GIMP.

**Feuillage :**
* Passage en noir et blanc
    * Seuillage

**Fleurs :**
* Passage en noir et blanc
    * Augmentation du contraste
* Inversion des couleurs
    * Passage en noir et blanc ?
    * Seuillage ?

## Problèmes :
* De jour : arrière-plan
* Tout le temps : sol, ciel

## Structure de la partie :
Chaque sous-partie est consacrée à une variété particulière et est elle-même partagée en 
plusieurs dossiers dédiés chacun à une image source.

Chaque sous-sous-partie contient un fichier .json apportant plus de détails sur le déroulement des 
analyses : date, source, opérations effectuées... Le fichier gimp.json décrit ces dernières avec précision.
