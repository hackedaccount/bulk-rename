import os, sys
import re
os.chdir('/home/shivam/')
cwd = os.getcwd()
# print(os.listdir())
for file in os.listdir():
    a=re.findall(r'\d+', file)
    if a:
        print(a)
        dst=a[0]+"_"+file
        os.rename(file,dst)
        print(dst)
