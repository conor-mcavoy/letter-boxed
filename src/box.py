class Box:
    def __init__(self, *sides):
        self.sides = sides
        self.letter_set = set(''.join(sides))

    def is_valid_word(self, word):
        if set(word) <= self.letter_set:
            for i in range(0, len(word) - 1):
                if not self.are_in_diff_sides(word[i], word[i + 1]):
                    return False
            return True
        return False

    def are_in_diff_sides(self, letter1, letter2):
        for side in self.sides:
            if letter1 in side:
                return letter2 not in side
            if letter2 in side:
                return letter1 not in side
        return False  # should never be reached
