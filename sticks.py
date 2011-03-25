from itertools import combinations_with_replacement
from itertools import permutations
from random import sample
from string import lowercase

def generate_instance(num_colors, num_sticks, stick_length):
    return sample(list(combinations_with_replacement(range(num_colors),
                                                     stick_length)),
                  num_sticks)

def tile_to_letters(tile):
    return tuple(map(lambda c: lowercase[c], tile))

def instance_to_letters(instance):
    return map(tile_to_letters, instance)

def overlap(tile1, tile2):
    # this is asymmetric
    if tile1 == tile2:
        return len(tile1)
    length = len(tile1)
    result = length - 1
    for i in range(1, length):
        if tile1[i:] == tile2[:-i]:
            break
        result -= 1
    return result

def score(layout):
    total_overlap = 0
    for i in range(len(layout) - 1):
        total_overlap += overlap(layout[i], layout[i + 1])
    return sum(map(len, layout)) - total_overlap

def brute_force(instance):
    # WARNING: this will take a looong time
    all_perms = permutations(instance)
    result = dict(zip(all_perms, map(score, all_perms)))

if __name__ == '__main__':
    num_colors = 10
    num_sticks = 5
    stick_length = 2
    instance = to_letters(generate_instance(num_colors, num_sticks,
                                            stick_length))
