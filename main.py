#!/usr/bin/env python

import os
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class EthScan:

    def __init__(self, API_KEY, URL, module, action, address, **kwargs) -> None:
        self.API_KEY = API_KEY
        self.URL = URL
        self.module = module
        self.action = action
        self.address = address
        self.kwargs = kwargs

    def url(self):
        final_url = URL+ f"?module={self.module}&action={self.action}&address={self.address}&apikey={self.API_KEY}"
        for key, value in self.kwargs.items():
            final_url+=f"&{key}={value}"
        return final_url
    
    def get_balance(self, balance_url):
        response = requests.get(url=balance_url)
        data = response.json()
        return int(data['result']) / 10**18

root = ttk.Window(themename="darkly")
l1 = ttk.Label(bootstyle="success", text="Hello")
l1.pack(side=LEFT, padx=5, pady=10)

root.mainloop()

load_dotenv()
address = "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"
API_KEY = os.getenv('API_KEY')
URL = 'https://api.etherscan.io/api'
eth1 = EthScan(
    API_KEY, 
    URL, 
    "account", 
    "balance", 
    address, 
    tag="latest"
    )
balance_url = eth1.url()
print(eth1.get_balance(balance_url))





'''
https://api.etherscan.io/api
   ?module=account
   &action=balance
   &address=0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae
   &tag=latest
   &apikey=YourApiKeyToken
'''
