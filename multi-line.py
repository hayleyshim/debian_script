#!/usr/bin/python3

import textwrap

i = textwrap.dedent("""
    one
    two three
      four
    five
""".lstrip('\n')).splitlines()

print(i)
