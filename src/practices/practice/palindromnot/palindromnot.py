def transform_palindrom(pal):
    countMap = {}
    for c in pal:
        countVal = 0
        try:
            countVal = countMap[c]
        except KeyError:
            pass
        countVal += 1
        countMap[c] = countVal

    resultString = ""
    for key in countMap.keys():
        resultString += key*countMap[key]
    return resultString


if __name__ == '__main__':
    pal = input()
    tr_pal = transform_palindrom(pal)
    print(tr_pal)
