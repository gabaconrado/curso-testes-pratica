import pytest

from examples.identifier import Identifier

@pytest.fixture(scope='function', params=['abcdef', 'a1'])
def identifier(request):
    return (Identifier(), request.param)

def test_valid_identifier(identifier):
    is_valid = identifier[0].validate_identifier(identifier[1])
    assert is_valid is True