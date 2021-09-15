import os
import time


a=[]
while True:
    try:
        c=open('primes.txt','r')
        for i in c:
            a.append(int(i))
        c.close()
        break
    except:
        c=open('primes.txt','a')
        c.write(str(3)+'\n')
        c.close()
while True:
    try:
        e=open('primes_time'
               '.txt','r')
        e.close()
        break
    except:
        e=open('primes_time'
               '.txt','a+')
        e.close()

c=open('primes.txt','r')
h=-1
for i in c:
    h += 1
print('Number of Prime until now:{}'.format(h+1))
c.close()
f=time.time()
e=open('primes.txt','a')
while True: #                                                                            여기부터
    e=open('primes.txt','a')
    for i in range(720):
        d = a[h] + 2  # d을 크게 하면서 찾아갈거임, 2씩 증가하게 함으로서 2를 나누는 수고를 덤
        b=0						#b는 a 까지 1씩 상승하면서 모든 소수를 대입시켜본다.
        while True:				#소수 한개 찾기
            if d%int(a[b])==0:#확실히 소수가 아님
                d+=2
                b=0
            else:
                if b!=h:
                    b+=1
                else:
                    a.append(d)
                    h+=1
                    #c.open('primes.txt','a')
                    e.write(str(d)+'\n')#                     여기까지 파일을 열어놓는건 비효율적일수 있음. 여기서 바로 파일을 열고 닫고 하는 경우의 수도 있음
                    #c.write(str(d)+'\n')
                    #print(d)
                    break


    #x=h-719
        #e.write(str(d)+'\n')
    e.close()
    e=open('primes_time'
           '.txt','a')
    g=time.time()
    e.write('Number of primes :{}, Time Cost: {} Last Prime Number: {}\n\n'.format(h+2,g-f,d))
    f=g
    print('Number of Primes Until now:{}개'.format(h+1))
    e.close()

