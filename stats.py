def count_words(text):
    words = text.split()
    return len(words)
def count_char(text):
    end_results = {}
    for char in text:
        lowercase_char = char.lower()
        if lowercase_char not in end_results:
            end_results[lowercase_char] = 1
        else:
            end_results[lowercase_char] += 1
    return end_results
def sort_char(char_dict):
    end_results = []
    for key in char_dict:
        if key.isalpha():
            end_results.append({"char": key, "num": char_dict[key]})
    end_results.sort(reverse=True, key=lambda item: item["num"])
    return end_results