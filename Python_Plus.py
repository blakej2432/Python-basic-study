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

import code
from ctypes import Structure
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


def calculate(x, y):
    total = x + y # 새로운 값이 할당되어 함수 내 total은 지역변수가 됨
    print ("In Function")
    print ("a:", str(a), "b:", str(b), "a+b:", str(a+b), "total :", str(total))
    return total

a = 5 # a와 b는 전역변수
b = 7
total = 0 # 전역변수 total
print ("In Program - 1")
print ("a:", str(a), "b:", str(b), "a+b:", str(a+b))

sum = calculate (a,b)
print ("After Calculation")
print ("Total :", str(total), " Sum:", str(sum)) # 지역변수는 전역변수에 영향 X


■ recursive function

def factorial(n):
    if n == 1:
            return 1
    else:
        return n * factorial(n-1)
        
print (factorial(int(input("Input Number for Factorial Calculation: "))))


■ function type hints

dynamic typing

def do_function(var_name: var_type) -> return_type:
    pass

def type_hint_example(name: str) -> str:
    return f"Hello, {name}"

■ function docstring

def type_hint_example(name: str) -> str:
    '''Returns the ~~~
        prameters : 
        returns : 
        examples : ''' # 이렇게 뭐하는 함수 인지 설명
    return f"Hello, {name}"


#### docstring generator 설치, 사용하기 ###########

함수 정의 밑에 쓰면 바로 이렇게 보여줌
# 위의 타입 힌트를 주고 닥스트링 넣으면 더 상세하게 다 만들어줘
# ctr + shift + p docsting 하면 바로 넣음
def calculate_rectangle_area(x , y):
    """_summary_

    Args:
        x (_type_): _description_
        y (_type_): _description_

    Returns:
        _type_: _description_
    """    
    result = x * y
    return result

rectangle_x = 10
rectangle_y = 20
print ("사각형 x의 길이: ", rectangle_x)
print ("사각형 y의 길이: ", rectangle_y)
# 넓이를 구하는 함수 호출
print ("사각형의 넓이: ", calculate_rectangle_area(rectangle_x, rectangle_y))

# 함수 이름 설정 가이드라인
verb_object()

def add_variables(x,y):
    return x + y
    
def add_variables(x,y):
    print (x, y) # 더한다는 함순데 출력을 해버리면 헷갈려
    return x + y

# 인자로 받은 값 자체 바꾸기 X, 내용 복사 선택

def count_word(string_variable):
    string_variable = list(string_variable)[:] # 내용만 복사하기. string_variable 자체를 변화시켜버릴수도 있으니까

# 규칙 -> 구글 python convention
# conda install flake8 : pep8에 맞게 오류 알려줌
# conda install black : pep8에 근접하게 오류 수정해줌

■ Data Structure

# stack (Last-in-first-out)
a = [1, 2, 3, 4, 5]
a

a.append(10)
a

c = a.pop()  # 10 출력
a.pop()은 return이 있음, a가 변함


word = input("Input a word : ")
word_list = list(word)
# print(word_list)
for _ in range(len(word_list)):
    print(word_list.pop())
    print(word_list)

# Queue (First-in-first-out)

a = [1, 2, 3, 4, 5]
a

a.append(10)
a

c = a.pop(0)  # 1 출력
a.pop(0)은 return이 있음, a가 변함


# tuple

t = 1  # 일반정수로 인식
type(t)

t = (1,)  # 값이 하나인 Tuple은 반드시 "," 를 붙여야 함
type(t)

# set
s = set([1, 2, 3, 1, 2, 3])  #  set 함수를 사용 1,2,3을 집합 객체 생성 , a = {1,2,3,4,5} 도 가능
s

a = {1, 2, 3, 4, 5}
type(a)

s.add(1)  #  한 원소 1만 추가,  추가, 중복불허로 추가 되지 않음
s
s.remove(1)  #  1 삭제
s

s.update([1, 4, 5, 6, 7])  #  [1,4,5,6,7] 추가
s

s.clear()  # 모든 원소 삭제

# dict

