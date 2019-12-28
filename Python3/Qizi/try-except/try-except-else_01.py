try:
    a = 1
except NameError:
    print("NameError!")
else:
    print(">>> a =", a)
finally:
    print("You must enter into finally!")


print("Is the program working properly?")
