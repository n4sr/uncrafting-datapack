#!/usr/bin/env python3
import csv

with open('stair_recipes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        input_item = row[0]
        result_item = row[1]
        filename = f'{result_item}.json'

        contents = (
            '{\n'
            '  "type": "minecraft:crafting_shaped",\n'
            #'  "group": "wooden_stairs",\n' #uncomment for wood stairs
            '  "pattern": [\n'
            '    "# ",\n'
            '    "##"\n'
            '  ],\n'
            '  "key": {\n'
            '    "#": {\n'
            f'      "item": "minecraft:{input_item}"\n'
            '    }\n'
            '  },\n'
            '  "result": {\n'
            f'    "item": "minecraft:{result_item}",\n'
            '    "count": 4\n'
            '  }\n'
            '}'
        )

        with open(f'{input_item}.json', 'w') as f:
            f.write(contents)

