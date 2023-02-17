file=open("datos.txt","r")
last=file.readlines()[-1]
list=last.split(" ")
pr=1
for i in list:
    pr*=int(i)
print(pr)
