from random import *  # random 라이브러리에 들어있는 모든 것을 사용

print(random())  # 0.0에서 1.0 미만의 임의의 값을 생성
print(random() * 10) # 0.0에서 10.0 미만의 임의의 값을 생성
print(int(random() * 10)) # 0에서 10 미만의 임의의 정수값 생성
print(int(random() * 10) + 1) # 1에서 11미만의 임의의 정수값 생성

print(int(random() * 45) + 1) # 1에서 46 미만의 임의의 정수값 생성
print(randrange(1, 46)) # 1에서 46 미만의 임의의 값 생성
print(randint(1, 45)) # 1에서 45 이하의 임의의 값 생성