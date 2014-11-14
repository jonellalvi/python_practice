# Create a function named string_factory that accepts a list of dictionaries and a
# string.
# Return a list of strings made by filling values from the dictionaries into
# the string.


dicts = [
    {'name': 'Michelangelo',
     'food': 'PIZZA'},
    {'name': 'Garfield',
     'food': 'lasanga'},
    {'name': 'Walter',
     'food': 'pancakes'},
    {'name': 'Galactus',
     'food': 'worlds'}
]

string = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(dicts, string):
    string_list = []
	
    for item in dicts:	
		string_list.append(string.format(**item))
	return string_list