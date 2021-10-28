python = "Python is Amazing"

print(python.lower()); # 모든 문자 소문자로 출력
print(python.upper()); # 모든 문자 대문자로 출력
print(python[0].isupper()); # 인덱스 0번째 문자가 대문자인지
print(len(python)) # python 문자열의 길이
print(python.replace("Python", "Java")); # 문자열 중 Python을 Java로 변경

index = python.index("n") # 문자 n의 인덱스 번호 출력
print(index) # index = 5
index = python.index("n", index + 1) # 위의 index의 값 + 1 부터 즉, 인덱스 6부터 문자 n을 찾음
print(index) # index = 15

print(python.find("n")) # 문자 n의 인덱스 번호 출력
print(python.find("Java")) # 문자열에 Java가 존재하지 않아 -1 출력 후 다음 코드 실행
print(python.index("Java")) # 문자열에 Java가 존재하지 않아 오류 출력 후 실행 중단

print(python.count("n")) # 문자 n이 문자열에서 몇 번 존재하는지 세줌