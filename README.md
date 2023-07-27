# Find My Number Solution


## Description
The provided solution is designed to calculate a sequence of 10 successive knight moves (by default), given a keypad and a starting key press

The solution treats the keypad as a grid and calculates possible moves based on key positions within the constraints of the grid

Therefore, it should work not only with the keypad from the assignment, but with the keypad of any size or layout

(assuming it has a sufficient amount of keys and rows to support knight moves)

You may also instruct the code to generate more or less than 10 subsequent moves if you wish

## Installation

No installation is required, the code is written using Python3 standard library modules and objects

It should work as long as it is run in a Python3.9+ environment

## Execution

Please run `main.py` to execute the solution against all the keys of the assignment keypad

If you wish to execute it differently, please see the example below:

```python
from path_finder import PathFinder

keypad = ()             # keypad as a tuple of key rows as tuples
sequence_size = 10      # the amount of successive L-moves in the sequence. Maximum possible number will vary depending on chosen keypad and key
vowel_list = 'AEIOUY'   # which characters are treated as vowels. 


pathfinder = PathFinder(keypad, sequence_size, vowel_list)

pathfinder.start()      # you can specify a single key either as a parameter to this method or enter it via user input 
```