"""
Minimal example, it can be run directly, but better rewrite the marked sections to the correct files.
Story: https://github.com/BoyNamedHsu/dbd-workshop/blob/main/Scripts/README.md
"""
import random
import sqlite3
from enum import Enum
from typing import NamedTuple

import db_utils

###
# Rewrite to config.py file
###
CASE_DB_NAME = "case_db.sqlite3"
CASE_CULPRIT = "Forest Everest" # Play on words "forever resting"

class GuestListRow(NamedTuple):
    # Schema definition, for the minimal example 1 table holds all of the data.
    # Usually, the data should be split up to make the player look for.
    # All types here should be simple like below:
    name: str
    """Full name of guest"""
    age: int
    """Age of guest in years"""
    title: str
    """Work title of the employee"""
    superior: str | None # CEO doesn't have superior, the value can be None / NULL
    """Manager of the employee"""
    is_manager: bool
    """Is the guest a manager"""
    alcohol: float
    """Amount of alcohol the guest has drunk in cups"""

GUEST_LIST = db_utils.Table[GuestListRow](
    name="guest_list",
    schema=GuestListRow
)

class WorkTitles(Enum):
    CEO = "Founder & CEO"
    MINIMUM_WAGE = "MW Data Expert"
    COMPETENT_SOLVER = "Competent Problem Solver"
    CREATIVE_INNOVATOR = "Creative Innovator"

MIN_AGE: int = 29 # The company doesn't hire freshers from college
MAX_AGE: int = 60 # The company fires workers before retirement
WORK_TITLES: tuple[WorkTitles, ...] = tuple(set(WorkTitles) - { WorkTitles.CEO }) # Create a static list of all WorkTitles except for CEO
REPORTER_NAME: str = "Karen Cox" # Name of the Reporter
CEO_NAME: str = "Zoran PonziScam" # Name of the CEO
REPORTER_AGE: int = random.randint(MIN_AGE + 10, MIN_AGE + 15) # Reporter should be young but not too young
CEO_AGE: int = random.randint(MAX_AGE + 10, MAX_AGE + 20) # Founder, should be the oldest
CULPRIT_AGE: int = random.randint(67, CEO_AGE - 1) # From シックス・セブン to still younger than CEO
MANAGER_COUNT: int = random.randint(5, 10) # Count of Managers other than the Culprit
EMPLOYEE_COUNT: int = random.randint(60, 100) # Count of Employees that are not Managers
MIN_DRUNK: float = 1.1 # Minimal amount drank
MAX_DRUNK: float = 4.9 # Maximal amount drank

###
# Rewrite to halloween.py / your_case.py file
###

random.seed(0) # Static seed to generate same values every time

# Create CEO, he's a manager to other managers
ceo = GuestListRow(
    name=CEO_NAME,
    age=CEO_AGE,
    alcohol=round(random.uniform(MAX_DRUNK + 1, MAX_DRUNK + 2), 1),
    is_manager=True,
    superior="",
    title=WorkTitles.CEO.value
)

# Define the Culprit, he's a manager
culprit = GuestListRow(
    name=CASE_CULPRIT,
    age=CULPRIT_AGE,
    alcohol=round(random.random(), 1),
    is_manager=True,
    superior=ceo.name,
    title=WorkTitles.COMPETENT_SOLVER.value
)

# Define the Reporter, her superior is the Culprit
reporter = GuestListRow(
    name=REPORTER_NAME,
    age=REPORTER_AGE,
    alcohol=round(random.random(), 1),
    is_manager=False,
    superior=culprit.name,
    title=WorkTitles.CREATIVE_INNOVATOR.value
)

GUEST_LIST.insert(ceo, culprit, reporter) # Add CEO, Culprit and Reporter to the list of guests

managers: list[GuestListRow] = [] # List of managers to random pick for employees, CEO is not part of it
managers.append(culprit) # Add Culprit to the list of managers

# Create other managers
for _ in range(MANAGER_COUNT):
    managers.append(
        GuestListRow(
            name=" ".join(db_utils.get_random_name()),
            age=random.randint(MIN_AGE, MAX_AGE),
            alcohol=round(random.uniform(MIN_DRUNK, MAX_DRUNK), 1),
            is_manager=True,
            superior=ceo.name,
            title=random.choice(WORK_TITLES).value
        )
    )
    GUEST_LIST.insert(managers[-1]) # Add latest manager to the list of guests

# Create employees
for _ in range(EMPLOYEE_COUNT):
    GUEST_LIST.insert(
        GuestListRow(
            name=" ".join(db_utils.get_random_name()),
            age=random.randint(MIN_AGE, MAX_AGE),
            alcohol=round(random.uniform(MIN_DRUNK, MAX_DRUNK), 1),
            is_manager=False,
            superior=random.choice(managers).name,
            title=random.choice(WORK_TITLES).value
        )
    )

# Shuffle rows to make them harder to spot simply by looking on the table
# It could also be sorted by age or by other value
# GUEST_LIST.rows.sort(key=lambda row: row.age)
random.shuffle(GUEST_LIST.rows)

with sqlite3.Connection(CASE_DB_NAME) as connection:
    # Init DB connection
    db_utils.CONNECTION = connection
    # Create table with data
    db_utils.create_populate_table(GUEST_LIST)
