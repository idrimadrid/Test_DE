import pandas as pd


def process_drugs(df):
    """
    drugs transformation :  drop code column
    :param df: Dataframe
    :return: Dataframe
    """
    df.drop('atccode', axis=1, inplace=True)
    return df


def date_uniform(df):
    """
    Uniformise le format date
    :param df: dataframe
    :return: dataframe
    """
    df.date = pd.to_datetime(df.date)
    df.date = df.date.astype('str')
    return df


def process_cli(df):
    """
    Clinical trials transformation : consolidation de données et suppression de Nan et doublants
    :param df: dataframe
    :return: dataframe
    """
    df = date_uniform(df)

    df = df.groupby("scientific_title")["id", "scientific_title", "date", "journal"].apply(lambda x: x.ffill().bfill()).drop_duplicates()
    df = df.where(df.scientific_title != "  ").dropna()
    return df


def process_pub(df1, df2):
    """
       publication transformation and concatenation
       :param df2:
       :param df1:
       :return: dataframe
       """
    df = pd.concat([df1, df2])
    df = date_uniform(df)
    return df
