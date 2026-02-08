# TP Chemin le plus long dans une matrice
**Auteur:** Émile Valade

**Objectif:** Créer un programme qui génère une matrice aléatoire et trouve la longueur du chemin le plus long possible en ne se déplaçant que vers des cellules adjacentes de valeur strictement inférieure.

**Fonctionnalités attendues:**
- [ ] saisie sécurisée avec re-saisie en cas d'erreur
- [ ] Affichage clair de la matrice avec ses indices
- [ ] Calcul et affichage de la longeur du chemin le plus long
- [ ] Possibilité de relancer le programme sans le quitter

**Contraintes techniques:**
- [ ] N'utiliser aucine librairie externe (autre que `random`)
- [ ] Le code doit être bien structuré avecs des fonctions
- [ ] Les messages d'erreur doivent être explicites
- [ ] Gestion propre de tous les cas d'erreur

---

## 1. Saisie utilisateur
- [x] Nombre de lignes de la matrice (entier positif)
  - [x] **ValueError:** si le nombre n'est pas entier
  - [x] **Valeur négatives ou nulles:** si le nombre est nulle ou négatif
  - [x] **Dimension trop grandes:** si au dessus de la limite imposé (10x10 max)
        
- [x] Nombre de collone de la matrice (entier positif)
  - [x] **ValueError:** si le nombre n'est pas entier
  - [x] **Valeur négatives ou nulles:** si le nombre est nulle ou négatif
  - [x] **Dimension trop grandes:** si au dessus de la limite imposé (10x10 max)
        
- [x] Valeur maximale pour les nombres aléatoires (entier positif >= 1)
  - [x] **ValueError:** si le nombre n'est pas entier
  - [x] **Valeur négatives ou nulles:** si le nombre est nulle ou négatif
        
- [x] Gestion de toute erreur inattendue avec un message clair
      
- [x] Test et fix de bug

---

## 2. Génération de la matrice
- [x] Générer une matrice (lignes x colonnes)
      
- [x] Remplir chaque cellule avec un entier aléatoire (1 à val max saisie)
      
- [x] Afficher la matrice de manière claire
      
- [x] Test et fix de bug

---

## 3. Navigation dans la matrice selon les règles du chemin le plus long
- On peut partir de n'importe quelle cellule
- On ne peut se déplacer que vers les 4 directions (haut, bas, gauche, droite)
- On ne peut aller que vers une cellule dont la valeur est strictement inférieure
- On ne peut pas sortir des limites de la matrice
- Objectif : trouver la longueur (nombre de cellules) du chemin le plus long possible

- [ ] trouver et resourdre un algorithme pour parse la matrice selon les règles
      
- [ ] Implementer l'algorithme
      
- [ ] Tester et resourde tous bug qui survient

### Exemples

**Exemple 1** :

```python
terrain = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Le chemin le plus long est : 9 → 8 → 7 → 4 → 1
Longueur : **5**

**Exemple 2** :

```python
terrain = [
    [9, 8, 7],
    [4, 5, 6],
    [3, 2, 1]
]
```

Le chemin le plus long est : 9 → 8 → 7 → 6 → 5 → 4 → 3 → 2 → 1
Longueur : **9**

**Exemple 3** :

```python
terrain = [
    [5, 5, 5],
    [5, 5, 5],
    [5, 5, 5]
]
```

Pas de déplacement possible (pas de cellule strictement inférieure)
Longueur : **1** (on reste sur place)

---

## 4. Structure et Logique du programme (boucle while principale)
- [ ] boucle while principale
      
- [ ] Demande du nombre de lignes
      
- [ ] Demande du nombre de colonnes
      
- [ ] Demande de la valeur maximales pour les nombres aleatoires
      
- [ ] Affichage de la matrice générée
      
- [ ] Message de chargement/calcul en cours
      
- [ ] Affichage du chemin le plus long calculé
      
- [ ] Demande si l'utilisateur souhaite effectuer un nouveau calcul ou quitter

---

## 5. Plus
- [ ] Afficher une example de chemin qui atteint la longeur maximale
      
- [ ] Proposer plusieurs stratégies de génération de matrice
      
- [ ] Afficher des statistiques sur la matrice
  - [ ] Nombre minimum
  - [ ] Nombre maximum
  - [ ] Moyenne
  - [ ] etc...
