#!/usr/bin/python3
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Licensed under MIT.

import flask

import storage
import utils

app = flask.Flask(__name__)

@app.route("/necsus/send", methods=["POST"])
def necsus_send():
	"Takes two parameters (to, msg)."

	# Get the request.
	request = flask.request.get_json()

	author = requests["author"]
	to = requests["params"]["to"]
	entry = {
		"from": author,
		"text": request["params"]["text"]
	}

	# Get the current set of unread messages for the user.
	try:
		mailbox = storage.fetch(utils.MAILBOX_UNREAD_KEY(to))
	except KeyError:
		mailbox = {"messages": []}
	# Add the entry.
	mailbox["messages"].append(entry)
	# Save it to storage.
	storage.store(utils.MAILBOX_UNREAD_KEY(to), mailbox)

	# Tell the sender it's delivered.
	return "%s: message delivered to %s." % (author, to)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)
