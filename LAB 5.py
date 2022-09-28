#LAB 5

#1.1
even_list=[2,4,6,8,10]
print(even_list)
#1.2
even_list=[i for i in range(2,11,2)]
print(even_list)
#1.3
nations=['Korea','China','India','Nepal']
print("nations = ",nations)
#1.4
friends=['길동','철수','은지','지은','영민']
print('friends =',friends)
#1.5
string = ['X','Y',"z"]
print("string = ",string)

#2.1
prime_list=[2,3,5,7]
print("prime_list의 첫 원소 : ",prime_list[0])
#2.2
print("prime_list의 마지막 원소 : ",prime_list[3])
#2.3
print("prime_list의 마지막 원소 : ",prime_list[-1])
#2.4
nations=["korea","China","Russia","Malaysia"]
print("nations 의 첫 원소 : ",nations[0])
#2.5
print("nations의 마지막 원소 : ",nations[-1])
#2.6
print("nations의 마지막 원소 : ",nations[len(nations)-1])

#3.1
prime_list = [2,3,5,7]
print("소수 목록 : ",prime_list)
prime_list.append(11)
print("추가 후 소수 목록 : ",prime_list)
#3.2
print("삭제 전 소수 목록 : ",prime_list)
prime_list.remove(3)
print("삭제 후 소수 목록 : ",prime_list)
#3.3
nations=["Korea","China","Russia","Malaysia"]
print("국가 목록 : ",nations)
nations.append("Nepal")
print("추가 후 국가 목록 : ",nations)
#3.4
def check(nation,arr):
    if(nation in arr):
        print(nation,"은 국가 목록에 있습니다")
    else:
        print(nation,"은 국가 목록에 없습니다")
check('Japan')
check("Russia")

#4.1
prime_list=[2,3,5,7]
print("1~10까지 소수 : ",prime_list)
print("최솟값 : ",min(prime_list))
print("최댓값 : ",max(prime_list))
print("합계 : ",sum(prime_list))
print("평균 : ",sum(prime_list)/len(prime_list))
#4.2
nations=["korea","China","Russia","Malaysia"]
print("국가 목록 : ",nations)
nations.sort()
print("사전에 가장 먼저 나오는 나라 : ",nations[0])
print("사전에 가장 뒤에 나오는 나라 : ",nations[-1])

#5.1
a=[1,2,3]
b=[10,20,30]
a.append(b)
print(a)# result = [1,2,3,[10,20,30]]
a=[1,2,3]
a.extend(b)
print(a)# result = [1,2,3,4,5,6]
#5.2
nlist=[i for i in range(1,11)]
print("nlist = ",nlist)
#5.3
nlist.insert(0,0)
print("nlist = ",nlist)
#5.4
nlist.sort(reverse=True)
print("nlist = ",nlist)
#5.5
print("마지막 원소 = ",nlist.pop())
print("nlist = ",nlist)

#6.1
n=int(input("정수를 입력하세요 : "))
list_=[1,2,3]
print(list_ * n)

#7.1
n_list=list(range(15))
print("n_list = ",n_list)
#7.2
print("s_list = ",n_list[:6])
print("s_list = ",n_list[5:11])
print("s_list = ",n_list[11:15])
print("s_list = ",n_list[2:12:2])
print("s_list = ",n_list[10:5:-1])
print("s_list = ",n_list[10:0:-2])
