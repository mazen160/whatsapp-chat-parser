#!/usr/bin/env python3
# coding=utf-8
# *****************************************************
# whatsapp-chat-parser: Parse WhatsApp exported chats.
# Author:
# Mazin Ahmed <mazin at mazinahmed dot net>
# https://github.com/mazen160/whatsapp-chat-parser
# *****************************************************
from datetime import datetime
import re

REGEX_DATE = """^(\u200e){0,1}\[[0-9\/]+(, )[0-9:]+\]"""
REGEX_CONTACT = """^(\u200e){0,1}\[[0-9\/]+(, )[0-9:]+\](.+?)(: )"""
REGEX_MESSAGE = """^(\u200e){0,1}\[[0-9\/]+(, )[0-9:]+\](.)+(: )(.+)"""


def __parse_timestamp(s):
    return datetime.strptime(s, '[%d/%m/%y, %H:%M:%S]')


def __remove_chars(s):
    chars = ["\u202a", "\u202c", "\xa0", "\u2011"]
    for c in chars:
        s = s.replace(c, "")
    return s


def get_messages(chat_export_path):
    f = open(chat_export_path, "r")
    original_messages = f.read().split("\n")
    f.close()
    messages = []
    descriptive_messages = []

    for m in original_messages:
        data = {"timestamp": "",
                "original_date": "",
                "author": "",
                "message": ""}

        if not re.match(REGEX_DATE, m):
            # Newline
            messages[-1]["message"] += "\n" + m
            continue

        if m.startswith("\u200e"):
            m = m[1:]

        original_timestamp = re.search(REGEX_DATE, m).group(0)
        data["original_date"] = original_timestamp
        data["timestamp"] = __parse_timestamp(original_timestamp)
        contact_original = re.search(REGEX_CONTACT, m)
        message_original = re.search(REGEX_MESSAGE, m)
        if not message_original:
            message_original = ""
        else:
            message_original = message_original.groups()[-1]

        if contact_original is None:
            descriptive_messages.append(m)
            continue
        if "security code changed." in m:
            descriptive_messages.append(m)
            continue

        data["author"] = contact_original.group(3)
        data["message"] = message_original

        if data["message"].startswith("\u200e"):
            data["message"] = data["message"][1:]

        data["author"] = __remove_chars(data["author"])
        if data["author"].startswith(" "):
            data["author"] = data["author"][1:]

        messages.append(data)

    return {"chats": messages, "descriptive_messages": descriptive_messages}
