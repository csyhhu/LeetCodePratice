# LeetCode 1079

## Description

Given an array (elements may be duplicated), find out the maximum number of the sorted (sub)arrays that can be possibly generated:

Examples:

- 'ABC' => 'A', 'B', 'C', 'AB', 'AC', 'BC', 'CB', 'BA', 'ABC', 'BCA', 'CBA'.

## Solution
Noticed that the length of the given array is limited (<=7). Brutal search with duplicated subarray elimination should works.

- Brutal serarch: Enumerate all the length of the subarray and enumerate the possible subarray given that length.

- Subarray elimination: ``set`` in ``Python``.


## Code
```
def numTilePossibilities(self, tiles):
    """
    :type tiles: str
    :rtype: int
    """
    max_len = len(tiles)
    permued_array = range(max_len)

    import itertools
    possible_tiles = set()

    for length in range(1, max_len + 1):
        for selected_idx in itertools.permutations(permuted_array, length):
            permuted_tiles = ''
            for idx in selected_idx:
                permuted_tiles += tiles[idx]
            possible_tiles.add(permuted_tiles)

    return len(possible_tiles)

```