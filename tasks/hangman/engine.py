class Engine():
    def __init__(self):
        pass

    def __change_index(self, word: str, index: int, letter: str):
        word_list = list(word)
        word_list[index] = letter
        word_list = "".join(word_list)
        return word_list

    def determine_body_status(guess_remains: int):
        if guess_remains == 6:
            return (True, True, True, True, True, True)
        elif guess_remains == 5:
            return (True, True, True, True, True, False)
        elif guess_remains == 4:
            return (True, True, True, True, False, False)
        elif guess_remains == 3:
            return (True, True, True, False, False, False)
        elif guess_remains == 2:
            return (True, True, False, False, False, False)
        elif guess_remains == 1:
            return (True, False, False, False, False, False)
        elif guess_remains == 0:
            return (False, False, False, False, False, False)

    def perform_check(self, target_word: str, input_letter: str, guessed_word: str):
        if not target_word.__contains__(input_letter):
            return None
        else:
            target_word_count = target_word.count(input_letter)
            guessed_word_count = guessed_word.count(input_letter)
            if target_word_count <= guessed_word_count:
                return None
            else:
                index = target_word.find(input_letter)
                exact_index = target_word.find(input_letter, index + (guessed_word_count))
                guessed_word = self.__change_index(guessed_word, exact_index, input_letter)
                return guessed_word
            
def main():
    eng = Engine()
    
    print(eng.perform_check("Hellow", "o", "_e___w"))

main()