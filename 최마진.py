print("AI 거짓말 탐지기 - LieCheck")
print("입력한 문장에서 과장 표현, 감정 단어 등을 분석합니다.\n")

# 사용자 문장 입력
text = input("분석할 문장을 입력하세요: ").lower()

# 분석 키워드 사전
exaggeration = ["절대", "완벽", "100%", "항상", "무조건"]
emotional_appeal = ["믿어줘", "진짜", "억울해", "내 말이 맞아", "거짓말 아니야"]
suspicious_phrases = ["진짜 진짜", "정말 정말", "거짓말 안 해", "진심이야", "진짜임"]

# 점수 계산
score = 100
penalty = 0

# 키워드 분석
for word in exaggeration:
    if word in text:
        penalty += 10
for word in emotional_appeal:
    if word in text:
        penalty += 15
for word in suspicious_phrases:
    if word in text:
        penalty += 20

score = max(0, score - penalty)

# 결과 출력
print("\nAI 분석 결과")
print(f"신뢰도 점수: {score}/100")
bar = "█" * (score // 10) + "░" * ((100 - score) // 10)
print(f"신뢰도 시각화: [{bar}]")

# 피드백
if score >= 80:
    print("✅ 이 문장은 신뢰할 수 있어 보입니다.")
elif score >= 50:
    print("⚠️ 이 문장은 약간의 과장이나 감정 호소가 포함되어 있습니다.")
else:
    print("❌ 이 문장은 신뢰도가 낮습니다. 거짓말일 가능성이 높아요!")

# 사용된 문제 단어 출력
print("\n❗ 감지된 의심 단어:")
for category, wordlist in {
    "과장 표현": exaggeration,
    "감정 호소": emotional_appeal,
    "강조 표현": suspicious_phrases
}.items():
    found = [w for w in wordlist if w in text]
    if found:
        print(f"- {category}: {', '.join(found)}")

# 현재 파이썬으로 구현할 수 있는 분석 키워드가 이게 한계이지만 추후에 AI가 진술의 전후 상황을 분석하고 다양한 키워드를 고려한다면 좋은 성능의 AI 거짓말 탐지기가 될 가능성이 높음음