country_code = {}  # Dict 생성, country_code = dict() 도 가능
country_code = {"America": 1, "Korea": 82, "China": 86, "Japan": 81}
country_code

for dict_items in country_code.items():  # Dict 데이터 출력
    print(type(dict_items))

country_code["German"] = 49  # Dict 추가
country_code

for k, v in country_code.items():
    print("Key : ", k)
    print("Value : ", v)

import csv


def getKey(item):  # 정렬을 위한 함수
    return item[1]  # 신경 쓸 필요 없음


command_data = []  # 파일 읽어오기
with open("command_data.csv", "r", encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",", quotechar='"')
    for row in spamreader:
        command_data.append(row)

command_counter = {}  # dict 생성, 아이디를 key값, 입력줄수를 value값
for data in command_data:  # list 데이터를 dict로 변경
    if data[1] in command_counter.keys():  # 아이디가 이미 Key값으로 변경되었을 때
        command_counter[data[1]] += 1  # 기존 출현한 아이디
    else:
        command_counter[data[1]] = 1  # 처음 나온 아이디

dictlist = []  # dict를 list로 변경
for key, value in command_counter.items():
    temp = [key, value]
    dictlist.append(temp)

sorted_dict = sorted(dictlist, key=getKey, reverse=True)  # list를 입력 줄 수로  정렬
print(sorted_dict[:100])  # List의 상위 10객값만 출력

# 터미널 전체 실행 ctrl + ' 
# 실행 멈추기 ctrl + c

ㅁ deque

from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i)
print(deque_list)

deque_list.appendleft(10) # insert랑 같은거임
print(deque_list)

deque_list.rotate(2)
print(deque_list)
deque_list.rotate(2)
print(deque_list)

print(deque_list)
print(deque(reversed(deque_list)))

deque_list.extend([5, 6, 7])
print(deque_list)

deque_list.extendleft([5, 6, 7])
print(deque_list)

##########

from collections import deque
import time

start_time = time.clock()
deque_list = deque()
# Stack
for i in range(10000):
    for i in range(10000):
        deque_list.append(i)
        deque_list.pop()
# print(time.clock() - start_time, "seconds")
%timeit deque_list()

import time

start_time = time.clock()
just_list = []
for i in range(10000):
    for i in range(10000):
        just_list.append(i)
        just_list.pop()
# print(time.clock() - start_time, "seconds")
%timeit general_list()

ㅁ defaultdict

dict type의 값에 기본값을 지정

from collections import defaultdict


d = defaultdict(lambda: 0)  # Default 값을 0으로 설정합
print(d["first"])

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()

print(text)

word_count = {}
for word in text:
    if word in word_count.keys():
        word_count[word] += 1
    else:
        word_count[word] = 0
print(word_count)

word_count = defaultdict(object)  # Default dictionary를 생성
word_count = defaultdict(lambda: 0)  # Default 값을 0으로 설정합
for word in text:
    word_count[word] += 1
for i, v in OrderedDict(
    sorted(word_count.items(), key=lambda t: t[1], reverse=True)
).items():
    print(i, v)

ㅁ counter

from collections import Counter

ball_or_strike_list = ["B", "S", "S", "S", "S", "B", "B"]

c = Counter(ball_or_strike_list)  # a new counter from an iterable
c

# 다시 리스트 형태로 풀어내려면
list(c.elements())

# set처럼 활용 가능

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
# print(c + d)
# print(c & d)
print(c | d)

text = """A press release is the quickest and easiest way to get free publicity. If well written, a press release can result in multiple published articles about your firm and its products. And that can mean new prospects contacting you asking you to sell to them. Talk about low-hanging fruit!
What's more, press releases are cost effective. If the release results in an article that (for instance) appears to recommend your firm or your product, that article is more likely to drive prospects to contact you than a comparable paid advertisement.
However, most press releases never accomplish that. Most press releases are just spray and pray. Nobody reads them, least of all the reporters and editors for whom they're intended. Worst case, a badly-written press release simply makes your firm look clueless and stupid.
For example, a while back I received a press release containing the following sentence: "Release 6.0 doubles the level of functionality available, providing organizations of all sizes with a fast-to-deploy, highly robust, and easy-to-use solution to better acquire, retain, and serve customers."
Translation: "The new release does more stuff." Why the extra verbiage? As I explained in the post "Why Marketers Speak Biz Blab", the BS words are simply a way to try to make something unimportant seem important. And, let's face it, a 6.0 release of a product probably isn't all that important.
As a reporter, my immediate response to that press release was that it's not important because it expended an entire sentence saying absolutely nothing. And I assumed (probably rightly) that the company's marketing team was a bunch of idiots.""".lower().split()
Counter(text)

