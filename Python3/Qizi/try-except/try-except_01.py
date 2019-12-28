# 1.
try:
    a = b
except ArithmeticError:
    print("ArithmeticError!")
except KeyError:
    print("KeyError!")
except TypeError:
    print("TypeError!")
except Exception:
    print("Some error!")

# 2.
try:
    a = b
except Exception as e:
    print(e)

# 3.
try:
    a = b
except NameError:
    print("NameError!")
finally:
    print("You must enter into finally!")


print("Is the program working properly?")
