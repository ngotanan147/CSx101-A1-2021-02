import re
s = input()

maleWord = ['lios', 'etr', 'initis']
femaleWord = ['liala', 'etra', 'inites']


def isInMaleWord(string):
    for word in maleWord:
        if (word in string):
            # print(string.index(word), (len(string) - len(word)))
            if (string.index(word) == (len(string)) - len(word)) or (string == word):
                return maleWord.index(word)
    return -1


def isInFemaleWord(string):
    for word in femaleWord:
        if (word in string):
            # print(string.index(word), (len(string) - len(word)))
            if (string.index(word) == (len(string)) - len(word)) or (string == word):
                return femaleWord.index(word)
    return -1


def checkAvailable(string):
    if (string.strip() == ''):
        return "NO"
    string = string.strip()
    words = str(string).split()
    check = []
    order = []
    check2 = True
    for word in words:
        if (bool(re.match('^[a-zA-Z0-9]*$', word)) == False):
            return "NO"

        if (len(words) == 1):
            if (isInFemaleWord(word) == 1) or (isInMaleWord(word) == 1):
                return "YES"

        if (isInMaleWord(word) != -1) or (isInFemaleWord(word) != -1):
            check2 = True
            if (isInMaleWord(word) != -1):
                order.append(isInMaleWord(word))
                check.append('male')
            if (isInFemaleWord(word) != -1):
                order.append(isInFemaleWord(word))
                check.append('female')
        else:
            check2 = False

        if (check2 == False):
            return "NO"
        if (len(list(dict.fromkeys(check))) > 1):
            return "NO"
        if (len(check) == 0):
            return "NO"
    if (order.count(1) != 1):
        return "NO"
    if (order != sorted(order)):
        return "NO"
    return "YES"


print(checkAvailable(s))
# if set('đetra').difference(printable):
#     print('Text has special characters.')
# else:
#     print("Text hasn't special characters.")
