import json


OUT_FILE = '../data/idtable.json'


idtable = {}

with open(OUT_FILE, 'r') as f:
    idtable = json.load(f)


def get_channel_name(id):
    return idtable.get('channels').get(id) or id


def get_role_name(id):
    return idtable.get('roles').get(id) or id
