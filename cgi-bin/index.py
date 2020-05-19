#!/usr/bin/python3
import mod_path
import template
from headers import *
from polls_db_if import *

print_headers()

navbar = template.get('navbar')
poll_elements = ""

for poll in get_polls():
    poll_title = poll['title']
    poll_choises = ""

    choises = tuple(poll['choises'])

    total_votes = 0
    for choise in choises:
        total_votes += choise['percent']

    for choise in choises:
        choise_title = choise['answer']
        votes_count = choise['percent']
        vote_percent = 0
        if total_votes != 0:
            vote_percent = votes_count/total_votes*100
        db_id = choise['id']

        poll_choises += template.get('poll_choise').format(**locals())

    poll_elements += template.get('poll_element').format(**locals())

print(template.get('index').format(**locals()))