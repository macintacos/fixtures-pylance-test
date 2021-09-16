"""Setup for pytest stuff."""

import pytest


@pytest.fixture(autouse=True)
def mocked_thing() -> str:
    """This is the documentation for mocked_thing."""
    return "some string"
