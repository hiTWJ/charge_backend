import json

CONFIG = {}

with open('./chargingInBupt/config.json', 'r', encoding='utf-8') as f:
    CONFIG = json.load(f)