#1-1
def print_star():
    print('*****************')
#함수호출문을 삭제하면 별표를 출력하지 않는다

#1-2
print_star()
print_star()
print_star()
print_star()
print_star()
print_star()

#2.1
def print_star5():
    print('***********************')
    print('***********************')
    print('***********************')
    print('***********************')
    print('***********************')
print_star5()
print_star5()

#3.1
def print_Hash():
    print('#################')
def print_star():
    print('*****************')
def print_plus():
    print('+++++++++++++++++')
print_Hash()
print_star()
print_plus()
print_plus()
print_star()
print_Hash()

#4.1
def print_star(n):
    for _ in range(n):
        print('****************')
print_star(10)

#4.2
def print_hash(n):
    for _ in range(n):
        print('################')
print_hash(10)

#4.3
print_hash(6)
#4.4
def print_hash(n):
    for i in range(n):
        print(i,'###############')
print_hash(6)

#5.1
def print_sub(a,b):
    result=a-b
    print(a,"와",b,"의 차는 ",result,"입니다")
print_sub(10,20)
#5.2
def print_mult(a,b):
    result=a*b
    print(a,"와",b,"의 곱은",result,"입니다")
print_mult(10,20)

#6.1
def print_root(a,b,c):
    r1=(-b+(b**2-4*a*c)**0.5)/(2*a)
    r2=(-b-(b**2-4*a*c)**0.5)/(2*a)
    print('해는',r1,'또는',r2)
print_root(1,4,-21)
print_root(1,-6,8)
#6.2
def print_area(width,height):
    area=width*height*0.5
    print('밑변',width,', 높이',height,'인 삼각형의 면적은 :',area)
print_area(10,20)

#7.1
def circle_area_circum(radius):
    area=radius*radius*3.14
    circum=2*3.14*radius
    return area,circum
radius=10
area,circum = circle_area_circum(10)
print('반지름',radius,'인 원의 면적은',area,'원의 둘레는',circum)

#8.1
def multiplies(n,m):
    nums=list()
    for i in range(1,m+1):
        nums.append(n*i)
    return nums
r1,r2,r3,r4=multiplies(3,4)
print(r1,r2,r3,r4)
r1,r2,r3,r4,r5=multiplies(2,5)
print(r1,r2,r3,r4,r5)

#9.1
def print_name(honorifics,first_name,last_name):
    print(honorifics,first_name,last_name)
print_name(first_name="Gildong",last_name='Hong',honorifics='Dr.')
print_name('Gildong','Hong','Dr.')
#10.1
def sum_nums(*nums):
    sum=0
    for num in nums:
        sum+=num
    print(len(nums),'개의 인자',nums)
    print('합계 :',sum,'평균 :',sum/len(nums))
sum_nums(10,20,30)
sum_nums(10,20,30,40,50)
#10.2
def min_nums(*nums):
    print('최솟값은',min(nums))
min_nums(20,40,50,10)

#11.1
def info():
    name=input("당신의 이름을 입력해주세요 : ")
    age=int(input("나이를 입력해주세요 : "))
    job=input("직업을 입력해주세요 : ")
    address=input("사는 곳을 입력해 주세요 : ")
    print('당신의 이름은 {}, 나이는 {}살, 직업은 {},사는 곳은 {}입니다'.\
          format(name,age,job,address))
    print('당신의 이름은',name,',나이는',age,'살,직업은',job,'사는 곳은',\
          address,'입니다')
info()
#12.1
print(','.join('ABCD'))
#12.2
s='My favorite thing is monsters.'
t=s.replace('monsters','cartoons')
print(t)
