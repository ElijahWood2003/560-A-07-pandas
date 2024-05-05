import pandas as pd

# Link to roster: https://goheels.com/sports/mens-basketball/roster

# Step 1: Create list of 3 last names and print
# roster = ["Bacot", "Davis", "Cadeau"]
# print(f"{roster}")

# Step 2: Print list using a for loop
# for name in roster:
#     print(f"{name}")

# Step 3: Make dataframe and print
# data = pd.DataFrame(roster)
# print(data)

# Step 4: Make last name dataframe
# player = {"Last Name": roster}
# data = pd.DataFrame(player)
# print(data)

# Step 5: 10 athletes in the dataframe
player = {"Last Name": ["Bacot", "Davis", "Cadeau", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Landry"],
            "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Rob"],
            "height": [83, 72, 73, 80, 74, 75, 78, 74, 72, 70],
            "weight": [240, 180, 180, 200, 210, 185, 184, 205, 190, 215]
            }
data = pd.DataFrame(player)

data["bmi"] = ((data["weight"]/2.025) / ((data["height"]/39.37)**2)).round(2)

print(data)

data.to_csv("bmi.csv")