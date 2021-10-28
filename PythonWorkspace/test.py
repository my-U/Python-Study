a = int(input())
b = int(input())
print(a*(b%10)) # 2360
print(a*((b - (b%100))//100))
print(a*((b%100)//10))
print((a*(b%10))+(a*((b%100)//10)*10)+((a*((b - (b%100))//100))*100))