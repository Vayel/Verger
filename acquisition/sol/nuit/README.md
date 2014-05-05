# Acquisition - images depuis le sol de nuit

## Objectifs :
Il nous faut être en mesure de prendre des clichés dont l'analyse donnera des résultats corrects 
mais de manière peu contraignante : effectivement, s'il faut passer une minute pour 
chaque photographie, le temps de prise sera trop important. Concrètement, il est 
nécessaire de capturer des images de qualité en roulant.

## Problèmes :
Le sol et le ciel constituent des gênes pour l'analyse. Nous devrions nous débarrasser 
simplement du premier en positionnement l'appareil de sorte que le bas de l'image s'arrête au bas du 
pommier et que sol soit invisible. Pour le ciel, peut-être qu'un éclairage particulier pourrait 
remédier au problème.

D'autre part, les images prises en roulant apparaissent floues et quasiment inexploitables. 
Des gênes sont rencontrées : une branche recouvrant l'objectif, une autre avec des fleurs 
ressortant du pommier et formant une importante tâche blanche sur l'image...

## Structure de la partie :
Le dossier img/ contient les photographies rangées par variété.

À chaque lot d'images est associé un fichier details.json comportant des 
informations supplémentaires sur la prise des photographies. La clé "appareil" 
fait référence au fichier ../../appareils.json.
