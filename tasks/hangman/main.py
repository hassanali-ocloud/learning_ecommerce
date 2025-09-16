from body_maker import Body_Maker
from engine import Engine
from database import Database

def take_target_word_input():
    target_word = input("Please input the target word of length 6: ")
    if len(target_word) == 6:
        return target_word
    else:
        print("Invalid Input")
        return take_target_word_input()

def take_letter_guess_input():
    guess_letter = input("Please input the guessed letter")
    if len(guess_letter) == 1 and guess_letter != " ":
        return guess_letter
    else:
        print("Invalid Input")
        return take_letter_guess_input()

def start_game(db: Database, eng: Engine, body_maker: Body_Maker):
    guess_letter = take_letter_guess_input()
    


def main():
    target_word = take_target_word_input()
    db = Database(target_word)
    eng = Engine()
    body_maker = Body_Maker()
    print("================ Game Started =================")
    body_maker.display(eng.determine_body_status(db.guess_remains))
    start_game()

main()