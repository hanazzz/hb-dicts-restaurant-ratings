"""Restaurant rating lister."""

# Step 1 - Read file & save to variable
# Step 2 - Create empty dictionary to store ratings (variable)
# Step 3 - Sort file into useable format & alphabetize
         # Iterate thru file, line by line & split line into
         # Restaurant name & rating (key:value)
         # Add (key:value) pairs into dictionary
# Step 4 - Alphabetize dict & print
# Step 5 - Ask user for input to add additional entries into dict
# Step 6 - Repeat Step 4
# put your code here

scores_file = open("scores.txt")
restaurant_ratings = {}
for line in scores_file:
    line = line.rstrip()
    restaurant_data = line.split(":")
    restaurant_name = restaurant_data[0]
    restaurant_rating = restaurant_data[1]
# in this dict restaurant_ratings the key restaurant_name 
# has a value restaurant_rating
# this key doesn't exist in the dict, so make it for us
    restaurant_ratings[restaurant_name] = restaurant_rating

restaurant_ratings_items = restaurant_ratings.items()
restaurant_ratings_items = sorted(restaurant_ratings_items)
for restaurant_ratings_item in restaurant_ratings_items:
    print(f"{restaurant_ratings_item[0]} is rated at {restaurant_ratings_item[1]}")
    # print(f"{restaurant_ratings_items[0][0]} is rated at {restaurant_ratings_items[0][1]}")

