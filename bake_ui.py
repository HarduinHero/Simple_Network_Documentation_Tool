#!/usr/bin/env python3

from os import listdir, system

directory = './app/ui/'

print('#### "COMPILING" UI FILES ####')
ui_files = [file for file in listdir(directory) if file.split('.')[-1]=='ui']
uipy_files = [f'{file.split(".")[0]}.py' for file in ui_files]
for uif, pyf in zip(ui_files, uipy_files) :
    system(f'pyside6-uic.exe {directory}{uif} -o {directory}{pyf}')
    print(f'\t{uif} -> {pyf}')

print('\n#### "COMPILING" RESSOURCE FILES ####')
qrc_file, py_qrc_file = 'ressources.qrc', 'ressources_rc.py'
system(f'pyside6-rcc.exe {directory}{qrc_file} -o {directory}{py_qrc_file}')
print(f'\t{qrc_file} -> {pyf}')

print('\n#### EDITING RESSOURCE FILES IMPORT IN UI FILES ####')
for pyf in uipy_files :
    print(f'\t{pyf}')

    file = open(f'{directory}{pyf}', 'r')
    txt = file.read()
    txt = txt.replace('ressources_rc', 'ui.ressources_rc')
    file.close()
    
    file = open(f'{directory}{pyf}', 'w')
    file.write(txt)
    file.close()

print('Done')
