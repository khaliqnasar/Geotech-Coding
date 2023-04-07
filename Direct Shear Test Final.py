n=1
NSlist=[]
SSlist=[]
while n>0:

    
    #Calculating the Shear Strength Parameters from Direct Shear Data
    Mass=float(input("Enter the applied normal load in kg:"))
    Area=float(input("Enter the sample area in metres square:"))
    PRC=float(input("Enter the proving ring constant of your apparatus in Kg/div:"))
    #Inserting the values of Horizental Dial Reading
    print("Entering the values of Horizental Dial Reading")

    user_input = input("Enter a list of values for Horizental dial separated by commas: ")
    Horz_dial = [float(val) for val in user_input.split(',')]

    #Entering the Values of Proving Ring, enter "ver" when the values are complete
    print("Entering the values of Proving Ring Reading")

    PR_Values = input("Enter a list of values for Proving Ring load readings separated by commas: ")
    PR_dial = [float(val) for val in PR_Values.split(',')]
    
    #Entering the Values of Vertial dial, enter "ver" when the values are complete
    print("Entering the values of Verical Dial Reading")   

    V_Values = input("Enter a list of values for Vertical dial separated by commas: ")
    Ver_dial = [float(val) for val in V_Values.split(',')]
    
    
    #Calculating the necessary Steps
    PRC_new=(PRC*9.8)/1000
    Normal_Stress=(Mass*9.8*10)/(Area*1000)
    NSlist.append(Normal_Stress)
    #Calculating the Horizental Deformation
    Horz_def=[]
    for i in Horz_dial:
        Horz_def.append(round(i*0.01,3))
 
    #Calculating the Vertical Deformation
    Vert_def=[]
    for i in Ver_dial:
        Vert_def.append(round(i*0.01,3))
    #Calculating the Shear Force
    Shear_Force=[]
    for i in PR_dial:
        Shear_Force.append(round(i*PRC_new,3))
    #Calculating Shear Stress
    Shear_Stress=[]
    for i in Shear_Force:
        
        Shear_Stress.append(round(i/Area,3))
    #Calculating the secant angles
    Secant_angle=[]
    import math
    for i in Shear_Stress:
        
        x=math.atan(i/Normal_Stress)
        y=math.degrees(x)
        Secant_angle.append(round(y,3))
    
    
    
    #Results
    print("The PR Constant in KN/div is:", PRC_new)

    print("The applied Nomral Stress in KPa is:",Normal_Stress)

    print("The Results of Direct Shear are mentioned below:")

    print("The list of Horizental deformation is:",Horz_def)

    print("The list of Vertical deformation is:",Vert_def)

    print("The list of Shear Force is:",Shear_Force)

    print("The list of Shear Stress is:",Shear_Stress)

    print("The list of Secant angles is:",Secant_angle)

    print("The angle of friction is:", max(Secant_angle), "and the shear stress at failure in KPa is:", max(Shear_Stress))
    SSlist.append(round(max(Shear_Stress),3))
    x=input("Do you want to perform another test:")
    if x=="yes":
        n=n+1
    else:
        n=0
#Plotting the Graph of Shear Stress and Normal Stress
import matplotlib.pyplot as plt
import numpy as np
import math

plt.plot(NSlist, SSlist,label='Direct Shear Strength', marker ='+')
# Add a trend line
m, b = np.polyfit(NSlist, SSlist, 1)
x_intercept = -b/m   # x-intercept of trendline
plt.plot(NSlist, m*np.array(NSlist) + b, '-', label='Trend Line')

# Plot y-intercept at the start of the graph
y_intercept = m * NSlist[0] + b   # y-intercept of trendline
plt.plot([NSlist[0], NSlist[0]], [0, y_intercept], 'r--', label='cohesion coefficient')

plt.text(NSlist[1], y_intercept+15, f'c(KPa): {y_intercept:.2f}', ha='left', va='center')

delta_n = NSlist[-1] - NSlist[0]
delta_s = SSlist[-1] - SSlist[0]

# Calculate the angle between the shear stress and normal stress
theta = math.atan(delta_s / delta_n)
theta=math.degrees(theta)
plt.text(NSlist[1], y_intercept+2, f'friction angle(deg): {theta:.2f}', ha='left', va='center')
plt.xlabel('Normal Stress(KPa)')
plt.ylabel('Shear Stress(KPa)')
plt.title('Direct Shear Test')
plt.legend()
plt.show()

#Calculate the y-intercept

print('coefficient of cohesion (c) is:', round(y_intercept,3))
print("Angle of friction is:",round(theta,3))