import json

test = json.loads(open('input').readline())

def addNumbers(data):

    total = 0
    #print data
    if getattr(data, '__iter__', False):
        if isinstance(data, dict):
            for key, value in data.iteritems():
                try:
                    total += key
                except TypeError:
                    pass
                total += addNumbers(value)
        else:
            for e in data:
                total += addNumbers(e)
    else:
        try:
            total += data
        except TypeError:
            pass



    return total

print addNumbers(test)
