
Blocks=[{
    "gym":False,
    "school":True,
    "store":False
},{
    "gym":True,
    "school":False,
    "store":False
},{
    "gym":True,
    "school":True,
    "store":False
},{
    "gym":False,
    "school":True,
    "store":False
},{
    "gym":False,
    "school":True,
    "store":True
}]

Reqs=["gym","school","store"]

x=0
arr =[]
iarr=[]
for i in range(len(Blocks)):
    Block=Blocks[i]
    if(i==0):
        BBlock={"gym":False,
                "school":False,
                "store":False}
    else:BBlock=Blocks[i-1]
    try:
        NBlock=Blocks[i+1]
    except:
        NBlock={"gym":False,
                "school":False,
                "store":False}
    for key in Block.keys():
        if(Block[key] or BBlock[key] or NBlock[key]):
            pass
        else:
            x+=1
        if key==Reqs[0]:
            f=0
        elif key==Reqs[1]:
            f=1
        elif key==Reqs[2]:
            f=2
        iarr.insert(f,x)
        x=0
    arr.insert(i,iarr)
    iarr=[]

newarr=[]
print(arr)
for i in range(len(arr)):
    distance=sum(arr[i])
    newarr.append(distance)

min =min(newarr)
for i in range(len(arr)):
    if(newarr[i]==min):
        minindex=i+1
print("number of the nearest block is: "+ str(minindex))