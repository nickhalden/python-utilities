#!/bin/python
"""
script to sync mysql to library database and get the mysqldump on books database

"""
import os,sys

commandline="""ssh -i dropone root@sql-server-ip 'mysqldump -u user --password="password" library book > dump.sql'"""

print "enter mysql password"
os.system(commandline)
#put("password")

print "------syncing-----"
os.system("rsync -avzh root@sql-server-ip:dump.sql /backup-dir")




print "executed"

