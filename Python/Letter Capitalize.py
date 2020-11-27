str = "h3llo yo people"

def LetterCapitalize(str):
    splitted = str.split(' ')
    words = [i.capitalize() for i in splitted]
    return words

print(LetterCapitalize(str))
