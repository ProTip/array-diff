from protip import diff_arrays
import sys

def main():
  current = map(int, sys.stdin.readline().rstrip().split(" "))
  target = map(int, sys.stdin.readline().rstrip().split(" "))

  adds, dels = diff_arrays(current, target)
  print("additions", adds)
  print("deletions", dels)

main()