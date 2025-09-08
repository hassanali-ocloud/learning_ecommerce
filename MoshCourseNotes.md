Python Full Course For Beginners:

# a: Strings:

1- Single quotes if want to use double quotes
2- ''' for multiple line strings.
3- Negative in str array starts from last.
4- string[0:3] from index 0 to 3
5- string[:] - copy all
6- string[1:-1] - Start at 1 and stop before the last character
7- len(string) - Get length
8- string.Upper() -> We call it method instead of function. As upper() is specific to strings so we call it a method.
len is function.
9- string.find(): Find the sub string or char
-> string.replace
-> "asf" in string -> returns a bool
-> string.title() -> return capitalization of each word

# b: Arthmetic:

1- 10/3 return floating point
2- 10//3 return integer floor
3- 10\*\*3 return 10 to power of 3
4- Precedence: Parenthesis, Expo, Multi or Div, Add or Sub
5- round(num) -> Round to bigger num
6- abs(num) -> Abs return + num
7- math.ceil and etc for math module. See math module functions
8- and, or are used as it is.

# c: Loops, Arrays, Tuple, Dict:
1- range -> Crate a range or number on which we can iterate.
range(5,10,2)
2- [2:4] -> index 4 is not included.
3- [[1,3], [4,5]] -> 2D List
4- list.insert(0, obj), .remove(5), .clear(), .index(val)
50 in list -> Gives bool
list.count(), list.sort(), list.reverse(), newcopy = list.copy() -> Produce independent list, not rference each other, list.split(' ')
5- Tuple: number = (1, 2, 3)
- Are const so no append etc method
6- x, y, z = coordinates -> open the tuple
7- Dict has unique keys.
cust = {
    "name": "Ali",
    "age": 30
}
8- dict.get(): returns none unlike dict[key here] gives error.
9- dict.get(key, default val) -> if not found key then add this
ali"

# d: Functions, Exception, Comments:
1- keyword arg: greet_user(firsName="syed", lastName="").
Increase readibility.
We can mix positional and keyword arg but keywords arg should be last.
2- try, except, finally
3- Use comments for why or how, not for what

# e: Classes:
1- Even if you not send or define var in class, still via instance of obj you can assign val to variable and it will be created.
- In above case, if access before assiging then error.
2- class Dog(Mammal): pass -> If no body in class then use pass

# f: Module, Packages:
1- import converters
from converters import kg_to_lbs
2- Make package file: make __init__.py
- To import it, import <folderName>.<fileName>
3- See python 3 module index.

# g: Random, Pathlib:
1- random.randint(10,20), random.random()
2- random.choice(list) -> get random entries of a list
3- random.ranint(1,6)
4- pathlib: classes to create object to work with dirs and files.
from pathlib import Path
path = Path("<DirName>") 
path.exists(), .mkdir, .rmdir, .glob("*") -> Go for all files and dir, provide generatorObjs.

# h: PyPI (Python Package Index):
1- openpyxl -> to work with excel sheets.
2- pip is used to install/remove packages on pypi.
3- xl.load_workbook("sheet path")

# i: pep:
1- python enchancment proposal: for best python practices.
2- 

# j: ML:
1. Numpy -> For multi-dimensional array etc
2. Pandas -> Data analysis library -> Read and Work with spreasheet
3. MatPlotLib -> 2 dimensional plotting library
4. Scikit-learn -> Algos for decision trees, NN etc.
5. Kaggle.com -> Data Science data

# k: Jupyter Notebook
1. Shortcuts:
-> See all hotkeys - h
-> See info about fun - Shift + Tab
-> Comment - Ctrl + /
-> Run Cell without creating new cell - Ctrl + Enter

# l: Django:
1. pip install django=2.1
2. djnago-admin startproject pyshop .
3. manage.py -> Manage server, work with database
4. python manage.py runserver -> Run server

5:08