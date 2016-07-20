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
    print(x,y)

    # If we have passed the end of a[] then remainder b[]'s are additions
    if (x == len(a)):
      print("end->append adds")
      additions += b[y:]
      break

    # If we have passed the end of b[] then remainder a[]'s are deletions'
    if (y == len(b)):
      print("end->append dels")
      deletions += a[x:]
      break

    curr = a[x]
    targ = b[y]
    print(curr,targ)

    # If we arrived at both ends we need to apply both differences
    if (nextX == len(a)) and (nextY == len(b)):
      print("end->both")
      if curr != targ:
        additions.append(targ)
        deletions.append(curr)
      break

    # No end scenarios

    if curr > targ:
      print("add", targ)
      additions.append(targ)
      y += 1
      continue
    elif curr < targ:
      print("del", curr)
      deletions.append(curr)
      x += 1
      continue
    elif curr == targ:
      print("eq")
      x += 1
      y += 1
      continue

  return additions, deletions