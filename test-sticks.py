import string
import unittest

from sticks import best
from sticks import generate_instance
from sticks import greedy
from sticks import instance_to_letters
from sticks import tile_to_letters
from sticks import overlap
from sticks import score
from sticks import brute_force

# the number of instances to generate when running multiple tests
NUM_INSTANCES = 10

COLORS = 6
TILES = 5
LENGTH = 2

class TestSticksFunctions(unittest.TestCase):
    """Test class for functions in the sticks module."""

    def test_best(self):
        """Test method for the best method."""
        layout1 = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
        layout2 = [(1, 2, 3), (3, 4, 5), (4, 5, 6)]
        layout3 = [(1, 2, 3), (4, 5, 6), (6, 7, 8)]
        self.assertIs(best((layout1, layout2, layout3)), layout1)

    def test_generate_instance(self):
        """Test method for the generate_instance method."""
        instance = generate_instance(3, 6, 2)
        expected = [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]
        self.assertItemsEqual(instance, expected)

    def test_greedy(self):
        """Test method for the greedy method."""
        for n in range(NUM_INSTANCES):
            instance = generate_instance(COLORS, TILES, LENGTH)

            print 'brute force'
            brute_force_solution = brute_force(instance)
            brute_force_score = score(brute_force_solution)
            print 'bf', brute_force_score, ':', brute_force_solution

            print 'greedy'
            greedy_solution = greedy(instance)
            greedy_score = score(greedy_solution)
            print 'gr', greedy_score, ':', greedy_solution

            self.assertEqual(greedy_score, brute_force_score)

    def test_tile_to_letters(self):
        """Test method for the tile_to_letters method."""
        tile = tuple(range(26))
        self.assertEqual(''.join(tile_to_letters(tile)), string.lowercase)

    def test_instance_to_letters(self):
        """Test method for the instance_to_letters method."""
        tile1 = (1, 2, 3)
        tile2 = (2, 3, 4)
        tile3 = (3, 4, 5)
        letters1 = ('b', 'c', 'd')
        letters2 = ('c', 'd', 'e')
        letters3 = ('d', 'e', 'f')
        instance = [tile1, tile2, tile3]
        expected = [letters1, letters2, letters3]
        self.assertEqual(instance_to_letters(instance), expected)

    def test_overlap(self):
        """Test method for the overlap method."""
        tile1 = (1, 2, 3)
        tile2 = (1, 2, 3)
        self.assertEqual(overlap(tile1, tile2), 3)
        tile2 = (2, 3, 4)
        self.assertEqual(overlap(tile1, tile2), 2)
        tile2 = (3, 4, 5)
        self.assertEqual(overlap(tile1, tile2), 1)
        tile2 = (4, 5, 6)
        self.assertEqual(overlap(tile1, tile2), 0)
        self.assertEqual(0, overlap((1, 3), (0, 2)))

    def test_score(self):
        """Test method for the score method."""
        layout = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
        self.assertEqual(score(layout), 7)
        layout = [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
        self.assertEqual(score(layout), 5)
        layout = [(1, 1), (1, 1), (1, 1)]
        self.assertEqual(score(layout), 2)

    def test_brute_force(self):
        """Test method for the brute_force method."""
        self.fail('Not yet implemented')

if __name__ == '__main__':
    unittest.main()
