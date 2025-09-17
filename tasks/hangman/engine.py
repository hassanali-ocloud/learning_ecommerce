from database import Database
from enum import Enum

class Game_Status(Enum):
    GAME_OVER = "game_over"
    GAME_WON = "game_won"
    CONTINUE = "continue"

class Engine():
    def __init__(self):
        pass

    def __change_index(self, word: str, index: int, letter: str):
        word_list = list(word)
        word_list[index] = letter
        word_list = "".join(word_list)
        return word_list

    def determine_body_status(self, guess_remains: int):
        if guess_remains == 6:
            return True, True, True, True, True, True
        elif guess_remains == 5:
            return True, True, True, True, True, False
        elif guess_remains == 4:
            return True, True, True, True, False, False
        elif guess_remains == 3:
            return True, True, True, False, False, False
        elif guess_remains == 2:
            return True, True, False, False, False, False
        elif guess_remains == 1:
            return True, False, False, False, False, False
        elif guess_remains == 0:
            return False, False, False, False, False, False

    def perform_check(self, target_word: str, input_letter: str, guessed_word: str):
        lower_target_word = target_word.lower()
        lower_input_letter = input_letter.lower()
        lower_guessed_word = guessed_word.lower()
        if not lower_target_word.__contains__(lower_input_letter):
            return False, None
        else:
            target_word_count = lower_target_word.count(lower_input_letter)
            guessed_word_count = lower_guessed_word.count(lower_input_letter)
            if target_word_count <= guessed_word_count:
                return False, None
            else:
                index = lower_target_word.find(lower_input_letter)
                exact_index = lower_target_word.find(lower_input_letter, index + (guessed_word_count))
                guessed_word = self.__change_index(guessed_word, exact_index, target_word[index])
                return True, guessed_word

    def determine_game_status(self, db: Database):
        if db.guess_remains <= 0:
            return Game_Status.GAME_OVER
        elif db.target_word == db.guessed_word:
            return Game_Status.GAME_WON
        else:
            return Game_Status.CONTINUE

def main():
    eng = Engine()
    
    print(eng.perform_check("Hellow", "H", "H_____"))

main()