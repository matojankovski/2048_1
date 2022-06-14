import random
import copy


class Game:
    def __init__(self):
        # 4x4 matrix of zeroes\
        self.matrix = [[0] * 4 for i in range(4)]
        self.score = 0
        self.start_game()

    def start_game(self):
        # 4x4 matrix of zeroes
        # self.matrix = [[0] * 4 for i in range(4)]

        # fill 2 random cells with number 2
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        self.matrix[x][y] = 2

        while (self.matrix[x][y] != 0):
            x = random.randint(0, 3)
            y = random.randint(0, 3)
        self.matrix[x][y] = 2

        self.display()

    def HasEmptyFields(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 0:
                    return True
        return False



    def addNewTwo(self):
        if not self.HasEmptyFields():
            raise Exception("Error. There are no empty fields")
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)
            if self.matrix[x][y] == 0:
                break
        self.matrix[x][y] = 2




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



    def stack(self):
        new_matrix = [[0] * 4 for i in range(4)]
        for i in range(4):
            position_to_fill = 0
            for j in range(4):
                if self.matrix[i][j] != 0:
                    new_matrix[i][position_to_fill] = self.matrix[i][j]
                    position_to_fill += 1
        self.matrix = new_matrix


    def transpose(self):
        new_matrix = [[0] * 4 for i in range(4)]
        for i in range(4):
            for j in range(4):
                new_matrix[i][j] = self.matrix[j][i]
        self.matrix = new_matrix


    def combine(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] != 0 and self.matrix[i][j] == self.matrix[i][j + 1]:
                    self.matrix[i][j] *= 2
                    self.matrix[i][j + 1] = 0
                    self.score += self.matrix[i][j]

    def reverse(self):
        new_matrix = []
        for i in range(4):
            new_matrix.append([])
            for j in range(4):
                new_matrix[i].append(self.matrix[i][3 - j])
        self.matrix = new_matrix

    def checkIfHorizontIsPossible(self):
        for i in range(4):
            for j in range(3):
                if self.matrix[i][j] == self.matrix[i][j+1]:
                    return True
        else:
            return False

    def checkIfVerticalIsPossible(self):
        for i in range(3):
            for j in range(4):
                if self.matrix[i][j] == self.matrix[i+1][j]:
                    return True
        else:
            return False

    def checkScore(self):
        for i in range(4):
            for j in range(4):
                if self.matrix[i][j] == 2048:
                    print("WINNER")
                    return True
        return not (self.checkIfVerticalIsPossible() or self.checkIfHorizontIsPossible())




    def stackRIGHT(self):
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()


    def stackLEFT(self):
        self.stack()
        self.combine()
        self.stack()


    def stackUP(self):
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()


    def stackDOWN(self):
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()

    def compareMatrix(self, temp):
        if temp == self.matrix:
            return True
        return False



    def play(self):
        while True:
            vstup = input()
            tempBoard = copy.deepcopy(self.matrix)
            if vstup == "4":
                print("DIRECTION: LEFT")
                self.stackLEFT()
            elif vstup == "8":
                print("DIRECTION: UP")
                self.stackUP()
            elif vstup == "6":
                print("DIRECTION: RIGHT")
                self.stackRIGHT()
            elif vstup == "2":
                print("DIRECTION: DOWN")
                self.stackDOWN()
            elif vstup == "q":
                break
            if self.compareMatrix(tempBoard):
                print("INVALID MOVE. MAKE NEW MOVE")
            else:
                if self.checkScore():
                    break
                else:
                    try:
                        self.addNewTwo()
                        self.display()
                    except Exception as ex:
                        print("Could not add new number", ex)
                        break


if __name__ == '__main__':
    game = Game()
    game.play()
