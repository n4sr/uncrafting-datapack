#!/usr/bin/env python3
import csv

with open('stair_recipes.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        input_item = row[1]
        result_item = row[0]
        contents = (
            '{\n'
            '  "type": "minecraft:crafting_shaped",\n'
            '  "pattern": [\n'
            '    "##",\n'
            '    "##"\n'
            '  ],\n'
            '  "key": {\n'
            '    "#": {\n'
            f'      "item": "minecraft:{input_item}"\n'
            '    }\n'
            '  },\n'
            '  "result": {\n'
            f'    "item": "minecraft:{result_item}"\n'
            '  }\n'
            '}\n'
        )

        with open(f'uncraft_{input_item}.json', 'w') as f:
            f.write(contents)

