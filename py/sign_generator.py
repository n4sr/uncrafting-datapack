#!/usr/bin/env python3
import csv

wood_types = [
    'oak',
    'dark_oak',
    'acacia',
    'spruce',
    'jungle',
    'birch'
]

for wood in wood_types:
    contents = (
        '{\n'
        '  "type": "minecraft:crafting_shaped",\n'
        '  "pattern": [\n'
        '    "#",\n'
        '    "I"\n'
        '  ],\n'
        '  "key": {\n'
        '    "#": {\n'
        f'      "item": "minecraft:{wood}_planks"\n'
        '    },\n'
        '    "I": {\n'
        '      "item": "minecraft:stick"\n'
        '    }\n'
        '  },\n'
        '  "result": {\n'
        f'    "item": "minecraft:{wood}_sign",\n'
        '    "count": 1\n'
        '  }\n'
        '}'
    )

    with open(f'{wood}_sign.json', 'w') as f:
        f.write(contents)

