def reverseList(list: list):
    newList = []
    len:int = list.__len__()
    for _ in range(len):
        newList.append(list.pop())
        
    print(f"New List: {newList}")

def nameOfOldest(tupList: list[tuple[str,int]]):
    oldestName: str = ""
    oldestAge: int = 0
    for tup in tupList:
        if (tup[1] > oldestAge):
            oldestAge = tup[1]
            oldestName = tup[0]
    print(f"Oldest Person: {oldestName}")

people = [("Alice", 70), ("Bob", 45), ("Charlie", 25), ("Diana", 50)]
nameOfOldest(people)