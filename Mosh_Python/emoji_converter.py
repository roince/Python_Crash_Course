def emoji_coverter(sentence):
    words = sentence.split()
    emojis = {
        ":)": "😀",
        ":(": "😞",
        ":P": "😛",
        ":D": "😁",
        "LOL": "🤣"
    }

    output = ""
    for word in words:
        output += emojis.get(word.upper(), word) + " "
    return output


print(emoji_coverter(input("> ")))
