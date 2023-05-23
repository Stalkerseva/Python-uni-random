import random 
print("Try to guess the 3 digit number!")
lefttries = 10
namenumber1 =random.randrange(100,999,1)
#print(namenumber1)
res = list(map(int, str(namenumber1)))
#print(res)
fermicount = 0
while lefttries>0:
    
    
    guessinput =input("Input your number")
    guessList = list(guessinput)
    for y in range(3):
        
        z=0
        for x in range(3):
          #print(guessList[y])
          #print(res[x])
          if int(guessList[y]) == int(res[x]):
              if(x == y):
                  print("Fermi")
                  z=2
                  fermicount +=1
                  
              else:
                  if(z!=2):
                      z =1
        if(z==1):
          print("Pico")                
        if(z ==0):
          print("Bagels")
          
    if(fermicount ==3):
          print("You win!")
          break    
    fermicount=0      
    lefttries -= 1
     

if(lefttries ==0):
    print("You lose!")
