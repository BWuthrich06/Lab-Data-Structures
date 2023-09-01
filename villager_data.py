"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """
    file = open(filename)
    species = set()

    for line in file:
        items = line.split('|')
      #  for item in items:
        species.add(items[1])

    return species

    # print(all_species("villagers.csv"))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    file = open(filename)
    villagers = []

    for line in file:

        name, species = line.split('|')[:2]        
        if search_string in ("All", species):
            villagers.append(name)

        sorted_villagers = sorted(villagers)

    return sorted_villagers
# print(get_villagers_by_species("villagers.csv", "Bear"))



def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code
    
    fitness = []
    nature = []
    education = []
    music = []
    play = []
    fashion = []
    
    file = open(filename)

    for line in file:
        
        list = line.split("|")
        name = list[0]
        hobby = list[3]
        
        if hobby == "Fitness":
            fitness.append(name)
        elif hobby == "Nature":
            nature.append(name)
        elif hobby == "Education":
            education.append(name)
        elif hobby == "Music":
            music.append(name)
        elif hobby == "Play":
            play.append(name)
        elif hobby == "Fashion":
            fashion.append(name)
       
    return [
        sorted(fitness),
        sorted(nature),
        sorted(education),
        sorted(music),
        sorted(play),
        sorted(fashion)]
        
        

# print(all_names_by_hobby("villagers.csv"))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """
    file = open(filename)
    all_data = []
    
    for line in file:
        
        list = line.split("|")
        all_data.append(tuple(list))
        

    return all_data

# print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code
    file = open(filename)

    for line in file:
        
        list = line.split("|")
        name = list[0]
        motto = list[4]

        if name == villager_name:
            return motto
            
        
        
# print(find_motto("villagers.csv", "Rodeo"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
