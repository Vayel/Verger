# Analyse - images depuis le sol

## Objectifs :
De nuit, seul le ciel s'avère un parasite. Une fois éliminé, calculer la densité 
de floraison est relativement simple à partir d'un seuillage. La difficulté majeure 
consiste donc à extraire l'arbre - feuillage + fleurs - de l'image afin de l'analyser 
sans problème. 

## Méthodes :
L'analyse des images se fera avec OpenCV ou GIMP.

**Feuillage :**
* Passage en noir et blanc
    * Seuillage

**Fleurs :**
* Passage en noir et blanc
    * Augmentation du contraste
* Inversion des couleurs
    * Passage en noir et blanc
    * [Contraste]
    * Seuillage

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
analyses : date, source, opérations effectuées... Le fichier ../gimp.json décrit ces dernières avec précision.
