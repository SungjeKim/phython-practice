age = int(input("당신의 나이는 몇 살인가요? "))

if age >= 20:
    print("성인입니다.")
else:
    print("미성년자입니다.")
score = int(input("시험 점수를 입력하세요: "))

if score >= 90:
    print("A등급입니다.")
elif score >= 80:
    print("B등급입니다.")
elif score >= 70:
    print("C등급입니다.")
else:
    print("F등급입니다.")

age = int(input("나이를 입력하세요: "))
has_id = input("신분증이 있나요? (yes/no): ")

if age >= 19 and has_id == "yes":
    print("입장 가능합니다.")
else:
    print("입장 불가능합니다.")

number = int(input("숫자를 입력하세요: "))

if number % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
