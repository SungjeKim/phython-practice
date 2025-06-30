print("=== 파이썬 계산기 ===")

num1 = int(input("첫 번째 숫자를 입력하세요: "))
op = input("연산자를 입력하세요 (+, -, *, /): ")
num2 = int(input("두 번째 숫자를 입력하세요: "))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "0으로 나눌 수 없습니다!"
else:
    result = "지원하지 않는 연산자입니다."

print("결과:", result)

