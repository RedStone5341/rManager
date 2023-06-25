import os, hashlib, io, json

if not os.path.exists('data'):
    os.mkdir('data')
if not os.path.exists('data/paths.json'):
    