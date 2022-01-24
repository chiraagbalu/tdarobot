import tda
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

response = c.get_quote('SPY')
print(response.json())