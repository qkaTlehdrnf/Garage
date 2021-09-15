import sys
from scipy.optimize import fmin
import numpy as np
import matplotlib.pyplot as plt
sys.setrecursionlimit(20000)
dp=130*10**-9
Stk50=0.49
N=1
atm=101325
Pin=1*atm
Tin=293         #####상온
mdot=5*10**-5
print(mdot)
sqrStk=0.49
pi=3.141592
W=0.56*10**-3
Nn=1
A=pi*W**2/4
M=28.97*10**-3  #28.96g/mol
Ru=8.31432#8.31446261815324	J⋅K−1⋅mol−1
P0=1
gamma=1.19 #################maybe
rhoin=1.2
rhop=1000
a=mdot/(A*N*rhoin) #0.203
b=(gamma-1)*M/(2*gamma*Ru*Tin)#1.6989*10^-6
print('a= ',a,', b=',b,', p=',Pin,', g=',gamma)

##### Stage 1 #####
def Loop1(x):#r=Pout/Pin
    r=x[0]
    if type(r)==int:
        if r>=1:
            return 100
    V1=-r/(2*a*b)+(1/b+(r/(2*a*b))**2)**0.5
    V2=(Pin*2*(1-r)/(rhoin*r**(1/gamma)))**0.5
    Err=V1-V2
    return abs(Err)
x = np.arange(0.0001, 1, 0.0001)

plt.plot(x, Loop1([x,0]))
plt.show()
e=2.7182
rmin=fmin(Loop1,np.array([0.0001]))[0]

##### Stage 2 #####
Pout=rmin*Pin
Vout=-rmin/(2*a*b)+(1/b+(rmin/(2*a*b))**2)**0.5
Cp=gamma*Ru/((gamma-1)*M)
Tout=Tin-Vout**2/(2*Cp)
mu=1.8*10**-5*(Tout/Tin)**(3/2)*((Tin+120)/(Tout+120))
Cc=1+(15.6+7*e**(-59*Pout*dp))/(1000*Pout*dp)
d50=((9*mu*W*Stk50)/(rhop*Vout*Cc))**0.5
print('\n\n######################################\nd50',d50,'m')
print('Pout',Pout/atm,'atm')
print('Vout',Vout,'m/s')
print('Tout',Tout,'K')
print('######################################\n\n######################################\n학생은 총체적으로 다 틀렸다 \n'
      '압력값을 잘못 계산하게 되어서 뒤의 값들도 다 틀리게 되었지만 \n'
      '기본적으로 식 또한 잘못 전개하였기에 d50의 값도 이상하게 나오게 되었다\n######################################')