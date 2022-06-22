import random
import copy


class Game:
    def __init__(self):
        # 4x4 matrix of zeroes\
        self.matrix = [[0] * 4 for i in range(4)]
        self.score = 0
        self.start_game()

    def start_game(self):
        # fill 2 random cells with number 2
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        self.matrix[x][y] = 2

        while (self.matrix[x][y] != 0):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.matrix[x][y] = 2

        self.display()

    #check if any field is empy
    def has_empty_fields(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return True
        return False

    #add random 2 into matrix
    def add_new_two(self):
        if not self.has_empty_fields():
            raise Exception("Error. There are no empty fields")
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.matrix[x][y] == 0:
                break
        self.matrix[x][y] = 2

    #display current matrix into console
    def display(self):
        spaces = 4
        for x in self.matrix:
            currX = "|"
            for element in x:
                if element == 0:
                    currX += " " * spaces +"|"
                else:
                    currX +=(" " * (spaces - len(str(element)))) + str(element) + "|"
            print(currX)
        print()
        print("SCORE:", self.score)

    #move all numbers to the farest left corner possible
    def stack(self):
        new_matrix = [[0] * 4 for i in range(4)]
        for i in range(4):
            position_to_fill = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][position_to_fill] = self.matrix[i][j]
                    position_to_fill += 1
        self.matrix = new_matrix

    #transpose matrix - used for vertical movement
    def transpose(self):
        new_matrix = [[0] * 4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix

    #combine cells of the same value into one another
    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    #will reverse matrix - used for horizontal movement
    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    #will check if horizontal movemnt is possible
    def check_if_horizont_is_possible(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        else:
            return False

    #will check if vertical movement is possible
    def check_if_vertical_is_possible(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        else:
            return False

    def check_score(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 2048:
                    print("WINNER")
                    return True
        return not (self.check_if_vertical_is_possible() or self.check_if_horizont_is_possible())

    #steps: 1. reverse matrix. 2. move the most left corner. 3. combine same cells in X line. 4. move to the most left corner.
    #5. reverse to get right matrix
    def stack_right(self):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()

    #steps: 1. move to the most left corner. 2. combine same cells in X line. 3. move to the most left corner
    def stack_left(self):
        self.stack()
        self.combine()
        self.stack()

    # steps: 1. transpose matrix. 2. move the most left corner. 3. combine same cells in X line. 4. move to the most left corner.
    # 5. transpose matrixx
    def stack_up(self):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()

    # steps: 1. transpose matrix. 2. reverse matrix. 3. move the most left corner. 3. combine same cells in X line. 4. move to the most left corner.
    # 5. reverse matrix 6. transpose matrixx
    def stack_down(self):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()

    #need to check if movement is possible in the matrix
    def compare_matrix(self, temp):
        if temp == self.matrix:
            return True
        return False

    def play(self):
        while True:
            vstup = input()
            temp_board = copy.deepcopy(self.matrix)
            if vstup == "4":
                print("DIRECTION: LEFT")
                self.stack_left()
            elif vstup == "8":
                print("DIRECTION: UP")
                self.stack_up()
            elif vstup == "6":
                print("DIRECTION: RIGHT")
                self.stack_right()
            elif vstup == "2":
                print("DIRECTION: DOWN")
                self.stack_down()
            elif vstup == "q":
                break
            if self.compare_matrix(temp_board):
                print("INVALID MOVE. MAKE NEW MOVE") #if movement is not possible
            else:
                if self.check_score():
                    break
                else:
                    try:
                        self.add_new_two()
                        self.display()
                    except Exception as ex:
                        print("Could not add new number", ex)
                        break


if __name__ == '__main__':
    game = Game()
    game.play()
