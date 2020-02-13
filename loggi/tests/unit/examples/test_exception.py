import pytest
from examples.identifier import Identifier

def test_exception_raised():
    identifier = Identifier()
    with pytest.raises(ValueError) as error:
        identifier.validate_identifier('')
    assert str(error.value) == 'Tipo errado'
