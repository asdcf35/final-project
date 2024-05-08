from math import *
import os
import subprocess
from rich.console import Console

ask = input("Global 3.10?*(y/n)")
if ask == "y":
    subprocess.run(
        [
            "C:\\'Program Files'\\Python310\\python.exe",
            "-m",
            "pip",
            "install",
            "pandas",
            "colorama",
        ]
    )

import pandas as pd


# rides
class Ride:
    def __init__(self, name, age_range, desc, working) -> None:
        self.name = name
        self.age_range = age_range
        self.desc = desc
        self.working = working

    def check_age(self, age) -> bool:
        return self.age_range[0] < age < self.age_range[1]

    def working(self) -> None:
        self.working = not self.working


def rides_from_file(filename="rides.csv") -> dict[str, Ride]:
    """
    Making Ride objects from a file

    Parameters
    ---
    filename : str, path object or file-like object
        the filename or object that you wish to use(must work with read_csv)
    """
    dataframe = pd.read_csv(filename)
    dataframe.loc[:, "Max"] = dataframe.loc[:, "Max"].fillna(999999999)
    dataframe.loc[:, "Min"] = dataframe.loc[:, "Min"].fillna(0)
    dataframe = dataframe.to_dict("records")
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(
            dictionary["Name"],
            (dictionary["Min"], dictionary["Max"]),
            dictionary["Description"],
            dictionary["Working"],
        )
    return rides


class Food_Item:
    def __init__(self, name, cost, amount_left) -> None:
        self.name = name
        self.cost = cost
        self.amount_left = amount_left


class Restaurant:

    def __init__(self, name, open, filename) -> None:
        self.name = name
        self.open = open
        dataframe = pd.read_csv(filename)
        self.item_names = tuple(dataframe.loc[:, "Items"])
        print(dataframe)
        self.items = [
            Food_Item(
                self.item_names[i],
                dataframe.loc[i, "Price"],
                dataframe.loc[i, "Amount Left"],
            ) for i in range(len(self.item_names))
        ]

    def display_foods(self, console: Console, discount=0) -> None:
        console.print(f"Welcome to {self.name}\n\n", justify="center")
        console.print(f"Menu", justify="center")
        console.print(f'{"":-^24}', justify='center')
        for food_item in self.items:
            print(f"{food_item.name} {" - ":^9} {food_item.cost}")


if __name__ == '__main__':
    Restaurant('Chicken Tenders', True, 'menu.csv').display_foods(Console())
