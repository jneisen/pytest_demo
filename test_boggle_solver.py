import unittest
from boggle_solver import Boggle

class TestAdd(unittest.TestCase):
    def test_0x0(self):
        grid = [[]]
        dictionary = ['abcd']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = []
        
        self.assertEqual(solution, expected)

    def test_1x1(self):
        grid = [['a']]
        dictionary = ['abcd']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = []
        
        self.assertEqual(solution, expected)

    def test_2x2(self):
        grid = [['a', 'b'], ['c', 'd']]
        dictionary = ['abcd']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['abcd'])
        
        self.assertEqual(solution, expected)

    def test_3x3(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['abcd', 'bef', 'abcedghief', 'abcdef']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['bef', 'abcedghief'])
        
        self.assertEqual(solution, expected)

    def test_5x5(self):
        grid = [['a', 'b', 'c', 'd', 'e'], ['d', 'e', 'f', 'g', 'h'], ['g', 'h', 'ie', 'j', 'k'], ['l', 'm', 'n', 'o', 'p'], ['qu', 'r', 'st', 't', 'u']]
        dictionary = ['abcd', 'bef', 'abcedghife', 'abcdef', 'abcdehgfedghiejkponmlqursttu']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['abcd', 'bef', 'abcdehgfedghiejkponmlqursttu'])
        
        self.assertEqual(solution, expected)

    def test_12x12(self):
        grid = [['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ie', 'j', 'k', 'l']]
        dictionary = ['abcdef', 'defghieieieie', 'llllllllllll', 'abcdefggfeddd', 'xquie']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['abcdef', 'defghieieieie', 'llllllllllll', 'abcdefggfeddd'])
        
        self.assertEqual(solution, expected)

    def test_every_direction(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['eabc', 'ebad', 'ecba', 'efcb', 'eief', 'ehief', 'egda', 'aieh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['eabc', 'ebad', 'ecba', 'efcb', 'eief', 'ehief', 'egda'])
        
        self.assertEqual(solution, expected)

    def test_short_dictionary_words(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['cbad', 'eab', 'bcf', 'ab', 'fie', 'gh', 'hd', 'e', 'a', '']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['cbad', 'eab', 'bcf', 'fie'])
        
        self.assertEqual(solution, expected)

    def test_st_qu_ie_dictionary_words(self):
        grid = [['st', 'b', 'c'], ['d', 'qu', 'f'], ['g', 'h', 'ie']]
        dictionary = ['stbc', 'fhqu', 'iequ', 'iehg', 'iequstc']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['stbc', 'fhqu', 'iequ', 'iehg'])
        
        self.assertEqual(solution, expected)

    def test_valid_duplicated_letters(self):
        grid = [['a', 'b', 'c'], ['a', 'e', 'a'], ['g', 'a', 'ie']]
        dictionary = ['abceg', 'abcaaa', 'aaaa', 'ieaa', 'gaie', 'giea']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['abceg', 'abcaaa', 'aaaa', 'ieaa', 'gaie'])
        
        self.assertEqual(solution, expected)

    def test_invalid_duplicated_letters(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['abcea', 'befgb', 'bbae', 'ghie']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['ghie'])
        
        self.assertEqual(solution, expected)

    def test_empty_dictionary(self):
        grid = [['a', 'b', 'c'], ['a', 'e', 'a'], ['g', 'a', 'ie']]
        dictionary = []
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = []
        
        self.assertEqual(solution, expected)

    def test_dictionary_includes_ints(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = [123, 456, 'abce']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_dictionary_invalid_type_set(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = {'abced', 'feda', 'aieh'}
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        solution = [word.lower() for word in solution]
        solution = sorted(solution)

        expected = sorted(['abced', 'feda'])
        
        self.assertEqual(solution, expected)

    def test_dictionary_invalid_type_int(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = 1
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())

        self.assertEqual(solution, [])

    def test_invalid_grid_letters_special_char(self):
        grid = [['$', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_s_char(self):
        grid = [['s', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_q_char(self):
        grid = [['q', 'b', 'c'], ['d', 'e', 'q'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_i_char(self):
        grid = [['a', 'b', 'c'], ['d', 'e', 'i'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_space_char(self):
        grid = [['a', 'b', 'c'], ['d', 'e', ' '], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_empty_char(self):
        grid = [['a', 'b', 'c'], ['d', 'e', ''], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_newline_char(self):
        grid = [['a', 'b', 'c'], ['d', 'e', '\n'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_letters_number_char(self):
        grid = [['a', 'b', 'c'], ['d', 'e', '4'], ['g', 'h', 'ie']]
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)
        
        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])

    def test_invalid_grid_not_2d_list(self):
        grid = ['a', 'b', 'c', 'd', 'e', '4', 'g', 'h', 'ie']
        dictionary = ['bceh']
        boggle = Boggle(grid, dictionary)

        solution = list(boggle.getSolution())
        
        self.assertEqual(solution, [])
