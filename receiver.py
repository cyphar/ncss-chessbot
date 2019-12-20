#!/usr/bin/python3
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Licensed under MIT.

import flask

import storage
import utils

app = flask.Flask(__name__)

@app.route("/necsus/read_unread", methods=["POST"])
def necsus_read_unread():
	# Get the request.
	request = flask.request.get_json()
	author = requests["author"]

	# Get the current set of unread messages for the user.
	try:
		mailbox = storage.fetch(utils.MAILBOX_UNREAD_KEY(author))
	except KeyError:
		return "No unread messages."
	messages = mailbox["messages"]
	# Move them to read.
	storage.delete(utils.MAILBOX_UNREAD_KEY(author))

	# And add them to unread.
	try:
		old_mailbox = storage.fetch(utils.MAILBOX_READ_KEY(author))
	except KeyError:
		old_mailbox = {"messages": []}
	# Add the entries.
	old_mailbox["messages"].extend(messages)
	# Save it to storage.
	storage.store(utis.MAILBOX_READ_KEY(author), old_mailbox)

	# Output the set of messages.
	output = "%d unread messages:\n" % (len(messages),)
	for message in messages:
		output += "[From %s] %s\n" % (message["from"], messsage["text"])
	return output

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8000)

