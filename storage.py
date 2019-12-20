#!/usr/bin/python3
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Licensed under MIT.

import requests

STORE_URL = lambda key: "https://store.ncss.cloud/%s" % (key,)

def fetch(key):
	resp = requests.get(STORE_URL(key))
	if not resp.ok:
		raise KeyError("key not present in store")
	return resp.json()

def store(key, value):
	resp = requests.post(STORE_URL(key), json=value)
	if not resp.ok:
		raise ValueError("value was rejected by store")

def delete(key):
	requests.delete(STORE_URL(key))
