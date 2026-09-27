"""
Utility functions for basic SQL commands.
"""
import random
import sqlite3
from pathlib import Path
from typing import Iterable, Mapping, Sequence, Tuple
from functools import cache, wraps

@cache
def _read_name_list(filename: str) -> list[str]:
    """
    Gets the name files. Assumes these files are in a
    folder called Names in the same directory as script.
    """
    path = Path(__file__).resolve().parent.joinpath("Names", filename)
    with path.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def _to_name_case(name: str) -> str:
    "Formats names to have the first character in uppercase and remaining characters in lowercase."
    formatted_name = name.strip()
    return formatted_name[0].upper() + formatted_name[1:].lower()

def get_random_name() -> Tuple[str, str]:
    "Gets a random name from the text files in the Names directory."
    male_first_names = _read_name_list("male-first-names.txt")
    female_first_names = _read_name_list("female-first-names.txt")
    last_names = _read_name_list("last-names.txt")

    first_names = male_first_names + female_first_names
    first_name = _to_name_case(random.choice(first_names))
    last_name = _to_name_case(random.choice(last_names))
    return first_name, last_name

def database_connection(database_name: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with sqlite3.connect(database_name) as connection:
                return func(*args, connection=connection, **kwargs)
        return wrapper
    return decorator

def create_populate_table(
    connection: sqlite3.Connection,
    table_name: str,
    columns: Mapping[str, str],
    rows: Iterable[dict]
) -> None:
    "Creates and populates a table with the given rows."
    column_definitions = ", ".join(f"{name} {data_type}" for name, data_type in columns.items())
    _create_table(connection, table_name, column_definitions)
    _populate_table(connection, table_name, list(columns.keys()), rows)

def _create_table(connection: sqlite3.Connection, table_name: str, columns: str) -> None:
    "Creates a table."
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
    connection.execute(query)
    connection.commit()

def _populate_table(
    connection: sqlite3.Connection,
    table_name: str,
    columns: Sequence[str],
    rows: Iterable[dict],
) -> None:
    "Populates a table with the given rows."
    rows = list(rows)
    sql_columns = ", ".join(columns)
    placeholders = ", ".join("?" for _ in columns)
    query = f"INSERT INTO {table_name} ({sql_columns}) VALUES ({placeholders})"

    values = [tuple(row.get(column) for column in columns) for row in rows]
    connection.executemany(query, values)
    connection.commit()

__all__ = [
    "get_random_name",
    "database_connection",
    "create_populate_table"
]
