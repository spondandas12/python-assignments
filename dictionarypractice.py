#assignment 3
d = {"q": 2 , "a" : 5}
print(d['q'])
d["k"] = 9  #addition of key
print(d)
d["q"] = 5   #update
print(d)
d.pop("a")    #delete
print(d)
x = {"c": 5, "l": "30"}
print(d|x)
del x["l"]
print(x)
x.clear()
print(x)
