import os
try:
    DEVELOP = os.environ.get('ENV') in ['DEV',]
except KeyError:
    DEVELOP = False

print (DEVELOP)

if DEVELOP:
    print ('DEVELOP')
    from .develop import *
else:
    print ('PRO')
    from .production import *