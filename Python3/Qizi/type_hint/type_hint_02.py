"""
this is "Variable Annotations"
this notes PyCharm is temporarily unrecognized
but code checking for third party libraries(such as "mypy") is valid
"""

from typing import Dict, List

# 1.
a = 1  # type:int
b = False  # type:bool

# 2.
c = []  # type:List[int]
d = {}  # type:Dict[str, int]

# after Python 3.6
# 3.
a1: int = 1
b1: bool = False

# 4.
c1: List[int] = []
d1: Dict[str, int] = {}
