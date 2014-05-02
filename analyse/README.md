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
Nous parvenons à des résultats tout à fait corrects mais le souci est que chaque image 
est analysée différemment : ou bien nous adaptons les règlages - plus de contraste, 
un seuil moins important... - ou bien ce sont carrément les opérations qui changent - 
inversion de couleur pour certaines, contraste pour d'autres... C'est pourquoi la 
méthode du *machine learning* est envisagée.

## Structure de la partie :
Chaque sous-partie est consacrée à une variété particulière et est elle-même partagée en 
plusieurs dossiers dédiés chacun à une image source.

Chaque sous-sous-partie contient un fichier .json apportant plus de détails sur le déroulement des 
analyses : date, source, opérations effectuées... Le fichier gimp.json décrit ces dernières avec précision.
