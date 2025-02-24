spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    """
    Returns a list of names for each spicy food
    Uses list comprehension to extract and return the name for each dictionary

    """
    return [ food [ "name" ] for food in spicy_foods ]
    pass

def get_spiciest_foods(spicy_foods):
    """
    Returns a list of spicy food with heart_level greater than 5.
    """
    return [ food for food in spicy_foods if food [ "heat_level" ] > 5]
    pass

def print_spicy_foods(spicy_foods):
    """
    Prints each spicy food in the format:
    'Name ( Cuisine ) | Heat Level:  🌶 🌶 🌶...'
    where the number of  🌶 eqauls to the heat level.
    """
    for food in spicy_foods:
        heat_emojis = "🌶" * food[ "heat_level" ]
        print(f"{food [ 'name' ] } ({ food [ 'cuisine' ] }) | Heat Level: {heat_emojis}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    """
    Returns the first spicy food dictionary in spicy_foods that matches the given cuisine.
    If none is found, return None.
    """
    for food in spicy_foods:
        if food [ "cuisine" ] == cuisine:
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    """
    Prints only the spicy foods with a heat_level greater than 5,
    in the same format as print_spicy_foods()
    """
    spiciest = get_spiciest_foods(spicy_foods)
    for food in spiciest:
        heat_emojis = "🌶" * food[ "heat_level" ]
        print( f"{food ['name'] } ({food [ 'cuisine' ] }) | Heat Level: { heat_emojis }" )
    pass

def get_average_heat_level(spicy_foods):
    """
    Return the average heat level ( as an integer ) of all spicy foods.
    If the list is empty, return 0.
    """
    if not spicy_foods:
        return 0
    total_heat = sum ( food [ "heat_level" ] for food in spicy_foods )
    return total_heat // len ( spicy_foods )
    pass

def create_spicy_food(spicy_foods, spicy_food):
    """
    Add the new spicy_food dictionary to the list and return the updated list.
    """
    spicy_foods.append ( spicy_food )
    return spicy_foods
    pass
