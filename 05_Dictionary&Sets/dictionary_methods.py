Marks = {
    "Pranali" : 100,
    "Sam" : 27,
    "Jerry" : 82,
    "Tom" : 37,
}
print(Marks.items())
print(Marks.keys())
print(Marks.values())
Marks.update({"Tom" : 88})
print(Marks.items())
print(Marks.get("Bob"))
print(Marks.get("Tom"))
print(Marks["Tom"])