```python
#파이썬 내장함수
print(abs(-10))
print(eval(ascii("ascii function")))#eval()가 평가하는 인수와 같은 객체가될 문자열 생성
print(bin(2),oct(2),hex(2))#정수를 2진수,8진수,16진수 문자열로 변환
print(bool('None'),bool([]))#뭔가 들어가있으면 True,아니면 False return
print(chr(97),ord('a'))#chr:정수를 유니코드가 맞는 문자로 반환, ord:반대
print(divmod(10,3))#나누기 한 결과의 몫,나머지 반환

array=['a','b','c','d']
print([(i,v) for i,v in enumerate(array)])#list의 원소에 index를 원소와같이반환
print(hash(1),hash('a'))#입력받은 값의 고유한 해시 값 반환
#print(help())#도움말 시스템
print(issubclass(int,float))#첫번째 인수가 두 번쨰 인수의 서브 클래스 인지를 판단
print(pow(2,10))#첫번째 인자의 두번째 인수 제곱 반환, 2^10

arr=list(range(1,5))
print(arr)#[1~4]
arr.reverse()
print((arr))#4~1 해당 list의 요소 순서를 뒤집는다

```

    10
    ascii function
    0b10 0o2 0x2
    True False
    a 97
    (3, 1)
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    1 -5670666742425996388
    False
    1024
    [1, 2, 3, 4]
    [4, 3, 2, 1]
    


```python

```
