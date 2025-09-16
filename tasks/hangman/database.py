class Database():
    def __init__(self, guess_word):
        self.guess_word = guess_word
        self._total_guess = 6
        self._guess_remains = 6
        self._guessed_word = "______"
    
    @property
    def guess_remains(self):
        return self._guess_remains