import pandas as pd
import json

def get_subtree(tree, row, index):
    if index == 0:
        return tree.get(row[0])
    elif index == 1:
        return tree.get(row[0]).get(row[1])
    elif index == 2:
        return tree.get(row[0]).get(row[1]).get(row[2])
    elif index == 3:
        return tree.get(row[0]).get(row[1]).get(row[2]).get(row[3])

def update_subtree(tree, subtree, row, index):
    if index == 0:
        if tree.get(row[0]) is not None:
            tree[row[0]].extend(subtree[row[0]])
        else:
            tree[row[0]] = subtree[row[0]]
    elif index == 1:
        if tree.get(row[0]) is not None:
            tree.get(row[0]).extend(subtree[row[1]])
        else:
            tree.get(row[0])[row[1]] = subtree[row[1]]
    elif index == 2:
        if tree.get(row[0]) is not None:
            tree.get(row[0]).get(row[1]).extend(subtree[row[2]])
        else:
            tree.get(row[0]).get(row[1])[row[2]] = subtree[row[2]]
    elif index == 3:
        if tree.get(row[0]) is not None:
            tree.get(row[0]).get(row[1]).get(row[2]).extend(subtree[row[3]])
        else:
            tree.get(row[0]).get(row[1]).get(row[2])[row[3]] = subtree[row[3]]

def update_tree(tree, index, row):
    if tree is None or len(tree) == 0:
        tree = {row[index]: {}}

        if index == 4:
            return
    else:
        if index == 4:
            tree[index].append(row[index])
            return
        else:
            tree[index].extend(row[index])

    update_tree(tree.get(index + 1), index + 1, row)

def csv2json():
    csvfile = open('file.csv', 'r')
    jsonfile = open('file.json', 'w')

    # reader = csv.DictReader(csvfile)
    tree = {}

    # for row in reader:
    rows = (("personal-account","your-address","taxation-account","due-date","15"),
              ("personal-account","your-address", "tar-credit-account", "due-date", "9898"),
              ("public-account","office-address","tax-credits-choice","enter-start-date","65656"),
              ("public-account","office-address","residency-choice","enter-start-date","657767"),
              ("public-account","office-address","sole","find-address","7654"),
              ("public-account","office-address","sole","enter-start-date","9999"))

    for row in rows:
        try:
            for index, col in enumerate(row):
                subtree = {}

                try:
                    subtree = get_subtree(tree, row, index)

                except AttributeError:
                    pass

                if subtree is None or len(subtree) == 0:
                    subtree = {col: []}
                else:
                    if index == 4:
                        subtree = col
                    else:
                        subtree = {col: []}

                update_subtree(tree, subtree, row, index)

        except AttributeError:
            pass

    json.dump(tree, jsonfile)
    jsonfile.write('\n')

def spark_json():
    jsonfile = open('file.json', 'w')

    # reader = csv.DictReader(csvfile)
    tree = {}

    # for row in reader:
    rows = (("personal-account","your-address","taxation-account","due-date","10076"),
              ("personal-account","your-address", "tax-credit-account", "due-date", "77777"),
              ("public-account","office-address","tax-credits-choice","enter-start-date","9769"),
              ("public-account","office-address","residency-choice","enter-start-date","7744"),
              ("public-account","office-address","sole","find-address","7777"),
              ("public-account","office-address","sole","enter-start-date","6788"))

    for row in rows:
        try:
            if tree.get(row[0]) is not None:
                if tree.get(row[0]).get(row[1]) is not None:
                    if tree.get(row[0]).get(row[1]).get(row[2]) is not None:
                        if tree.get(row[0]).get(row[1]).get(row[2]).get(row[3]) is not None and row[4] is int:
                            tree.get(row[0]).get(row[1]).get(row[2])[row[3]] = tree.get(row[0]).get(row[1]).get(row[2])[row[3]] + row[4]
                        else:
                            tree.get(row[0]).get(row[1]).get(row[2])[row[3]] = row[4]
                    else:
                        tree.get(row[0]).get(row[1])[row[2]] = {row[3]: row[4]}
                else:
                    tree.get(row[0])[row[1]] = {row[2]: {row[3]: row[4]}}
            else:
                tree[row[0]] = {row[1]: {row[2]: {row[3]: row[4]}}}

        except AttributeError:
            pass

    json.dump(tree, jsonfile)
    jsonfile.write('\n')

def aggregate_json():
    # for row in reader:
    data = ({"one": "personal-account","two":"your-address","three":"taxation-account","four":"due-date","uniquePageviews":"15"},
              ("personal-account","your-address", "tar-credit-account", "due-date", "276655"),
              ("public-account","office-address","tax-credits-choice","enter-start-date","9769"),
              ("public-account","office-address","residency-choice","enter-start-date","7744"),
              ("public-account","office-address","sole","find-address","7444"),
              ("public-account","office-address","sole","enter-start-date","6788"))

    aggregation_functions = {'price': 'sum', 'amount': 'sum', 'name': 'first'}
    df_new = pd.groupby(pd['id']).aggregate(aggregation_functions)

spark_json()