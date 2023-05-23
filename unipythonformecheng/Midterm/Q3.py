import math#importing math for pow etc
b=0.955 #m
V_h=3.14 #litre
ρ_w=1000 #kg/m3
ρ_fuel=840 #kg/m3
ρ_Hg=13600 #kg/m3
R_air=0.287 #kJ/kgK
c_w=4.20 #kJ/kgK
c_exh=1.09 #kJ/kgK
d_orifice=11.70 #mm
α_orifice=0.63 #-
H_u= 43200#KJ/kg
AFratio =14.5 #kg air/kg fuel
g=9.81#m/s2
TP=[0,0,0,0]#initializing the holder for test points
P_e,m_fuel=[0,0,0,0],[0,0,0,0]#initializing the holders
ρ_air,m_air,m_exh,m_water,Qtotal,Qe,Qwater,Qexh,Qfriction,ratioe,ratiowater,ratioexh,ratiofriction=[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)],[0 for x in range(4)]#initializing the holders
class Testpoints:#making class to store things more easily 
  def __init__(self, n,F,V_fuel,deltat_fuel,V_air,deltat_air,exgasT,coolingwaterF,inflowwaterT,outflowwaterT,atmoP,ambiairT):#initializing each variable
    self.n = n
    self.F = F
    self.V_fuel = V_fuel
    self.deltat_fuel = deltat_fuel
    self.V_air = V_air
    self.deltat_air = deltat_air
    self.exgasT = exgasT
    self.coolingwaterF = coolingwaterF
    self.inflowwaterT = inflowwaterT
    self.outflowwaterT = outflowwaterT
    self.atmoP = atmoP
    self.ambiairT = ambiairT
    
TP[0]=Testpoints(1750,205,50,17.5,2,49.4,576.4,179,81.9,89.8,1020,25)#writing test points variables 
TP[1]=Testpoints(2100,175,50,15.7,2,43.04,575,190,81,88,1020,26)
TP[2]=Testpoints(1900,180,50,16.61,2,47.64,580,180,83,89,1020,26.5)
TP[3]=Testpoints(1700,205,50,17.98,2,51.63,573,185,80,90,1020,27)

def m_fuelfunc(ρ_fuel,TP):#creating the function
    for i in range(4):#looping 4 times
        m_fuel[i]=(ρ_fuel*((TP[i].V_fuel)/1000000))/TP[i].deltat_fuel#calculating the fuel amount (cm3->to m3)

def torquefunc(TP,b):#creating the function
    for i in range(4):#looping 4 times
        T_e=(TP[i].F)*b#calculating the torque amount
        print("TP",i+1,"'s effective Torque=",T_e,"Nm")#printing the result

def effectivepowerfunc(TP):#creating the function
    for i in range(4):#looping 4 times
        P_e[i]=(TP[i].F*TP[i].n)/10000#calculating the effective power
        print("TP",i+1,"'s effective Power=",P_e[i],"kW")#printing the result
def brakemeanPfunc(TP,P_e,V_h):#creating the function
    for i in range(4):#looping 4 times
        bmep=(120*P_e[i])/(TP[i].n*V_h) #calculating the break mean effective pressure
        print("TP",i+1,"'s effective mean Pressure=",bmep,"bar")#printing the result

def brakespecificfuelfunc(m_fuel,P_e):#creating the function
    for i in range(4):#looping 4 times
        bsfc=(m_fuel[i]*3600)/P_e[i]#calculating the brake specific fuel
        print("TP",i+1,"'s effective brake specific fuel consumption=",bsfc,"g/kWh")#printing the result
    
    
def volumetricefffunc(TP,V_h):#creating the function
    for i in range(4):#looping 4 times
        n_v=(TP[i].V_air*120)/(V_h*TP[i].deltat_air*TP[i].n)#calculating the volumetric efficiency
        print("TP",i+1,"'s volumetric efficiency=",n_v)#printing the result
def m_airfunc(TP,R_air):#creating the function
    for i in range(4):#looping 4 times
        ρ_air[i]=(0.1*TP[i].atmoP)/(R_air*(TP[i].ambiairT+273))#calculating the density of air
        m_air[i]=(ρ_air[i]*TP[i].V_air)/TP[i].deltat_air#calculating the mass of air
def m_exhfunc(m_air,m_fuel):#creating the function
    for i in range(4):#looping 4 times
        m_exh[i]=m_air[i]+m_fuel[i]#calculating the mass of exhaust
def m_waterfunc(ρ_w,d_orifice,α_orifice,TP,ρ_Hg,g):#creating the function
    for i in range(4): #looping 4 times
        m_water[i]=ρ_w*math.pi*((pow(d_orifice*0.001,2))/4)*α_orifice*pow(2*g*(TP[i].coolingwaterF/1000)*(ρ_Hg-ρ_w)/(ρ_w),0.5)#calculating the mass of water
def Q_functions(H_u,TP,P_e,m_water,c_w,m_exh,c_exh):#creating the function
    for i in range(4):#looping 4 times
        Qtotal[i]=m_fuel[i]*H_u#finding the Total chemical heat of fuel h_u is !!!!!43200!!!!!
        Qe[i]=P_e[i]#calculating the effective power
        Qwater[i]=m_water[i]*c_w*(TP[i].outflowwaterT-TP[i].inflowwaterT)#calculating the rejected to cooling
        Qexh[i]=m_exh[i]*c_exh*(TP[i].exgasT-TP[i].ambiairT)#calculating the rejected to exhaust
        Qfriction[i]=Qtotal[i]-(Qe[i]+Qwater[i]+Qexh[i])#calculating the rejected to overall friction
        
def Q_ratiosfunc(Qe,Qfriction,Qtotal,Qwater,Qexh):#creating the function
    for i in range(4):#looping 4 times
        ratioe[i]=(Qe[i]/Qtotal[i])*100#calculating heat balance in proportions of heat for power
        ratiowater[i]=(Qwater[i]/Qtotal[i])*100#calculating the heat balance in propotions of heat rejected to cooling
        ratioexh[i]=(Qexh[i]/Qtotal[i])*100#calculating heat balance in proportions of heat rejected to exhaust
        ratiofriction[i]=(Qfriction[i]/Qtotal[i])*100#calculating heat balance in proportions of heat rejected to overall friction
        ratiosss=[ratioe[i],ratiowater[i],ratioexh[i],ratiofriction[i]]#creating a list to store ratios
        print("TP",i+1,sorted(ratiosss))#ordering ratios and printing ordered ratios
        
torquefunc(TP,b)#running the func with TP class and b parameter
effectivepowerfunc(TP)#running the func with TP class
brakemeanPfunc(TP,P_e,V_h)#running the func with TP class,P_e list and V_h parameter
m_fuelfunc(ρ_fuel,TP)#running the func with TP class,and ρ_fuel list 
brakespecificfuelfunc(m_fuel,P_e)#running the func with m_fuel list and p_e list
volumetricefffunc(TP,V_h)#running the func with TP class and V_h variable
m_airfunc(TP,R_air)#running the func with TP class and R_air variable
m_exhfunc(m_air,m_fuel)#running the func with m_air and m_fuel lists
m_waterfunc(ρ_w,d_orifice,α_orifice,TP,ρ_Hg,g)#running the func with TP class,ρ_w,d_orifice,α_orifice,ρ_Hg and g variables
Q_functions(H_u,TP,P_e,m_water,c_w,m_exh,c_exh)#running the func with TP class,p_e,m_water,m_exh lists and H_u,c_w and c_exh variables
Q_ratiosfunc(Qe,Qfriction,Qtotal,Qwater,Qexh)#running the func with Q lists 


