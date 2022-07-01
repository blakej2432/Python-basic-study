1. 개발환경 준비
cmder 다운 or
windows store -> windows Terminal, Ubuntu(리눅스 환경도 작동할 수 있게)

C:\Users\USER>cd workspace
지정된 경로를 찾을 수 없습니다.

C:\Users\USER>mkdir workspace

C:\Users\USER>cd workspace

C:\Users\USER\workspace>dir
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: F4C5-D847

 C:\Users\USER\workspace 디렉터리

2022-06-30  오후 12:01    <DIR>          .
2022-06-30  오후 12:01    <DIR>          ..
               0개 파일                   0 바이트
               2개 디렉터리  25,965,355,008 바이트 남음

C:\Users\USER\workspace>mkdir test

C:\Users\USER\workspace>cd test

C:\Users\USER\workspace\test>dir ..\test
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: F4C5-D847

 C:\Users\USER\workspace\test 디렉터리

2022-06-30  오후 12:02    <DIR>          .
2022-06-30  오후 12:02    <DIR>          ..
               0개 파일                   0 바이트
               2개 디렉터리  25,964,064,768 바이트 남음

C:\Users\USER\workspace\test>mkdir one-depth

C:\Users\USER\workspace\test>cd one-depth

C:\Users\USER\workspace\test\one-depth>copy ..\..\abc.txt
지정된 파일을 찾을 수 없습니다.

C:\Users\USER\workspace\test\one-depth>

cmd, cmder 등 이용할 때 꼭 (base) -> conda activate base



2. 파이썬 플러스

.append
.extend!!!!!!!!!!!!!!! 

b = a 메모리 공유하게 만드는거말고 a의 값만 가져오고싶으면
b = a[:] -> one dimentional만 되고, two dimentional은 안됨
그 떄는 b = copy.deepcopy(a) 

# function & IO

from random import random
from re import I
from sympy import O


def calculate_rectangle_area(x , y):
    result = x * y
    return result

rectangle_x = 10
rectangle_y = 20
print ("사각형 x의 길이: ", rectangle_x)
print ("사각형 y의 길이: ", rectangle_y)
# 넓이를 구하는 함수 호출
print ("사각형의 넓이: ", calculate_rectangle_area(rectangle_x, rectangle_y))

def f(x):
    return 2*x + 7

def g(x):
    return x**2

x = 2

f(x) + g(x) +f(g(x)) + g(f(x))


■ console i/O

GUI CLI

print('enter your name')
somebody = input()
print('Hi', somebody)

