import pandas as pd


def read_files():
    med = pd.read_csv(r'depot\drugs.csv')
    clt = pd.read_csv(r'depot\clinical_trials.csv')
    pub = pd.read_csv(r'depot\pubmed.csv')
    pub_json = pd.read_json(r'depot\pubmed.json')

    return med, clt, pub, pub_json
