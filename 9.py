def repeated(text):

    text = ''.join(char.lower() if char.isalnum() else ' ' for char in text)
    words = text.split()

    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    repeated = max(count, key=count.get)
    return repeated, count[repeated]

text = "Hello How are you brother? I am fine brother!! What about u brother and how is ur brother?"
print(repeated(text))  
