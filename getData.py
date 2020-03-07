import json
import csv

path = 'data/data.csv'

def read_csv(DataType):
    if DataType is 'list':
        return to_list()
    elif DataType is 'dict':
        return to_dict()
    else:
        msg = "[Params Error] Please enter either 'list' or 'dict'"
        return msg

def to_list():
    with open(path, encoding='UTF-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list()
        for row in reader:
            row = [x for x in row if x]
            if row: data.append(row)
        return data
    
def to_dict():
    with open(path, encoding='UTF-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        data = dict()
        for row in reader:
            row = [x for x in row if x]
            if row: data[row[0]] = row[1]
        data = json.dumps(data, indent=4)
        return data
