X = int(input())                                       
shoe_sizes = input().split()                            
N = int(input())                                       
wanted =[]
price =0
for i in range(N):
    key, value = input().split()
    dic = {key: value}
    wanted.append(dic)
print(wanted)                                          

for i in range(N):
    for ele in wanted:
        if list(ele.keys())[0] in shoe_sizes:
            shoe_sizes.remove(list(ele.keys())[0])
            print(shoe_sizes)
            price += int(list(ele.values())[0])
            print(price)
            
print(price)
