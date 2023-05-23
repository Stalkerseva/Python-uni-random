i=20000#defining the top number 
primecounter=0#prime counter
cumsum=0#the sum of prime numbers

def primecalc(x):#function to check the number for being prime
    
    if x==1 or x==0:#if x=1 or 0 return not prime
        return 1#not prime(1)
    for i in range(2,x):#in range of every number before it divide it if it divisable then it is not prime number
        if (x % i) == 0:#if remainder is 0 from division 
            return 1#return not prime
    else: #if there is no division thus no return 1 return prime instead(2)
        return 2#prime
               
def primenumberfunc(x,z,b):#recursive function (x is number,z is prime number count,b is the sum of numbers)
    
    if x ==0 or x<0:#if x is 0 or x is negative finish the loop of the function 
        print("The amount of prime numbers is ",z,)#printing the prime number count
        print("the cum sum is ",b,)#printing the sum of numbers
        return#finish the loop
    if x>=1000:#if x is bigger than 1000 do the calculation in the loop 1000 times
    #The reason for this is to avoid  recursion loop cap in python 
        for a in range(x-999,x+1):#looping numbers from x-999 to x+1 e.g if number is 2256 loop from 1257 to 2256 next loop loop from 257 to 1256
            if primecalc(a)!=1:#if prime number 
                b+=a#sum with the all prime numbers
                z+=1#add 1 to prime count 
    if x<1000:# if x is smaller than 1000 do the calculation 1 by one 
        if primecalc(x)!=1:#if prime number
            b+=x#sum with the all prime numbers
            z+=1#add 1 to prime count 
        
    if x>=1000:# if x is bigger than 1000 to avoid cap use x-1000 with recursion function
        primenumberfunc(x-1000,z,b)#recursion loop 
    if x<1000:# if x is smaller than 1000 use x- with tge recursion function
        primenumberfunc(x-1,z,b)#recursion loop 
        
primenumberfunc(i,primecounter,cumsum)#calling the cunction