sorted(Counter(text).items(), key=lambda t: t[1], reverse=True)

print(Counter(text)["a"])

ㅁ namedtuple

from collections import namedtuple

# Basic example
Point = namedtuple("Point", ["x", "y"])
Point

p = Point(x=11, y=22)
p[0], p[1]

ㅁ pythonic code

.split('')
.join('')

# list comprehension

result = [i for i in range(10)]

result

result = [i for i in range(10) if i % 2 == 0]
result

# Nested loop
import pprint
word_1 = "Hello"
word_2 = "World"

pprint.pprint([i + j for i in word_1 for j in word_2])


result = [i + j for i in word_1 for j in word_2 if not(i==j)]

result = [i + j if not(i==j) else i for i in word_1 for j in word_2]

# two dimentional list

words = "The quick brown fox jumps over the lazy dog".split()
words

pprint.pprint([[w.upper(), w.lower(), len(w)] for w in words])


case_1 = ["A", "B", "C"]
case_2 = ["C", "E", "A"]

[i + j for i in case_1 for j in case_2]
[[i + j for i in case_1] for j in case_2] # 여기선 for j in case_2가 먼저 돌아
[[i + j for i in case_1 if j != 'C'] for j in case_2]

ㅁ enumerate, zip

for i, v in enumerate("ABC"):
    print("{0} \t {1}".format(i, v))

my_str = "ABCD"
{v: i for i, v in enumerate(my_str)}

text = "Samsung Group is a South Korean multinational conglomerate headquartered in Samsung Town, Seoul."
{i: v.lower() for i, v in enumerate(text.split())}

# zip
값을 병렬적으로 추출
alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

[[a, b] for a, b in zip(alist, blist)]
#     print(a, b)

math = (100, 90, 80)
kor = (90, 90, 70)
eng = (90, 80, 70)

[sum(value) / 3 for value in zip(math, kor, eng)]


alist = ["a1", "a2", "a3"]
blist = ["b1", "b2", "b3"]

for i, values in enumerate(zip(alist, blist)):
    print(i, values)


# lambda
(lambda x, y: x + y)(10, 50)

# pep8에서는 그냥 def 만드라고 하는데 아직도 lambda 많이 쓰여
 
# map


def f(x):
    return x + 5

ex = [1, 2, 3, 4, 5]
list(map(f, ex))

# 사실 위에 저거 보다는 리스트 내장 객체로 권장
[f(value) for value in ex]


f = lambda x, y: x + y
list(map(f, ex, ex))

# reduce

from functools import reduce

reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
x,y를 함수한 값을 다시 x로 잡고 계속 통합 계산

ㅁ iterable object
시퀀스형 데이터

# list of cities
cities = ["Seoul", "Busan", "Jeju"]
cities
memory_address_cities = iter(cities) # 메모리의 주소를 순서대로 가져온다고 보면됨
memory_address_cities

next(memory_address_cities)
next(memory_address_cities)
next(memory_address_cities)


# generator
def general_list(value):
    result = []
    for i in range(value):
        result.append(i)
    return result

print(general_list(50))

def generator_list(value):
    result = []
    for i in range(value):
        yield i # 메모리를 한번에 차지하고 있지 않고

for a in generator_list(50): # 이렇게 필요로 할때만 불러줌
    print(a)


gen_ex = (n * n for n in range(500))
print(type(gen_ex))

list(gen_ex)

ㅁ function arguments
# keyword arguments

def print_somthing(my_name, your_name, third_name):
    print("Hello {0}, My name is {1}".format(your_name, my_name))


