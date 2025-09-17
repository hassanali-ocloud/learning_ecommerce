from body_maker import Body_Maker
from engine import Engine, Game_Status
from database import Database

def take_target_word_input():
    target_word = input("Please input the target word of length 6: ")
    if len(target_word) == 6:
        return target_word
    else:
        print("Invalid Input")
        return take_target_word_input()

def take_letter_guess_input():
    guess_letter = input("Please input the guessed letter: ")
    if len(guess_letter) == 1 and guess_letter != " ":
        return guess_letter
    else:
        print("Invalid Input")
        return take_letter_guess_input()

def start_round(db: Database, eng: Engine, body_maker: Body_Maker):
    input_letter = take_letter_guess_input()
    if (len(input_letter) > 1 or len(input_letter) == 0):
        print("Invalid Input")
        start_round(db, eng, body_maker)
    else:
        guess_status, guessed_word = eng.perform_check(db.target_word, input_letter, db.guessed_word)
        if guess_status == False:
            print("Wrong Letter")
            db.update_guess_remains()
            if eng.determine_game_status(db) == Game_Status.GAME_OVER:
                print(db.guessed_word)
                print("Game Over")
                return
            elif eng.determine_game_status(db) == Game_Status.CONTINUE:
                body_maker.display(*eng.determine_body_status(db.guess_remains))
                print(db.guessed_word)
                start_round(db, eng, body_maker)
        else:
            db.update_guessed_word(guessed_word)
            if eng.determine_game_status(db) == Game_Status.GAME_WON:
                body_maker.display(*eng.determine_body_status(db.guess_remains))
                print(db.guessed_word)
                print("Congratulations You Won")
                return
            elif eng.determine_game_status(db) == Game_Status.CONTINUE:
                print("You Guessed Right")
                body_maker.display(*eng.determine_body_status(db.guess_remains))
                print(db.guessed_word)

            start_round(db, eng, body_maker)

def main():
    target_word = take_target_word_input()
    db = Database(target_word)
    eng = Engine()
    body_maker = Body_Maker()
    print("================ Game Started =================")

    body_maker.display(*eng.determine_body_status(db.guess_remains))
    start_round(db, eng, body_maker)

main()