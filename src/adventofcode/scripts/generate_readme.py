import os
import re
from typing import Dict, List

from adventofcode.config import ROOT_DIR
from adventofcode.util.module_helpers import (
    get_functions_from_day_file,
    get_full_day_paths,
    get_full_year_paths,
    clean_day,
    clean_year,
)

YearDayType = Dict[int, Dict[int, Dict[str, bool]]]


def generate_readme():
    path = os.path.join(ROOT_DIR, "../../README.md")
    readme_file = os.path.abspath(path)

    with open(readme_file) as f:
        current_readme = f.read()

    readme = _replace_between_tags(
        current_readme, _create_completed_text(), "<!-- start completed section -->", "<!-- end completed section -->"
    )

    readme = _update_stars(readme)

    with open(readme_file, "w") as f:
        f.write(readme)


def _replace_between_tags(readme: str, content: str, start: str, end: str) -> str:
    content = "\n".join([start, content, end])

    return re.sub(
        pattern=rf"{start}.*?{end}",
        repl=content,
        string=readme,
        flags=re.DOTALL,
    )


def _update_stars(readme: str) -> str:
    star_count = _count_stars()

    return re.sub(
        pattern=r"&message=\d+",
        repl=f"&message={star_count}",
        string=readme,
        flags=re.DOTALL,
    )


def _count_stars() -> int:
    found = _find_completed_days()
    return sum([val for days in found.values() for parts in days.values() for val in parts.values()])


def _update_year_readme(year: int) -> None:
    found = _find_completed_days()[year]
    header: List[str] = [f"# {year}"]

    days = found.keys()
    completed_parts = sum([len(parts.keys()) for parts in found.values()])
    body: List[str] = [
        f'Solutions for {len(days)} {"day" if len(days) == 0 else "days"} in {year} '
        f"with a total of {completed_parts} stars collected",
        "",
    ]

    body = body + _create_year_overview(found)
    year_readme_file = os.path.join(ROOT_DIR, f"year_{year}/README.md")
    text = header + body

    with open(year_readme_file, "w") as f:
        f.write("\n".join(text))


def _create_year_overview(completed_days: Dict[int, Dict[str, bool]]) -> List[str]:
    text: List[str] = ["| day   | part one | part two |", "| :---: | :------: | :------: |"]

    for day, parts in completed_days.items():
        part_one = "⭐️" if parts["part_one"] else "–"
        part_two = "⭐️" if parts["part_two"] else "–"
        text.append(f"| {day:02} | {part_one} | {part_two} |")

    return text


def _create_completed_text() -> str:
    found = _find_completed_days()

    text = ["## Completed ⭐️"]
    for year, days in found.items():
        _update_year_readme(year)
        text.append(f"### {year}")
        text.append(f"<details><summary>Solutions for {year}</summary>")
        text.append("<p>")
        text.append("")  # whitespace required
        text = text + _create_year_overview(days)
        text.append("")  # whitespace required
        text.append("</p>")
        text.append("</details>")
        text.append("")  # whitespace required

    text.append("")
    return "\n".join(text)


def _find_completed_days() -> YearDayType:
    """
    Loops through all the year directories, all the day files
    and checks if the file contains functions 'part_one' and 'part_two'

    Returns the results as a Dict
    """
    items: YearDayType = {}

    for year_path in get_full_year_paths():
        year = clean_year(year_path)
        items[year] = {}

        for day_file in get_full_day_paths(year_path):
            day = clean_day(day_file)
            items[year][day] = {}
            funcs = get_functions_from_day_file(day_file)

            items[year][day]["part_one"] = "part_one" in funcs
            items[year][day]["part_two"] = "part_two" in funcs

    return items
