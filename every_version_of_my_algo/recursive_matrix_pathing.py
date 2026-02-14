

matrix = [
    [9, 8, 7],
    [4, 5, 6],
    [3, 2, 1]
]

path_length = 0
position = (0,0) # position[0] -> m ; position[1] -> n


# navigate right
def nav_right(position):
    global path_length
    # position = (i, j)

    #Cas de base / definit les tuples de position et les valeurs a examiner
    try:
        next_pos = (position[0], position[1] + 1)
        current_val = matrix[position[0]][position[1]]
        next_val = matrix[next_pos[0]][next_pos[1]]

    except IndexError:
        print("\nERREUR:Index out of range")
        return 0

    if current_val < next_val:
        print("\nERREUR:Cant move right anymore")
        return 0

    else:
        path_length += 1 # increase path length by one cuz movement is possible
        print(f"\nCurrent position: {position}, Current value: {current_val}")
        print(f"Next position: {next_pos}, Next position: {next_val}")
        print(f"Path_length: {path_length}")
        return path_length + nav_right(next_pos)

# print(nav_right(position))

#=================================================================================#
#                                                                                 #
#=================================================================================#

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

path_length = 0
position = (2,2) # position[0] -> m ; position[1] -> n

# navigate left
def nav_left(position):
    global path_length
    # position = (i, j)

    #Cas de base / definit les tuples de position et les valeurs a examiner
    try:
        next_pos = (position[0], position[1] - 1)
        current_val = matrix[position[0]][position[1]]
        next_val = matrix[next_pos[0]][next_pos[1]]

    except IndexError:
        print("\nERREUR:Index out of range")
        return 0

    if current_val < next_val:
        print("\nERREUR:Cant move left anymore")
        return 0

    else:
        path_length += 1 # increase path length by one cuz movement is possible
        print(f"\nCurrent position: {position}, Current value: {current_val}")
        print(f"Next position: {next_pos}, Next position: {next_val}")
        print(f"Path_length: {path_length}")
        return path_length + nav_left(next_pos)

# print(nav_left(position))

#=================================================================================#
#                                                                                 #
#=================================================================================#

matrix = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

path_length = 0
position = (2,2) # position[0] -> m ; position[1] -> n

# navigate up
def nav_up(position):
    global path_length
    # position = (i, j)

    #Cas de base / definit les tuples de position et les valeurs a examiner
    try:
        next_pos = (position[0] - 1, position[1])
        current_val = matrix[position[0]][position[1]]
        next_val = matrix[next_pos[0]][next_pos[1]]

    except IndexError:
        print("\nERREUR:Index out of range")
        return 0

    if current_val < next_val:
        print("\nERREUR:Cant move up anymore")
        return 0

    else:
        path_length += 1 # increase path length by one cuz movement is possible
        print(f"\nCurrent position: {position}, Current value: {current_val}")
        print(f"Next position: {next_pos}, Next position: {next_val}")
        print(f"Path_length: {path_length}")
        return path_length + nav_up(next_pos)

# print(nav_up(position))

#=================================================================================#
#                                                                                 #
#=================================================================================#

matrix = [
    [9, 6, 3],
    [1, 5, 2],
    [23, 4, 1]
]
path_length = 0
position = (0,0) # position[0] -> m ; position[1] -> n

# navigate down
def nav_down(position):
    global path_length
    # position = (i, j)

    #Cas de base / definit les tuples de position et les valeurs a examiner
    try:
        next_pos = (position[0] + 1, position[1])
        current_val = matrix[position[0]][position[1]]
        next_val = matrix[next_pos[0]][next_pos[1]]

    except IndexError:
        print("\nERREUR:Index out of range")
        return 0

    if current_val < next_val:
        print("\nERREUR:Cant move down anymore")
        return 0

    else:
        path_length += 1 # increase path length by one cuz movement is possible
        print(f"\nCurrent position: {position}, Current value: {current_val}")
        print(f"Next position: {next_pos}, Next position: {next_val}")
        print(f"Path_length: {path_length}")
        return path_length + nav_down(next_pos)

print(nav_down(position))
