#1-1
score=int(input())
if(score>=1000):
    print("game_score = ",score)
    print("당신은 고수입니다")
else:
    print("game_score = ",score)
#1-2
num_a,num_b=100,200
print("num_a = ",num_a,"num_b = ",num_b)
if(num_a==num_b):
    print("두 값이 일치합니다")
num_a,num_b=300,300
print("num_a = ",num_a,"num_b = ",num_b)
if(num_a==num_b):
    print("두 값이 일치합니다")

#2-1
n=int(input('정수를 입력하세요 : '))
print("n = ",n)
if(n%2==0):
    print(n,"은 짝수입니다")
#2-2
x=int(input("정수를 입력하세요 : "))
print("x = ",x)
if(x>0):
    print(x,"는 자연수입니다")
else:
    print("x = ",x)

#3-1
score=int(input('게임점수를 입력하시오 : '))
print('game_score = ',score)
if(score>=1000):
    print("고수입니다")
else:#score<1000
    print("입문자 입니다")
#3-2
n=int(input('한 정수를 입력하시오 : '))
m=int(input('다른 정수를 입력하시오 : '))
if(n==m):
    print('두 값이 일치합니다')
else:
    print('두 값이 일치하지않습니다')
#3-3
age=int(input('당신은 성인인가요(성인이면 1,미성년이면 0)'))
if(age==0):
    print('당신은 미성년자입니다')
elif(age==1):
    marriage=int(input('결혼을 하셨나요(기혼 1,미혼 0)'))
    if(marriage==1):
        print('당신은 결혼한 성인입니다')
    elif(marriage==0):
        print('당신은 결혼하지 않은 성인입니다')
#4-1
num=2
if(num >=1 and num<=10):
    print("True")
#4-2
age=int(input('나이를 입력하세요'))
print("age = ",age)
if(age>10 and age<19):
    print('청소년입니다')
#5-1
speed=int(input('자동차의 속도를 입력하세요(단위 : km/h ) : '))
if(speed >=100):print('고속')
elif(speed<100 and speed>=60):print('중속')
else:print('저속')
#5-2
dust=int(input('미세먼지 농도를 입력하세요(단위 : microgram/m^3) : '))
if(dust>=0 and dust<=15):
    print('좋음')
elif(dust>=16 and dust<=35):
    print('보통')
elif(dust>=36 and dust<=75):
    print('나쁨')
elif(dust >=76):
    print('매우 나쁨')
#6-1
for _ in range(5):
    print("Hello, Python!")
#6-2
for i in range(5):
    print(i)
#7-1
nums = list(range(1,101))
#7-2
nums=list(range(2,101,2))
#7-3
nums=list(range(1,101,2))
#7-4
nums = list(range(-1,-100,-1))

#8-1
print(sum(range(1,101)))
#8-2
print(sum(range(0,101,2)))
#8-3
print(sum(range(1,101,2)))
#9-1
for i in range(7):
    for j in range(7-(i+1)):
        print(' ',end='')
    print('#')


