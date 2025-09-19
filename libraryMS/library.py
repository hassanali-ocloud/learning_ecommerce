from database import Database
from data import Keys
from typing import Tuple

class Library():
    def __init__(self):
        self.db = Database()

    def add_new_book(self, title: str, author: str, content: str) -> Tuple[bool, bool]:
        data = {
            Keys.TITLE: title,
            Keys.AUTHOR: author,
            Keys.CONTENT: content,
            Keys.AVAILABLE: False
        }
        success, exception = self.db.create(data)
        return success, exception
    
    def read_book(self, title: str) -> Tuple[bool, bool, object]:
        success, content, exception = self.db.read(title)
        return success, content, exception
    
    def delete_book(self, title: str) -> Tuple[bool, bool]:
        success, exception= self.db.delete(title)
        return success, exception

    def edit_book(self, title, new_title: str = None, author: str = None, content: str = None) -> Tuple[bool, bool, object]:
        data = {
            Keys.TITLE: new_title,
            Keys.AUTHOR: author,
            Keys.CONTENT: content
        }
        success, exception = self.db.update(title, data)
        return success, exception

    def show_books(self) -> None:
        pass

    def borrow_book(self, title: str) -> None:
        pass

    def return_book(self, title: str) -> None:
        pass

# async def main():
#     lb = Library()
#     await lb.add_new_book("A", "B", "C")
#     # await lb.read_book("A")

# asyncio.run(main())