import random

samplesize = input("Requested sample size")
totalconnections= 0
dataarray = [[0 for x in range(2)] for y in range(int(samplesize))] 
x=0
z=0
q=0
birthdaymatched=0
while x <100000:
	for i in range(0,int(samplesize),1):
		monthrandom =random.randrange(1,13,1)
		dataarray[i][0]= monthrandom
		daysrandom =random.randrange(1,32,1)
		dataarray[i][1]=daysrandom
	for a in range(0,int(samplesize)-1,1):
		if (birthdaymatched==1):
			break;
		z = a+1
		while z< int(samplesize):
			if (dataarray[a][0]==dataarray[z][0] and dataarray[a][1]==dataarray[z][1]):
				birthdaymatched =1
			z+=1
	if(birthdaymatched !=0):
		q+=1
	birthdaymatched =0
	x +=1	
    
print("The sample size has a possibility of  " , (q/100000)*100 ,"% To have similar birthdays")
