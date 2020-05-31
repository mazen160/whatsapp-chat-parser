# whatsapp-chat-parser

## A module to parse WhatsApp chats


# Use-Cases?

- Analysis of WhatsApp messages for different domain-specific motives.
- Processing WhatsApp messages.
- Having an interface for reading raw WhatsApp chat exports.

# Usage

### Installing module

```shell
python3 setup.py install
```

### Running the module

```python
from whatsapp_chat_parser import get_messages
messages = get_messages("chat.txt")
for message in messages["chats"]:
  print(message["author"])
  print(message["message"])
  print(message["timestamp"])

for descriptive_message in messages["descriptive_messages"]:
  print(descriptive_message)
```

# API

```python
>>> messages = whatsapp_chat_parser.get_messages("chat.txt")
>>> messages["chats"]  # Chats, ordered by timestamp.
>>> for message in messages["chats"]:
>>>   message["chats"]["timestamp"] # Timestamp in datetime
>>>   message["chats"]["original_date"] # Original timestamp
>>>   message["chats"]["message"] # Message
>>>   message["chats"]["Author"] # Author
>>> message["descriptive_messages"]  # List of descriptive messages that was sent by WhatsApp, ordered by timestamp.
```

# Examples
The `./examples` directory has CLI examples.

```python
$ python parse_chat.py
-::: parse-chat.py (for whatsapp-chat-parser) :::-
-::: by: Mazin Ahmed (mazin[at]mazinahmed.net) :::-

Usage parse_chat.py [_chat.txt]
```

```python
$ python get_author_count.py
25000 --> X
30 --> Y
1 --> Z
```

# Exporting Chats

Exporting chats is done from the WhatsApp app. You can follow WhatsApp documentation for the details.

[https://faq.whatsapp.com/en/android/23756533/](https://faq.whatsapp.com/en/android/23756533/).


# Requirements

- Python 3


# License
The project is licensed under MIT License.


# Author
*Mazin Ahmed*
* Website: [https://mazinahmed.net](https://mazinahmed.net)
* Email: *mazin [at] mazinahmed [dot] net*
* Twitter: [https://twitter.com/mazen160](https://twitter.com/mazen160)
* Linkedin: [http://linkedin.com/in/infosecmazinahmed](http://linkedin.com/in/infosecmazinahmed)
