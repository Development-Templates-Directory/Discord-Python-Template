""" Entry points.
"""

from os import system
from pymon import main, Arguments as MonitorArguments
from .components import greet


def start() -> None:
    """start Launches the program."""
    greeting: str = greet()
    print(greeting)


def start_watch() -> None:
    """start_watch Launches the program in watch mode."""
    arguments = MonitorArguments(
        command="poetry -q run start",
        patterns=["*.py"],
        watch="./package",
        args=[],
        debug=True,
        clean=False,
    )

    main(arguments)


def dev() -> None:
    """dev Development entry point."""
    system("mprocs")


if __name__ == "__main__":
    start()
