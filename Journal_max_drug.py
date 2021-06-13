import json


def open_json(path):
    """ Read Json file"""
    with open(path) as f:
        file = json.load(f)
    return file


def count_journal(file):
    """ count journal in each drug"""
    count = {}
    for drug in list(file.keys()):
        js = []
        for j in file[drug]["journal"]:
            js.append(j["title"])
        count[drug] = js
    return count


def count_med_journal(counts):
    """ Count drug in each journal"""
    count_med = {}
    for x in counts:
        for j in counts[x]:
            if j not in list(count_med.keys()):
                count_med[j] = 1
            else:
                count_med[j] += 1
    return count_med


def get_journal_max_med(num):
    """ Show journal with most cited drugs"""
    j = max(num, key=num.get)
    n = num[max(num, key=num.get)]
    print("Le journal \"{}\" contient {} drugs différents".format(j, n))
    return j, n


if __name__ == "__main__":
    data = open_json('output.json')
    counter = count_journal(data)
    num_med = count_med_journal(counter)
    get_journal_max_med(num_med)