print_somthing(third_name="abc", my_name="Sungchul", your_name="TEAMLAB") 
# 변수로 = "" 해주면 그에 맞게 들어감. 근데 "", "","" 이렇게 넣으면 순서대로 나오겠지

# default arguments
default 값을 함수 사용할때 ()안에 입력안해도 나온다.


ㅁ variable-length asterisk

함수의 parameter가 정해져있지 않을 때

가변인자
def asterisk_test(a, b, *args):
    print(list(args))
    print(type(args))
    return a + b + sum(args)


asterisk_test(1, 2, 3, 4, 5)

# keyword variable-length
parameter 이름을 따로 지정하지 않고 입력하는 방법

def kwargs_test_1(**kwargs):
    print(kwargs)
    print(type(kwargs))


kwargs_test_1(first=3, second=4, third=5) # 무슨변수를 쓰든 dict 타입으로 뽑아줘

# ex
def kwargs_test_3(one, two=3, *args, **kwargs):
    print(one + two + sum(args))
    print(two)
    print(args)
    print(kwargs)


kwargs_test_3(10, 300, 3,4,5,6,7,8, first=3, second=4, third=5)
# 기본적으로 키워드 형태 아닌 거(입력값만쓰는거) 먼저넣고, 키워드 정해진거 뒤

ㅁ asterisk *

unpacking 할 때도 씀 ############################

def asterisk_test(a, *args):
    print(a, *args)
    print(a, args)
    print(type(args))


test = (2, 3, 4, 5, 6)
asterisk_test(1, *test) # -> (1,2,3,4,5,6)


a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)

data = ([1, 2], [3, 4], [5, 6])
print(*data)


# keyword asterisk **

def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)


data = {"d": 1, "c": 2, "b": 3}
asterisk_test(10, **data)
# asterisk_test(10, b = 3 , c=2, d=1, e=56)


#############################################################

ㅁ object oriented programming

만들어 놓은 코드 재사용하고 싶다.
class에는 속성(정보) 와 행동(method)

class SoccerPlayer(object): # class명은 print_something 이렇게 안하고 붙여서
    def __init__(self, name: str, position: str, back_number: int): # 속성정보 -> __init__
        self.name = name
        self.position = position
        self.back_number = back_number

    def __str__(self): # __str__ : print(객체)를 사용했을 때 이걸 return
        return "Hello, My name is %s. My back number is %d" % (
            self.name,
            self.back_number,
        )

    def __add__(self, other): # __add__ : 두 객체 더했을 때 시행되는
        return self.name + other.name


abc = SoccerPlayer("son", "FW", 7) # 객체 생성
park = SoccerPlayer("park", "WF", 13)

# https://corikachu.github.io/articles/python/python-magic-method : __str__같은 magic method 관련

class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경합니다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. My back number is %d" % (
            self.name,
            self.back_number,
        )

###### self 란 ###########
생성된 인스턴스 자신

choi = SoccerPlayer("Jinhyun", "mf", 10)
print(choi)

choi.change_back_number(7)
print(choi)

# 이렇게 할 수 있지만 권장하지 않음
choi.back_number = 20
print(choi)

# oop 만들기 - 노트북

class Note(object):
    def __init__(self, content = None):
        self.content = content
    def write_content(self, content):
        self.content = content
    def remove_all(self):
        self.content = ""
    def __add__(self, other):
        return self.content + other.content
    def __str__(self):
        return self.content


class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = 0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다")

    def get_number_of_pages(self):
        return len(self.notes.keys())

##############
# 만든거 사용하기

from teamlab_note import Note
from teamlab_note import NoteBook

my_notebook = NoteBook("팀랩 강의노트")
my_notebook

my_notebook.title

new_note = Note("아 수업 하기 싫다")
print(new_note)

print(new_note)

new_note_2 = Note("파이썬 강의")
print(new_note2)

new_note_2

my_notebook.add_note(new_note)
my_notebook.add_note(new_note_2, 100)

print(my_notebook.notes[1])

print(my_notebook.notes[100])

