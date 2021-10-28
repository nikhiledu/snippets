import csv
import json

def csv2json():
    csvfile = open('file.csv', 'r')
    jsonfile = open('file.json', 'w')

    fieldnames = ("one","two","three","four","uniquePageviews")
    reader = csv.DictReader( csvfile, fieldnames)
    tree = {}
    subtree = {}

    resp = []

    for row in reader:
        print(row)

        for key, dict_list in row.items():
            Service = dict_list[0]
            UniqueID = dict_list[1]
            Device = dict_list[2]
            Pagepath = dict_list[3]
            NumVisit = dict_list[4]
            resp.append({'Service': Service['v'], 'UniqueID': UniqueID['v'], 'Device': Device['v'],
                         'Pagepath': Pagepath['v'], 'NumVisit': NumVisit['v']})

    json.dump(tree, jsonfile)
    jsonfile.write('\n')

csv2json()