from itertools import combinations_with_replacement as comb_with_repl
from itertools import permutations
from random import sample
from string import lowercase

def generate_instance(colors, sticks, length):
    """Returns a random instance of the sticks problem, which is a list (of
    length sticks) of tuples (of size length) whose elements are
    chosen from range(colors).

    The returned list has no repeated tiles (including flipped tiles).
    """
    # need that list() call because sample doesn't take arbitrary iterables
    return sample(list(comb_with_repl(range(colors), length)), sticks)

def tile_to_letters(tile):
    """Translates the specified tile from numeric elements to corresponding
    lowercase characters.
    
    Elements of the tile must be numbers less then 26.

    """
    return tuple(map(lambda c: lowercase[c], tile))

def instance_to_letters(instance):
    """Translates each tile in the specified instance to have alphabetical
    cells instead of numerical cells by calling the tile_to_letters() method on
    each tile.

    """
    return map(tile_to_letters, instance)

def overlap(tile1, tile2):
    """Returns the number of cells on which tile1 and tile2 overlap.

    This method is asymmetric; overlap(s, t) might not equal overlap(t,
    s). tile1 is considered to be the left tile, and tile2 is considered to be
    the right tile.

    The lengths of tile1 and tile2 must be equal. The behavior of this method
    is undefined if tile1 and tile2 do not have the same length.

    """
    length = len(tile1)
    i = 0
    while i < length and tile1[i:] != tile2[:length - i]:
        i += 1
    return length - i

def score(layout):
    """Returns the overall score of the specified layout (a list of tiles).

    The computed score is l * n - o, where l is the length of a single tile, n
    is the total number of tiles, and o is the total number of overlaps for
    each sequential pair of tiles.

    """
    s = sum(overlap(layout[i], layout[i + 1]) for i in range(len(layout) - 1))
    return sum(map(len, layout)) - s

def best(layouts):
    """Returns the layout with the minimum score of the specified iterable of
    layouts.

    """
    return min(layouts, key=score)

def greedy(instance):
    """Performs a greedy search for the best solution of instances with tiles
    of size two.

    """
    # TODO hold double tiles until the end!!!
    result = []
    while len(instance) > 0:
        tile = instance.pop()
        i = 0
        while i < len(result) and overlap(tile, result[i]) > 1:
            i += 1
        result.insert(i, tile)
    return result

def brute_force(instance):
    """Performs a brute force search to find the layout with the minimum
    possible layout of the tiles specified in the instance.

    WARNING: use at your own risk. This will take a very long time.

    """
    return best(permutations(instance))

if __name__ == '__main__':
    instance = generate_instance(6, 8, 2)
    b = brute_force(instance)
    print 'original instance:', instance
    print 'best layout (score', score(b), '):', instance_to_letters(b)
