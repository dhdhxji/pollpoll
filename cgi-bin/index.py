#!/usr/bin/python3
import mod_path
import template
from headers import *

print_headers()

navbar = template.get('navbar')
print(template.get('index').format(**locals()))