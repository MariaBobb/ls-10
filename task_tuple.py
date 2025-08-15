



# словарь

d = {}
d = dict()

print(type(d))


d = {
    
    "один": 1,
    "два": 2,
    'три': 3
}

print(d)
print(d["один"])
print(d[1])


s = "один два два один три" .split() # [ 1 2 2 1 3]
res = [d[x]for word in s] # в одну строку
#for word in s:
    # print( word, d[word])
    # res.append(d[word])
print(res)
print(sum(res))

