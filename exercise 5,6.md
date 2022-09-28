```python
#5.3
list1=[3,5,7]
list2=[2,3,4,5,6]
for x in list1:
    for y in list2:
        print(x,"*",y,' =',x*y)
```

    3 * 2  = 6
    3 * 3  = 9
    3 * 4  = 12
    3 * 5  = 15
    3 * 6  = 18
    5 * 2  = 10
    5 * 3  = 15
    5 * 4  = 20
    5 * 5  = 25
    5 * 6  = 30
    7 * 2  = 14
    7 * 3  = 21
    7 * 4  = 28
    7 * 5  = 35
    7 * 6  = 42
    


```python
#5.4
a=[2,3,4,5,6]
print(a)
rev_a=list()
for num in a:
    rev_a.append(a.pop())
print(rev_a)
```

    [2, 3, 4, 5, 6]
    [6, 5, 4]
    


```python
#5.11
nums=list(map(int,input('5개의 수를 입력하세요').split()))
print('합 :',sum(nums))
print('평균 :',sum(nums)/len(nums))
print('최댓값 :',max(nums))
print('최솟값 :',min(nums))
```

    5개의 수를 입력하세요1 2 3 4 5
    합 : 15
    평균 : 3.0
    최댓값 : 5
    최솟값 : 1
    


```python
#5.13
import math
nums=list(map(int,input('10개의 수를 입력하세요 : ').split()))
print('합 :',sum(nums))
average=sum(nums)/len(nums)
print('평균 :',average)
sd=0#표준편차
for num in nums:
    sd+=math.pow((num-average),2)
sd/=10
sd=math.sqrt(sd)
print('표준편차 :',sd)

```

    10개의 수를 입력하세요 : 1 2 3 4 5 6 7 8 9 10
    합 : 55
    평균 : 5.5
    표준편차 : 2.8722813232690143
    


```python
#5.18
s_list=['abc','bcd','bcdefg','abba','cddc','opq']
min_len=len(s_list[0])
max_len=0
ans1=s_list[0]
for str in s_list:
    if min_len >len(str):
        min_len=len(str)
        ans1=str
    if max_len <len(str):
        max_len=len(str);
        ans2=str
print(ans1)#길이가 가장 짧은 문자열
print(ans2)#길이가 가장 긴 문자열
print('길이가 가장 짧은 문자열 : ')
s_list.sort(key=len)
min_len=len(s_list[0])
for str in s_list:
    if len(str)==min_len:
        print(str,end=' ')#길이가 가장 짧은 문자열들
```

    abc
    bcdefg
    길이가 가장 짧은 문자열 : 
    abc bcd opq 


```python
#5.19
s_list=['abc','bcd','abc','abba','cddc','opq','opq']
s_list=set(s_list)
new_s_list=list(s_list)
print(new_s_list)
```

    ['abc', 'bcd', 'opq', 'abba', 'cddc']
    


```python
#6.4
t=(10,20,30,40)
t[0]=0#tuple형에 요소 할당 불가능
t.append(50)#tuple형에 append로 요소 추가 불가능
t.remove(40)#tuple형에 remove로 요소 제거 불가능

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Input In [42], in <cell line: 3>()
          1 #6.4
          2 t=(10,20,30,40)
    ----> 3 t[0]=0#tuple형에 요소 할당 불가능
          4 t.append(50)#tuple형에 append로 요소 추가 불가능
          5 t.remove(40)
    

    TypeError: 'tuple' object does not support item assignment



```python
#6.6
t1='a','b','c'
t2=('a','b','c')
t1==t2#True
t3=('d','e')
t2+t3#('a','b','c','d','e')
```


```python
#6.7
sales=(100,121,120,130,140,120,122,123,190,125)
cnt=0#answer
for i in range(1,10):
    if sales[i] <sales[i-1]:
        cnt+=1
print('지난 10일동안 전일대비 매출이 감소한 날은',cnt,'일 입니다')
```


```python
#6.14
arr=[5,6,31,9,2,12,13,8,7]
sorted_list=[]
i=1
while(sorted_list !=sorted(arr)):
    sorted_list.append((max(arr)))
    arr.remove(max(arr))
    sorted_list.sort()
    if(arr==list()):
        print("정렬 된 리스트 :",sorted_list)
        break
    print(i,"단계 :",arr,sorted_list)
    i+=1
```


```python
#6.19
s1={0,1,2,3,4,5}
s2={3,4,5,6,7}
print(s1&s2)#{3,4,5} intersection
print(s1|s2)#{0,1,2,3,4,5,6,7} union
print(s2-s1)#difference {6,7}
print(s1-s2)#difference {0,1,2}
print(s1^s2)#symmetric difference {0,1,2,6,7}
print(2 in s1)#True
```
