def longest_path(matrix):
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

#=================================================================================#
# Test de la fonction
#=================================================================================#
m1 = [ # expected -> 5
 [5, 4, 3],
 [6, 1, 2]
]
print(f"Expected: 5\nGot: {longest_path(m1)}\n")

m2 = [ # expected -> 8
 [9, 8, 7],
 [2, 3, 6],
 [1, 4, 5]
]
print(f"Expected: 8\nGot: {longest_path(m2)}\n")

m3 = [ # expected -> 5
 [10, 3, 2],
 [9, 8, 1],
 [4, 7, 6]
]
print(f"Expected: 5\nGot: {longest_path(m3)}\n")


m4 = [ # expected -> 0
 [5, 5, 5],
 [5, 5, 5]
]
print(f"Expected: 0\nGot: {longest_path(m4)}\n")


m5 = [ # expected -> 4
 [7],
 [6],
 [5],
 [4],
 [3]
]
print(f"Expected: 4\nGot: {longest_path(m5)}\n")


m6 = [ # expected -> 7
 [8, 7, 2],
 [9, 6, 1],
 [4, 5, 3]
]
print(f"Expected: 7\nGot: {longest_path(m6)}\n")


m7 = [ # expected -> 6
 [9, 8, 10, 1],
 [4, 5, 6, 2],
 [3, 2, 1, 3]
]
print(f"Expected: 6\nGot: {longest_path(m7)}\n")
