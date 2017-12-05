num = 368078
cur = 1
corners = [1, 1, 1, 1]
r = 0

corner_indexes = [0]
cur_increment = 1
n = 0
#soooo inneficient
while n < num:
    for x in range(0, 4):
        n = n + cur_increment*2
        corner_indexes.append(n)
    corner_indexes[-1] = corner_indexes[-1] +1
    cur_increment += 1
pre_corners = [c - 1 for c in corner_indexes[1:]]
post_corners = [c + 1 for c in corner_indexes[1:]]

#when there are sides
n = 10
#for non-corner pieces, corresponding pair
pairs = {}
diff = 9
while n < num:
    if n in corner_indexes:
        diff += 2
    else:
        pairs[n] = n - diff
    n += 1

# current starts here, dont have to worry about initial scenarios
n = 10
spiral = [1, 1, 2, 4, 5, 10, 11, 23, 25, 26]
## THERE ABSOLUTELY HAS TO BE A WAY TO GENERALIZE THIS
while spiral[-1] < num:
    if n in corner_indexes:
        i = pairs[n - 1]
        curr = spiral[n - 1] + spiral[i]
    elif n in pre_corners:
        i = pairs[n]
        curr = spiral[n - 1] + spiral[i] + spiral[i - 1]
    elif n in post_corners:
        i = pairs[n]
        curr = spiral[n - 1] + spiral[n - 2] + spiral[i] + spiral[i + 1]
    else:
        i = pairs[n]
        curr = spiral[n - 1] + spiral[i] + spiral[i + 1] + spiral[i - 1]
    spiral.append(curr)
    n += 1

print spiral
