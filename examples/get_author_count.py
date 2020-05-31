from datetime import datetime
from datetime import timedelta
import json
import sys
from whatsapp_chat_parser import get_messages


def sort_authors_by_message_count():
    authors_f = open("_authors_count.json", "r")
    authors = json.loads(authors_f.read())

    authors_sorted = sorted(authors.items(), key=lambda x: x[1], reverse=True)

    for i in authors_sorted:
        print(f"{i[1]} --> {i[0]}")


def main():
    messages = get_messages(sys.argv[1])
    ALL_AUTHORS = set()
    for m in messages["chats"]:
        ALL_AUTHORS.add(m["author"])
    ALL_AUTHORS = list(ALL_AUTHORS)
    AUTHORS_DICT = {}
    for _ in ALL_AUTHORS:
        AUTHORS_DICT[_] = 0
    now_timestamp = datetime.now()
    six_months_delta = now_timestamp - timedelta(days=30 * 6)
    for message in messages["chats"]:
        if message["timestamp"] > six_months_delta:

            current_author = message["author"]
            AUTHORS_DICT[current_author] += 1

    f_authors_dict = open("_authors_count.json", "w")
    f_authors_dict.write(json.dumps(AUTHORS_DICT))
    f_authors_dict.close()

    sort_authors_by_message_count()


if __name__ == "__main__":
    main()