my_notebook.get_number_of_pages()

my_notebook.notes[2] = Note("안녕")

print(my_notebook.notes[2])

print(my_notebook.notes[2])


# OOP characteristics

상속(inheritace), 다형성(polymorphism), visibility 

# 상속

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "저의 이름은 {0} 입니다. 나이는 {1} 입니다".format(self.name, self.age)


class Korean(Person):
    pass

first_korean = Korean("Sungchul", 35)
print(first_korean)

########

class Person:  # 부모 클래스 Person 선언
    def __init__(self, name, age, gender):
        self.name = name  # 속성값 지정, 해당 변수가 클래스의 attribute임을 명확히하기 위해 self를 붙임
        self.age = age
        self.gender = gender

    def about_me(self):  # Method 선언
        print("저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다.")

    def __str__(self):
        return "저의 이름은 ", self.name, "이구요, 제 나이는 ", str(self.age), "살 입니다."


class Employee(Person):  # 부모 클래스 Person으로 부터 상속
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)  # 부모객체 사용 부모의 init 불러옴
        self.salary = salary
        self.hire_date = hire_date  # 속성값 추가

    def do_work(self):  # 새로운 메서드 추가
        print("열심히 일을 합니다.")

    def about_me(self):  # 부모 클래스 함수 재정의
        super().about_me()  # 부모 클래스 함수 사용
        print("제 급여는 ", self.salary, "원 이구요, 제 입사일은 ", self.hire_date, " 입니다.")

myPerson = Person("John", 34, "Male")
myPerson.about_me()

myEmployee = Employee("Daeho", 34, "Male", 300000, "2012/03/01")
myEmployee.about_me()

# polymorphism

draw(rectangle), draw(circle) # 같은 일을 하는데, 같은 이름인데 다른 역할 하게

class Animal:
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")

class Cat(Animal):
    def talk(self):
        return "Meow!"


class Dog(Animal): 
    def talk(self): # talk 같은데 return 다르게. 하는 일은 비슷
        return "Woof! Woof!"

animals = [Cat("Missy"), Cat("Mr. Mistoffelees"), Dog("Lassie")]

for animal in animals:
    print(animal.name + ": " + animal.talk())

# visibility

객체 안의 모든 정보를 보여줄 필요는 없음

캡슐화 혹은 은닉

class Product(object):
    pass

class Inventory(object):
    def __init__(self):
        self.items = []
        self.test = "abc"

    def add_new_item(self, product):
        if type(product) == Product:
            self.items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.items)


my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
my_inventory


class Inventory(object):
    def __init__(self):
        self.__items = [] # __items -> 외부에서 접근 못함

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)


class Inventory(object):
    def __init__(self):
        self.__items = [] # __items -> 외부에서 접근 못함

    def add_new_item(self, product):
        if type(product) == Product:
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invalid Item")

    def get_number_of_items(self):
        return len(self.__items)

    @property
    def items(self): # 함수명을 attribute 명 처럼 사용하게 해줌
        return self.__items # 외부에선 접근 안되지만 내부에선 접근할 수 있게 @property


ㅁ decorator

# first class object 
일급함수, 일급객체
변수나 데이터 구조에 할당이 가능한 객체
파라메터로 전달 가능 , 리턴값으로 사용

def formula(method, argument_list):
    return [method(value) for value in argument_list]

argument_list = [1,2,3,4,5]

# inner function
내재함수

def print_msg(msg):
    def printer():
        print(msg)
    printer()

print_msg("Hello, Python")

def print_msg(msg):
    def printer():
        print(msg)
    return printer

another = print_msg("Hello, Python")
another()






def star(func):
    def inner(*args, **kwargs):
        print(args[1] * 30)
        func(*args, **kwargs)
        print(args[1] * 30)

    return inner


@star
def printer(msg, mark):
    print(msg)

printer("Hello", "*")



def generate_power(exponent):
    def wrapper(f):
        def inner(*args):
            result = f(*args)
            return exponent ** result

        return inner

    return wrapper


@generate_power(2)
def raise_two(n):
    return n ** 2

print(raise_two(7))




