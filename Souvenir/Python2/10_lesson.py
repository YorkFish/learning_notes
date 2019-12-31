# -*-coding:utf-8-*-

import random
import string
import sys


def generate_pwd(s1="xdw", s2="ibxo"):
    tmp1 = str(random.random())
    tmp2 = str(random.uniform(1, 99))
    passwd1 = tmp1.replace('.', s1)
    passwd2 = tmp2.replace('.', s2)
    pwd = passwd1 + passwd2
    return pwd


if __name__ == "__main__":
    MAX_COUNT = 5  # 需要产生几条，可以改成相应数字
    for i in range(MAX_COUNT):
        str1 = "insert into temp values("
        zone_id = 101
        num_id = i + 1
        test_code = "test" + str(MAX_COUNT*1000 + num_id)

        pwd = generate_pwd()
        while len(pwd) != 32:
            pwd = generate_pwd("yiq", "acid")

    	test_name = "test%d" % num_id
        test_ip = 2087917712
        test_mac = "00-00-00-00-00-00"
        test_state = "1);"

        print str1 + repr(num_id) + ', ' +\
                repr(zone_id) + ', ' +\
                test_code + ', ' +\
                pwd + ', ' +\
                test_name + ', ' +\
                repr(test_ip) + ', ' +\
                test_mac + ', ' +\
                test_state

    print "commit;"

# python2 10_lesson-2.py $1 > temp.sql
