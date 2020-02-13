import pytest

from dispatch.utils import get_checkin_geofence_radius

''' 
According to the specification, we have the following constraints for our tests
|  Vehicle  |   Minimun distance for check-in   |
|Motorcycle |600m                               |
|Van        |1500m                              |
|Others     |743.59m                            |

Our valid equivalence classes are:
    - Motorcycle
    - Van
    - Others
'''

# Equivalent classes

@pytest.mark.parametrize(
    'vehicle, expected',
    [
        ('motocycle', 600),
        ('van', 1500),
        ('others', 743.59)
    ]
)
def test_minimun_distance_checkin(vehicle, expected):
    assert get_checkin_geofence_radius(vehicle) == expected