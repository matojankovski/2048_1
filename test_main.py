import unittest
from main import Game

class TestMatrixLogic(unittest.TestCase):

    def test_stack(self):
        example_board = Game()
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
        example_board.stack()
        self.assertEqual(example_board.matrix, [[0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 0], [0, 0, 0, 0]])
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 2]]
        example_board.stack()
        self.assertEqual(example_board.matrix, [[0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
        example_board.matrix = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        example_board.stack()
        self.assertEqual(example_board.matrix, [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_combine(self):
        example_board = Game()
        example_board.matrix = [[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        example_board.combine()
        self.assertEqual(example_board.matrix, [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
        example_board.matrix = [[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        example_board.combine()
        self.assertEqual(example_board.matrix, [[2, 0, 0, 0], [2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

    def test_reverse(self):
        example_board = Game()
        example_board.matrix = [[2, 2, 4, 0], [4, 2, 16, 8], [0, 8, 4, 0], [2, 0, 2, 0]]
        example_board.reverse()
        self.assertEqual(example_board.matrix, [[0, 4, 2, 2], [8, 16, 2, 4], [0, 4, 8, 0], [0, 2, 0, 2]])
        example_board.matrix = [[4, 2, 4, 2], [0, 8, 16, 2], [2, 4, 8, 16], [0, 0, 0, 0]]
        example_board.reverse()
        self.assertEqual(example_board.matrix, [[2, 4, 2, 4], [2, 16, 8, 0], [16, 8, 4, 2], [0, 0, 0, 0]])

    def test_transpose(self):
        example_board = Game()
        example_board.matrix = [[2, 2, 4, 0], [4, 2, 16, 8], [0, 8, 4, 0], [2, 0, 2, 0]]
        example_board.transpose()
        self.assertEqual(example_board.matrix, [[2, 4, 0, 2], [2, 2, 8, 0], [4, 16, 4, 2], [0, 8, 0, 0]])
        example_board.matrix = [[4, 2, 4, 2], [0, 8, 16, 2], [2, 4, 8, 16], [0, 0, 0, 0]]
        example_board.transpose()
        self.assertEqual(example_board.matrix, [[4, 0, 2, 0], [2, 8, 4, 0], [4, 16, 8, 0], [2, 2, 16, 0]])

    def test_merge_directions(self):
        example_board = Game()
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
        example_board.stack_right()
        self.assertEqual(example_board.matrix, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 0]], "If we move 2x 2 from [0,2,2,0] in the third row to RIGHT we will get [0,0,0,4]")
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
        example_board.stack_left()
        self.assertEqual(example_board.matrix, [[0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]], "If we move 2x 2 from [0,2,2,0] in the third row to LEFT we will get [4,0,0,0]")
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
        example_board.stack_down()
        self.assertEqual(example_board.matrix, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0]], "If we move 2x 2 from [0,2,2,0] in the third row to DOWN we will get [0,2,2,0]")
        example_board.matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
        example_board.stack_up()
        self.assertEqual(example_board.matrix, [[0, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "If we move 2x 2 from [0,2,2,0] in the third row to UP  we will get [0,2,2,0]")

    def test_compareMatrix(self):
        example_board = Game()
        example_board.matrix = [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]]
        example_board_copy = [[0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 2]]
        self.assertTrue(example_board.compare_matrix(example_board_copy))
        example_board_copy = [[0, 0, 0, 2], [0, 0, 0, 2], [2, 0, 0, 2], [0, 0, 0, 2]]
        self.assertFalse(example_board.compare_matrix(example_board_copy))

    def test_checkIfHorizontIsPossible(self):
        example_board = Game()
        example_board.matrix = [[2, 4, 8, 16], [4, 8, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        self.assertFalse(example_board.check_if_horizont_is_possible())
        example_board.matrix = [[2, 4, 8, 16], [2, 2, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        self.assertTrue(example_board.check_if_horizont_is_possible())

    def test_checkIfVerticalIsPossible(self):
        example_board = Game()
        example_board.matrix = [[2, 4, 8, 16], [4, 8, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        self.assertFalse(example_board.check_if_vertical_is_possible())
        example_board.matrix = [[2, 4, 8, 16], [2, 2, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        self.assertTrue(example_board.check_if_vertical_is_possible())

    def test_check_score(self):
        example_board = Game()
        example_board.matrix = [[2, 2, 2, 2], [0, 0, 0, 2], [0, 0, 0, 2], [0, 0, 0, 0]]
        self.assertFalse(example_board.check_score())
        example_board.matrix = [[2, 2, 2, 2], [0, 2048, 0, 2], [0, 0, 0, 2], [0, 0, 0, 0]]
        self.assertTrue(example_board.check_score())

    def test_addNewTwo(self):
        example_board = Game()
        example_board.matrix = [[2, 4, 8, 16], [4, 8, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        self.assertRaises(Exception, example_board.add_new_two)
        example_board.matrix = [[0, 4, 8, 16], [4, 8, 16, 2], [2, 4, 8, 16], [4, 8, 16, 2]]
        example_board.add_new_two()



if __name__ == '__main__':
    unittest.main()
