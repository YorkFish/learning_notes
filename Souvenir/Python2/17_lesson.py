# -*-coding:utf-8-*-

"""
readline() 读取当前行
readlines() 读取每一行
"""
list1 = [x for x in (file("www.txt").readlines())]  # file/open 都可以打开文件
print list1

for i in range(2):
    if i % 2 == 0:
        table_name = list1[i + 1]
        print table_name
        head = ("#!/bin/bash\n"
                "dba_user=qadba\n"
                "dba_passwd=qadba321\n"
                "tnsname=esuit_221\n"
                "sqlplus -s $ {dba_user}/$dba_passwd@$ tnsname<<EOF\n"
                "set feedback off\n"
                "set echo on\n"
                "set heading off\n"
                "set pagesize 0\n"
                "set trimspool on\n"
                "set verify off\n"
                "set space 0\n"
                "set linesize 660\n"
                "spool /home/oracle/asd.txt\n"
                "select 4||','||\n")

        tails = "from erating_xiyou_mysql.%s"\
                % (table_name + ";\n" + "spool off;\n" + "EOF\n")

        list2 = head + list1[i] + tails
        print list2
