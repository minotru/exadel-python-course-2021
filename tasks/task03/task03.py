import string

texts = [
    "Hello, World!",
    "The world is mine",
    "Hello, how are you?"
]

def create_statistics(strings):
    result = {}
    for index, _string in enumerate(strings):
        words = _string.lower().translate(str.maketrans(dict.fromkeys(string.punctuation))).split()
        for word in words:            
            if word in result.keys():
                result[word]["count"] += 1
            else:
                result[word] = {"word": word, "count": 1, "first_line": index}
    return result.values()

def print_line(info):
    print('\t'.join(info))

def print_statistics(items):
    print_line(["word", "count", "first line"])
    for item in items:
        print_line([item["word"], str(item["count"]), str(item["first_line"])])    

print_statistics(create_statistics(texts))
