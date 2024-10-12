def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet_with("Sai", "Chennai")
# greet_with("Chennai","Sai")

greet_with(location="Chennai", name="Sai")



#Functions with more than one input (eg. Positional Argument)
def greet(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}")
greet("Sushyam Sai","Chennai")


def greet(name, location):
    print(f"Its {name}!")
    print(f'From {location}')
greet(location="Chennai", name="Sushyam Sai") #eg. Keyword Argument
