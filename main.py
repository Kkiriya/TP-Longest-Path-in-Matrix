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
def generation_matrice(nbr_lignes:int, nbr_colonnes:int, valeur_max:int):
    """Genere une matrice selon un nombre de lignes et colonnes passee en arguments et la remplie de nombre aleatoire ne depassant pas la valeur max passee en argument

    Args:
        nbr_lignes (int): le nombre de lignes de la matrice a generer
        nbr_colonnes (int): le nombre de colonnes  de la matrice a generer
        valeur_max (int): la valeur maximum des nombre aleatoire
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
        print("|" + "|".join(f"{n:0{nbr_width}d}".center(nbr_width + 2) for n in lignes) + "|") # join toute les valeur de n dans lignes




# contient le code qui execute la logique du programme
def main():
    # --- TEST DE SAISIE DE L'UTILISATEUR ---
    # print(saisie_utilisateur()) # -> done and tested

    # --- TEST DE GENERATION ET AFFICHAGE DE MATRICE ---
    # generation_matrice(3, 3, 10)
    # generation_matrice(5, 5 , 5)
    # generation_matrice(1, 1, 2)
    # generation_matrice(10, 10, 100) # -> done and tested


    # === LOGIQUE PRINCIPALE DU CODE ===
    print("=== CHEMIN LE PLUS LONG DANS UNE MATRICE ===")

    # while


if __name__ == "__main__":
    main()
