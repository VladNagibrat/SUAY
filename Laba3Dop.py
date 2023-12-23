print("\u001b[35m")
while True:
    try:
        Z=input()
        break
    except:
        Z='^Z'
        break
B=Z.split()
count=0
while True:
    try:
        M=input()
        break
    except:
        M='^Z'
        break
if M=='':

p=len(M)
for elem in B:
    count+=1
for i in range(count):
    Z = B[i]
    if len(Z) > 0 and len(Z)>=p:
        C=-1
        F=1
        for i in range(0,p):
            if Z[C]==M[C]:
                F=F
            else:
                F=0
            C-=1
        if F==1:
            print(Z)