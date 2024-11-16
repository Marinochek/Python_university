# TODO решите задачу
import json
FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as file:
        data = json.load(file)
        total_sum = sum(item.get("score", 0) * item.get("weight", 0) for item in data)
        return round(total_sum, 3)

if __name__ == '__main__':
    print(task())




