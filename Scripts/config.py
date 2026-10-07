"""
Config for the case
"""
from enum import Enum
from typing import NamedTuple

import db_utils

###
# Config.json section
# Set values that will go to the config.json
# Except for the "lockedTables" as this is generated based on defined tables below
###

# Required
CASE_NAME = "A Case of Stolen Candy"
"""Name of the case displayed in-game"""
CASE_DB_NAME = "halloween"
"""Name of your database here"""
CASE_CULPRIT = "Candy Georgino"
"""Name of the culprit inside the DB"""
CASE_EVIDENCE = ["crime scene.jpg"]
"""List of image files shown as evidence clues in-game"""

# Optional
CASE_AUTHOR = "Grandma Hsu"
"""Author of the case, reporter name displayed in-game"""
CASE_DIFFICULTY = "Medium"
"""Easy, Medium, Hard used as Tag in Steam Workshop"""
CASE_CONCEPTS = ["GROUP BY"]
"""List of concepts like JOIN, GROUP BY, HAVING et.c, displayed both in-game and used as Tags in Workshop Steam"""
CASE_AUDIO_EVIDENCE = ["message from grandma.mp3"]
"""List of audio evidence files"""
CASE_PREVIEW_IMAGE = "police report 1x1.png"
"""Name of image file shown as Preview in Steam Workshop"""
CASE_CULPRIT_ARREST_IMAGE = "culprit.jpg"
"""Name of image file shown during corret arrest of culprit"""
CASE_ARREST_WARRANT = "warrant.png"
"""Name of image file used for warrant"""
CASE_VOICE_MESSAGE = "message from grandma.mp3"
"""Name of MP3 audio file"""
CASE_VOICE_TRANSCRIPT = "message from grandma transcript.txt"
"""Name of text file with the transcript"""
CASE_QUERY_HINTS = [
    "We should first find the total\namount of items each suspect\nhas taken.",
    "We can find this by applying a\nGROUP BY on the names and items taken\nof each trick-or-treater.",
    "We can use the COUNT function\nto find the number of items\neach trick-or-treater has taken.",
    "We should then find the total\namount of items they can take\nbased on the households they've\nbeen to, and compare the results!",
]
"""List of SQL query hints"""
CASE_STORY_HINTS = [
    "It seems like you can only take\none of each type of item offered\nby each household!"
]
"""List of hints related to the story or case itself"""

###
# Tables section
# Define Row schemas (column names are properties) and Table objects
# Internal Python types like str, int get converted to SQLite format later in Table class
###

class NeighborhoodRow(NamedTuple):
    household: str
    candy_offered: str

NEIGHBORHOOD = db_utils.Table[NeighborhoodRow](
    name="neighborhood",
    schema=NeighborhoodRow
)

class TrickOrTreatersRow(NamedTuple):
    name: str
    household_visited: str

TRICK_OR_TREATERS = db_utils.Table[TrickOrTreatersRow](
    name="trick_or_treaters",
    schema=TrickOrTreatersRow
)

class CandiesTakenRow(NamedTuple):
    name: str
    candy_taken: str

CANDIES_TAKEN = db_utils.Table[CandiesTakenRow](
    name="candies_taken",
    schema=CandiesTakenRow
)

# Trick to gather the lockedTables based on the definitions above
CASE_LOCKED_TABLES: tuple[str, ...] = tuple(obj.name
    for obj in globals().values()  # pyright: ignore[reportAny]
    if isinstance(obj, db_utils.Table)
)

###
# Your case section
# Define helper objects specific to your case
###

# When using Python version >3.10 StrEnum is better as it doesn't require .value
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

HOUSEHOLD_COUNT = 150 # Number of rows in `neighborhood` table
TRICK_OR_TREATER_COUNT = 310 # Number of trick-or-treaters (not counting suspect)
HEALTHY_FOODS = [Candy.CARROTS, Candy.RAISINS] # One of these will differ for the culprit
