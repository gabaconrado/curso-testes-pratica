import pytest

from examples.identifier import Identifier


@pytest.mark.parametrize(
    'id_str, expected',
    [
        ('a', True),
        ('ab', True),
        ('abcde', True),
        ('abcdef', True),
        ('abcdefg', False),
        ('1a', False),
        ('a1', True),
        ('açaí', False),
    ]
)
def test_valid_identifier(id_str, expected):
    identifier = Identifier()

    is_valid = identifier.validate_identifier(id_str)

    assert is_valid is expected
