import pytest

from base.utils.phone import format_phone_number

"""
According to our specification, our valid equivalence classes are:
    - Phones with 9 characteres (Mobile w/o State code)
    - Phones with 11 characteres (Mobile with State code)
    - Phones with 8 characteres (Landlines w/o State code)
    - Phones with 10 characteres (Landline with State code)
"""


@pytest.mark.parametrize(
    'input, expected',
    [
        ('912340000', '91234-0000'),
        ('11912340000', '(11) 91234-0000'),
        ('51235432', '5123-5432'),
        ('1151235432', '(11) 5123-5432'),
        ('(11) 91234-0000', '(11) 91234-0000'),
        ('123456789012', '123456789012'), # Invalid (More than maximun)
        ('1234567', '1234567'), # Invalid (Less than minimun)
        ('phone_number', None), # Invalid (Characteres)
    ]
)
def test_format_phone_number(input, expected):
    assert format_phone_number(input) == expected
