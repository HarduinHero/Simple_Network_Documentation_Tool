#!/usr/bin/env python3

from os import listdir, system

directory = './app/ui/'

ui_files = [file for file in listdir(directory) if file.split('.')[-1]=='ui']
py_files = [f'{file.split(".")[0]}.py' for file in ui_files]

for uif, pyf in zip(ui_files, py_files) :
    system(f'pyuic6 {directory}{uif} -o {directory}{pyf}')
    print(f'{uif} -> {pyf}')
print('Done')
