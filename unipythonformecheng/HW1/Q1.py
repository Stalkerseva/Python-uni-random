name=input("Input your Name ")#Inputs by user (name input)
sname=input("Input your Surname ")#Inputs by user (surname input)
num=input("Input your Student Number ")#Inputs by user (student number  input)
print('Hello' ,name, sname, 'Your student number is ',num,)#Printing the inputs on screen
num = int(num)#Making python understand that (num) is not a string but a integer 

if(num%2==0):#finding the reminder of division by 2 thus finding if it is even or not
    print("Your student number is even")#even
else:
    print("Your student number is odd")#odd

    
lname=list(name)#converting name input to the list
lsname=list(sname)#converting surname input to the list 
vowels= ["a", "e", "ı", "i", "o", "ö", "u", "ü","A","E","I","İ","O","Ö","U","Ü"]#making a vowels list 
countername=0#creating this variable for tracking vowels in the name  
countersname=0#creating this variable for tracking vowels in the surname  
print(len(lname))
for x in range(len(lname)):#making a loop for every names letter eg. seva has 4 letters with range function x gonna be 0,1,2,3 respectively 
    for y in range(len(vowels)):#same thing in first function but for vowels to check every vowel with a letter from name
        if lname[x]==vowels[y]:#checking every name letter to see if it is vowel
            countername+=1 #if it is vowel add 1
for x in range(len(lsname)): #same operation but for surname
    for y in range(len(vowels)):
        if lsname[x]==vowels[y]:
            countersname+=1            
    
print("Your name has ",countername,"vowels and ",len(lname)-countername,"constants!")#printing the end vowel count and constant count for name 
print("Your name has ",countersname,"vowels and ",len(lsname)-countersname,"constants!")#printing the end vowel count and constant count for surname     
  
        
    
       


