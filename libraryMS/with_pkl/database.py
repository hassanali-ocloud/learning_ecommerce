import pickle
from data import Keys
from typing import Tuple, Optional
import os
from pathlib import Path

class Database():
    def create(self, data) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{data[Keys.TITLE]}.pkl"
            with open(file_name, "wb") as file:
                pickle.dump(data, file)
            return True, None
        except Exception as e:
            return False, e

    def read(self, title) -> Tuple[bool, object, Optional[Exception]]:
        try:
            file_name = f"{title}.pkl"
            with open(file_name, "rb") as file:
                content = pickle.load(file)
            return True, content, None
        except Exception as e:
            return False, None, e

    def update(self, title, data) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{title}.pkl"
            with open(file_name, "rb") as file:
                content = pickle.load(file)
                if data.get(Keys.TITLE) != None:
                    content[Keys.TITLE] = data[Keys.TITLE]     
                if data.get(Keys.AUTHOR) != None:
                    content[Keys.AUTHOR] = data[Keys.AUTHOR]
                if data.get(Keys.CONTENT) != None:
                    content[Keys.CONTENT] = data[Keys.CONTENT]
                if data.get(Keys.BORROWER) != None:
                    content[Keys.BORROWER] = data[Keys.BORROWER]
                if data.get(Keys.AVAILABLE) != None:
                    content[Keys.AVAILABLE] = data[Keys.AVAILABLE]

            try:
                with open(file_name, "wb") as file:
                    pickle.dump(content, file)

                if data.get(Keys.TITLE) != None:
                    new_file_name = f"{data[Keys.TITLE]}.pkl"
                    os.rename(file_name, new_file_name)
                return True, None
            except Exception as e:
                return False, e

        except Exception as e:
            return False, e

    def delete(self, title) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{title}.pkl"
            if os.path.exists(file_name):
                os.remove(file_name)
                return True, None
            else:
                return False, Exception("File Path Does Not Exist")
        except Exception as e:
            return False, e
        
    def peek(self) -> Tuple[bool, object, Optional[Exception]]:
        try:
            path = Path(".")
            files = sorted(path.glob("*.pkl"))
            if len(files) > 0:
                return True, files, None
            else:
                return False, None, Exception("Currently No Titles in the directory")
        except Exception as e:
            return False, None, e