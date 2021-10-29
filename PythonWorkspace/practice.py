# 서식 지정자
print("나는 %d살입니다." %20) # d는 정수만 가능
print("나는 %s을 좋아해요." %"파이썬") # s는 문자열만 가능
print("Apple은 %c로 시작해요." %"A") # c는 문자 1개

print("나는 %s살입니다." %20) # s는 숫자 또한 사용 가능
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간")) # 여러 개의 값을 표현할 땐 괄호 사용

# str.format
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) # 포맷의 인덱스 번호

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간")) # 인덱스보다 명확한 사용을 위해 
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# f-string(3.6v 이상부터 지원)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")