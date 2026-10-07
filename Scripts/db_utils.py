"""
Utility functions for basic SQL commands.
"""
import random
import sqlite3
from dataclasses import dataclass
from enum import Enum
from functools import cache
from pathlib import Path
from typing import Generic, NamedTuple, TypeVar

__all__ = [
    "Table",
    "create_populate_table",
    "get_random_name",
]

R = TypeVar("R") # Generic type representing Table Row

CONNECTION: sqlite3.Connection | None = None
"""Initialized inside halloween.py"""

# Let's limit the DB to these types to not test the parser too much
PY_TO_DB_MAP: dict[type, str] = {
    str: "TEXT",
    int: "INTEGER",
    float: "REAL",
    bool: "BOOLEAN",
}

@dataclass(frozen=True)
class Column:
    name: str
    db_type: str

class Table(Generic[R]):
    def __init__(self, name: str, schema: type[NamedTuple]) -> None:
        super().__init__()
        self.name: str = name
        self.schema: type[NamedTuple] = schema
        self._rows: list[R] = []

    @property
    def columns(self):
        return tuple(
            Column(name=name, db_type=self._py_to_db(py_type)) # pyright: ignore[reportAny]
            for name, py_type in   # pyright: ignore[reportAny]
            self.schema.__annotations__.items()
        )

    @property
    def rows(self) -> list[R]:
        return self._rows

    def insert(self, *rows: R) -> None:
        self._rows.extend(rows)

    def _py_to_db(self, py_type: type) -> str:
        for key, value in PY_TO_DB_MAP.items():
            if key.__name__ in str(py_type): # "str" in "str | None"
                return value
        return PY_TO_DB_MAP[py_type]

def get_random_name() -> tuple[str, str]:
    """
    Gets a random name from the text files in the Names directory.
    """
    male_first_names = _read_name_list("male-first-names.txt")
    female_first_names = _read_name_list("female-first-names.txt")
    last_names = _read_name_list("last-names.txt")

    first_names = male_first_names + female_first_names
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    return first_name.title(), last_name.title()

@cache
def _read_name_list(filename: str) -> list[str]:
    """
    Gets the name files. Assumes these files are in a folder called Names in the same directory as script.
    """
    path = Path(__file__).resolve().parent / "Names" / filename
    with path.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]

def create_populate_table(table: Table[R]) -> None:
    """
    Creates and populates a table with the given rows.
    """

    if CONNECTION is None:
        raise sqlite3.ProgrammingError("Connection was not initialized")

    _create_table(CONNECTION, table)
    _populate_table(CONNECTION, table)

def _create_table(connection: sqlite3.Connection, table: Table[R]) -> None:
    """
    Creates a table.
    """
    columns = ", ".join(f"{c.name} {c.db_type}" for c in table.columns)
    cursor = (connection.cursor()
        .execute(f"DROP TABLE IF EXISTS {table.name}")
        .execute(f"CREATE TABLE IF NOT EXISTS {table.name} ({columns})")
    )
    connection.commit()
    cursor.close()

def _populate_table(
    connection: sqlite3.Connection,
    table: Table[R]
) -> None:
    """
    Populates a table with the given rows.
    """
    columns = tuple(c.name for c in table.columns)
    sql_columns = ", ".join(columns)
    placeholders = ", ".join("?" for _ in columns)
    query = f"INSERT INTO {table.name} ({sql_columns}) VALUES ({placeholders})"

    values = tuple(tuple(map(_convert_value, (getattr(row, column) for column in columns))) for row in table.rows)
    cursor = connection.executemany(query, values)
    connection.commit()
    cursor.close()

def _convert_value(value: str | bool | None | float):
    """
    Helper function for DB value assignment
    """
    if isinstance(value, bool):
        return int(value)

    if isinstance(value, str) and value == "":
        return None

    if isinstance(value, Enum):
        return value.value  # pyright: ignore[reportAny]

    return value
