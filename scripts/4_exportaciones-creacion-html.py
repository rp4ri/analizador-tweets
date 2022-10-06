import pandas as pd

def get_sentimientos():
    """read the raw file and return a dataframe with the data
    Returns:
        df(pd.DataFrame): a dataframe with the raw data
    """
    df = pd.read_json('data/1_intermediate/0_intermediate-sentimientos.json', orient='records', lines=True)
    df = df.drop_duplicates(subset=['texto-original'])
    df = df.drop(columns=['texto-traducido'])

    df.to_excel('data/2_processed/1_sentimientos.xlsx', index=False)
    return df
def main():
    get_sentimientos()
if __name__ == '__main__':
    main()
