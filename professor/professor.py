import random

def main():
    # Prompts the user for a level
    level = get_level()
    tries = 0
    score = 0
    # Randomly generates ten (10) math problems formatted as X + Y = . No need to support operations other than addition (+).
    while tries < 10:
        tries += 1
        x = generate_integer(level)
        y = generate_integer(level)
        result = x + y
        incorrect = 0
        # Prompts the user to solve each of those problems.
        while incorrect < 4:
            try:
                answer = int(input(f'{x} + {y} = '))
                if result == answer:
                    score += 1
                    break
                # If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, up to three tries.
                if result != answer:
                    incorrect += 1
                    print('EEE')
                    # If the user has still not answered correctly after three tries, the program should output the correct answer.
                    if incorrect == 3:
                        print(f'{x} + {y} = {result}')
                        break
            # If not a number
            except ValueError:
                incorrect += 1
                print('EEE')
                if incorrect == 3:
                    print(f'{x} + {y} = {result}')
                    break
    # Outputs the user’s score: the number of correct answers out of 10.
    print(f'Score: {score}')

# Prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3
def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in {1, 2, 3}:
                return level
            # If the user does not input 1, 2, or 3, the program should prompt again.
            else:
                pass
        except ValueError:
            pass

# returns a randomly generated int > 0 with level digits or raises a ValueError if level is not 1, 2, or 3
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)



if __name__ == "__main__":
    main()