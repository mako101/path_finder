# Find My Number Solution


## Description
The provide solution is designed to provide a sequence of 10 knight moves (by default), given a keypad and the starting key press

The solution treats keyboard as a grid and calculates possible moves within the constraints of the grid

Therefore, it should work not only with the keypad from the assignment, but with the keypad of any size or layout

(assuming it has enough keys to generate 10 knight moves)

## Installation

No installation is required, the code is written using Python3 standard library modules and objects

It should work as long as it is run Python3.9+ environment

## Execution

Please run `main.py` to execute the solution against all the keys of the assignment keypad

If you wish to execute it differently, please use the following code

```python
from path_finder import PathFinder

keypad = ()             # keypad as a tuple of key rows as tuples
sequence_size = 10      # the amount of successive L-moves in the sequence. Maximum possible number will vary depending on chosen keypad and key
vowel_list = 'AEIOUY'   # which characters are treated as vowels. 


pathfinder = PathFinder(keypad, sequence_size, vowel_list)

pathfinder.start()      # you can specify a single key either as a parameter to this method or enter it via user input 
```