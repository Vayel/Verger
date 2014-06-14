# Analyse - images depuis le sol de nuit

## Objectifs :
De nuit, seul le ciel s'avère un parasite. Il nous faut donc l'éliminer afin de 
ne conserver que le feuillage. Ensuite, un simple seuillage devrait convenir.

## Méthodes :
* Canal rouge (fe) :
    * La sélection du canal rouge pour éliminer en partie le ciel puis un seuillage 
    pour peaufiner semble s'avérer efficace. Le canal rouge donne globalement un 
    histogramme avec un pic vers zéro : le seuillage paraît optimal en prenant la 
    valeur au milieu de la pente du pic.
    * À priori, cette méthode ne présente pas de problème particulier.
    * Il faut à présent déterminer de manière automatique le seuil à appliquer : 
    une faible augmentation du contraste semble rendre l'histogramme plus enclin 
    à être analysé.
    * [Contraste](http://pippin.gimp.org/image_processing/chap_point.html)
    * Régler le seuil à partir d'une image du ciel vierge.

* Inversion de couleurs (fl) : 
   * L'inversion de couleurs fait remarquablement ressortir les fleurs. 
   * Seulement, cette méthode se voit incapable d'extraire le feuillage lorsque 
   le ciel est présent.

* Contraste (fl) : 
   * Un passage en noir et blanc puis une augmentation du contraste fait ressortir 
   les fleurs : les zones obscures deviennent noires alors que les claires blanches. 
    * Seulement, les valeurs efficaces du contraste ne semblent pas suivre de 
    logique particulière.
	
* Trichromie canal jaune (fe) :
	* Décomposition trichromie
	* Canal jaune
	* Contraste
	* Seuillage

## Problèmes :
Nous parvenons à des résultats tout à fait corrects mais le souci est que chaque image 
est analysée différemment : ou bien nous adaptons les règlages - plus de contraste, 
un seuil moins important... - ou bien ce sont complètement les opérations qui changent - 
inversion de couleur pour certaines, contraste pour d'autres... 

En outre, l'extraction des fleurs s'avère relativement simple, contrairement à la 
détermination du feuillage, pour laquelle le ciel représente une gêne considérable.

## Structure de la partie :
Chaque sous-partie est consacrée à un principe d'analyse et dédie une sous-partie 
à chaque variété, qui est elle-même partagée en plusieurs dossiers pour chaque 
image source.

Chaque sous-partie contient un fichier details.json apportant plus de détails sur 
les opérations effectuées lors des analyses. Le fichier ../../gimp.json décrit 
ces dernières avec précision.
