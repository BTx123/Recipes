import configparser as cp
import logging
import pathlib as pl
import click
import re
import json


logging.getLogger().setLevel(logging.INFO)

SETTINGS_FILE = "settings.ini"
PARENT_FOLDER = "recipes"
CATEGORIES = "CATEGORIES"

DEFAULT_SETTINGS = {
    CATEGORIES: {
        "appetizers": None,
        "breakfast": None,
        "entrees": None,
        "desserts": None,
        "drinks": None,
        "other": None
    }
}

TEMPLATE = \
    """---
path: /recipes
category: {category}
servings: {servings}
active: {active}
total: {total}
rating: {rating}
url: {url}
tags: {tags}
---

# {title}

## Tools

*
*
*

## Ingredients

*
*
*

## Steps

1.
1.
1.
"""


def read_settings_with_default(file=SETTINGS_FILE):
    config = cp.ConfigParser(
        allow_no_value=True
    )

    found = config.read(file)

    if not found:
        logging.warning(
            f"Settings file '{file}' not found. Falling back to default settings.")
        config.read_dict(DEFAULT_SETTINGS)
        with open(file, 'w') as f:
            logging.info(
                f"Writing settings file '{file}'."
            )
            config.write(f)

    return config


CONFIG = read_settings_with_default()


class UrlParamType(click.ParamType):
    name = "url"

    def convert(self, value, param, ctx):
        pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
        match = re.fullmatch(pattern, value)

        if match is None:
            self.fail(
                "expected URL with HTTP protocol, got "
                f"{value}"
            )


URL = UrlParamType()


@click.command()
@click.argument("title")
@click.argument("category", type=click.Choice(CONFIG[CATEGORIES].keys()))
@click.option("--servings", "-s", type=click.IntRange(min=1), default=1, help="Number of servings.")
@click.option("--active", type=click.IntRange(min=0), help="Active cooking time.")
@click.option("--total", "-t", type=click.IntRange(min=0), help="Total cooking time.")
@click.option("--rating", "-r", type=click.FloatRange(min=0, max=5), help="Rating for recipe.")
@click.option("--url", "-u", type=URL, help="URL recipe was originally found at or based upon.")
@click.option("--tags", "-k", type=click.STRING, multiple=True, help="Keywords associated with the recipe.")
def main(title, category, servings, active, total, rating, url, tags):
    # Retrieve local variables
    kwargs = locals()
    # Modify arguments before writing to template
    kwargs = {k: "" if v is None else v for k, v in kwargs.items()}
    kwargs["title"] = title.title()
    kwargs["tags"] = json.dumps(tags)

    try:
        # Create template in category directory
        path = pl.Path(PARENT_FOLDER) / category
        path.mkdir(parents=True, exist_ok=True)
        path /= f"{'-'.join(title.lower().split())}.md"
        if path.exists():
            print(f"File {path} already exists!")
            exit()
        logging.info(f"Creating file {path}...")
        template = TEMPLATE.format(**kwargs)
        logging.info(f"Writing template to {path}...")
        path.touch(exist_ok=False)
        path.write_text(template)
        logging.info("Done!")
    except FileExistsError as error:
        # Fails if file (recipe) already exists
        logging.error(error)
    # TODO: Anything else to catch?


if __name__ == "__main__":
    main()
