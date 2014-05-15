# Analyse - images depuis le sol de nuit

## Objectifs :
De nuit, seul le ciel s'avère un parasite. Il nous faut donc l'éliminer afin de 
ne conserver que le feuillage. Ensuite, un simple seuillage devrait convenir.

## Méthodes :
* Canal rouge (fl + fe) :
    * La sélection du canal rouge pour éliminer en partie le ciel puis un seuillage pour 
peaufiner semble s'avérer efficace. Le canal rouge donne globalement un histogramme avec 
un pic vers zéro : le seuillage paraît optimal en prenant la valeur au milieu de la pente 
du pic.
    * À priori, cette méthode ne présente pas de problème particulier.

* Inversion de couleurs (fl) : 
   * L'inversion de couleurs fait remarquablement ressortir les fleurs. 
   * Seulement, cette méthode se voit incapable d'extraire le feuillage lorsque le ciel est présent.

* Contraste (fl) : 
   * Un passage en noir et blanc puis une augmentation du contraste fait ressortir les 
fleurs : les zones obscures deviennent noires alors que les claires blanches. 
    * Seulement, les valeurs efficaces du contraste ne semblent pas suivre de logique particulière.

## Problèmes :
Nous parvenons à des résultats tout à fait corrects mais le souci est que chaque image 
est analysée différemment : ou bien nous adaptons les règlages - plus de contraste, 
un seuil moins important... - ou bien ce sont complètement les opérations qui changent - 
inversion de couleur pour certaines, contraste pour d'autres... 

En outre, l'extraction des fleurs s'avère relativement simple, contrairement à la détermination 
du feuillage, pour laquelle le ciel représente une gêne considérable.

La méthode du *machine learning* pourrait être envisagée.

## Structure de la partie :
Chaque sous-partie est consacrée à une variété particulière et est elle-même partagée en 
plusieurs dossiers dédiés chacun à une image source.

Chaque sous-sous-partie contient un fichier details.json apportant plus de détails sur les analyses : 
date, source et opérations effectuées. Le fichier ../../gimp.json décrit ces dernières avec précision.
