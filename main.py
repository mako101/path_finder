from path_finder import PathFinder

keypad = (
    ('A', 'B', 'C', 'D', 'E'),
    ('F', 'G', 'H', 'I', 'J'),
    ('K', 'L', 'M', 'N', 'O'),
    (' ', '1', '2', '3', ' ')
)

pathfinder = PathFinder(keypad)


# Run against all keys on the given keypad
all_keys = list()
for row in keypad:
    for key in row:
        if key != ' ':
            all_keys.append(key)

for key in all_keys:
    pathfinder.start(key)
