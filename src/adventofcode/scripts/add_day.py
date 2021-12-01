import os
import sys
from argparse import ArgumentParser
from typing import List

from requests import HTTPError  # noqa

from adventofcode.config import ROOT_DIR
from adventofcode.scripts.get_inputs import get_input
from adventofcode.util.console import console
from adventofcode.util.input_helpers import get_input_for_day


def add_day():
    year, day = _parse_args(sys.argv[1:])

    module_path = os.path.join(ROOT_DIR, f"year_{year}")
    full_path = os.path.join(module_path, f"day_{day:02}_{year}.py")
    create_dir(module_path)
    if not day_exists(year, day):
        console.print(f"Creating solution day file for year {year} day {day}")
        write_template(full_path, read_template(year, day))
        console.print(f"Wrote template to {full_path}")
    verify_test_exists(year, day)
    verify_input_exists(year, day)


def create_dir(path: str) -> None:
    if not os.path.exists(path):
        os.mkdir(path)


def day_exists(year: int, day: int) -> bool:
    module_path = os.path.join(ROOT_DIR, f"year_{year}")
    filename = os.path.join(module_path, f"day_{day:02}_{year}.py")
    exists = os.path.isfile(filename)
    if exists:
        console.print(
            f"Code file already exists for year {year} day {day}, skipping creation"
        )
    return exists


def verify_test_exists(year: int, day: int) -> None:
    module_path = os.path.join(ROOT_DIR, "..", "..", "tests", f"year_{year}")
    filename = os.path.join(module_path, f"test_day_{day:02}_{year}.py")
    if os.path.isfile(filename):
        console.print(
            f"Test file already exists for year {year} day {day}, skipping creation"
        )
        return
    write_template(filename, read_template(year, day, True))
    console.print(f"Wrote test template to {filename}")


def verify_input_exists(year: int, day: int) -> None:
    try:
        _ = get_input_for_day(year, day)
        console.print(
            f"Input data already exists for year {year} day {day}, skipping download"
        )
        return
    except FileNotFoundError:
        try:
            get_input(year, day)
            console.print(
                f"Automatically downloaded input data for year {year} day {day}"
            )
            return
        except HTTPError as e:
            console.print(
                f"[red]Could not retrieve input data for year {year} day {day} automatically: {e}"
            )
        except FileNotFoundError:
            console.print(
                f"[red]Could not retrieve input data for year {year} day {day}: .session not set correctly"
            )

    raise ValueError("unknown exception occurred in verify_input_exists")


def read_template(year: int, day: int, test: bool = False) -> str:
    if test:
        template_path = os.path.join(ROOT_DIR, "scripts/templates/test_template.txt")
    else:
        template_path = os.path.join(ROOT_DIR, "scripts/templates/day_template.txt")

    with open(template_path) as f:
        template = f.read()

    template = template.replace("{year}", str(year))
    template = template.replace("{day}", str(day))
    template = template.replace("{day:02}", f"{day:02}")

    return template


def write_template(filename: str, template: str):
    with open(filename, "w") as f:
        f.write(template)


def _parse_args(args: List[str]) -> tuple[int, int]:
    parser = ArgumentParser(description="Add a day")
    parser.add_argument("year", type=int, help="The year of the exercise")
    parser.add_argument("day", type=int, help="The day of the exercise")
    parsed = parser.parse_args(args)
    return parsed.year, parsed.day


if __name__ == "__main__":
    add_day()
