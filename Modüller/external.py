import termcolor

result = dir(termcolor)
# result = help(termcolor)
result = termcolor.colored('Hello, World!', 'blue', ['bold', 'dark'])

from termcolor import colored
result = colored('Hello, World!', color ='blue', attrs=['bold', 'italic'])
print(result)


"""
pip3 list
Package   Version
--------- -------
pip       26.1.1
termcolor 3.3.0
"""


"""
pip3 uninstall termcolor
Found existing installation: termcolor 3.3.0
Uninstalling termcolor-3.3.0:
  Would remove:
    /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/termcolor-3.3.0.dist-info/*
    /Library/Frameworks/Python.framework/Versions/3.14/lib/python3.14/site-packages/termcolor/*
Proceed (Y/n)? 
"""
