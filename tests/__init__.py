""" Testing package
"""

import sys
import pytest

from pymon import main, Arguments as MonitorArguments


def test() -> None:
    """test Runs a the full battery of tests."""
    sys.exit(pytest.main())


def test_watch() -> None:
    """start_watch Launches the program in watch mode."""
    arguments = MonitorArguments(
        command="poetry -q run test",
        patterns=["*.py"],
        watch="./package",
        args=[],
        debug=True,
        clean=False,
    )

    main(arguments)


def coverage() -> None:
    """coverage Generate a test coverage report"""
    pytest_args = [
        "--cov=package",
        "--cov-report=term",
        "--cov-report=html",
        "tests/",
    ]
    sys.exit(pytest.main(pytest_args))


if __name__ == "__main__":
    test()
