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
print("\n")

os.system('curl --insecure -I '+url)


