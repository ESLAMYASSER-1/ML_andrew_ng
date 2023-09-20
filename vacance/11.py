n= 5 
width = (2*n-1)+(2*n-2)
lst=[]
def centerWithDash(string,width):
    return string.center(width,"-")


for row in range(1,5):
    for i in range((int((2*n-1)/2))+1):
        # print(chr(96+n-i) ,end="")
        if chr(96+n-i) not in lst:
            lst.append(chr(96+n-i))

x=n

for i in range(1,len(lst)+1):
    # for x in range(1,n-i):
    # print(lst[i-1].center(width,"-"))
    m=0
    for x in range(i):
        new_lst=lst[:i]
        new_lst.reverse()
        # print(new_lst)
        line=new_lst[0]
        #  print(line)
        while m <=x:
            line=line.center(len(line),"-")
            try:
                line+=line.center(len(line),new_lst[2])
            except Exception as e:
                print(e, x)
            m+=1
    print(line)

