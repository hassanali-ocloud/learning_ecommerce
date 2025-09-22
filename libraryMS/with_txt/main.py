from library import Library
import asyncio
from data import Keys
import os

def check_validation(input: str):
    try:
        int(input)
        return True
    except Exception as e:
        return False
    
def edit_sub_menu(library: Library, title: str):
    edit_guide = """
        1: Title
        2: Author
        3: Content
        4: Go Back"""
    print(edit_guide)
    num_input_str = input("Enter You Choice: ")

    if check_validation(num_input_str):
        num_input = int(num_input_str)
        if num_input == 1:
            new_title = input("Enter new title of the book: ")
            success, exception = library.edit_book(title=title, new_title=new_title.lower())
            if success:
                print("Successfully updated title")
            else:
                print(f"Exception: {exception}")
        elif num_input == 2:
            new_author = input("Enter new author of the book: ")
            success, exception = library.edit_book(title=title, author=new_author.lower())
            if success:
                print("Successfully updated author")
            else:
                print(f"Exception: {exception}")
        elif num_input == 3:
            new_content = input("Enter new content of the book: ")
            success, exception = library.edit_book(title=title, content=new_content.lower())
            if success:
                print("Successfully updated content")
            else:
                print(f"Exception: {exception}")
        elif num_input == 4:
            return
        else:
            print("Invalid Input")
            edit_sub_menu(library, title)
    else:
        print("Invalid Input")
        edit_sub_menu(library, title)

def main():
    library = Library()

    print("""***** WELCOME TO LIBRARY MANAGEMENT SYSTEM *****""")

    guide = """
        1: Add
        2: Read
        3: Delete
        4: Edit
        5: Show Titles
        6: Borrow
        7: Return
        8: Print Guide
        9: Quit"""

    while True:
        print(guide)
        isValidInput = False
        while not isValidInput:
            try:
                inp = int(input("\nEnter your choice: "))
                isValidInput = True
            except Exception as e:
                print("Invalid Input..")

        match inp:
            case 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                content = input("Enter book content: ")
                success, exception = library.add_new_book(title.strip(), author.strip(), content.strip())
                if success:
                    print("Successfully Added")
                else:
                    print(f"Exception: {exception}")
            case 2:
                title = input("Enter title of the book you want to read: ")
                success, data, exception = library.read_book(title.lower())
                if success:
                    print(f"Book Title: {data[Keys.TITLE]}")
                    print(f"Book Author: {data[Keys.AUTHOR]}")
                    print(f"Book Content: {data[Keys.CONTENT]}")
                    print(f"Available to Borrow: {data[Keys.AVAILABLE]}")
                    if data[Keys.AVAILABLE] == False:
                        print(f"Borrower Name: {data[Keys.BORROWER]}")
                else:
                    print(f"Exception: {exception}")
            case 3:
                title = input("Enter title of the book you want to delete: ")
                success, exception = library.delete_book(title.lower())
                if success:
                    print(f"Successfully Deleted")
                else:
                    print(f"Exception: {exception}")
            case 4:
                title = input("Enter title of the book you want to edit: ")
                edit_sub_menu(library, title)
            case 5:
                success, data, exception = library.show_books()
                if success:
                    for x in data:
                        print(f"Title: {x}")
                else:
                    print(f"Exception: {exception}")
            case 6:
                title = input("Enter title of the book you want to borrow: ")
                borrower = input("Enter your name: ")
                success, exception = library.borrow_book(title.lower(), borrower)
                if success:
                    print(f"Successfully Borrowed")
                else:
                    print(f"Exception: {exception}")
            case 7:
                title = input("Enter title of the book you want to return: ")
                success, exception = library.return_book(title.lower())
                if success:
                    print(f"Book Successfully Returned")
                else:
                    print(f"Eexception: {exception}")
            case 8:
                print(guide)
            case 9:
                print("Thank you..\n")
                break
            case _:
                print("Invalid input..")

if __name__ == "__main__":
    main() 
    