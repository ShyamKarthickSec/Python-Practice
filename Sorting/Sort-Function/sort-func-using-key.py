def keyFun(s):
    return len(s)

s = ['apple', 'banana', 'kiwi', 'cherry', 'blueberry']
s.sort(key=keyFun)
print(s)
s.sort(key=keyFun, reverse=True)
print(s)