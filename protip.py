def diff_arrays(a, b):
    a.sort()
    b.sort()

    additions = []
    deletions = []

    x = 0
    y = 0
    while True:
        nextX = x + 1
        nextY = y + 1

        # If we have passed the end of a[] then remainder b[]'s are additions
        if (x == len(a)):
            additions += b[y:]
            break

        # If we have passed the end of b[] then remainder a[]'s are deletions'
        if (y == len(b)):
            deletions += a[x:]
            break

        curr = a[x]
        targ = b[y]

        # If we arrived at both ends we need to apply both differences
        if (nextX == len(a)) and (nextY == len(b)):
            if curr != targ:
                additions.append(targ)
                deletions.append(curr)
            break

        # No end scenarios

        if curr > targ:
            additions.append(targ)
            y += 1
            continue
        elif curr < targ:
            deletions.append(curr)
            x += 1
            continue
        elif curr == targ:
            x += 1
            y += 1
            continue

    return additions, deletions
