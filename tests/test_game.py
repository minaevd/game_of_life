from context import game
import unittest


class BasicTestsGame(unittest.TestCase):
    """Basic test cases for Game."""

    @classmethod
    def setUpClass(self):
        cells = [
              (2,2)
            , (3,3)
            , (4,4)
            , (5,5)
            , (6,6)
            , (7,7)
        ]
        self.g = game.Game(10,10,cells)

    def test_first_gen(self):
        self.g.next_gen()
        self.assertEqual(self.g.u.coords[2][2].alive, False, 'Error in the Universe after first generation')
        self.assertEqual(self.g.u.coords[7][7].alive, False, 'Error in the Universe after first generation')

    def test_second_gen(self):
        self.g.next_gen()
        self.assertEqual(self.g.u.coords[2][2].alive, False, 'Error in the Universe after second generation')
        self.assertEqual(self.g.u.coords[3][3].alive, False, 'Error in the Universe after second generation')
        self.assertEqual(self.g.u.coords[6][6].alive, False, 'Error in the Universe after second generation')
        self.assertEqual(self.g.u.coords[7][7].alive, False, 'Error in the Universe after second generation')

    def test_third_gen(self):
        self.g.next_gen()
        self.assertEqual(self.g.u.coords[2][2].alive, False, 'Error in the Universe after third generation')
        self.assertEqual(self.g.u.coords[3][3].alive, False, 'Error in the Universe after third generation')
        self.assertEqual(self.g.u.coords[4][4].alive, False, 'Error in the Universe after third generation')
        self.assertEqual(self.g.u.coords[5][5].alive, False, 'Error in the Universe after third generation')
        self.assertEqual(self.g.u.coords[6][6].alive, False, 'Error in the Universe after third generation')
        self.assertEqual(self.g.u.coords[7][7].alive, False, 'Error in the Universe after third generation')

if __name__ == '__main__':
    unittest.main()