import re
from const import Const

_PATTERN = Const()
_PATTERN.ipv4 = re.compile('(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')

def is_ipv4(value):
    match = _PATTERN.ipv4.match(value)
    if match is None:
        return False
    seg0 = int(match.group(1))
    if seg0 > 254:
        return False
    seg1 = int(match.group(2))
    if seg1 > 254:
        return False
    seg2 = int(match.group(3))
    if seg2 > 254:
        return False
    seg3 = int(match.group(4))
    if seg3 > 254:
        return False
    return True
