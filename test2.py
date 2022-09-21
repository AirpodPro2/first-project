#1
for Celsius in range(0,55,5):
    Fa = (9/5)*Celsius+32
    print("섭씨 : ",Celsius,"화씨 : ",Fa)
print("---------------------------------")
#2
a=2*2//2#2
b=3//2*3#3
print(a,b)
print("----------------------------")
#3
s3,s5=0,0
for i in range(3,1000):
    if(i%3==0):
        s3+=i
    elif(i%5==0):
        s5+=i
print(s3+s5)
print("--------------------")
