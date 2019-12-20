#!/usr/bin/python3
# Copyright (C) 2019 Aleksa Sarai <cyphar@cyphar.com>
# Licensed under MIT.

MAILBOX_UNREAD_KEY = lambda user: "cyphar/mailbox/%s/unread" % (user,)
MAILBOX_READ_KEY   = lambda user: "cyphar/mailbox/%s/read" % (user,)
