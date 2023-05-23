import random#importing random module
w,h= 6, 200 #defining width and height of matrix which going to store exam success and grades 
examperc=[[50,120,170,200],[40,110,160,200],[40,100,150,200]]#defining a matrix for the success rates         
matrix = [[0 for x in range(w)] for y in range(h)]#defining the multidimensional matrix
randomnumbers1=random.sample(range(200),200)#randomising the numbers
randomnumbers2=random.sample(range(200),200)
randomnumbers3=random.sample(range(200),200)

def standartdev():#function for the standart deviation
    add=[[0,0,0],[0,0,0],[0,0,0]]#defining a matrix for the less clutter([k][0] index is sum of the numbers,[k][1] index is for each exams mean,[k][2]is for each exams standart deviation ) 
    c=1#defining a variable to get the grades from the matrix 
    for k in range(3):#making for loop for the 3 exams
        sum1=0#defining a variable for the standart deviation(sum part)
        for y in range(200):#looping all the numbers in the matrix 
            add[k][0]=matrix[y][c]+add[k][0]#summing the numbers at [][0] index
           
        add[k][1]=add[k][0]/200#getting the mean for each exam
        for a in range(200):# looping all the numbers for sum part of deviation 
            sum1=(matrix[a][c]-add[k][1])**2#summing 
            
        add[k][2]=(sum1/200)**0.5#finding the standart deviation 
        c=c+2#adding the number for applying next exam scores    
    return print("1 exam standart deviation is",add[0][2],"\n2 exam standart deviation is",add[1][2],"\n3 exam standart deviation is",add[2][2])#printing the results     
def avrgstudent():#function for the average grade of each student 
    for x in range(200):#making loop for each student 
        sum2,avrg=0,0#defining the sum of each particular students grades 
        for y in range(1,7,2):#making a loop for each particular exam 
            sum2=matrix[x][y]+sum2#summing
        avrg=sum2/3#getting the average of exams    
        
        print(x+1,"Student average ",avrg)#printing the result         
    
y=0#defining the  index in matrix for success rates 0 is 1 exam,2 is 2 exam,4 is 3 exam
for x in range(3):#making a loop for each exam success rate
    
    for z in range(200):#loop for all random selected  students 
        if z<examperc[x][0]:#if z is smaller than first percentage make it 4 
            matrix[randomnumbers1[z]][y]=4#assigning 4(Upper-intermedia) for random selected students 
        if examperc[x][0]<=z<examperc[x][1]:#same thing as first one but now between them 
            matrix[randomnumbers1[z]][y]=3#assigning 3(Intermedia) for random selected students
        if examperc[x][1]<=z<examperc[x][2]:
            matrix[randomnumbers1[z]][y]=2 #assigning 2(Conditional pass) for random selected students
        if examperc[x][2]<=z<examperc[x][3]:
            matrix[randomnumbers1[z]][y]=1#assigning 1(Failed) for random selected students
    y+=2# making other index take the next exam success rates 
z=0#defining the index for success rates 

for x in range(3):#looping for the 3 exams
    
    for y in range(200):#looping for all the students 
        if matrix[y][z] ==4:#if success rate is 4 
            matrix[y][z+1]=random.randint(75, 100)# the index after it e.g(0==4,1=random number between 75-100)
        if matrix[y][z] ==3:#if success rate is 3
            matrix[y][z+1]=random.randint(51, 74)#randomising for the accurate success rate 
        if matrix[y][z] ==2:#if success rate is 2
            matrix[y][z+1]=random.randint(45, 50)#randomising for the accurate success rate 
        if matrix[y][z] ==1:#if success rate is 1 
            matrix[y][z+1]=random.randint(0, 44)#randomising for the accurate success rate 
    z=z+2#making next exams success rate into loop

standartdev()#calling standart deviation function
avrgstudent()#calling average grade for students function