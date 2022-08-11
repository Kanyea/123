# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 17:42:54 2021

@author: kan.wu
"""

import os
# import shutil

print(os.getcwd())
print(os.path.exists("C:\\demo"))
#os.makedirs("C:/Python/Learning/path122/a/b/c")
#shutil.rmtree("C:/Python/Learning/path1")
tuples = os.walk("C:/Python/Learning")
for tuple1 in tuples:
    print(tuple1,'\n')
    
fileinfo = os.stat("ABC.docx")
print(os.path.abspath("ABC.docx"))
print(fileinfo.st_ino)
print(fileinfo.st_dev)
print(fileinfo.st_size,'Byte')
print(fileinfo.st_atime)
print(fileinfo.st_mtime)
print(fileinfo.st_ctime)