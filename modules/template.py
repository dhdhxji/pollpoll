#!/usr/bin/python3

def get(name):
    t = open("template/" + name + ".html", 'r')
    content = t.read()
    t.close()

    return content