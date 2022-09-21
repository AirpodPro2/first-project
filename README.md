# first-project
###This is Chap.3 Exercise<br>
~~~python
<br>
<pre>
<code>
#3.6
a,b,c = map(int,input("세 정수를 입력하시오 : ").split())
if(a>b):
    if(b>c):print(c,b,a)
    else:
        if(a>c):print(b,c,a)
        else:print(b,a,c)
else:
    if(a>c):print(c,a,b)
    else:
        if(b<c):print(a,b,c)
        else:print(a,c,b)


---
#3.9
num = int(input("정수 입력 : "))
if(num%2==0):print(num,"은 2로 나누어집니다")
else:print(num,"은 2로 나누어 지지 않습니다")

if(num%5==0):print(num,"은 5로 나누어집니다")
else:print(num,"은 5로 나누어 지지 않습니다")

if(num%6==0):print(num,"은 2와 3 모두로 나누어집니다")
else:print(num,"은 2와3 모두로 나누어 지지 않습니다")

<hr/>
#3.11
lotto=[2,3,9]
my_lotto=list(map(int,input("세 복권번호를 입력하세요 : ").split()))
intersection = list(set(lotto) &set(my_lotto))
ans=len(intersection)
if(ans==3):print('1억원')
elif(ans==2):print("1천만 원")
elif(ans==1):print("1만원")
elif(ans==0):print("다음 기회에")
<br>
#3.12
import math
x,y=map(int,input("x y좌표를 입력하세요 : ").split())
#radius=5
distance =math.sqrt(x**2+y**2)
if(distance<=5):print("원의 내부에 있음")
else:print("원의 외부에 있음")
<br>
#3.14
char=input("알파벳을 입력하세요 : ")
target=['a','e','i','o','u']
if(char in target):
    print(char,"은 모음 입니다")
else:print(char,"은 자음 입니다")
<br>
#3.16
n=int(input("1에서 9까지의 수를 입력하세요 : "))
while True:
    if(n<1 or n>9):
        n=int(input("1에서 9까지의 수를 다시 입력하세요 : "))
        continue
    
    for i in range(1,10):
        print(n,"*",i," = ",n*i)
    break
<br>
#3.24
n=int(input("정수를 입력하세요 : "))
s=0
for i in range(1,n+1):
   s+=1/(i**2)
print("결과는 ",s,"입니다")

</code>
</pre>
~~~
