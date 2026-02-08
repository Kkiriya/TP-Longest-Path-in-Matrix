matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

position = (0,0) # position[0] -> m ; position[1] -> n
longest_path = 0
path_length = 0
path_history = []

def find_path(matrice, position,longest_path, path_length, path_history):
    try
        # Test vers la droite
        if position[1] + 1 <= len(matrice[0]):
            position = (position[0], position[1]+1)
            path_length += 1
            path_history += 1



    return longest_path
