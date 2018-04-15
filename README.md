# TCE Python Public Archive (TCE - PPA)
TCE Python Club and their experiement files will be added here

Please follow our basic rules mentioned below:
* Clone **template.py** file (under org/tce/template folder) to create a new file. It has the basic python details including comments, etc.
* Please mention your name in the author list. If more than one authors involved, add them in next lines
* If you use any tutorials, please paste the link in the **source** section


## Base code and comments
```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
author:
    [author name(s) should come here]
source: (if any)
    If you followed any tutorial, please paste the link so everyone will benefit from it
    
    sample:
    https://pythonspot.com/python-set/
    
'''
```

The above lines should be there in every **.py** file. It will help other developers to understand more about your python resources involved. Also, they can learn from those sources you shared here.


## Python Initiator (like public static void main(..) in java)
```
def main():
    print('Main')
    print(test())

if __name__ == '__main__':
    main()
```

Thought it is not mandatory, we recommend you to keep this format for every .py file. 


For Markdwon ref: https://guides.github.com/features/mastering-markdown/#examples
