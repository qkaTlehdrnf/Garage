import matplotlib.pyplot as plt
def make_condition(N=100,L=0.1,D=0.01,h=100,k=300,T0=80,Too=20):
    Dt={0:T0}
    deltax=L/N
    z=k/(h*deltax)
    m=k*D/(4*h*deltax**2)
    for i in range(1,N+1):
        Dt[i]=Too
    print(N,L,D,h,k,T0,Too,deltax,m,z)
    return Dt,m,z,N,Too
def cond(T1,T3,Too,m):
    return (2*m+1)**(-1)*(Too+m*(T1+T3))
def conv(Tn_1,z,Too):
    return (z*Tn_1+Too)*(1+z)**(-1)
def process(condition,decision):
    Dt, m, z, N, Too=condition
    for j in range(N**2*2):
        for i in range(1,N):
            Dt[i]=cond(Dt[i-1],Dt[i+1],Too,m)
        if decision:
            Dt[N]=conv(Dt[N-1],z,Too)
        else:
            Dt[N]=Dt[N-1]
    return Dt, m, z, N, Too
def main(cond,adiabatic=1):
    return process(cond,adiabatic)[0]

plot1=main(make_condition(k=300))
plot2=main(make_condition(k=15))
plot3=main(make_condition(k=1))
plot4=main(make_condition(),adiabatic=0)
plot5={}
for i in range(100):
    plot5[i]=plot1[i]-plot4[i]
DD=plot1,plot2,plot3,plot4,plot5

for D in DD:
    plt.bar(range(len(D)), list(D.values()), align='center')
    plt.xticks(range(len(D)), list(D.keys()))
    plt.show()
