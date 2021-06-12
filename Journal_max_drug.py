import json


def open_json(path):
    with open(path) as f:
        data = json.load(f)
    return data


def count_journal(data):
    counter = {}
    for drug in list(data.keys()):
        js = []
        for j in data[drug]["journal"]:
            js.append(j["title"])
        counter[drug] = js
    return counter


def count_med_journal(counter):
    num_med = {}
    for x in counter:
        for j in counter[x]:
            if j not in list(num_med.keys()):
                num_med[j] = 1
            else:
                num_med[j] += 1
    return num_med


def get_journal_max_med(num_med):
    j = max(num_med, key=num_med.get)
    n = num_med[max(num_med, key=num_med.get)]
    return "Le journal {} contient {} drugs différents".format(j, n)


if __name__ == "__main__":
    data = open_json('output.json')
    count_journal(data)