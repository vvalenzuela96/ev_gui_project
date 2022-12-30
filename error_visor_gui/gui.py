"""
@author Victor Valenzuela M
@since 30-12-22
"""

import json


def view_all_logs():
    with open('logs/log.ev', 'r') as file:
        all_logs = json.load(file)

    for registry in all_logs:
        print(f"""[{registry["type"].upper()}]
{registry["description"]}
{registry["filename"]}
{registry["context"]}
{registry["line"]}
{registry["timestamp"]}
""")