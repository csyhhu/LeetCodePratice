import sys

n, m, c = sys.stdin.readline().strip('\n').split()
n, m, c  = int(n), int(m), int(c)

bracelet = []
for idx in range(n):
    bracelet.append([0] * c)
    line = sys.stdin.readline().strip('\n').split()
    n_cur_color = int(line[0])
    for color_idx in range(n_cur_color):
        color = int(line[color_idx + 1])
        bracelet[-1][color-1] += 1
        # bracelet[-1][color_idx] += 1

invalid = [0] * c
for idx in range(n):
    start, end = idx, (idx + m) % n
    if start < end:
        part = list(zip(*bracelet[start: end]))
    else:
        end_part = bracelet[start::]
        begin_part = bracelet[0: end]
        part = list(zip(*(end_part + begin_part)))
    for color_idx in range(c):
        if invalid[color_idx] == 0:
            # Check its validility
            if sum(part[color_idx]) >= m:
                invalid[color_idx] = 1
print(sum(invalid))