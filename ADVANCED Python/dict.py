# dict is unorderd , mutable Key-value pairs 

mydict = {"name":"eslam","age":19}

mydict["mm"+"eslam"]="hi"
print(mydict)

newdict = {}
for i in range(len(mydict)):
    for key, value in mydict.items():
        try:
            newdict[key]="new "+value
        except:
            newdict[key]=value
print(newdict)

