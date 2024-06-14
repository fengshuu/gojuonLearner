import os
import random
import csv
import argparse

class Japanese:
    def __init__(self, index, hira, kata, roma, weight):
        self.index = int(index)
        self.hira = hira
        self.kata = kata
        self.roma = roma
        self.weight = weight

    def __str__(self):
        return f"{self.weight - 1}\t{self.hira}\t{self.kata}\t{self.roma}"

def load_data(file_path, reset_weights):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        data = [Japanese(int(row['index']), row['hira'], row['kata'], row['roma'], int(row['weight'])) for row in reader]
    if reset_weights:
        for item in data:
            item.weight = 1
    return data

def save_data(file_path, data):
    headers = ['index', 'hira', 'kata', 'roma', 'weight']
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for item in data:
            writer.writerow({
                'index': str(item.index),
                'roma': item.roma,
                'hira': item.hira,
                'kata': item.kata,
                'weight': str(item.weight)
            })

def main():
    parser = argparse.ArgumentParser(description='A tool to help memorize the Japanese syllabaries')
    parser.add_argument('-f', '--file', default='data.csv', help='Specify the path to the data file')
    parser.add_argument('-r', '--reset', action='store_true', help='Reset all weights to 1')
    parser.add_argument('-i', '--input', default='roma', help='Specify the attribute to input, hira kata roma')
    parser.add_argument('-d', '--display', default='hira', help='Specify the attribute to display, hira kata roma')
    args = parser.parse_args()

    data = load_data(args.file, args.reset)
    sorted_data = sorted(data, key=lambda x: x.index)

    while True:
        item = get_random_item_by_weight(sorted_data)
        print(getattr(item, args.display))
        wrong = False
        while True:
            user_input = input().strip()
            if user_input.lower() == 'q':
                break
            if user_input == getattr(item, args.input):
                break
            if user_input == '?':
                print(getattr(item, args.input))
            wrong = True

        if os.name == 'nt':
            os.system('cls')
        elif os.name == 'posix':
            os.system("clear")

        if wrong:
            item.weight += 1

        if user_input.lower() == 'q':
            save_data(args.file, sorted_data)
            error_data = sorted(sorted_data, key=lambda x: x.weight, reverse=True)
            print("ErrN\tHira\tKata\tRoma")
            for obj in error_data:
                print(obj)
            break

def get_random_item_by_weight(items):
    total_weight = sum(item.weight for item in items)
    rnd = random.uniform(0, total_weight)
    upto = 0
    for item in items:
        upto += item.weight
        if rnd < upto:
            return item

if __name__ == "__main__":
    main()
