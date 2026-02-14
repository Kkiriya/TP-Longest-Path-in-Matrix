matrix = [
    [9, 8, 7, 1],
    [4, 5, 6, 2],
    [3, 2, 1, 3]
]
path_length = 0

def navigate_matrix(direction="right", position=(0,0), path_length=0):
    direction_to_position = {
        "right": (0, 1), # will apply i+0, j+1
        "left": (0, -1), # will apply i+0, j-1
        "up": (-1, 0), # will apply i-1, j+0
        "down": (1, 0), # will apply i+1, j+0
    }

    current_position = position # contains current position (mainly for clarity)
    next_position = (position[0] + direction_to_position[direction][0], position[1] + direction_to_position[direction][1]) # contains the next position to evaluate

    try: # contains the current value of the position within the matrix and the next one
        current_val = matrix[current_position[0]][current_position[1]]
        next_val = matrix[next_position[0]][next_position[1]]

    except IndexError:
        return 0 # if we end up outside the matrix we stop moving in that direction

    if current_val < next_val:
        return 0 # if the next value is bigger we stop moving in that direction

    else:
        path_length += 1 # increase the path length by one upon succesful movement
        return path_length + navigate_matrix(direction, next_position, path_length)


#=================================================================================#
# Testing of navigate matrix with right side
#=================================================================================#

print(navigate_matrix("up", (2,3), path_length))
