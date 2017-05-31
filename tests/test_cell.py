from context import cell
import unittest


class BasicTestsCell(unittest.TestCase):
    """Basic test cases for Cell."""

    @classmethod
    def setUpClass(self):
        self.c = cell.Cell(1,1)

    def test_alive_cell(self):
        self.assertEqual(self.c.alive, True, 'Error in checking if cell is alive right after initialization')

    def test_die(self):
        self.c.die()
        self.assertEqual(self.c.alive, False, 'Error in destroying cell')

    def test_be_born(self):
        self.c.be_born()
        self.assertEqual(self.c.alive, True, 'Error in getting cell into the world')

if __name__ == '__main__':
    unittest.main()