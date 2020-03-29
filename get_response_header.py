import optparse
import re
import pylab
import warnings
import os
import glob
import pyfiglet

warnings.filterwarnings("ignore")
#Banner 
ascii_banner = pyfiglet.figlet_format("Response \t Header",width=100)

print(ascii_banner)

url = input("\033[93mEnter a URL:")
certificate = input("\033[93mEnter certificate TLS/SSL:")
print("\n")
if(certificate == 'TLS'):
    os.system('curl --head '+url)
else:
    os.system('curl --head --insecure '+url)

