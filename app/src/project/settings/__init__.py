import os
try:
    DEVELOP = os.environ.get('ENV') in ['DEV',]
except KeyError:
    DEVELOP = False

if DEVELOP:
    print ('DEV')
    from .develop import *
else:
    print ('PRO')
    from .production import *