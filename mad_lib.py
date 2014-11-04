
#Setup:

prompt = ":::--->"

# Welcome statement
print("Welcome to Mad Libs")

# Ask for user's name
print("What is your name?")
name = raw_input(prompt)

# Instructions:

print("Hello {}! Please enter the following: ").format(name)

# Get the stuff:
verb = raw_input("Enter a verb: ")
noun = raw_input("Enter a noun: ")
adjective = raw_input("Enter an adjective: ")
adverb = raw_input("Enter an adverb: ")
funny_name = raw_input("Enter a funny name: ")

# print(verb, noun, adjective, adverb, funny_name)
# Tell the story:

print("""
Once upon a time, there was a {} {} named {}.
One day, {} {} {}.
The end.
""").format(adjective, noun, funny_name, funny_name, adverb, verb)


