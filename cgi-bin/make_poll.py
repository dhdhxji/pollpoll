#!/usr/bin/python3

import mod_path
import template
from headers import *
from polls_db_if import *
import cgi


fields = form = cgi.FieldStorage()

if form.getvalue('choise') is not None:
    choise_id = int(form.getvalue('choise'))
    poll(choise_id)

print_headers()
print("""
<script>
function goBack() {
    let prev = document.referrer;
    window.location.replace(prev);
}

goBack()
</script>
""")