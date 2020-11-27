sen = "fun&!! time"
sen1 = "I love dogs"
sen2 = "a confusing /:sentence:/[ this is not!!!!!!!~"
sen3 = '123456789 98765432'

import re

def LongestWord(sen):
    counter = 0
    idx = 0
    splitted = sen.split(' ')
    splitted =[''.join(re.findall('[a-zA-Z0-9]', x)) for x in splitted]

    for i, n in enumerate(splitted):
        if len(n) > counter and len(n) != counter:
            counter = len(n)
            idx = i
    return splitted[idx]


print(LongestWord(sen3))
