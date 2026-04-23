spam_words = ["free", "win", "offer", "click", "money", "prize", "urgent"]

message = input("Enter a message: ").lower()

is_spam = False

for word in spam_words:
    if word in message:
        is_spam = True
        break

if is_spam:
    print("This message looks like SPAM!")
else:
    print("This message looks SAFE.")