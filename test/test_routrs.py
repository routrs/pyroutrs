import pytest  # noqa

import routrs


def test_it_works():
    assert 1 == 1
    assert routrs.add_numbers(left=1, right=1) == 2
