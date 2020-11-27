str = "hello worldz"

def LetterChanges(str):
    newStr = ''

    for i in str:
        if i.isalpha():
            if i.lower() == 'z':
                i = 'a'
            else:
                i = chr(ord(i) + 1)
        if i in 'aeiou':
            i = i.upper()

        newStr += i
    return newStr

print(LetterChanges(str))
