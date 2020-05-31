import sys
from whatsapp_chat_parser import get_messages


def main():
    if len(sys.argv) <= 1:
        print("\t-::: parse-chat.py (for whatsapp-chat-parser) :::-")
        print("\t-::: by: Mazin Ahmed (mazin[at]mazinahmed.net) :::-")
        print("\nUsage %s [_chat.txt]\n" % (sys.argv[0]))
        sys.exit(0)

    messages = get_messages(sys.argv[1])
    print("[*] Chats:")
    for message in messages["chats"]:
        print(message)
        print("*" * 40)
    print("[*] Descriptive Messages:")
    for message in messages["descriptive_messages"]:
        print(message)
        print("*" * 40)


if __name__ == "__main__":
    main()
