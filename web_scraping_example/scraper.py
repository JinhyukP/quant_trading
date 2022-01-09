# useful functions for web scarpping

import pandas as pd

def get_ticker(company_name):
    '''
    input: company name (string)
    output: corresponding ticker'''

    df = pd.read_csv('tickers_KOSPI_KOSDAQ.csv')

    ticker = df.loc[df['종목명'] == company_name]['종목코드'].values[0]

    return ticker

if __name__ == "__main__":
    print('Test for function get_ticker(company_name)')
    print(get_ticker('삼성전자'))
    print(get_ticker('SK텔레콤'))
    print(get_ticker('앱코'))