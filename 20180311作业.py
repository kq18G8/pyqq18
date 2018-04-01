#di 3 shou di 6 ge yinfu dayin
f=open("my123.txt","r")
my123=f.read()
data=my123.split("\n")
data_list=[]
for D in data:
    data_list.append(D.split(","))
print(data_list[3][6])
