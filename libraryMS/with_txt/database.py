import pickle
from data import Keys
from typing import Tuple, Optional
import os
from pathlib import Path

class Database():
    def __read_file(self, file_name):
        content = {}
        with open(file_name, "rb") as file:
            lines = file.readlines()
            content[Keys.TITLE] = lines[0].decode().replace("\n", "")
            content[Keys.AUTHOR] = lines[1].decode().replace("\n", "")
            content[Keys.CONTENT] = lines[2].decode().replace("\n", "")
            content[Keys.AVAILABLE] = lines[3].decode().replace("\n", "").lower() in [
                'true'
            ]
            content[Keys.BORROWER] = lines[4].decode().replace("\n", "") if len(lines) > 4 else None
        return content
    
    def __write_file(self, file_name, data):
        with open(file_name, "wb") as file:
            content = (f"{data[Keys.TITLE]}\n{data[Keys.AUTHOR]}\n{data[Keys.CONTENT]}\n{data[Keys.AVAILABLE]}\n{data.get(Keys.BORROWER)}")
            file.write(content.encode())

    def create(self, data) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{data[Keys.TITLE]}.txt"
            self.__write_file(file_name, data)
            return True, None
        except Exception as e:
            return False, e

    def read(self, title) -> Tuple[bool, object, Optional[Exception]]:
        try:
            file_name = f"{title}.txt"
            content = self.__read_file(file_name)
            return True, content, None
        except Exception as e:
            return False, None, e

    def update(self, title, data) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{title}.txt"
            with open(file_name, "rb") as file:
                content = self.__read_file(file_name)
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
                self.__write_file(file_name, content)

                if data.get(Keys.TITLE) != None:
                    new_file_name = f"{data[Keys.TITLE]}.txt"
                    os.rename(file_name, new_file_name)
                return True, None
            except Exception as e:
                return False, e

        except Exception as e:
            return False, e

    def delete(self, title) -> Tuple[bool, Optional[Exception]]:
        try:
            file_name = f"{title}.txt"
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
            files = sorted(path.glob("*.txt"))
            if len(files) > 0:
                return True, files, None
            else:
                return False, None, Exception("Currently No Titles in the directory")
        except Exception as e:
            return False, None, e