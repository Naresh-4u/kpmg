def getKey(obj: dict):
    keys = list(obj)
    if len(keys) != 1:
        raise Exception('The entered Key is not in the expected format')
    else:
        return keys[0]


def getNestedValue(obj: dict, key: str, isFound = False):
    if type(obj) is not dict and not isFound:
        return None
    if (isFound or (key in obj.keys())) :
        if type(obj[key]) is dict:
            return getNestedValue(obj[key], getKey(obj[key]), True)
        else:
            return obj[getKey(obj)]
    else:
        nestedKey = getKey(obj)
        return getNestedValue(obj[nestedKey], key, False)

if __name__ == '__main__':
    obj = {'x': {'y': {'c': 'a'}}}
    value = getNestedValue(obj, 'y')
    print(value)
