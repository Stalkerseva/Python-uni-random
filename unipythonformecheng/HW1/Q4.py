xa=[0,1,2,-3,-6,200,-9]# listing all x values 

def func1(x):#making a function to find y 
    y=(pow(x,3)-3*x+12)
    return y #returning the number 

for x in range(len(xa)):# making a loop for all x list numbers       
    print(func1(xa[x]),end= " ")#printing the y value without new line 
    a=0#checking whatever there is undefined result 
    if (func1(xa[x])==-690):#checking whatever is y is -690
        print("y equals to",func1(xa[x],))#if it is print it 
        a=1#no undefined result 
    if (func1(xa[x])>0):#checking whatever is y is positive 
        print("y is positive")#if it is print it
        a=1#no undefined result
    if (func1(xa[x])<0 and func1(xa[x])!=-690 ):#checking whatever is y is  negative and not -690
        print("y is negative")#if it is print it
        a=1#no undefined result
    if (a==0):#if a is 0 thus undefined result
        print("undefined result for y")#if it is print it