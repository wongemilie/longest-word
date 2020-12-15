import random
import string

class Game:

    def __init__(self):
        self.grid = []
        self.random_grid()


    def random_grid(self):
        print('Generating 9 random letters...')

        while len(self.grid) < 9:
            letter = random.choice(string.ascii_uppercase)
            print(f'Add {letter} in grid')
            self.grid.append(letter)

        print(f'{len(self.grid)} letters have been successfully generated')


    def is_valid(self, word):
        if isinstance(word, str):
            if not word:
                return False

            for letter in word:
                if letter not in self.grid:
                    print(f'Letter {letter} is not valid !')
                    return False
        else:
            print(f'{word} is not a string !')
            return False

        return True



if __name__ == "__main__":
    g = Game()
    g.is_valid("Hello")
