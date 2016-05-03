from re import search
from unittest import TestCase
from closurepr import rich_repr


@rich_repr
def adder(a, b):
    return lambda c: (a + b + c)


def rr(obj):
    match = search(r'<function ([\w\W]+) at ([0-9a-zA-Z]+)>', repr(obj))
    assert match
    name, _ = match.groups()
    return name


class TestRichRepr(TestCase):
    def test_simple(self):
        add = adder(1, 2)
        assert rr(add) == 'adder(1,2)'
        assert add(3) == 6

    def test_complex(self):
        add = adder(1, b=2)
        assert rr(add) == 'adder(1,b=2)'
        assert add(3) == 6
