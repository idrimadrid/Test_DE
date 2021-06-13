import json


def save_json(data):
    """ write  json file"""
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=2)


def gen_json(df1, df2, df3):
    """
    Generate Json file as this schema :
    {'drug': {
      'publication': [1, 2, 3],
      'journal': [1, 2, 3],
      'clinical_trial': [1, 2, 3]
      }}
    """
    data = {}
    for drug in df1.drug.to_list():
        # get cited drug rows in clinical trials
        cited_clinical_trial = df3[df3.scientific_title.str.contains(drug, case=False)]
        citation = []
        for row in cited_clinical_trial.iterrows():
            citation.append((row[1]).to_dict())
        clinical_trial = []
        journal = []
        # filling dictionary with infos
        for cite in citation:
            p = {"title": cite['scientific_title'], "date": cite['date']}
            clinical_trial.append(p)
            j = {"title": cite['journal'], "date": cite['date']}
            journal.append(j) if j not in journal else next
        # get cited drug rows in publication
        cited_publication = df2[df2.title.str.contains(drug, case=False)]
        citation = []
        for row in cited_publication.iterrows():
            citation.append((row[1]).to_dict())
        publication = []
        # filling dictionary with infos
        for cite in citation:
            p = {"title": cite["title"], "date": cite['date']}
            publication.append(p)
            j = {"title": cite['journal'], "date": cite['date']}
            journal.append(j) if j not in journal else next

        # adding dicts to main dictionary
        dic = {'publication': publication, 'journal': journal, 'clinical_trial': clinical_trial}
        data[drug] = dic

    # saving final json
    save_json(data)
