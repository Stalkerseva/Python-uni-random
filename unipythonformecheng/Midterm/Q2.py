A=[1, 6, -6, 32, 7, "exam", 0.01]#initializing the first list 
B=[8, 78, 4, 6, "exam", 4, 0.1]#initializing the second list 

for x in range(len(A)):#looping all of the first loop
    for y in range(len(B)):# looping all of the second loop
        if A[x]==B[y]: #if there is match 
            print(A[x])#print the match