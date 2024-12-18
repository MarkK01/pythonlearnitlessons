# Appending to a list

#  .append() method adds an item to the end of a list
sample_list = [1, 2, 3]
print(sample_list)
sample_list.append(4)
print(sample_list)

party_list = ["Helen", "Vitalii", "Tobias"]
print(party_list)
party_list[1] = party_list[1] + " Shumilo"
print(party_list)

# Insert items into a list
# .insert(<index>,<value>) to define an index where to insert an object
party_list = ["Joana", "Alton", "Tobias"]
print("Before:", party_list)
print("index 1 is", party_list[1])
print("index 2 is", party_list[2])
party_list.insert(1, "Colette")
print("After:", party_list)
print("index 1 is", party_list[1])
print("index 2 is", party_list[2])
# party_list.insert(10, "Mark")
# print("After:", party_list)
# print("index 10 is", party_list[10])  # IndexError: List index out of range

# Iterate through lists
# For In
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "Sao Paulo", "Hyderabad"]
for city in cities:
    print(city)

sales = [6, 8, 9, 11, 12, 17, 19, 20, 22]
total = 0

for sale in sales:
    print(sale)
    total += sale
print("Total sales:", total)

# Sort and Filter
# use comparison operators while iterating lists
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
              "intermediate cuneiform", "medial cuneiform"]

longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += bone_name + "\n"
    else:
        longer_names += bone_name + "\n"

print("SHORT NAMES:\n" + shorter_names)
print("LONG NAMES:\n" + longer_names)

# Iterate lists of strings to find occurances of a character
# .count() - finds character or substring occurences in a string
cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search_letter = "a"
total = 0

for city_name in cities:
    total += city_name.lower().count(search_letter)
    print(total)

print("The total # of \"" + search_letter + "\" found in the list is", total)

#
# city_search function
#
def city_search(search_item, cities = ["New York", "Shanghai", "Munich", "Tokyo"]):
    for city in cities:
        if city.lower() == search_item.lower():
            return True
        else:
            pass

    return False

visited_cities = ["New York", "Shanghai", "Munich", "Tokyo", "Dubai", "Mexico City", "São Paulo", "Hyderabad"]
search = input("enter a city visited: ")
print()

print(search.title(), "in default cities is", city_search(search))  # Send one aruguement - function uses default for second arguement
print(search.title(), "in visited_cities list is", city_search(search, visited_cities))  # Send two arguements

# Quiz

def check_visited(city, visited):
    for city in visited:
        if city == visited:
            return True
        else:
            pass
        
    return False
    
visited_cities = ['New York', 'Paris', 'London', 'Tokyo']
cities_to_check  = ['Paris', 'Sydney', 'London', 'Toronto']


for city in cities_to_check:
    if check_visited(city, visited_cities):
        print(city, 'is already visited')
    else:
        print(city, 'is not yet visited')

def combine_list_extend(list1, list2):
    for item in list2:
        if item in list1:
            print("Item ", item, "exists in list")
        else:
            list1.append(item)
    return list1

fruit_list1 = ['apple', 'banana', 'cherry']
fruit_list2 = ['orange', 'pear', 'kiwi']
fruit_list3 = ['orange', 'pear', 'kiwi']

combine_list_extend(fruit_list1, fruit_list2)
print(fruit_list1)
    
all_fruits = fruit_list2 + fruit_list3
print(all_fruits)             