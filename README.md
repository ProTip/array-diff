# array-diff

## Assumptions

**Order doesn't matter**</br>
Example array order may be coincidence, however no order information necessary
to reconstruct the original array is supplied in the example output.

**Duplicates need to be handled**</br>
While there are no duplicates in the example, they are not explicitly ruled out.
Otherwise converting to sets and diffing them would most likely be more efficient.

**Exact input/output format is not important**</br>
There doesn't appear to be a test harnes in place and the example input is not machine friendly.

## Time complexity
**O(n)**ish for diff generation. **O(n log n)** for Python sort.

## Running
Tested on ```python 2.7.6```.

Takes input in stdin as two lines representing the current array and target array. Numbers are
seperated by spaces:
```
1 2 3 4
2 4 50 100
```

**tests**</br>
```
$ python test.py
```

**program**</br>
```
$ python main.py < input.txt
```
