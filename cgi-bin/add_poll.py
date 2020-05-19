#!/usr/bin//python3

import cgi
import mod_path
from headers import *
from polls_db_if import *

fields = cgi.FieldStorage()

poll_title = ""
answers = []

for key in fields.keys():
    if key == 'poll_title':
        poll_title = fields[key].value
    elif fields[key] is not None:
        answers.append(fields[key].value)

add_poll(poll_title, answers)

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