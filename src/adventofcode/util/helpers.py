import cProfile
import os
import pstats
import time
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Literal
from typing import Tuple

from adventofcode.config import RUNNING_ALL
from adventofcode.config import RUNNING_BENCHMARKS
from adventofcode.util.console import console
from adventofcode.util.exceptions import SolutionNotFoundException


def _get_year_from_segment(segment: str) -> int:
    if not segment.startswith("year_"):
        raise ValueError(f"invalid year segment received: {segment}")

    return int(segment[5:])


def get_year_from_file(file: str):
    """
    Pass __file__ as parameter to get the year the file is in.

    Should not be used outside of a year_* module
    """
    segments = os.path.dirname(os.path.realpath(file)).split(os.sep)
    year_segment = segments[-1]
    return _get_year_from_segment(year_segment)


def _get_prefix(year: int, day: int, part: int, version: str) -> str:
    if not day or not part:
        raise ValueError("incorrect values provided for solution timer")

    if version:
        version = f" [yellow]{version}[/yellow]"

    if RUNNING_ALL:
        prefix = f"[blue]  - day {day:02} part {part:02}[/blue]{version}: "
    else:
        prefix = f"[blue]{year} day {day:02} part {part:02}[/blue]{version}: "

    return prefix


def solution_timer(year: int, day: int, part: int, version: str = ""):  # noqa: C901, type: ignore
    prefix = _get_prefix(year, day, part, version)

    def decorator(func: Callable):  # type: ignore
        def wrapper(*args, **kwargs):
            try:
                start = time.perf_counter()
                solution = func(*args, **kwargs)

                if solution is None:
                    raise SolutionNotFoundException(year, day, part)

                diff = (time.perf_counter() - start) * 1000

                if not RUNNING_BENCHMARKS:
                    console.print(f"{prefix}{solution} in {diff:.2f} ms")
            except (ValueError, ArithmeticError, TypeError):
                console.print_exception()
            except SolutionNotFoundException:
                console.print(f"{prefix}[red]solution not found")
            else:
                if RUNNING_BENCHMARKS:
                    return diff

                return solution

        return wrapper

    return decorator


def solution_profiler(
    year: int, day: int, part: int, version: str = "", stats_amount: int = 10, sort: Literal["time", "cumulative"] = "time"
):  # noqa: C901, type: ignore
    prefix = _get_prefix(year, day, part, version)

    def decorator(func: Callable):  # type: ignore
        def wrapper(*args, **kwargs):
            with cProfile.Profile() as profiler:
                solution = func(*args, **kwargs)

            stats = pstats.Stats(profiler)

            if sort == "time":
                stats.sort_stats(pstats.SortKey.TIME)
            elif sort == "cumulative":
                stats.sort_stats(pstats.SortKey.CUMULATIVE)
            else:
                raise ValueError('only "time" and "cumulative" are supported')

            stats.sort_stats(pstats.SortKey.TIME)
            console.print(f"{prefix} profiling")
            stats.print_stats(stats_amount)
            return solution

        return wrapper

    return decorator


def memoize(func: Callable):  # type: ignore
    cache: Dict[Any, Any] = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


def manhattan_distance(start: Tuple[int, int], end: Tuple[int, int]):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


def grid_to_string(grid: Dict[Tuple[int, int], Any]) -> str:
    lines: List[str] = []
    max_x, max_y = max(grid.keys())

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            line += str(grid[(x, y)])

        lines.append(line)

    return "\n".join(lines)
