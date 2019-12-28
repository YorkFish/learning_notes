"""
1.
Comparisons can be chained arbitrarily,
e.g., x < y <= z is equivalent to x < y and y <= z,
except that y is evaluated only once
(but in both cases z is not evaluated at all when x < y is found to be false).

Formally, if a, b, c, …, y, z are expressions and op1, op2, …, opN are comparison operators,
then a op1 b op2 c ... y opN z is equivalent to a op1 b and b op2 c and ... y opN z,
except that each expression is evaluated at most once.

Note that a op1 b op2 c doesn’t imply any kind of comparison between a and c,
so that, e.g., x < y > z is perfectly legal (though perhaps not pretty).
"""
print(">>> 1 < 2 < 3:", 1 < 2 < 3)  # True
print(">>> -3 < -2 < -1:", -3 < -2 < -1)  # True

# 2.
print("False is False is False:", False is False is False)  # True
# False is False is False
# => (False is False) and (False is False)
