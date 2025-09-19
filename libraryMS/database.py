import pickle
from data import Keys
from typing import Tuple
import os

class Database():
    def create(self, data) -> Tuple[bool, Exception]:
        try:
            file_name = f"{data[Keys.TITLE]}.pkl"
            with open(file_name, "wb") as file:
                pickle.dump(data, file)
            return True, None
        except Exception as e:
            return False, e

    def read(self, title) -> Tuple[bool, object, Exception]:
        try:
            file_name = f"{title}.pkl"
            with open(file_name, "rb") as file:
                content = pickle.load(file)
            return True, content, None
        except Exception as e:
            return False, e

    def update(self, title, data) -> Tuple[bool, Exception]:
        try:
            file_name = f"{title}.pkl"
            with open(file_name, "rb") as file:
                content = pickle.load(file)
                if data[Keys.TITLE] != None:
                    content[Keys.TITLE] = data[Keys.TITLE]     
                if data[Keys.AUTHOR] != None:
                    content[Keys.AUTHOR] = data[Keys.AUTHOR]
                if data[Keys.CONTENT] != None:
                    content[Keys.CONTENT] = data[Keys.CONTENT]

            try:
                with open(file_name, "wb") as file:
                    pickle.dump(content, file)

                if data[Keys.TITLE] != None:
                    new_file_name = f"{data[Keys.TITLE]}.pkl"
                    os.rename(file_name, new_file_name)
                return True, None
            except Exception as e:
                return False, e

        except Exception as e:
            return False, e

    def delete(self, title) -> Tuple[bool, Exception]:
        try:
            file_name = f"{title}.pkl"
            if os.path.exists(file_name):
                os.remove(file_name)
                return True, None
            else:
                return False, Exception("File Path Does Not Exist")
        except Exception as e:
            return False, e