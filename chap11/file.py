#!/usr/bin/env python3
f = open('somefile.txt')
file_as_list = f.readlines()
for line in file_as_list:
    print(line, end='')
