import random
from db_utils import create_populate_table, database_connection, get_random_name
from enum import Enum

class Candy(Enum):
    PEANUT_BARS = "Peanut Bars"
    SWEETUMS = "Sweetums"
    BROWNIE_BITS = "Brownie Bits"
    COOKIE = "Cookie Cutters"
    SUGARSLOP = "SugarSlop"
    YUMYUM = "Yum Yum Bars"
    GOOBERS = "GOOBERS"
    CHOCO_BARS = "Choco Bars"
    CARROTS = "Carrots"
    RAISINS = "Raisins"

DATABASE_NAME = "halloween" # Put the name of your database here
CULPRIT_NAME = "Candy Georgino"
HOUSEHOLD_COUNT = 150 # Number of rows in `neighborhood` table
TRICK_OR_TREATER_COUNT = 310 # Number of trick-or-treaters (not counting suspect)
HEALTHY_FOODS = [Candy.CARROTS, Candy.RAISINS]

@database_connection(DATABASE_NAME)
def create_tables(connection: sqlite3.Connection) -> None:
    neighborhood_info, victim_household = generate_neighborhood(connection)
    generate_trick_or_treaters(connection, neighborhood_info, victim_household)

def generate_neighborhood(connection: sqlite3.Connection) -> Tuple[dict, str]:
    """
    Creates the neighborhood table.
    Returns a tuple of...
        1: a map of households to candy limits for the trick-or-treaters tables.
        2: the name/household of the victim
    """
    neighborhood_info = {}
    neighborhood_rows = []
    candies = list(Candy)
    for i in range(HOUSEHOLD_COUNT):
        candies_offered = []
        is_caller = i == 0
        is_like_victim = i > 0 and i < 20 # households that have CARROTS & RAISINS and some other third item
        _, household = get_random_name()
        if is_caller:
            household = "Hsu" # To be consistent with the voice message
        while household in neighborhood_info:
            # Make sure household name is unique.
            _, household = get_random_name()
        if is_caller:
            # Grandma Hsu only gives out raisins
            # The person calling is not the victim
            chosen_candy = Candy.RAISINS
            candies_offered.append(chosen_candy)
            neighborhood_rows.append({
                "household": household,
                "candy_offered": chosen_candy.value
            })
        elif is_like_victim:
            candies_offered = list(HEALTHY_FOODS)
            # Households that are giving away similar candies as the victim (or are the victim)
            # This is to ensure the player has to GROUP BY by candies
            candy_options = [Candy.CHOCO_BARS, Candy.PEANUT_BARS, Candy.COOKIE, Candy.BROWNIE_BITS, Candy.YUMYUM]
            candies_offered.append(random.choice(candy_options))
            for candy in candies_offered:
                neighborhood_rows.append({
                    "household": household,
                    "candy_offered": candy.value
                })
            if i == 1:
                # Honestly it doesn't really matter who the victim is, as long as they have raisins + carrots
                victim_household = household
        else:
            # The amount of candy types the current household is giving
            household_candies = random.randint(1, 3)
            for _ in range(household_candies):
                # Create candy limits for each household 
                candy_options = subtract_list(candies, candies_offered)
                chosen_candy = random.choice(candy_options)
                candies_offered.append(chosen_candy)
                neighborhood_rows.append({
                    "household": household,
                    "candy_offered": chosen_candy.value
                })
        neighborhood_info[household] = candies_offered
    neighborhood_rows.sort(key=lambda row: row["household"])
    create_neighborhood_table(connection, neighborhood_rows) # Create the table here
    return neighborhood_info, victim_household

def create_neighborhood_table(connection: sqlite3.Connection, neighborhood_rows: list) -> None:
    table_name = "neighborhood"
    columns = {
        "household": "TEXT",
        "candy_offered": "TEXT"
    }
    create_populate_table(connection, table_name, columns, neighborhood_rows)

def create_trick_or_treaters_table(connection: sqlite3.Connection, trick_or_treaters_rows: list) -> None:
    table_name = "trick_or_treaters"
    columns = {
        "name": "TEXT",
        "household_visited": "TEXT"
    }
    create_populate_table(connection, table_name, columns, trick_or_treaters_rows)

def create_candies_taken_table(connection: sqlite3.Connection, candies_taken_rows: list) -> None:
    table_name = "candies_taken"
    columns = {
        "name": "TEXT",
        "candy_taken": "TEXT"
    }
    create_populate_table(connection, table_name, columns, candies_taken_rows)

def generate_trick_or_treaters(connection: sqlite3.Connection, neighborhood: dict, victim_household: str) -> None:
    "Creates the tables related to trick-or-treaters (trick_or_treaters and candies_taken)"
    trick_or_treaters_rows = []
    candies_taken_rows = []

    # Adding culprit
    add_visited_household(CULPRIT_NAME, neighborhood, candies_taken_rows, trick_or_treaters_rows)
    culprit_candy = subtract_list(neighborhood[victim_household], HEALTHY_FOODS)[0] # There should only be one element left
    add_victim_visit(victim_household, culprit_candy, candies_taken_rows, trick_or_treaters_rows)

    for _ in range(TRICK_OR_TREATER_COUNT):
        # Create trick-or-treaters
        first_name, last_name = get_random_name()
        add_visited_household(f"{first_name} {last_name}", neighborhood, candies_taken_rows, trick_or_treaters_rows)

    # Sort by name so that the culprit doesn't appear first
    trick_or_treaters_rows.sort(key=lambda row: row["name"])
    candies_taken_rows.sort(key=lambda row: row["name"])

    # Add the trick-or-treater tables to the database
    create_trick_or_treaters_table(connection, trick_or_treaters_rows)
    create_candies_taken_table(connection, candies_taken_rows)

def add_visited_household(name: str, neighborhood: dict, candies_taken_rows: list, trick_or_treaters_rows: list) -> None:
    households_visited = random.sample(list(neighborhood.keys()), random.randint(20, 60))
    for i in range(len(households_visited)):
        # Add the household each trick-or-treater visited to their table.
        household = households_visited[i]
        has_taken = False # household is only considered visited if an item is taken
        for j in range(len(neighborhood[household])):
            # And add each candy they take to the `candies_taken` table.
            candy_taken = neighborhood[household][j]
            if skip_if_healthy(candy_taken):
                continue

            has_taken = True
            candies_taken_rows.append({
                "name": name,
                "candy_taken": candy_taken.value
            })

        if has_taken:
            trick_or_treaters_rows.append({
                "name": name,
                "household_visited": household
            })

def add_victim_visit(victim_household: str, victim_candy: Candy, candies_taken_rows: list, trick_or_treaters_rows: list) -> None:
    print(f"Suspect went to {victim_household} and took an extra {victim_candy}")
    trick_or_treaters_rows.append({
        "name": CULPRIT_NAME,
        "household_visited": victim_household
    })
    for i in range(2):
        candies_taken_rows.append({
            "name": CULPRIT_NAME,
            "candy_taken": victim_candy.value
        })

def skip_if_healthy(item: Candy) -> bool:
    # Most trick-or-treaters will skip healthy items
    skip_rate = 0
    if item == Candy.CARROTS:
        skip_rate = 90
    elif item == Candy.RAISINS:
        skip_rate = 70

    return random.randint(1, 100) <= skip_rate

def subtract_list(list1: list, list2: list) -> list:
    return [x for x in list1 if x not in list2]

def main() -> None:
    create_tables()

if __name__ == "__main__":
    main()