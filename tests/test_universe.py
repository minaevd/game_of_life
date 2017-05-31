from context import universe
import unittest


class BasicTestsUniverse(unittest.TestCase):
    """Basic test cases for Universe."""

    @classmethod
    def setUpClass(self):
        self.u = universe.Universe(10, 10)

        self.u.give_life(2, 2)
        self.u.give_life(2, 3)
        self.u.give_life(2, 4)

        self.u.give_life(3, 2)
        self.u.give_life(3, 3)
        self.u.give_life(3, 4)

        self.u.give_life(4, 2)
        self.u.give_life(4, 3)
        self.u.give_life(4, 4)

    def test_get_neighbours_for_surrounded(self):
        self.assertEqual(self.u.get_neighbours(3, 3), 8,
                         'Error in getting neighbours for a cell surrounded with neighbours')

    def test_get_neighbours_for_surrounded_three_sides(self):
        self.assertEqual(self.u.get_neighbours(4, 3), 5,
                         'Error in getting neighbours for a cell surrounded with neighbours from three sides and two corners')

    def test_get_neighbours_for_surrounded_one_side(self):
        self.assertEqual(self.u.get_neighbours(5, 3), 3,
                         'Error in getting neighbours for a cell surrounded with neighbours from one side and two corners only')

    def test_give_life(self):
        self.u.give_life(6,6)
        self.assertEqual(self.u.get_neighbours(7, 6), 1,
                         'Error in getting neighbours for a cell surrounded with just a single neighbour')

    def test_take_life(self):
        self.u.take_life(6,6)
        self.assertEqual(self.u.get_neighbours(7, 6), 0,
                         'Error in getting neighbours for a cell surrounded with no neighbours')

if __name__ == '__main__':
    unittest.main()