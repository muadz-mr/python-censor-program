watchWords = ["apple", "head", "example", "bend"]

message = input("What do you want to say? : ")

for word in watchWords:
    censoredWord = "*"*len(word)

    if word in message:
        msgWord = word
        approvedMessage = message.replace(msgWord, censoredWord)
        message = approvedMessage

print(message)