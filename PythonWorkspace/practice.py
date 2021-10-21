animal = "강아지"
name = "고치"
age = 4
hobby = "산책"
is_adult = age >= 3 # age가 3 이상이면 true

print("우리집 " + animal + "의 이름은 " + name + "예요.")
print(name + "는 " + str(age) + "살이며, " + hobby + "를 아주 좋아해요") # str() : 정수형이나 불린형 등을 문자형으로 변경해줌
print(name + "는 어른일까요? " + str(is_adult))