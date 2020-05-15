#!/usr/bin//python3

import cgi
import mod_path
from headers import *

fields = cgi.FieldStorage()

print_headers()
print(fields)
