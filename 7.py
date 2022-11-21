# print sum of digits of a given by user 
# example : 1298   => 1+2+9+8 =20

n=input()
total=0
for i in range(0,len(n)):
    total+=int(n[i])
print(total)