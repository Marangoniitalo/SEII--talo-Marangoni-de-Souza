import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    print(csv_reader)

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    for line in csv_reader:
        print(line[2])

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')

    for line in csv_reader:
        csv_writer.writerow(line)

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')

    for line in csv_reader:
        csv_writer.writerow(line)

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.Dictreader(csv_file)

    for line in csv_reader:
        print(line)

import csv

with open('names.csv', 'r') as csv_file:
    csv_reader = csv.Dictreader(csv_file)

    with open('new_names.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.Dictwriter(new_file, fiednames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

    for line in csv_reader:
        del line['email']
        csv_writer.writerow(line)
