# editable array with add and remove methods

x ="eslam"
m=list(x)
print(m)

mylist = ["eslam","yasser","fathy"]
print(mylist)

mylist.append([(i for i in range(0,2)),2,3])
print(mylist)

mylist.insert(0,"Eng")
print(mylist)

mylist.remove("fathy")
print(mylist)

mylist.pop()
print(mylist)

mylist.clear()
print(mylist)
print(list(i for i in range(0,2) if i <3))