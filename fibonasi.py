# n=int(input("Enter no:"))
n=10
f=0
s=1
print(f,s,end=" ")
for i in range(n):
    t=f+s
    print(t,end=" ")
    f=s
    s=t
print("")
print("==============")
f=0
s=1
for i in range(10):
    print(f,end=" ")
    t=f+s
    f=s
    s=t