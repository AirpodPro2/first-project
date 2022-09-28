#LAB 6

#1.1
from typing import ChainMap


capital_dic={'Korea':'Seoul','China':'Beijing','USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic["USA"])
#1.2
fruits_dic={'apple':5000,'banana':4000,'grape':5300,'melon':6500}
for key,val in fruits_dic.items():
    print('{}의 가격은 {}원 입니다'.format(key,val))
    
#2.1
person={'이름':'홍길동','나이':26,'몸무게':62,'특기':'분신술'}
person['특기']='분신술'
print(person)
#2.2
person['아버지']='홍판서'
print(person)
#2.3
del person['나이']
print(person)

#3.1
capital_dic={'Korea':'Seoul','China':'Beijing','USA':'WAshington Dc'}
print('Korea' in capital_dic)#true
print('China' in capital_dic)#true
print('Indonesia' in capital_dic)#false
print('Beijing' in capital_dic)#false, in연산자는 key가 dict 안에 존재하는지만 확인

#4.1
fruits_dic={'apple':6000,'melon':3000,'banana' :5000,'orange':7000}
print(fruits_dic.keys())
print(fruits_dic.values())
fruits_dic.pop('apple')
fruits_dic.clear()

#5.1
fruits_dic={'apple':6000,'melon':3000,'banana' :5000,'orange':4000}
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print("fruits_dic의 항목의 개수 : ",len(fruits_dic))
if('apple' in fruits_dic):
    print('appele is in fruits_dic')
if('mango' not in fruits_dic):
    print('mango is not in fruits_dic')

#6.1
the_day=(1919,3,1)
year,month,day=the_day#unpacking
print(year,'년 ',month,'월 ',day,'일은 삼일절입니다')
#6.2
nums=tuple([10,20,30])
a,b,c=nums#unpacking
print('a =',a)
print('b =',b)
print('c =',c)

#7.1
person=('홍길동',20190031,179)
#person[1]=2019003 값을 수정하려고 하면 TypeError발생
person=list(person)
person[1]=2020003
print(tuple(person))

#9.1
lst=['apple','mango','banana']
s1=set(lst)
print("s1 =",s1)
#9.2
greet='Good afternoon'
s2=set(greet)
print("s2 = ",s2)

#10.1
s1={10,20,30,40}
s2={30,40,50,60,70}
print(s1|s2)#union 10~70 unordered
print(s1&s2)#intersection 30 40 unordered
print(s1-s2)#difference 10 20 unordered
print(s1^s2)#symmetric_difference 10 20 50 60 70 unordered
print(s1.issubset(s2))#부분집합인가? false
print(s1.issuperset(s2))#상위집합인가? false
print(s1.isdisjoint(s2))#서로소인가? false

#except lab8 lab11 lab12
