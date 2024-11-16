# TODO импортировать необходимые молули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [OrderedDict(row) for row in reader]

    with open(OUTPUT_FILENAME, mode='w') as json_file:
        json.dump(data, json_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")