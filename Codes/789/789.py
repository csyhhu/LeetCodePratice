def escapeGhosts(ghosts, target):

    distance_to_target = abs(target[0]) + abs(target[1])

    for g in ghosts:
        distance_ghost_to_target = abs(target[0] - g[0]) + abs(target[1] - g[1])
        if distance_ghost_to_target <= distance_to_target:
            return False

    return True


print(escapeGhosts([[1,0],[0,3]], target = [0,1]))
print(escapeGhosts([[1,0]], target = [2,0]))
print(escapeGhosts([[2,0]], target = [1,0]))
print(escapeGhosts(ghosts = [[5,0],[-10,-2],[0,-5],[-2,-2],[-7,1]], target = [7,7]))
print(escapeGhosts(ghosts = [[-1,0],[0,1],[-1,0],[0,1],[-1,0]], target = [0,0]))