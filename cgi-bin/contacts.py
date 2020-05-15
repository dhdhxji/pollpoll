#!/usr/bin/python3
import sys
import os
import mod_path
import template
from headers import *

print_headers()

navbar = template.get("navbar")
print(template.get('contacts').format(**locals()))