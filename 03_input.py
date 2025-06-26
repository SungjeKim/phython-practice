# 사용자로부터 이름을 입력받기
name = input("당신의 이름은 무엇인가요? ")

print("안녕하세요, " + name + "님!")


birth_year = input("태어난 해를 입력하세요 (예: 1990): ")

# 문자열을 숫자로 바꿔야 계산 가능
age = 2025 - int(birth_year)

print("당신은", age, "살이군요!")

num1 = input("첫 번째 숫자를 입력하세요: ")
num2 = input("두 번째 숫자를 입력하세요: ")

# 문자열 → 숫자로 바꾸기
sum = int(num1) + int(num2)

print("두 수의 합은:", sum)

name = input("이름을 입력하세요: ")
job = input("직업을 입력하세요: ")
hobby = input("취미를 입력하세요: ")

print("\n==== 자기소개서 ====")
print("이름:", name)
print("직업:", job)
print("취미:", hobby)


