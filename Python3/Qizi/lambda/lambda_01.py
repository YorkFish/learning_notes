# 1.1
a = lambda x: x ** 2  # PEP-8 remaind: do not assign a lambda expression, use a def
print(a(2))

# 1.2
def f(x): return x ** 2
print(f(2))

# 2.
b = lambda x, y: x if x < y else y  # min(x, y)
print(b(1, 2))

# 3.
lst = [lambda x: x.strip(), lambda x: x ** 2]
print(lst)
print(lst[0]("  giao  "))
print(lst[1](3))

# 4.
def main():
    return lambda x: x ** 2

print(main())
print(main()(4))
