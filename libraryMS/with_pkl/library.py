from database import Database
from data import Keys
from typing import Tuple, Optional

class Library():
    def __init__(self):
        self.db = Database()

    def add_new_book(self, title: str, author: str, content: str) -> Tuple[bool, bool]:
        data = {
            Keys.TITLE: title,
            Keys.AUTHOR: author,
            Keys.CONTENT: content,
            Keys.AVAILABLE: True
        }
        success, exception = self.db.create(data)
        return success, exception
    
    def read_book(self, title: str) -> Tuple[bool, bool, object]:
        success, content, exception = self.db.read(title)
        return success, content, exception
    
    def delete_book(self, title: str) -> Tuple[bool, bool]:
        success, exception= self.db.delete(title)
        return success, exception

    def edit_book(self, title: str, new_title: Optional[str] = None, author: Optional[str] = None, content: Optional[str] = None) -> Tuple[bool, object]:
        data = {
            Keys.TITLE: new_title,
            Keys.AUTHOR: author,
            Keys.CONTENT: content,
        }
        success, exception = self.db.update(title, data)
        return success, exception

    def show_books(self) -> Tuple[bool, object, Exception]:
        success, data, exception = self.db.peek()
        return success, data, exception
        
    def borrow_book(self, title: str, borrower: str) -> Tuple[bool, object]:
        read_success, read_data, read_exception = self.db.read(title)
        if read_success:        
            data = {
                Keys.BORROWER: borrower,
                Keys.AVAILABLE: False,
            }
            success, exception = self.db.update(title, data)
            return success, exception
        else:
            return read_success, read_exception

    def return_book(self, title: str) -> Tuple[bool, object]:
        data = {
            Keys.BORROWER: None,
            Keys.AVAILABLE: True,
        }
        success, exception = self.db.update(title, data)
        return success, exception

# async def main():
#     lb = Library()
#     await lb.add_new_book("A", "B", "C")
#     # await lb.read_book("A")

# asyncio.run(main())