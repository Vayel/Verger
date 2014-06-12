# Analyse

## Objectifs :
Il nous faut déterminer à partir d'images la densité de floraison de la zone 
considérée.

De plus, il est nécessaire d'être capable de mesurer le volume du feuillage 
(fleurs + feuilles + branches) puisque la densité de floraison sera calculée 
comme cela : (quantité de fleurs)/(quantité de feuillage).

La difficulté majeure est d'extraire l'arbre de l'arrière-plan. En principe, 
une fois le feuillage déterminé, la calcul de densité de floraison devrait 
s'effectuer par un simple seuillage.

## Méthodes :
S'agissant d'un sujet complètement expérimental, la démarche globale consiste à 
essayer d'analyser les images à la main, en particulier en effectuant des opérations 
dessus avec GIMP. Dans le cas de résultats convenables, il nous faut chercher 
un lien entre les analyses - valeur du seuil par rapport à l'histogramme par exemple - 
afin de généraliser et d'automatiser. Enfin, une fois les scripts écrits, vérifier le 
bon fonctionnement de la méthode en analysant derechef les images, mais via 
notre programme cette fois.

# Problèmes :
Les images variant fortement, l'analyse s'avère complexe et il va probablement falloir 
imposer des contraintes à l'acquisition.

Se référer au fichier README.md de chaque sous-partie pour plus de renseignements.
