def pathInZigZagTree(label):

    import math

    path = []
    while label != 1:
        label = int(label / 2)
        # Reverse label
        level = int(math.log2(label))
        label = 2**(level+1) - label - 1 + 2**(level)
        path.append(label)
    path.append(1)
    return reversed(path)

