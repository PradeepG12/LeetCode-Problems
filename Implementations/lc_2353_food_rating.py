from typing import List
from collections import defaultdict
import heapq

datas = [
    [
        ["kimchi","miso","sushi","moussaka","ramen","bulgogi"],
        ["korean","japanese","japanese","greek","japanese","korean"],
        [9,12,8,15,14,7]
    ],
    ["korean"],
    ["japanese"],
    ["sushi",16],
    ["japanese"],
    ["ramen",1],
    ["japanese"]
]

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = set(foods)
        self.cuisines = cuisines
        self.ratings = ratings
        self.foods_entry = self.arrange_foods(foods, cuisines, ratings)
        self.cuisines_data = self.arrange_cuisines_data(foods, cuisines, ratings)

    def arrange_foods(self, foods, cuisines, ratings):
        food_list = defaultdict(int)
        for idx, food in enumerate(foods):
            food_list[food] = (ratings[idx], cuisines[idx])
        return food_list

    def arrange_cuisines_data(self, foods, cuisines, ratings):
        cuisines_list = defaultdict(list)
        for idx, cuisine in enumerate(cuisines):
            rating = ratings[idx]
            food = foods[idx]
            heapq.heappush(cuisines_list[cuisine], (-rating, food))
        return cuisines_list

    def changeRating(self, food: str, newRating: int) -> None:
        _, cuisine = self.foods_entry[food]
        self.foods_entry[food] = (newRating, cuisine)
        heapq.heappush(self.cuisines_data[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        cuisine_list =  self.cuisines_data[cuisine]
        while cuisine_list:
            d_rating, food = cuisine_list[0]
            o_rating, o_cuisine = self.foods_entry[food]
            if -d_rating == o_rating:
                return food
            else:
                heapq.heappop(cuisine_list)
        return "Suck Your Dik"

data = datas[0]
system = FoodRatings(data[0], data[1], data[2])
d1 = system.foods_entry
d2 = system.cuisines_data
print(d1, "\n", d2)
print(system.highestRated("japanese"))
print(system.changeRating(datas[-2][0], datas[-2][1]))
print(system.highestRated("japanese"))