print(1,2,3)
print("a" + " " + "b" + " " + "c")
print("%d %d %d" % (1,2,3))
print("{} {} {}".format("a","b","c"))
print(f"value is {value})

print(1,2,3)
print("a" + " " + "b" + " " + "c")
print("%d %d %d" % (1,2,3))
print("{} {} {}".format("a","b","c"))
print(f"value is {value})

print("Art: %5d, Price per Unit: %8.2f" %(453, 59.058))
print("Product: %10s, Price: %10.1f." %("Apple",5.39594))
print("Product: {0}, Price: {1:.3f}.".format("Apple",5.39594))
print("Product: {0}, Price: {1:.3f}.".format("Apple",5.39594))
print("Product: {0}, Price: {1:10.3f}.".format("Apple",5.39594))
# 0, 1 순서고 10자리 비워놓고 소수점 3자리 -> {1:10.3f}
print("Product: {0:>10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))
print("Product: {0:<10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))

# f string이 대세임
name = "Sungchul"
age = 39
print(f"Hello, {name}. You are {age}.")
print(f'{name:20}')
print(f'{name:>20}')
print(f'{name:*<20}')
print(f'{name:*>20}')
print(f'{name:*^20}')
number = 3.141592653589793
print(f'{number:.2f}')
print(f'{number:*<10.2f}')

# Fahrenheit converter
print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
number = float(input("변환하고 싶은 섭씨 온도를 입력해주세요: "))
fahren = (9/5)*number + 32
print(f"섭씨온도: {number}, \n화씨온도: {fahren:.2f}")

■ conditionals

print("Tell me your age?")
myage = int(input()) # 나이를 입력 받아 myage 변수에 할당
if myage < 30: # myage 가 30 미만일 때
    print("Welcome to the club")
else: # myage 가 30 이상일 때
    print("Oh! No. You are not accepted.")


x is y # == 이랑 다름. 메모리 주소를 비교하는 것 , -5 부터 256은 가능(얘네까지는 같은 메모리주소 쓰게 해서)

if 1:
    print('Hello')

# all 사용 판단
lst =[True,False,True,False,True]
all(lst)

# 삼항 연산자
value = 12
is_even = True if value % 2 == 0 else False
is_even


birth = int(input('당신이 태어난 년도를 입력하세요'))
age = 2022 - birth + 1

if  age >= 20 and age <= 26:
    print('대학생')
elif age >= 17 and age < 20:
    print('고등학생')
elif age >= 14 and age < 17:
    print('중학생')
elif age >= 8 and age < 14:
    print('초등학생')

'''
else:
    print('초등학생') 가능
'''

■ loop
for i in "abcdefg":
    print(i)

i =0
while i < 10:
    print (i,)
    i += 1
else:
    print ("EOP") # break로 종료된 반복문은 else block이 수행되지 않음 그 때 필요
    
# 구구단 계산기

for i in range(1,10):
    hap = 5 * i
    print(f'5 x {i} = {hap}')


# 이진수

decimal = 10
result =''
while (decimal > 0):
    remainder = decimal % 2
    decimal = decimal // 2
    result = str(remainder) + result
print (result)


import random
answer = random.randint(1,100)

print('숫자를 맞춰보세요 (1~100)')
num = 999999

while num != answer:
    num = int(input('예상 입력: '))
    if num < answer:
        print('숫자가 너무 작습니다.')
    elif num > answer:
        print('숫자가 너무 큽니다.')
    else:
        break
print(f'정답입니다. 숫자는 {answer}입니다.')

# 1~9단 만들기


while True:
    dan = int(input('구구단 몇 단을 계산할까요(1~9)? : '))
    if 1 <= dan and dan < 10:
        print(f'구구단 {dan}단을 계산합니다.')
        for i in range(1,10):
            print(f'{dan} x {i} = {dan*i}')
    elif dan ==0:
        print('구구단 게임을 종료합니다.')
        break
    else:
        print('잘못 입력하셨습니다.')



■ 디버깅
문법적 오류, 논리적 오류



■ String and advanced function concept

import sys

>>> a = "Artificial Intelligence and Machine Learning"
>>> print (a[0:6], " AND ", a[-9:]) # a 변수의 0부터 5까지, -9부터 끝까지
Artifi AND Learning
>>> print (a[:]) # a변수의 처음부터 끝까지
Artificial Intelligence and Machine Learning
>>> print (a[-50:50]) # 범위를 넘어갈 경우 자동으로 최대 범위를 지정
Artificial Intelligence and Machine Learning
>>> print (a[::2], " AND ", a[::-1]) # 2칸 단위로, 역으로 슬라이싱
Atfca nelgneadMcieLann AND gninraeL enihcaM dna ecnegilletnI laicifitrA

title = "TEAMLAB X Upstage"
title.title()
title.isdigit()
title.count('a')

# '를 str로 쓸때
a = 'It\'s OK'
a

raw_string = r'이제 그만 \n할래'
raw_string


f = open("c:/data/yesterday.txt", 'r')
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()
print()

n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY") # 대소문자 구분 제거
print ("Number of a Word 'Yesterday'" , n_of_yesterday)

■ function2

call by value

call by reference
-
def f(x), a=7, f(a) -> x 바뀌면 a 한테도 영향을 줘버려


파이썬은 call by object reference
파이썬은 객체의 주소가 함수로 전달되는 방식
전달된 객체를 참조하여 변경 시 호출자에게 영향을 주나,
새로운 객체를 만들 경우 호출자에게 영향을 주지 않음
def spam(eggs):
    eggs.append(1) # 기존 객체의 주소값에 [1] 추가
    eggs = [2, 3] # 새로운 객체 생성 -> 관계가 끊김
ham = [0]
spam(ham)
print(ham) # [0, 1]


# swap
list_ex = [1,2,3,4,5]
def swap_reference (list_ex, offset_x, offset_y):
    temp_list = list_ex[:] # 원래 있던 list_ex에 영향 줄 수 있으니까 항상 이렇게 값을 복사해놓고 작업하는게 좋아
    temp = list[offset_x]
    list[offset_x] = list[offset_y]
    list[offset_y] = temp

# scoping rule
변수의 범위
local variable, global variable

def test(t):
    print(x) # 함수 밖의 x, global
    t = 20 # 함수 안의 t, local # 여기서 t랑 x랑 연결고리 끊어짐
    print ("In Function :", t)
x = 10
test(x)
print(t) # 이거는 로컬 변수니까 안ㄴㅏ오지

#################################################

def f():
    s = "I love London!"
    print(s)
    
s = "I love Paris!"
f()
print(s) # 같은 s여도 local global 다름


###################################################
# 함수 안에서 글로벌 변수 사용할때

def f():
    global s
    s = "I love London!"
    print(s)
    
s = "I love Paris!"
f()
print(s)
























