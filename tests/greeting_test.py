""" Greeting testing.
"""

from package.components import greet


def test_greeting():
    """test_greeting Test if greets correctly."""
    assert greet() == "Hello, world!"
