p= [0 for x in range(10)]#initializing the list for storing student data
avg=[0,0,0,0,0,0]#initializing the holder for average notes for each assignment avg[0]=hw1,avg[1]=hw2 etc.
points=[0 for x in range(10)]#initializing the weighted points for each student
dictpoints={}#initializing dictionary for the names and weighted points for each student 

class Student:#making class to store things more easily 
  def __init__(self, name,hw1,hw2,hw3,hw4,midterm,final):#initializing each assignments
    self.name = name 
    self.hw1 = hw1
    self.hw2 = hw2
    self.hw3 = hw3
    self.hw4 = hw4
    self.midterm = midterm
    self.final = final
    
p[0] = Student("Jack",25,65,80,50,75,30)#initializing each student 
p[1] = Student("Maria",100,20,45,90,40,45)
p[2] = Student("Julia",85,90,70,85,90,85)
p[3] = Student("David",45,50,20,100,85,100)
p[4] = Student("Kevin",15,70,100,90,25,90)
p[5] = Student("Lisa",0,40,60,45,65,10)
p[6] = Student("Linda",60,35,5,0,15,15)
p[7] = Student("Emily",95,25,60,60,25,75)
p[8] = Student("Oliver",80,95,45,30,100,85)
p[9] = Student("Alfie",55,10,70,15,80,40)

for i in range(10):#for looping each student 0 to 9
    avg[0]+=p[i].hw1#adding each students hw1 note to the pool
    avg[1]+=p[i].hw2#adding each students hw2 note to the pool
    avg[2]+=p[i].hw3#adding each students hw3 note to the pool
    avg[3]+=p[i].hw4#adding each students hw4 note to the pool
    avg[4]+=p[i].midterm#adding each students midterm note to the pool
    avg[5]+=p[i].final#adding each students midterm note to the pool

for x in range(6):#for looping each assignment 0 to 5 
    avg[x]=avg[x]/10# getting average for each exam
    if 0<=x<4:#if x is from 0 to 3 print homeworks avg
        print("Homework",x+1, "average is",avg[x])
    if x==4:#if x is 4 print midterm avg
        print("Midterm average is ",avg[x])
    if x==5:#if x is 5 print final avg
        print("Final average is ",avg[x])
for y in range(10):#looping each student 0 to 9
    points[y]=(p[y].hw1*0.05)+(p[y].hw2*0.05)+(p[y].hw3*0.05)+(p[y].hw4*0.05)+(p[y].midterm*0.30)+(p[y].final*0.50)#calculate the weighted note
    
for a in range(10):# looping each student name and point 
    dictpoints[p[a].name]=points[a]#writing to dict
def passfailfunc(p, dictpoints):#initializing the func, func needs p list and dictpoints dictionary
    for b in range(10):#looping each student 0 to 9
        if 0<=dictpoints[p[b].name]<=29:#if student grade is between 0 and 29 print his letter number and pass situation
            print(p[b].name,"has a FF letter grade and he/she failed")
        elif 30<=dictpoints[p[b].name]<=39:#if student grade is between 30 and 39 print his letter number and pass situation
            print(p[b].name,"has a DD letter grade and he/she failed")
        elif 40<=dictpoints[p[b].name]<=49:#if student grade is between 40 and 49 print his letter number and pass situation
            print(p[b].name,"has a CC letter grade and he/she did pass")
        elif 50<=dictpoints[p[b].name]<=59:#if student grade is between 50 and 59 print his letter number and pass situation
            print(p[b].name,"has a CB letter grade and he/she did pass")
        elif 60<=dictpoints[p[b].name]<=69:#if student grade is between 60 and 69 print his letter number and pass situation
            print(p[b].name,"has a BB letter grade and he/she did pass")
        elif 70<=dictpoints[p[b].name]<=79:#if student grade is between 70 and 79 print his letter number and pass situation
            print(p[b].name,"has a BA letter grade and he/she did pass")
        elif 80<=dictpoints[p[b].name]<=100:#if student grade is between 80 and 100 print his letter number and pass situation
            print(p[b].name,"has a AA letter grade and he/she did pass")

passfailfunc(p, dictpoints)#run the function
    

    
    
    