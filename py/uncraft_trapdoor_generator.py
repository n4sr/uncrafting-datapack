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
        '  "type": "minecraft:crafting_shapeless",\n'
        '  "ingredients": [\n'
        '    {\n'
        f'      "item": "minecraft:{wood}_trapdoor"\n'
        '    }\n'
        '  ],\n'
        '  "result": {\n'
        f'    "item": "minecraft:{wood}_planks",\n'
        '    "count": 2\n'
        '  }\n'
        '}'
    )

    with open(f'uncraft_{wood}_trapdoor.json', 'w') as f:
        f.write(contents)

