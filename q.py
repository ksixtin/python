
'''
문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하세요 :)
'''

''' 내 코드
print("이름을 입력해 주세요!")
a = input()
text_f = a[:1]
text_e = a[2:]

print(text_f+text_e)
'''

''' 답안
sample = input('문자를 입력해 주세요')
print(sample[0])
print(sample[-1])
print(f"첫 글자 : {sample[0]}")
print(f"마지막글자 : {sample[-1]}")
'''

''' 2번 문제 답안
문제 : 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성해주세요 :)

n = int(input('숫자를 입력하세요: '))

for i in range(n):
	print(i+1)
for i in range(1, n+1):
	print(i)
'''

''' 3번 문제 답안
문제 : 숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성해주세요 :)


number = int(input('숫자를 입력하세요: '))
print(number % 2)
if number % 2 == 1:
	print('홀수 입니다.')
else:
	print('짝수 입니다.')

if number % 2:					# == 1을 생략 가능
	print('홀수 입니다.')
else:
	print('짝수 입니다.')

'''
''' 4번 문제 답안
문제 : 
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다.
국어는 90점 이상,
영어는 80점 초과,
수학은 85점 초과, 
과학은 80점 이상일 때 합격이라고 정했습니다.(한 과목이라도 조건에 만족하지 않으면 불합격)
다음 코드를 완성하여 합격이면 True, 불합격이면 False가 출력되도록 작성하시오. 
'''
'''
a = int(input('국어: '))
b = int(input('영어: '))
c = int(input('수학: '))
d = int(input('과학: '))


if a >= 90 and b > 80 and c > 85 and d >=80:
	print(True)
else:
	print(false)
'''
	

''' 5번 문제 답안
문제 : 
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# print(prices.split(";"))
makes = prices.split(";")
boxes = []
# list > append(리스트에 데이터를 넣어줌)
print(makes)
for make in makes:
	boxes.append(int(make))
# print(boxes)

# list > sort()
boxes.sort(reverse=True)
# print(sorted(boxes))
# print(boxes)
for box in boxes:
	print(box)