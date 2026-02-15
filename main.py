# Author: Émile
# Date: 2026-02-08
# But: Créer un programme qui génère une matrice aléatoire et trouve la longueur du chemin le plus long possible en ne se déplaçant que vers des cellules adjacentes de valeur strictement inférieure.
import random

# Variables & Functions -> snake_case
# Classes -> PascalCase
# Constants -> UPPER_SNAKE_CASE
# Methods (inside classes) -> snake_case
# Private/Internal use -> leading underscore

# Erreur en cas de nombre negatif ou nulle
class NombreNegatifOuNulle(Exception):
    pass

# Erreur en cas de nombre plus eleve que la dimension max
class NombreOverDimensionMax(Exception):
    pass

#Variables globale
DIMENSION_MAX = 10

# === SAISIE UTILISATEUR ===
def saisie_utilisateur():
    """Gere la logique pour la saisie de l'utilisateur et retourne la reponse au trois question l'une apres l'autres

    Raises:
        NombreNegatifOuNulle: _description_
        NombreOverDimensionMax: _description_

    Returns:
        _type_: _description_
    """

    # permet de reutiliser le code
    def user_input(choix_question: str) -> int:
        """Demande a l'utilisateur une question et retourne la reponse en int.
        Les question possible sont:
            - Entrez le nombre de lignes:
            - Entrez le nombre de colonnes:
            - Entrez la valeur maximale pour les nombres aléatoires:

        pour choisir la question desirer utiliser respectivement:
            - 'l' -> lignes
            - 'c' -> colonnes
            - 'm' -> valeur max
        a l'argument choix_question

        Args:
            choix_question (str): permet de choisir la question a afficher

        Returns:
            int: La reponse en int
        """
        questions = {
            'l': "Entrez le nombre de lignes: ",
            'c': "Entrez le nombre de colonnes: ",
            'm': "Entrez la valeur maximale pour les nombres aléatoires: "
        }
        # while qui permet la verification du input de maniere dynamique
        while True:
            try:
                nbr = int(input(questions[choix_question]).strip()) # check si le nombre est un int

                if nbr <= 0: # Check si le nombre est negatif ou nulle
                    raise NombreNegatifOuNulle
                elif choix_question in ['l', 'c'] and nbr > DIMENSION_MAX: # check si le nbr est plus grand que la dimension max; ne s'applique que pour la ligne et la colonne
                    raise NombreOverDimensionMax

                return nbr # si tous vas bien retourne le nombre

            except ValueError:
                    print("Erreur: Veuillez entrer un nombre entier!")
            except NombreNegatifOuNulle:
                print("Erreur: Veuillez entrer un nombre plus grand ou egale a 1!")
            except NombreOverDimensionMax:
                print("Erreur: Veuillez entrer un nombre plus petit que la dimentsion maximale!")
            except Exception as e:
                print(f"Erreur Inattendue: {e}")


    # appelle la fonction et stocke la reponse dans une variables
    nbr_lignes = user_input('l')
    nbr_colonnes = user_input('c')
    nbr_aleatoire_max = user_input('m')

    return nbr_lignes, nbr_colonnes, nbr_aleatoire_max

# === GENERATION DE LA MATRICE ===
def generation_matrice(nbr_lignes:int, nbr_colonnes:int, valeur_max:int) -> list:
    """Genere une matrice selon un nombre de lignes et colonnes passee en arguments et la remplie de nombre aleatoire ne depassant pas la valeur max passee en argument

    Args:
        nbr_lignes (int): le nombre de lignes de la matrice a generer
        nbr_colonnes (int): le nombre de colonnes  de la matrice a generer
        valeur_max (int): la valeur maximum des nombre aleatoire

    Returns:
            list: la matrice generer
    """
    matrice = [] # liste qui contient la matrice

    for m in range(nbr_lignes):
        ligne = [] # liste qui contient la lignes courante
        for n in range(nbr_colonnes):
            ligne.append(random.randint(1,valeur_max)) # ajoute une valeurs a la ligne courante
        matrice.append(ligne) # ajoute la ligne courante a la matrice

    # Affichage de la matrice
    print(f"Matrice {nbr_lignes}x{nbr_colonnes} générée:")

    nbr_width = max(len(str(nbr)) for ligne in matrice for nbr in ligne) # retourne le nbr de charactere du nombre le plus grand de la matrice pour effectuer un formattage dynamique

    for lignes in matrice:
        print(" " + " ".join(f"{n:{nbr_width}d}".center(nbr_width + 2) for n in lignes) + " ") # join toute les valeur de n dans lignes

    return matrice

# === CHEMIN LE PLUS LONG ===
def chemin_plus_long(matrix):
    cache = {} # garde le resultat du chemin de chaque cellule pour rendre la recursion moins intense et plus effice

    # fonction qui trouve le chemin le plus a partir d'une seule position
    def nav(position):
        if position in cache: # permet de ne pas avoir a recalculle les path deja calcule
            return cache[position]

        possible_movements = [
            (-1,0), # up
            (1,0), # down
            (0,-1), # left
            (0,1) # right
        ]
        current_value = matrix[position[0]][position[1]]
        longest_length = 0

        for move in possible_movements:
            try:
                eval_cell = (position[0] + move[0], position[1] + move[1])
                eval_val = matrix[eval_cell[0]][eval_cell[1]]
            except IndexError:
                continue

            if eval_cell[0] < 0 or eval_cell[1] < 0:
                continue

            if eval_val < current_value: #we ran out of movements
                length = 1 + nav(eval_cell)
                if length > longest_length:
                    longest_length = length

        cache[position] = longest_length
        return longest_length

    longest_matrix_path = 0

    for i, ligne in enumerate(matrix):
        for j, colonne in enumerate(ligne):
            current_path = nav((i,j))
            if current_path > longest_matrix_path:
                longest_matrix_path = current_path

    return longest_matrix_path




# contient le code qui execute la logique du programme
def main():
    # --- TEST DE SAISIE DE L'UTILISATEUR ---
    # print(saisie_utilisateur()) # -> done and tested

    # --- TEST DE GENERATION ET AFFICHAGE DE MATRICE ---
    # generation_matrice(3, 3, 10)
    # generation_matrice(5, 5 , 5)
    # generation_matrice(1, 1, 2)
    # generation_matrice(10, 10, 100) # -> done and tested

    # --- TEST DE CHEMIN LE PLUS LONG ---
    # effectuer dans un autre fichier

    # === LOGIQUE PRINCIPALE DU CODE ===
    while True:
        print("=== CHEMIN LE PLUS LONG DANS UNE MATRICE ===")
        # demande le nombre de lignes, colonnes et le max pour les nombres aleatoires
        nbr_lignes, nbr_colonnes, nbr_aleatoire_max = saisie_utilisateur()

        # genere et affiche la matrice
        matrice = generation_matrice(nbr_lignes,nbr_colonnes, nbr_aleatoire_max)

        # message de chargement
        print("\nCalul en cours...")

        # affiche le resultat
        print(f"Longeur du chemin le plus long: {chemin_plus_long(matrice)}")

        # demande si on souhaitre reccomencer
        choix = input("\nvoulez vous-reccomencez? (O/N): ").strip().lower() # toute autre input que 'O' arrete le programme

        if choix != 'o':
            break
        else:
            print()
            continue




if __name__ == "__main__":
    main()
