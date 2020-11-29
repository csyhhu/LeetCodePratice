def minimumEffort(tasks:list):

    tasks.sort(key=lambda x: x[0] - x[1])

    # prev_saved: Energy saved after last task, To start a new task, we need to add mmin - prev_saved energy.
    ans = prev_saved = 0
    for cost, mmin in tasks:
        if mmin > prev_saved:
            ans += (mmin - prev_saved)
            prev_saved = mmin - cost
        else:
            prev_saved -= cost
    return ans

print(minimumEffort([[1,2],[2,4],[4,8]]))
print(minimumEffort([[1,3],[2,4],[10,11],[10,12],[8,9]]))
print(minimumEffort([[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]))