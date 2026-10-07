# Database Scripts
You can use any method you want to create your SQLite database file! There are many, many ways to create SQLite database files and most programming languages support this functionality.

To help you start things off, this guide provides a template script in Python.

[_A Case of Stolen Candy_](https://steamcommunity.com/sharedfiles/filedetails/?id=3807683717) was created by running the [`halloween.py`](halloween.py) Python script.

## Technical description

The data for the case generation is set in [`config.py`](config.py). The configuration includes values that will go into `config.json` file, table definitions, helper objects to aid the data generation process.

The data is created in the main [`halloween.py`](halloween.py) file. The neighborhood is generated first, each random household gets a list of candies it offers, and a victim household is selected. Afterwards, random trick-or-treaters go to multiple households at random and take treats, while avoiding healthy foods (also at random). 

<details>
    <summary>Culprit logic</summary>

    The culprit is added just like any other trick-or-treater, but has to be more deliberate than random. The culprit goes to the victim household, and takes one too many of one candy that isn't healthy. This is constrained against the list of possible offered candies in that household.
    
</details>

The database is saved to disk with general ready to use functions inside [`db_utils.py`](db_utils.py).
The `config.json` file is created inside [`generate_config.py`](generate_config.py).

### Alternative minimal case

You can try to implement this simple case as another starting point or practice.

<details open>
    <summary>Beer Party Incident</summary>

    Hello, Detective. I’m Karen Cox from MW Media Group, and I need your help with a matter of **considerable corporate gravity**. Our CEO threw a party for all employees after we hit some mysterious income quota, with one irresistible incentive: **free beer**. The beer was carefully tracked to prevent abuse, but far too many employees showed up, and the evening quickly descended into **unmitigated pandemonium**. Nobody was hurt and nothing was damaged, but the situation was becoming increasingly unruly.
    
    Company policy states that, in such circumstances, the **oldest and most capable problem-solver present** must restore order. Yet nobody stepped forward. Detective, find the person responsible for this **egregious dereliction of duty**, which allowed this utterly **calamitous beer-fuelled debacle** to continue.
  
</details>

If you need more reference this case is implemented in the [`minimal.py`](minimal.py) file.

## Python installation

At the time of writing the guide, the [`uv`](https://docs.astral.sh/uv/) project is slowly becoming the industry standard for managing Python installations. You can read up on the [installation guide](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) there.

Minimal version to run the scripts is Python 3.10 that just turned [EOL](https://devguide.python.org/versions/).

### How to run

To create both the database and `config.json` files using `uv`, simply run this command:

```shell
uv run python ./halloween.py
```

To only create the `config.json`, run this command:

```shell
uv run python ./generate_config.py
```
