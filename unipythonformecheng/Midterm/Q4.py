import math# import maths
P_1=7 #kn
q1=2 #kn/m
M_1=19#kn.m
L_1,L_2,L_3=1.8,0.6,0.6#each partition length
P_1x=7*math.cos(math.radians(45))#finding the x part of P force 
P_1y=7*math.sin(math.radians(45))#finding the y part of P force 
F_x=0# all of the x forces should add up to 0
#x axis is positive on right y axis is positive on up
#F_x=H_a+P_1y 
H_a=F_x-P_1y #finding the H_a
F_y=0# all of the y forces should add up to 0
#F_y=R_a-P_1y-(q1*L_1)
R_a=F_y+P_1y+(q1*L_1)#finding R_a
M_atotal=0#the total moment should be 0
#M_atotal=M_a+(q1*1.8)/2-M_1+P_1y*3
M_a=M_atotal-q1*(pow(L_1,2)/2)+M_1-P_1y*3#finding the M_a
print("H_a is",H_a,"kN")#printing the result
print("R_a is",R_a,"kN")#printing the result
print("M_a is",M_a,"kNm")#printing the result
""" 1 sheer area extremes """
#F_k1=R_a-q1*z_1 F_k=0
z_1extreme=(R_a-0)/q1#since there is one up force and one down there is possible one extreme
""" 1 moment area"""
z_1=0#initializing variable
M_x11=M_a+(R_a*z_1)-(q1*pow(z_1,2))/2#calculating the 0 point
print(M_x11,"kNm")#printing the result
M_x1extreme=M_a+(R_a*z_1extreme)-(q1*pow(z_1extreme,2))/2#calculating the extreme point
print(M_x1extreme,"kNm")#printing the result
z_1=L_1#changing the variable
M_x12=M_a+(R_a*z_1)-(q1*pow(z_1,2))/2#calculating the 1.8 point
print(M_x12,"kNm")#printing the result
"""2 sheer area extremes """
#since there is no f change there is no extremes
""" 2 moment area"""
z_2=0#initializing variable
M_x21=M_a+(R_a*(L_1+z_2))-(q1*L_1*((L_1/2)+z_2))#calculating the 1.8 point
print(M_x21,"kNm")#printing the result
z_2=L_2#changing the variable
M_x22=M_a+(R_a*(L_1+z_2))-(q1*L_1*((L_1/2)+z_2))#calculating the 2.4 point
print(M_x22,"kNm")#printing the result
"""3 sheer area extremes """
#since there is no f change there is no extremes
""" 3 moment area"""
z_3=0#initializing variable
M_x31=M_a-M_1+(R_a*(L_1+z_2+z_3))-(q1*L_1*((L_1/2)+z_2+z_3))#calculating the 2.4 point
print(M_x31,"kNm")#printing the result
z_3=L_3#changing the variable
M_x32=M_a-M_1+(R_a*(L_1+z_2+z_3))-(q1*L_1*((L_1/2)+z_2+z_3))#calculating the 3 point
print(M_x32,"kNm")#printing the result
print("The maximum bending moment is ",M_x1extreme,"kNm")#printing the maximum moment

