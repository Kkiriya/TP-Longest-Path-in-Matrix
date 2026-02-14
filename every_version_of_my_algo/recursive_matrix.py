from colorama import Fore, Back, Style

matrix = [
            [9, 8, 10, 1],
            [4, 5, 6, 2],
            [3, 2, 1, 3]
        ]

def navigate(directions=['right','down','left','up'], position=(0,0), path_length=0):
    # Stop condition
    if len(directions) == 0:
        #

        test_str = [
            "\n",
            Fore.RED + "=== IN STOP CONDITION ===" + Style.RESET_ALL,
            f"direction: {directions}",
            f"position: {position}",
            f"path_length: {path_length}"
        ]
        for t in test_str: print(t)

        #
        return 0

    direction_to_position = {
        "right": (0, 1), # will apply i+0, j+1
        "left": (0, -1), # will apply i+0, j-1
        "up": (-1, 0), # will apply i-1, j+0
        "down": (1, 0), # will apply i+1, j+0
    }
    direction = directions[0] # contains the direction we are evaluating rn

    current_position = position # redundant but helps maintain visual clarity
    next_position = (position[0] + direction_to_position[direction][0], position[1] + direction_to_position[direction][1]) # offsets current position to get the next one in current direction

    try: # contains the current value of the position within the matrix and the next one
        current_val = matrix[current_position[0]][current_position[1]]
        next_val = matrix[next_position[0]][next_position[1]]

    except IndexError:

        test_str = [
            "\n",
            Fore.YELLOW + "=== IN INDEXERROR ===" + Style.RESET_ALL,
            f"direction: {direction}\ndirection_left: {directions}",
            f"position: {next_position}",
            f"path_length: {path_length}"
        ]
        for t in test_str: print(t)

        return navigate(directions[1:], position) # if we end up outside the matrix we move on to the next direction without adding to the path_length or changing the current position
    if next_position[0] < 0 or next_position[1] < 0:
        test_str = [
            "\n",
            Fore.YELLOW + "=== IN NEGATIVE INDEX ===" + Style.RESET_ALL,
            f"direction: {direction}\ndirection_left: {directions}",
            f"position: {next_position}",
            f"path_length: {path_length}"
        ]
        for t in test_str: print(t)


        return navigate(directions[1:], position) # negative value work in python however they do not fit the logic of our code

    if current_val < next_val:

        test_str = [
            "\n",
            Fore.YELLOW + "=== IN NEXT VAL BIGGER ===" + Style.RESET_ALL,
            f"direction: {direction}\ndirection_left: {directions}",
            f"position: {next_position}",
            f"path_length: {path_length}"
        ]
        for t in test_str: print(t)

        return navigate(directions[1:], position) # if the next position is bigger then the current one we move on to the next direction without adding to the path_length or changing the current position

    else: #  increase the path length by one upon succesful movement, and go to next cell

        test_str = [
            "\n",
            Fore.GREEN + "=== IN NEXT_CELL ===" + Style.RESET_ALL,
            f"direction: {direction}\ndirection_left: {directions}",
            f"position: {next_position}",
            f"path_length: {path_length}"
        ]
        for t in test_str: print(t)

        return 1 + navigate(directions, next_position, path_length)



print(navigate())
