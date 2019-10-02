class Solution(object):
    
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        max_len = len(tiles)
        permuted_array = range(max_len)

        import itertools
        possible_tiles = set()

        for length in range(1, max_len + 1):
            for selected_idx in itertools.permutations(permuted_array, length):
                permuted_tiles = ''
                for idx in selected_idx:
                    permuted_tiles += tiles[idx]
                possible_tiles.add(permuted_tiles)

        return len(possible_tiles)



s = Solution()
print(s.numTilePossibilities("AAABBC"))