""" Entry points.
"""

from os import system, getenv
from pymon import main, Arguments as MonitorArguments
from .components import greet
from .__core__ import Core
from .__decorators__ import run_script, load_env
from .utils.logger import logger


@load_env()
@run_script("./.scripts/setup_log.sh")
@run_script("./.scripts/env_sync.sh")
def start() -> None:
    """start Launches the program."""
    greeting: str = greet()
    print(greeting)

    token = getenv("DISCORD_BOT_TOKEN")
    if token is not None:
        Core().run(token=token)
    else:
        logger.error("Provide a valid DISCORD_BOT_TOKEN in .env file.")


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
