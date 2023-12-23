Z=input('Input English string:')
B=Z.split()
count=0



A=['N']*800
b=0
C=('E','Y','U','I','O','A','e','y','u','i','o','a','У','Е','А','О','Я','И','Ы','Ю','Э','э','у','е','ы','а','о','я','и','ю')
for i in range(ord('A'),ord('Z')):
    if chr(i) in C:
        b+=1
    else:
        A[b]=chr(i)
        b+=1
for i in range(ord('a'),ord('z')):
    if chr(i) in C:
        b+=1
    else:
        A[b]=chr(i)
        b+=1
for i in range(ord('А'),ord('Я')):
    if chr(i) in C:
        b+=1
    else:
        A[b]=chr(i)
        b+=1
for i in range(ord('а'),ord('я')):
    if chr(i) in C:
        b+=1
    else:
        A[b]=chr(i)
        b+=1



for elem in B:
    count+=1
for i in range(count):
    Z = B[i]
    if len(Z) > 0:
        if Z[-1] in A:
            print(Z)