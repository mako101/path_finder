import random


class PathFinder:
    """
    A class to find a sequence of 10 successive knight moves,
    given a keypad and an initial keystroke
    The provided solution is designed to work with any keypad
    i.e. of varying size and available keys, as long as:
    - the keys on the keypad are in standard English
      (for other languages, please update the vowel list as necessary)
    - the keypad is provided as a tuple of key row tuples
    - any missing keys on the keyboard are passed in as ` `
      (such as those in the last row of the sample keypad, which only has 3 actual keys)
    """

    def __init__(self, keypad: tuple, vowel_list: str = None):
        self.keypad = keypad
        self.keypad_layout = None
        self.start_key = None
        self.start_position = None
        self.all_moves = None
        self.possible_moves = None
        self.valid_moves = None
        self.move_sequence = None
        self.keypress_sequence = None
        self.vowel_list = vowel_list
        if not vowel_list:
            self.vowel_list = 'AEIOUY'
        self.get_keypad_layout()

    def get_keypad_layout(self):
        """Create a dictionary of {keypad_row: row_length}"""
        self.keypad_layout = {
            row_index: len(key_row) for row_index, key_row in enumerate(self.keypad)
        }

    def get_start_position(self, key: str):
        """Determine which key was pressed (ie where it is on the keypad)"""
        for row_index, key_row in enumerate(self.keypad):
            if key in key_row:
                self.start_position = row_index, key_row.index(key)
                break
        else:
            raise Exception(f'Key {key} not found on the keypad')

    def get_all_moves(self):
        """
        There are 8 possible moves from any given position on the keyboard.
        We calculate them as tuples of index postions,
        relative to the given key
        :param key:
        :return:
        """

        line_index, key_index = self.start_position
        # print(line_index, key_index)

        h_right_base = [
            (line_index, key_index),
            (line_index, key_index + 1),
            (line_index, key_index + 2),
        ]

        h_right_down = h_right_base.copy()
        h_right_down.append(
            (line_index + 1, key_index + 2)
        )

        h_right_up = h_right_base.copy()
        h_right_up.append(
            (line_index - 1, key_index + 2)
        )

        h_left_base = [
            (line_index, key_index),
            (line_index, key_index - 1),
            (line_index, key_index - 2),
            ]

        h_left_down = h_left_base.copy()
        h_left_down.append(
            (line_index + 1, key_index - 2))

        h_left_up = h_left_base.copy()
        h_left_up.append(
            (line_index - 1, key_index - 2))

        v_down_base = [
            (line_index, key_index),
            (line_index + 1, key_index),
            (line_index + 2, key_index),
        ]

        v_down_right = v_down_base.copy()
        v_down_right.append(
            (line_index + 2, key_index + 1)
        )

        v_down_left = v_down_base.copy()
        v_down_left.append(
            (line_index + 2, key_index - 1)
        )

        v_up_base = [
            (line_index, key_index),
            (line_index - 1, key_index),
            (line_index - 2, key_index),
        ]

        v_up_right = v_up_base.copy()
        v_up_right.append(
            (line_index - 2, key_index + 1)
        )

        v_up_left = v_up_base.copy()
        v_up_left.append(
            (line_index - 2, key_index - 1)
        )

        self.all_moves = h_left_down, h_left_up, h_right_down, h_right_up, \
            v_down_left, v_down_right, v_up_left, v_up_right

    def get_possible_moves(self):
        """
        We filter out impossible moves at this stage
        Impossible move is the one where the expected position
        is outside of possible index positions in the given row
        """
        # TODO refactor
        self.possible_moves = list()
        for move in self.all_moves:
            possible = True
            for row, index in move:
                if (row not in self.keypad_layout.keys()) or (index not in range(0, self.keypad_layout[row])):
                    possible = False
                    break
            if possible:
                self.possible_moves.append(move)

    def is_vowel(self, key):
        """Check if the key is a vowel."""
        return key in self.vowel_list

    def get_valid_moves(self):
        """Filter out moves including missing keys"""
        # TODO optimize and remove - just check for blanks?
        self.valid_moves = list()
        for move in self.possible_moves:
            move_sequence = [self.keypad[x][y] for x, y in move]
            if ' ' in move_sequence:
                continue
            self.valid_moves.append(move_sequence)

    def get_next_move_set(self, key):
        """Given a key, get a list of possible valid moves from this position"""
        self.get_start_position(key)
        self.get_all_moves()
        self.get_possible_moves()
        self.get_valid_moves()

    def get_start_key(self):
        user_message = 'Given the keypad below:\n'
        for row in self.keypad:
            user_message += f'|{"|".join(row)}|\n'
        user_message += 'Please enter a key to start the move sequence from: '
        self.start_key = input(user_message)

    def get_move_sequence(self):
        """Get 10 moves based on and initial key"""
        self.move_sequence = list()
        while len(self.move_sequence) < 10:
            if not self.move_sequence:
                # get a random valid move
                self.get_next_move_set(self.start_key)
                self.move_sequence.append(random.choice(self.valid_moves))

            else:
                next_key = self.move_sequence[-1][-1]
                self.get_next_move_set(next_key)
                # filter out the moves already in the sequence
                # this is to avoid the code looping over the same characters infinitely
                self.valid_moves = list(filter(lambda i: i not in self.move_sequence, self.valid_moves))
                # TODO ADD check for going back to the same character
                self.move_sequence.append(random.choice(self.valid_moves))
                self.keypress_sequence = [move[0] for move in self.move_sequence]
                # check the vowel count and abort if it is more than 2
                vowel_count = sum(map(lambda x: self.is_vowel(x), self.keypress_sequence))
                if vowel_count > 2:
                    raise ValueError()


        else:
            # TODO FIX THE OUTPUT
            print(self.move_sequence)
            return self.keypress_sequence

    def start(self, start_key=None):
        """
        Start the exercise
        The initial key can be passed as an argument or received via user input
        As valid moves are chosen at random it is possible that the final sequence may contain less than 10 moves
        in which case IndexError will be raised
        we catch the error and attempt the exercise again until we get a sequence of 10 moves
        """
        if start_key:
            self.start_key = start_key
        else:
            self.get_start_key()
        result = None
        while not result:
            try:
                result = self.get_move_sequence()
                print(result)
            except (IndexError, ValueError):
                pass
