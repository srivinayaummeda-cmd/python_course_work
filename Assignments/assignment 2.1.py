chat = []


n = int(input("How many messages? "))
print("Enter messages in format: Name: message")

for _ in range(n):
    line = input()
    if ":" in line:
        name, msg = line.split(":", 1)
        chat.append((name.strip(), msg.strip()))
    else:
        chat.append(("Unknown", line.strip()))

# Helper functions
def total_words():
    return sum(len(msg.split()) for _, msg in chat)

def user_list():
    return {name for name, _ in chat}

def messages_by(user):
    return [msg for name, msg in chat if name.lower() == user.lower()]

# Menu loop
while True:
    print("\n--- MENU ---")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Average words/message")
    print("5. Longest message")
    print("6. Most active user")
    print("7. Messages by a user")
    print("8. Show all questions")
    print("9. Deleted messages count")
    print("0. Exit")

    ch = int(input("Choice: "))

    if ch == 0:
        break

    elif ch == 1:
        print("Total messages:", len(chat))

    elif ch == 2:
        print("Users:", user_list())

    elif ch == 3:
        print("Total words:", total_words())

    elif ch == 4:
        print("Average words/message:", total_words() / len(chat))

    elif ch == 5:
        longest = max(chat, key=lambda x: len(x[1]))
        print("Longest message from:", longest[0])
        print("Message:", longest[1])

    elif ch == 6:
        count = {}
        for name, _ in chat:
            count[name] = count.get(name, 0) + 1
        most_active = max(count, key=count.get)
        print("Most active user:", most_active)

    elif ch == 7:
        u = input("Enter user name: ")
        msgs = messages_by(u)
        print("Messages:", msgs if msgs else "No messages")

    elif ch == 8:
        qs = [f"{name}: {msg}" for name, msg in chat if "?" in msg]
        print("Questions:")
        for q in qs:
            print(q)

    elif ch == 9:
        deleted = sum(1 for _, msg in chat if msg == "This message was deleted")
        print("Deleted messages:", deleted)

    else:
        print("Invalid choice")
