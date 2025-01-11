# 
def merge(w1, w2):
    m = ""
    minLen = min(len(w1), len(w2))
    for i in range(minLen):
        m += w1[i]
        m += w2[i]
    m += w1[minLen:]
    m += w2[minLen:]
    return m


print(merge('Hello', 'World'))
print(merge('World', "Hello"))