class Body_Maker():
    def __init__(self):
        pass

    def __get_indent_str(self, indent:int):
        str = ""
        for x in range(indent):
            str += " "
        return str

    def __make_head(self):
        indent = 20
        print(self.__get_indent_str(indent) + "  ___")
        print(self.__get_indent_str(indent) + " /   \\")
        print(self.__get_indent_str(indent) + "|     |")
        print(self.__get_indent_str(indent) + " \\___/")

    def __make_chest(self, left_arm, right_arm):
        if left_arm and right_arm:
            indent = 17
            print(self.__get_indent_str(indent) + "   /-----\\")
            print(self.__get_indent_str(indent) + "  / ||||| \\")
            print(self.__get_indent_str(indent) + " /  |||||  \\")
            print(self.__get_indent_str(indent) + "/   -----   \\")
        elif left_arm:
            indent = 17
            print(self.__get_indent_str(indent) + "   /-----")
            print(self.__get_indent_str(indent) + "  / |||||")
            print(self.__get_indent_str(indent) + " /  |||||")
            print(self.__get_indent_str(indent) + "/   -----")
        elif right_arm:
            indent = 17
            print(self.__get_indent_str(indent) + "    -----\\")
            print(self.__get_indent_str(indent) + "    ||||| \\")
            print(self.__get_indent_str(indent) + "    |||||  \\")
            print(self.__get_indent_str(indent) + "    -----   \\")
        else:
            indent = 17
            print(self.__get_indent_str(indent) + "    -----")
            print(self.__get_indent_str(indent) + "    ||||| ")
            print(self.__get_indent_str(indent) + "    |||||   ")
            print(self.__get_indent_str(indent) + "    -----    ")

    def __make_legs(self, left_leg, right_leg):
        if left_leg and right_leg:
            indent = 17
            print(self.__get_indent_str(indent) + "    || ||")
            print(self.__get_indent_str(indent) + "    || ||")
            print(self.__get_indent_str(indent) + "    || ||")
            print(self.__get_indent_str(indent) + "    || ||")
        elif left_leg:
            indent = 17
            print(self.__get_indent_str(indent) + "    || ")
            print(self.__get_indent_str(indent) + "    || ")
            print(self.__get_indent_str(indent) + "    || ")
            print(self.__get_indent_str(indent) + "    || ")
        elif right_leg:
            indent = 17
            print(self.__get_indent_str(indent) + "       ||")
            print(self.__get_indent_str(indent) + "       ||")
            print(self.__get_indent_str(indent) + "       ||")
            print(self.__get_indent_str(indent) + "       ||")
    
    def display(self, head, chest, left_arm, right_arm, left_leg, right_leg):
        if head:
            self.__make_head()
        if chest:
            self.__make_chest(left_arm, right_arm)
        if left_leg or right_leg:
            self.__make_legs(left_leg, right_leg)