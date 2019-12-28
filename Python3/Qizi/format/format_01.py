str_a = 'a'
int_b = 1
tuple_c1 = (1,)
tuple_c2 = (1, 2)
list_d = [1, 2]
dict_e = {"e1": 1, "e2": 2}

# 1.
print(">>> str_a =", str_a)
print(">>> int_a = " + str_a)
print(">>> str_a = %s" % str_a)
print(">>> int_b = %d" % int_b)

# 2.
print(">>> tuple_c1 = %d" % tuple_c1)
print(">>> tuple_c2 = (%d, %d)" % tuple_c2)

print(">>> list_d = %s" % list_d)
print(">>> dict_e = %s" % dict_e)

# 3.
print(">>> tuple_c2 = {}".format(tuple_c2))
print(">>> tuple_c2[0] = {0}, tuple_c2[1] = {1}".format(*tuple_c2))

# 4.
print(">>> dict_e['e1'] = {e1}, dict_e['e2'] = {e2}".format(**dict_e))
