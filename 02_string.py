'''
String 조작하기

1. 글자 합체
string + string

2. 글자 삽입(수술)

3. 글자 자르기


'''

# 1. 글자 합체

hphk = "happy" + "hacking"      # 쌍따옴표나 홀따옴표나 감싸주면 스트링으로 인식

print(hphk)

# 2. 글자 삽입

name = "LEO"
age = 20
text = "제 이름은 {}입니다. 나이는 {}살 입니다!".format(name, age)
print(text)

f_text = f"제 이름은 {name}입니다. 나이는 {age}살 입니다!!" # f스트링
print(f_text)

# 3. 글자 자르기

text_name = text[:14]       # : 처음부터 14번째까지 다 자름
print(text_name)

text_age = text[14:]        # :14번째 뒤로 다 자름
print(text_age)

text_split = text.split()
print(text_split)