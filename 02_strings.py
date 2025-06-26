# 문자열 기본
greeting = "안녕하세요"
name = "SJ"
message = greeting + ", " + name + "님 반가워요!"

print(message)

text = "파이썬 정말 재밌다!"
print("문장의 길이:", len(text))

sentence = "오늘은 파이썬 공부하는 날!"

print("앞 2글자:", sentence[0:2])
print("중간 단어:", sentence[4:7])
print("끝에서 3글자:", sentence[-3:])

msg = "Python is Awesome!"

print("소문자:", msg.lower())
print("대문자:", msg.upper())
print("포함 여부(Python):", "Python" in msg)
print("교체:", msg.replace("Awesome", "Fantastic"))
