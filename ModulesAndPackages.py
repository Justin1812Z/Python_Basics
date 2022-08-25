from distutils.filelist import findall
import re

# Your code goes here
find_members = []

for x in dir(re):
    if x.startswith("find"):
        find_members.append(x) 
print (find_members)
