import datetime
import tda
import pandas as pd
from tda import auth, client
import json
import config


try:
    c = auth.client_from_token_file(config.token_path, config.api_key)
except FileNotFoundError:
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    s = Service('/Users/chiraagbalu/PycharmProjects/tdarobot/chromedriver')
    with webdriver.Chrome(service=s) as driver:
        c = auth.client_from_login_flow(
            driver, config.api_key, config.redirect_uri, config.token_path)

option_chain_dict = []
query = c.get_option_chain('SPY').json()
#use both puts and calls
for put_call in ['callExpDateMap', 'putExpDateMap']:
    #make dictionary of contracts where keys are expirations
    contract = dict(query)[put_call]
    expirations = contract.keys()
    #use every expiry
    for expiry in list(expirations):
        # take the strikes at each expiry
        strikes = contract[expiry].keys()
        #use every strike in the chain
        for strike in list(strikes):
            #add each strike's information to the option chain dictionary
            entry = contract[expiry][strike][0]
            option_chain_dict.append(entry)
option_chain_df = pd.DataFrame(option_chain_dict)
#keep original, work with easy name
ocdf = option_chain_df.copy(deep=False)
ocdf.drop(['exchangeName', 'bidSize', 'askSize', 'tradeTimeInLong', 'quoteTimeInLong', 'rho', 'optionDeliverablesList', 'multiplier', 'settlementType', 'deliverableNote', 'isIndexOption', 'nonStandard', 'pennyPilot','mini'], axis='columns', inplace=True)
print(ocdf.columns)







