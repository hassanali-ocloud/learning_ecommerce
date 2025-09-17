class Database():
    def __get_blank_guess_word(self, target_word: str):
        guessed_word = ""
        for x in range(len(target_word)):
            guessed_word += "_"
        return guessed_word

    def __init__(self, target_word, total_guess):
        self.__target_word = target_word
        self.__total_guess = total_guess
        self.__guess_amount = 0
        self.__guessed_word = self.__get_blank_guess_word(target_word)
    
    @property
    def total_guess(self):
        return self.__total_guess

    @property
    def target_word(self):
        return self.__target_word

    @property
    def guess_amount(self):
        return self.__guess_amount
    
    @property
    def guessed_word(self):
        return self.__guessed_word

    def update_guessed_word(self, value):
        self.__guessed_word = value
    
    def update_guess_amount(self):
        self.__guess_amount += 1
        
    
    