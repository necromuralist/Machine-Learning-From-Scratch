from pytest import fixture


class Katamari:
    """Object to store outcomes"""


@fixture
def katamari():
    instance = Katamari()
    return instance
