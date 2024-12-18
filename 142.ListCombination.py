# The extend method
# Extends the existing list
visited_cities = ['New York', 'Paris', 'London']
wish_cities  = ['Tokyo', 'Sydney', 'Rio de Janeiro']

visited_cities.extend(wish_cities)
print(visited_cities)

# List concatenation
# create a new list by combining one or more lists
visited_cities = ['New York', 'Paris', 'London']
wish_cities  = ['Tokyo', 'Sydney', 'Rio de Janeiro']

all_cities = visited_cities + wish_cities
for city in all_cities:
    print(city)
