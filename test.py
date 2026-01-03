def intermilan():
    yield "apple"
    yield "banana"
    yield "cherry"

# mylist = iter(["apple", "banana", "cherry"])
mylist = intermilan()
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)