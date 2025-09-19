import pandas as pd
import numpy as np

def chaining(animals: pd.DataFrame) -> pd.DataFrame:
    animals = (animals
               .loc[animals["weight"] > 100]
               .sort_values(by="weight", ascending=False)
               .loc[:, ["name"]])
    print(animals)
    return animals


data = {
    "name": ["Tatiana", "Khaled", "Alex", "Jonathan", "Stefan", "Tommy"],
    "species": ["Snake", "Giraffe", "Leopard", "Monkey", "Bear", "Panda"],
    "age": [98, 50, 6, 45, 100, 26],
    "weight": [464, 41, 328, 463, 50, 349]
}

animals = pd.DataFrame(data)
chaining(animals)