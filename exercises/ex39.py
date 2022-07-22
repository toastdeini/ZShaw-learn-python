# Mapping state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Creating a basic set of states and some relevant cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Add some cities!
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities...
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# Now some states...
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Accessing cities from the states dict, then cities
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# Every state's abbreviation!
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# Every city in state...
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# Both at once...
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has abbreviation {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# Safely get an abbreviation by state that might not exist
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# Get a city with a default value
city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")