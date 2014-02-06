#!/usr/bin/env python
"""
This script consumes the already up-to-date 'items.json' file and creates
'index.html' file using it.
"""
import json

if __name__ == "__main__":
    with open('items.json') as fp:
        joblisting = json.load(fp)
    print joblisting[0]['title']

    # Construct HTML
    with open('index.html', 'wb') as fp:
        fp.write('<!DOCTYPE html>\n')
        for job in joblisting:
            fp.write('<a href=%(link)s>%(title)s</a>\n' % job)
