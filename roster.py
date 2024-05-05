import pandas as pd

# Link to roster: https://goheels.com/sports/mens-basketball/roster

# Step 1: Create list of 3 last names and print
roster = ["Bacot", "Davis", "Cadeau"]
# print(f"{roster}")

# Step 2: Print list using a for loop
# for name in roster:
#     print(f"{name}")

# Step 3: Make dataframe and print
# data = pd.DataFrame(roster)
# print(data)

# Step 4: Make last name dataframe
player = {"Last Name": roster}
data = pd.DataFrame(player)
print(data)