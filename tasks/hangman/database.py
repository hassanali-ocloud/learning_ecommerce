class Database():
    def __init__(self, target_word):
        self.__target_word = target_word
        self.__total_guess = 6
        self.__guess_remains = self.__total_guess
        self.__guessed_word = "______"
    
    @property
    def target_word(self):
        return self.__target_word

    @property
    def guess_remains(self):
        return self.__guess_remains
    
    @property
    def guessed_word(self):
        return self.__guessed_word

    def update_guessed_word(self, value):
        self.__guessed_word = value
    
    def update_guess_remains(self):
        self.__guess_remains -= 1
        
    
    