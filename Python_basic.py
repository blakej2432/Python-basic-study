import copy
import keyword
import math
PYTHON
1990년 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어
interpreter language(인터프리터 언어): 한줄씩 소스코드를 해석해서 바로
실행해 결과를 확인할 수 있는 언어

특징
1. 문법이 쉽다.
2. 가독성이 좋다.
3. 무료이다.
4. 이식성이 좋다.
    - 쉽게 라이브러리를 추가할 수 있다.
    - 운영체제에 종속되지 않습니다.
5. 풍부한 라이브러리
    - numpy: 수학, 과학 모듈
    - pandas: 데이터 검색 모듈
    - matplotlib: 시각화 모듈
    - beautiple soup: 웹스크래핑 모듈
    - scikit-learn: 머신러닝 모듈
6. 동적 타이밍
    - 런타임시에 type 을 체크하는 동적타이밍을 지원
    - 메모리 관리를 자동

print("오늘 하루도 행복하자")

# 주석
'''
'''

"""
여러행 주석
"""

# 사칙연산
1+2
2-1
2*3
7/2
7//2  # 몫
7 % 2  # 나머지
2**3  # 제곱연산

math.pow(2, 3)
type(math.pow(2, 3))
type(2**3)

# 변수
- 첫글자 영문, (한글), _(밑줄)
- 두번째 글자 부터는 영문, 한글, 숫자, _
- 대소문자 구분한다.
- 예약어는 사용할 수 없다.
"""
"""


keyword.kwlist

type(keyword.kwlist)

x = 10
x
type(10)
dir()  # 메모리에 생성되어 있는 객체 확인
del x

f = 10.
type(f)  # float, 실수형, 부동소숫점

e = 10.4e3  # 지수 표현
e
10.4 * 10**3


# 연산자 축약

x = 1
x = x + 1
x += 1
x
x -= 1
x
x *= 1
x
x //= 1
x
x %= 1

[문제1] x, y 변수에 있는 값을 기준으로 수행한 결과 입니다.
x 와 y 변수에 어떤 값이 있어야 하나요.
또한 결과값이 나오기 위해서 어떤 계산식을 만들어야 하는지 계산식을 만들어 보세요.

result_1 = 7
result_2 = 3
result_3 = -3
result_4 = 10
result_5 = 0.4
result_6 = 0
result_7 = 2
result_8 = 32
result_9 = 7.0
result_10 = -21
result_11 = 50
result_12 = 29

x = 2
y = 5

x + y
y - x
x - y
x * y
x / y
x // y
x % y
x ** y
(x*y)/x + x
(x+y)*(x-y)
(y**x)*x
(x**2)+(y**2)

# 논리연산자
x = 1
y = 2
x == y  # 같다
x != y  # 같지 않다
x > y  # 크다
x >= y  # 크거나 같다
x < y  # 작다
x <= y  # 작거나 같다

True and True
True and False
True or True
True or False
type(not True)  # bool

# 문자열
str = "대한민국"
type(str)

str = '대한민국'
str

str = '''대한민국
짝짝짝'''
str

str = """대한민국
짝짝짝"""
str


# escape code
# \n 줄바꿈

str = '대한민국\n짝짝짝'
str

print(str)

# \t 줄바꿈
str = '대한민국\t짝짝짝'
print(str)

# \0 = NULL
str = '대한민국\0짝짝짝'
str
print(str)

str = "대한민국'짝짝짝'"
str
print(str)


# \' 문자로 표현
str = "대한민국\"짝짝짝\""
str
print(str)

x = "홍길동"
y = "파이썬 개발자"

x + y
x + ' ' + y  # 문자 + 문자 = 문자, 연결연산자

(x + ' ' + y) * 100  # 문자 복제

print("*"*100)

x = "홍길동"
y = "발라드"

# {} 위치
print("안녕하세요,{}입니다. 즐겨 듣는 음악은 {}입니다.".format(x, y))

"안녕하세요,{}입니다. 즐겨 듣는 음악은 {}입니다.".format(x, y)
z = "안녕하세요,{}입니다. 즐겨 듣는 음악은 {}입니다.".format(x, y)
z

"안녕하세요, "+x+"입니다. 즐겨 듣는 음악은 "+y+"입니다."

# %s 문자의 위치
z = "안녕하세요,%s입니다. 즐겨 듣는 음악은 %s입니다." % (x, y)
z

z = "안녕하세요,%s입니다. 즐겨 듣는 음악은 %s입니다." % ('제임스', '락')
z

# 문자랑 숫자를 연산할 수 는 없다
x = 100
"문자" + x + "문자"

x = "100"
"문자" + x + "문자"

# 문자 사칙연산(+) 문자 = 연결연산자
# 문자 사칙연산(+) 숫자 = 오류

x = 996
y = 8

quotient = x//y
remainder = x % y

print("{}를 {}로 나누면 몫은 {}이고 나머지는 {}입니다."
      .format(x, y, quotient, remainder))

print("%s를 %s로 나누면 몫은 %s이고 나머지는 %s입니다."
      % (x, y, quotient, remainder))

# %d 숫자
print("%d를 %d로 나누면 몫은 %d이고 나머지는 %d입니다."
      % (x, y, quotient, remainder))

divmod(x, y)
type(divmod(x, y))  # tuple 자료형

q, r = divmod(x, y)
q
r

print("%d를 %d로 나누면 몫은 %d이고 나머지는 %d입니다."
      % (x, y, q, r))

print("원주율은 %s" % 3.141592)
print("원주율은 {}".format(3.141592))
print("원주율은 %d" % 3.141592)  # %d는 정수로 수행된다.
print("원주율은 %f" % 3.141592)  # %f는 실수로 수행된다.

x = "행복한 하루를 보내자"
len(x)  # 문자의 길이

# 인덱싱, 슬라이싱
x[0]
x[1]
x[-1]
x[-2]

x[:]
x[0:3]  # [이상 : 미만] #########주의######
x[4:]
x[4:-5]

x = '0123456789'
x
x[::1]
x[::2]
x[::3]  # 증가분 표현
x[0:7:2]
x[1:9:2]
x[5::2]
x[::-1]  # 역순으로 출력

x = '파리썬'
x[1] = '이'  # 인덱스 번호를 이용해서 문자를 수정할 수 없다.
x[0]+'이'+x[2]

# 문자함수
x = '파리썬'
x.replace('리', '이')  # 문자를 치환하는 함수
x = x.replace('리', '이')  # 이렇게 새로 넣어줘야 함
x

x = '파리썬 파리썬'
x = x.replace('리', '이')  # 전부 수정
x

# 원본 문자열이 입력한 문자로 시작하는 지 판단하는 함수
x = 'hello world'
x[0] == 'h'
x.startswith('h')

x[0] == 'H'
x.startswith('H')


# 원본 문자열이 입력한 문자로 끝나는 지 판단하는 함수
x = 'hello world'
x[len(x)-1] == 'd'
x[-1] == 'd'

x.endswith('d')

x[-2:] == 'ld'
x.endswith('ld')

x = 'hello world'
x.find('w')

# 원본문자열에서 입력한 문자가 존재하는 위치를 찾는 함수
x[x.find('w')]
x.find('W')  # 없으면 -1로 리턴한다
x.find('world')
x.find('o')
x.find('o', 0)
x.find('o', 5)
x.find('o', 8)

# index도 찾는 함수지만, 없으면 오류로 리턴
x.index('o')
x.index('o', 5)
x.index('o', 8)  # 찾는 문자열이 없으면 오류 발생

# 입력한 문자열이 몇 번 나오는지를 리턴하는 함수
x.count('o')
x.count('l')

# 변수에 문자열이 있으면 True 없으면 False를 리턴해야 한다면
x.find('o') >= 0
x.find('O') >= 0

'o' in x
'O' in x

x = "hello world"
x.upper()  # 대문자로 리턴하는 함수
x.lower()  # 소문자로 리턴하는 함수
x.capitalize()  # 첫글자 대문자 나머지는 소문자로 리턴하는 함수
x.title()  # 공백문자를 기준으로 단어 별로 첫글자 대문자 나머지는 소문자

x = "Hello World"
x.swapcase()  # 대문자 -> 소문자, 소문자 -> 대문자

# 자리수를 고정 시킨 후 문자열을 중앙, 왼쪽, 오른쪽에 배치하는 함수
x.center(20)
x.ljust(20)
x.rjust(20)

x = '     hello    '
x
len(x)

# 양쪽, 왼쪽, 오른쪽 공백을 제거하는 함수
x.strip()  # x.strip(' ') 이거랑 같게 된다
x.lstrip()
x.rstrip()

x.strip(' ')
x.lstrip(' ')
x.rstrip(' ')

# 접두, 접미 부분에 문자열 제거
x = 'whellow'
x.strip('w')
x.lstrip('w')
x.rstrip('w')

x = 'hello'
y = 'hello2022'
z = '안녕하세요'

# 문자열 안에 알파벳, 한글로만 이루어져 있는지 확인하는 함수
x.isalpha()
y.isalpha()
z.isalpha()

# 문자열 안에 알파벳, 한글, 숫자로 이루어져 있는지 확인하는 함수
x.isalnum()
y.isalnum()
z.isalnum()

# 문자열 안에 숫자로만 이루어져 있는지 확인하는 함수
x.isnumeric()
y.isnumeric()
z.isnumeric()

d = '2022'
d.isalpha()
d.isalnum()
d.isnumeric()

# 문자 분리하기, 분할하는 함수
x = 'hello,world'
x.split(',')

x = 'hello world'
x.split(' ')

# 문자열 사이에 문자 넣기
x = 'abc'
','.join(x)

z = ','.join(x)
z.split(',')

z = ' '.join(x)
z.split(' ')

x = "a b c d e f g"
[문제2] x 변수의 문자의 갯수를 구하세요.
len(x)

[문제3] x 변수의 공백문자의 갯수를 구하세요.
x.count(' ')

[문제4] x 변수의 공백문자를 제외한 갯수를 구하세요.
x = x.replace(' ', '')
len(x)
len(x.replace(' ', ''))

답
len(x) - x.count(' ')


[문제5] x 변수에 있는 공백문자를 제거한 후 y변수에 입력해주세요
y = x.replace(' ', '')

[문제6] y 변수에 있는 문자를 분리한 후 z변수에 입력해주세요.
z = ' '.join(y)
z = z.split(' ')
z

답
z = ' '.join(y).split(' ')

''.join(z)  # 붙이기

url = 'http://www.python.org'
[문제7] http: // 제거한 후 url 변수에 입력해 주세요.
url = url.replace('http://', '')

답
url = url.lstrip('https://')

[문제8] url변수에 있는 문자 데이터에 '.'을 기준으로 분리하세요.
url = url.split('.')

[문제9] url변수에 있는 문자데이터를 www.python.org 모양으로 만드세요.
url = '.'.join(url)

[문제10] url변수에 있는 문자데이터를 대문자로 변환하세요.
url.upper()

[문제11] url변수에 있는 문자데이터를 소문자로 변환하세요.
url.lower()

■ python 자료형
1. list  # R에서 벡터가 파이썬 list
- 데이터의 목록을 다루는 자료형
- 서로 다른 데이터 타입을 가질 수 있는 자료형
- 중첩할 수 있다
- []
- list()

x1 = []
type(x1)

x2 = list()
type(x2)

x = [10, 20, 30]
x
type(x)
len(x)

x[0]
x[1]
x[2]
x[-1]

x[0:2]
x[1:]
x[:-1]

# 리스트 값 수정
x[0] = 100
x[1:3] = [200, 300]
x

# 리스트에 값을 추가
x.append(400)
x

# 기존 리스트 변수에 다른 리스트 변수를 이어 붙이는 함수

x1 = [600, 700]
x.extend(x1)
x

# 인덱스를 이용해서 특정한 위치에 값을 입력하는 함수
x[4]
x.insert(4, 500)
x

x2 = [800, 900, 1000]

x
x2

# 서로 다른 리스트를 결합
x + x2

z = x + x2
z

# 마지막 값 제거하기
z[:-1]
del z[-1]
z

z.pop()
z

# 특정한 인덱스에 있는 값을 제거하는 방법

del z[2]
z.pop(2)
z

drink = ['콜라', '사이다', '콜라', '환타', '사이다', '콜라']
len(drink)
drink.count('콜라')
drink.find('콜라')  # 리스트 변수에서는 find 함수 사용 불가
drink.index('콜라')
drink.index('콜라', 1)
drink.index('콜라', 3)
drink.index('콜라', 6)

del drink[drink.index('콜라')]

drink.pop(drink.index('콜라'))
drink.pop(drink.index('콜라', 1))
drink.pop(drink.index('콜라', 3))
drink.pop(drink.index('콜라', 6))

# 리스트 변수에 있는 값을 제거 하는 방법
drink.remove('콜라')
drink

drink.remove('콜라')
drink.remove('콜라')
drink.remove('콜라')

# 중첩 리스트
x = [1, 2, 3, ['a', 'b', 'c'], 4, 5, 6]
x

type(x)
type(x[0])
type(x[3])
x[3][0]
x[3][0:2]

x[3].append('d')
x[3].pop()
x[3][0] = x[3][0].upper()
x
x[3][1] = x[3][1].upper()
x

# 리스트 변수값을 아예 지우는 함수
x.clear()
x

x.append(1)
x
x.append(2)

dir()
id(x)  # 메모리주소

del x  # 변수 삭제

# 리스트 변수 안에 값을 기준으로 오름차순 정렬
x = [1, 5, 3, 4, 2]
x.sort()  # 미리보기 아님. 바로 적용
x

# 리스트 변수 안에 값을 기준으로 내림차순 정렬
x = [1, 5, 3, 4, 2]
x.sort(reverse=True)  # 미리보기 아님. 바로 적용
x

# 리스트 변수 안에 값을 기준으로 오름차순 정렬
x = [1, 5, 3, 4, 2]
sorted(x)  # 미리보기
x

# 리스트 변수 안에 값을 기준으로 내림차순 정렬
x = [1, 5, 3, 4, 2]
sorted(x, reverse=True)  # 미리보기
x

# 리스트 변수값을 역순으로 출력
x = [1, 5, 3, 4, 2]
x = x[::-1]  # 미리보기
x

# 리스트 변수값을 역순으로 출력
x = [1, 5, 3, 4, 2]
x.reverse()  # 바로적용
x

king = [['주몽', '유리왕', '대무신왕'], ['태종무열왕', '경덕왕'], ['온조왕', '개로왕']]
[문제12] 1번 인덱스에 '원성왕' 추가하세요.
king[1].append('원성왕')

[문제13] 2번 인덱스에 '무왕' 추가하세요.
king[2].append('무왕')

[문제14] 0번 인덱스에 '대무신왕' 추가하세요.
king[0].append('대무신왕')

[문제15] 0번 인덱스에 '미천왕', '미천왕', '광개토대왕' 한꺼번에 추가하세요.
king[0].extend(['미천왕', '미천왕', '광개토대왕'])
king[0]


[문제16] 2번 인덱스에 2번 위치에 '성왕' 추가하세요.
king[2].insert(2, '성왕')
king[2]

[문제17] '미천왕' 건수를 세어주세요.
king.count('미천왕')  # 중첩되어 있는 것은 셀 수 없다

king[0].count('미천왕')
king[1].count('미천왕')
king[2].count('미천왕')


[문제18] 0번 인덱스만 오름차순 정렬해주세요.
king[0].sort()


[문제19] 1번 인덱스만 내림차순 정렬해주세요.
king[1].sort(reverse=True)

[문제20] 0번 인덱스에 마지막 데이터를 삭제해주세요.
king[0].pop()

del king[0][len(king[0])-1]

2. tuple
- 리스트와 유사하지만 수정, 삭제, 추가 할 수 없다
- ()

lst = []
type(lst)

tuple1 = ()
type(tuple1)

tuple2 = 10, 20
type(tuple2)

tuple3 = 10
type(tuple3)

tuple3 = (10)  # 하나의 값은 이렇게 해도 int로 들어감
type(tuple3)

tuple3 = (10,)  # 하나만 tuple로 넣기
type(tuple3)

tuple4 = (1, 2, 3, 4, 5)
tuple5 = ('a', 'b', ('ab', 'bc'))
tuple6 = (1, 2, ('ab', 'bc'))

x = (1, 2, 3)
y = (4, 5, 6)
z = x + y  # 여러 tuple을 하나로 결합

z[0] = 10  # tuple은 수정 X

z.sort()  # 정렬도 X
z.reverse()  # X

###### tuple에서 가능한 것들 ########
sorted(z)  # tuple에서 정렬하려면 sorted 수행, list형으로 바뀜
z[::-1]  # 역순

x = 1, 2, 3
type(x)
one, two, three = x
one
two
three

lst = [1, 2, 3]
lst
x = lst[0]
y = lst[1]

x, y = lst[0:2]
x
y

3. dictionary
- key, value 값을 가지는 자료형
- {}
- {key1: value1, key2: value2, , , , }

dic = {}
type(dic)

dic = {'이름': '홍길동', '전화번호': '010-1000-1004', '주소': '서울'}
dic['이름']
dic['전화번호']
dic.keys()
dic.values()
dic.items()

sports = {'축구': '메시', '농구': '하든', '야구': '박찬호'}
sports['축구']
sports['컬링'] = '김영미'
sports
sports['컬링'] = ['김영미', '김은정', '김경애', '김선영', '김초희']
sports

sports['농구']
sports.get('농구')

sports['골프']  # 키가 없으면 오류
sports.get('골프')  # 키가 없으면 none, 아무것도 일어나지 않음

'농구' in sports.keys()
'골프' in sports.keys()
'메시' in sports.values()
'김영미' in sports.values()
['김영미', '김은정', '김경애', '김선영'] in sports.values()  # 하나라도 빠져있으면 False

del sports['야구']  # key, value 삭제
sports

sports['축구'] = []  # value 값 삭제
sports['축구'] = ''
sports

sports['축구'] = '손흥민'  # value값 수정
sports

v = sports.values()
type(v)
list(v)  # list 자료형으로 변환

list(sports.keys())
list(sports.items())

4. set
- 집합
- 리스트와 비슷. 단, 인덱스가 없다
- 중복을 허용하지 않음
- {}
- set()


s = {1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5}
s
s[0]  # 순서가 없어서 오류

lst = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5]
lst.count(1)
set(lst)
list(set(lst))

x = {1, 2, 3, 6}
y = {1, 2, 3, 4, 5}

# 합집합
x.union(y)
y.union(x)
x | y


x = [1, 2, 3, 6]
y = [1, 2, 3, 4, 5]

set(x).union(set(y))  # 다른 변수들은 union 할 수 없다. set으로 수정해야 함
set(y).union(set(y))
set(x) | set(y)

x = {1, 2, 3, 6}
y = {1, 2, 3, 4, 5}

# 교집합
x.intersection(y)
x & y

# 차집합
x.difference(y)
x-y

y.difference(x)
y-x

# 대칭 차집합(symmentric difference)
x-y | y-x
x.symmetric_difference(y)

x ^ y

# 서로소 집합 (disjoint set) : 두 집합에 공통된 원소가 없는 집합
{1, 2, 3}.isdisjoint({1, 2, 3})
{1, 2, 3}.isdisjoint({4, 5, 6})

# 부분집합(subset)
{1, 2, 3}.issubset({1, 2, 3, 4})
{1, 2, 3} <= {1, 2, 3, 4}
{5, 6, 7} <= {1, 2, 3, 4}

x = {1, 2, 3}
y = {1, 2, 3, 4}
x <= y

x.issubset(y)  # 부분집합인지 확인하는 함수
y.issuperset(x)  # 상위집합인지 확인하는 함수

1 in x
7 in x

x.remove(1)  # 집합에 있는 값을 삭제
x.add(1)  # 집합에 하나의 값을 추가
x.add([8, 9])  # 오류
x.update([8, 9])  # 집합에 여러개의 값을 추가
# 집합에 있는 값을 수정 할 수는 없기 때문에 지우고 다시 추가해야 한다

l = []
type(l)
t = ()
type(t)

5. bool
- 참(True), 거짓(False)을 나타내는 자료형

x = True
y = False
type(x)
type(y)

# 조건제어문에서 True 표현 방법
bool(1)
bool(100)
bool(-1)
bool('홍길동')
bool('python')
bool([1, 2, 3])
bool((1, 2, 3))
bool({1, 2, 3})
not 0
not None


# 조건제어문에서 False 표현 방법
bool(0)
bool(None)
bool([])
bool(())
bool({})
bool('')
bool("")
not 1
not -1

■ 파이썬 변수 복제 주의
x = [1, 2, 3]
y = x  # x변수와 y변수는 동일한 메모리 공간을 사용한다. y가 계속 x를 참조하고 있어
y
x[0] = 10  # x에서 변경하면 y도 변경돼
x
y

x = [1, 2, 3]  # x변수를 복제하지만 다른 메모리 공간을 사용한다.
z = x[:]
id(x)
id(z)
x[0] = 10
z

w = copy.deepcopy(x)  # 다른 메모리 공간에 복제하기
w

■ input()
- 사용자로부터 입력을 받아들여 프로그램에게 전달하는 함수
- *문자형 * 으로 전달된다.

x = input()
x

type(x)

y = input()
y
x + y  # 문자열 결합

int(x) + int(y)

x = int(input())
y = int(input())
x+y

■ 조건제어문
1. if문

if 조건문:
    True 일 때 수행해야 할 문장

if 조건문:
    True 일 때 수행해야 할 문장
else:
    False 일 때 수행해야 할 문장

x = 20
if x == 10:
    print("오늘 하루도 10배 행복하자")
else:
    print("오늘 하루도 {}배 행복하자".format(x))

if 1:
    print('참')
else:
    print('거짓')

if 0:
    print('참')
else:
    print('거짓')

if [1, 2]:
    print('참')
else:
    print('거짓')

if []:
    print('참')
else:
    print('거짓')

if True:
    print('참')
else:
    print('거짓')

x = 12
if x > 10 and x % 2 == 0:
    print('참')
else:
    print('거짓')

x = 0
if x > 10 and x % 2 == 0:
    print('참')
else:
    print('거짓')

x = 4
if x > 10 or x % 2 == 0:
    print('참')
else:
    print('거짓')

num = int(input("점수를 입력해주세요: "))

num

if 90 <= num < 100:
    grade = 'A'
elif 80 <= num < 90:
    grade = 'B'
elif 70 <= num < 80:
    grade = 'C'
elif 60 <= num < 70:
    grade = 'D'
else:
    grade = 'F'

print("학점은 " + grade)
print("학점은 {}".format(grade))

[문제21] 숫자를 입력값으로 받아서 그 값이 짝수면 짝수, 홀수면 홀수를 출력해세요.


if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

답

if int(input("숫자를 입력하세요: ")) % 2 == 0:
    print("짝수")
else:
    print("홀수")

num = int(input("숫자를 입력하세요: "))
if num % 2 == 0:
    print('짝수')
else:
    print('홀수')

[문제22] 한글, alphabet만 입력받아서 문자를 출력하고 아니면 "다른 문자가 포함되어 있습니다"를 출력해주세요.
al = input()
if al.isalpha() == True:
    print(al)
else:
    print("다른 문자가 포함되어 있습니다")

답
var = input("문자를 입력하세요 : ")
if var.replace(" ", "").isalpha():
    print(var)
else:
    print("다른 문자가 포함되어 있습니다")  # 공백문자가 들어있으면 False가 나온다.

var.replace(" ", "").isalpha()


[문제23] 숫자를 입력값으로 받아서 숫자면 입력받은 숫자를 출력하고 아니면 "숫자 이외의 문자가 포함되어 있습니다" 출력해주세요.
num = "100"
if num.isnumeric() == True:
    print(num)
else:
    print("숫자 이외의 문자가 포함되어 있습니다")

답
num = input("숫자를 입력하세요 : ")

if num.isnumeric():
    print(num)
else:
    if num == "":
        print("입력값이 없습니다.")
    else:
        print("숫자 이외의 문자가 포함되어 있습니다.")

num = ''
num == ''  # 빈 문자열인지 보는 방법
num == ""
num == None  # None은 아예 없는거
num

x = None
x == None
x

if x == None:
    print('참')
else:
    print('거짓')

if x is None:
    print('참')
else:
    print('거짓')

num = 1

num.isnumeric()  # isnumeric() 함수는 문자 변수에서 숫자를 체크하는 함수

isinstance(num, int)

num = '1'
isinstance(num, int)

f = 1.2
isinstance(f, int)
isinstance(f, float)
isinstance(f, str)
dir()
del str

b = True
isinstance(b, bool)
isinstance(b, str)

x = [1, 2]
y = [2, 1]

x == y  # 인덱스 끼리 비교하는 거임
x[0] == y[0] and x[1] == y[1]

set(x) == set(y)  # 값 비교 -> 집합으로 바꿔서 비교

sal = 1000
comm = None
sal * comm

if comm is None:
    annual = sal * 12
else:
    annual = sal * 12 + comm

print(annual)

# 위에껄 한 줄로 만들기 이렇게
# 참값 if 조건 else 거짓

sal * 12 if comm is None else sal * 12 + comm
annual = sal * 12 if comm is None else sal * 12 + comm
print(annual)

■ 반복문

1. while 문
- 조건이 True 인 동안에 반복을 수행한다.

while 조건문:
    반복수행 할 문장

i = 0
while i <= 10:
    print(i)
    # i = i +1
    i += 1

[문제24] 1부터 100까지 합을 구하세요.

i = 1
z = 0
while i <= 100:
    z = z + i
    i += 1
    print(z)

답

i = 1
hap = 0
while i <= 100:
    hap += i
    i += 1

print(hap)


[문제25] 1부터 100까지 3의 배수를 출력하고 합도 구하세요.

i = 1
z = 0
while i <= 10:
    if i % 3 == 0:
        print(i)
        i += 1


답

i = 1
hap = 0
while i <= 100:
    if i % 3 == 0:
        print(i)
        hap += i
    i += 1

print(hap)

두번째 답

i = 0
hap = 0
while i <= 100:
    i += 3
    if i >= 100:
        break  # 반복문을 중단하는 함수
    else:
        print(i)
        hap += i

print(hap)


[문제26] 1부터 10까지 홀수값만 출력해주세요.
i = 1
while i <= 10:
    if i % 2 != 0:
        print(i)
    i += 1

i = 1
while i <= 10:
    if i == 1:
        print(i)
        i += 2
    else:
        print(i)
        i += 2

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue  # 이 문을 만나면 다음 반복을 수행한다 R에서 next
    print(i)


i = 0
while True:
    if i == 0:
        i = 1
    elif i > 10:
        break
    print(i)
    i += 2

[문제27] 1부터 10까지 출력하세요. 단 4, 6은 제외하세요.
i = 0
while i < 10:
    i += 1
    if i in [4, 6]:
        continue
    print(i)

답
i = 1
while <= 10:
    if i != 4 and i != 6:
        print(i)
    i += 1

i = 1
while <= 10:
    if i == 4 and i == 6:
        i += 1
        continue
    else:
        print(i)
    i += 1


[문제28] 학생들의 점수가 90, 55, 63, 78, 80점이 있습니다. 60점 이상 이면 합격, 60점 미만이면 불합격 출력해 주세요.
score = [90, 55, 63, 78, 80]
i = 0
while i <= 4:
    if score[i] >= 60:
        print('합격')
    else:
        print('불합격')
    i += 1

답
score = [90, 55, 63, 78, 80]
i = 0
while i < len(score):
    if score[i] >= 60:
        print('합격')
    else:
        print('불합격')
    i += 1


# 하나씩 뽑아가지고 하는 방법 스택 알고리즘과 연관 (push & pop)
score = [90, 55, 63, 78, 80]
while score:
    v_s = score.pop()
    if v_s >= 60:
        print("점수 {} -> 합격".format(v_s))
    else:
        print("점수 {} -> 불합격".format(v_s))
score

[문제29] 아래화면과 같이 출력해주세요.
*
**
***
****
*****

i = 1
while i <= 5:
    print("*"*i)
    i += 1

답  # 곱셈 이용하지 않고 풀기
i = 1
while i <= 5:
    j = i
    v_star = ''
    while j > 0:
        v_star = v_star + '*'
        j -= 1
    print(v_star)
    i += 1

i = 1
while i <= 5:
    j = i
    while j > 0:
        print('*', end='')  # print를 가로로 이어붙이기
        j -= 1
    print()  # 다음 줄로 떨어뜨리기
    i += 1


[문제30] 반복횟수를 입력값으로 받아서 아래 화면과 같이 출력해주세요.

반복횟수를 입력해주세요: 5
*****
****
***
**
*

rep = int(input("반복횟수를 입력해주세요 : "))
while rep >= 1:
    print("*"*rep)
    rep -= 1

[문제31] 아래화면과 같이 수행 해보세요.
수를 입력해주세요: 5
*****

수를 입력해주세요: 4
****

수를 입력해주세요: 0
종료


num = int(input("수를 입력해주세요 : "))
if num == 0:
    print('종료')
else:
    print('*'*num)


답
while True:
    i = int(input("수를 입력해주세요 : "))
    if i == 0:
        print("종료")
        break
    else:
        print(i*'*')


[문제32] 단을 입력값으로 받아서 구구단을 출력해주세요.
dan = int(input("단을 입력하세요 : "))
i = 1
while i <= 9:
    print(dan, "*", i, "=", dan*i)
    i += 1

답
dan = int(input("단을 입력하세요 : "))
i = 1
while i <= 9:
    print("{} * {} = {}".format(dan, i, dan*i))
    i += 1

[문제33] 2단 ~ 9단까지 구구단을 출력해주세요.
j = 2
while j <= 9:
    i = 1
    while i <= 9:
        print(j, "*", i, "=", j*i)
        i += 1
    j += 1

답
j = 2
while j <= 9:
    i = 1
    while i <= 9:
        print("{} * {} = {}".format(j, i, j*i))
        i += 1
    j += 1


[문제34]  2단을 가로로 출력해주세요.
2 * 1 = 2    2 * 2 = 4    2 * 3 = 6    2 * 4 = 8    2 * 5 = 10   2 * 6 = 12   2 * 7 = 14   2 * 8 = 16   2 * 9 = 18

i = 1
while i <= 9:
    print(2, "*", i, "=", 2*i, end='   ')
    i += 1

답
i = 1
result = ''
while i <= 9:
    result = result + "{} * {} = {} ".format(2, i, str(2*i).ljust(5))
    i += 1

result


[문제35] 구구단을 가로로 출력해주세요.

2 * 1 = 2  3 * 1 = 3  ....
2 * 2 = 4  3 * 2 = 6  .....

j = 2
while j <= 9:
    i = 1
    while i <= 9:
        print(j, "*", i, "=", j*i)
        i += 1
    j += 1


j = 1
while j <= 9:
    i = 2
    while i <= 9:
        print(i, "*", j, "=", i*j, end='   ')
        i += 1
    print('\n')  # 이건 그냥 print()
    j += 1

답
i = 1
result = ''
while i <= 9:
    dan = 2
    while dan <= 9:
        result = result + "{} * {} = {} ".format(dan, i, str(dan*i).ljust(5))
        dan += 1
    result = result + '\n'
    i += 1

print(result)


[문제36] 구구단을 아래 화면과 같이 출력해주세요.
1 2 3 4 5 6 7 8 9
2 4 6 81012141618
3 6 9121518212427
4 812162024283236
51015202530354045
61218243036424854
71421283542495663
81624324048566472
91827364554637281

i = 1
result = ''
while i <= 9:
    dan = 1
    while dan <= 9:
        result = result + "{}".format(str(dan*i).rjust(2))
        dan += 1
    result = result + '\n'
    i += 1

print(result)


x = 'python'
"내가 좋아하는 프로그래밍 언어는 {}이다.".format(x)
"내가 좋아하는 프로그래밍 언어는 %s이다." % (x)

f"내가 좋아하는 프로그래밍 언어는 {x}이다."  # f를 붙이면 바로 변수값 넣기 가능
print(f"내가 좋아하는 프로그래밍 언어는 {x}이다.")

# 자리수 고정 시킨 후 왼쪽 정렬
x.ljust(10)
f'{x:10}'
f'{x:<10}'

# 자리수 고정시킨 후 오른쪽 정렬
x.rjust(10)
f'{x:>10}'

# 자리수 고정시킨 후 가운데 정렬
x.center(10)
f'{x:^10}'

i = 1
while i <= 9:
    dan = 1
    while dan <= 9:
        print(f'{dan*i:>2}', end='')
        dan += 1
    print()
    i += 1

2. for 문
리스트, 튜플, 문자열의 첫번째 값부터 마지막 값까지 순서대로 변수에 입력해서 반복수행

for 변수 in (리스트, 튜플, 문자열):
    반복수행할 문장

x = ['sql', 'r', 'python']
x

for i in x:
    print(i)

x = ('sql', 'r', 'python')
x

for i in x:
    print(i)

for i in 'python':
    print(i)

x = [(1, 2), (3, 4), (5, 6)]

for i, j in x:
    print(i)

for i, j in x:
    print(i, j)

for i, j in x:
    print(i+j)

[문제37] 학생들의 점수가 90, 55, 63, 78, 80점이 있습니다. 60점 이상 이면 합격, 60점 미만이면 불합격 출력해 주세요.
score = [90, 55, 63, 78, 80]  # for문 이용

for i in score:
    if i >= 60:
        print('합격')
    else:
        print('불합격')

range(시작, 끝(미만), 증가분)
list(range(1, 11, 1))
range(5)  # 시작점 안쓰면 0부터 시작, 증가분 디폴트 1

for i in range(1, 11, 1):
    print(i)

[문제38] 1부터 100까지 합을 구하세요.
hap = 0
for i in range(1, 101, 1):
    hap = hap + i
hap


[문제39] 1부터 10까지 합을 구하세요. 단, 4, 6 제외
hap = 0
for i in range(1, 11, 1):
    if i != 4 and i != 6:
        hap = hap + i
hap

hap = 0
for i in range(1, 11, 1):
    if i == 4 or i == 6:
        continue
        hap = hap + i
hap

hap

[문제40] 2단 ~ 9단까지 구구단을 출력하세요. 단, for문 이용

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        print(f'{i} * {j} = {i*j}')

답
for dan in range(2, 10, 1):
    for i in range(1, 10, 1):
        print(f'{dan} * {i} = {dan*i}')

[문제41]리스트 변수에 18, 2, 3, 1, 4, 5, 7, 8, 9, 10, 11, 15, 16 값이 들어 있습니다. 짝수만 합을 구하세요.
x = [18, 2, 3, 1, 4, 5, 7, 8, 9, 10, 11, 15, 16]


1) while문
i=0
hap=0
while i < len(x):
    if x[i] % 2 == 0:
        hap=hap + x[i]
    i += 1
print(hap)



2) for 문
hap=0
for i in x:
    if i % 2 == 0:
        hap += i

print(hap)

[문제42] 과일의 빈도수를 만들어 주세요.

fruit=("사과", "귤", "오렌지", "배", "포도", "바나나", "키위", "딸기", "블루베리", "망고",
         "수박", "사과", "귤", "키위", "포도", "바나나", "사과", "딸기", "블루베리", "망고",
         "사과", "귤", "오렌지", "배", "포도", "바나나", "사과", "딸기", "파인애플")

# 33
fruit.count('사과')
fruit.count('귤')

for i in set(fruit):
    print('{} : {}'.format(i, fruit.count(i)))

################################

result=''
for i in set(fruit):
    result=result + '{} : {}'.format(i, fruit.count(i)) + '\n'

print(result)
#################################

result=[]
for i in set(fruit):
    result.append((i, fruit.count(i)))  # 리스트 안에 튜플로 넣는거야

result

[문제43] 과일의 빈도수를 만들어 주세요. 딕셔러니 변수에 저장해주세요.

{'사과': 5,
 '귤': 3,
 '오렌지': 2,
 '배': 2,
 '포도': 3,
 '바나나': 3,
 '키위': 2,
 '딸기': 3,
 '블루베리': 2,
 '망고': 2,
 '수박': 1,
 '파인애플': 1}

fruit_dict={}
fruit_dict
fruit_dict.keys()
fruit_dict.values()


'사과' in fruit_dict.keys()
1. 만약 '사과' key 없으면
    fruit_dict['사과']=1
fruit_dict

2. 만약 '사과' key 있으면
    fruit_dict['사과']=fruit_dict['사과'] + 1

fruit_dict={}

for i in fruit:
    if i not in fruit_dict.keys():
        fruit_dict[i]=1
    else:
        fruit_dict[i]=fruit_dict[i] + 1

fruit_dict


fruit_dict={}
p = fruit_dict.get('사과',0)
fruit_dict['사과'] = p + 1
fruit_dict

fruit_dict={}
for i in fruit:
    p = fruit_dict.get(i,0)
    fruit_dict[i] = p + 1
fruit_dict

import collections
fruit_dict = collections.defaultdict(int)

for i in fruit:
    fruit_dict[i] = fruit_dict[i] + 1

fruit_dict




[문제44] data 변수에 있는 문장에서 공백 문자를 기준으로 분리한 후 빈도수를 구하세요. 단 딕셔러니 자료형을 이용하세요.
data="별 하나에 추억과 별 하나에 사랑과 별 하나에 쓸쓸함과 별 하나에 동경과 별 하나에 시와 별 하나에 어머니 어머니"

data=data.split(' ')
data_dict={}

for i in data:
    if i not in data_dict.keys():
            data_dict[i]=1
    else:
        data_dict[i]=data_dict[i]+1

data_dict

sorted(data_dict)
sorted(data_dict.keys())
sorted(data_dict.values())
sorted(data_dict.items())  # 키값을 기준으로 정렬

for k, v in sorted(data_dict.items()):
    print(k, v)

for k, v in sorted(data_dict.items(), reverse=True):
    print(k, v)

import operator

# 키를 기준으로 정렬
for k, v in sorted(data_dict.items(), key=operator.itemgetter(0)):
    print(k, v)

# 값을 기준으로 정렬
for k, v in sorted(data_dict.items(), key=operator.itemgetter(1)):
    print(k, v)


# collentions.Counter - 알아서 dictionary 형태로 바꿔준다
import collections

data_dict=collections.Counter(data)
data_dict.keys()

[문제45] x변수에 1부터 10까지 있습니다. y 변수는 x 변수의 값을 2곱한 값으로 입력해주세요.
x=list(range(1, 11))
x
y=[]
for i in x:
    y.append(i*2)
y

# 리스트 내장객체(list comprehension)
[표현식 for 변수 in 반복 가능한 자료형]
[i*2 for i in x]



[문제46] x변수에 apple, banana, orange  있습니다. 	이 값들의 문자의 길이를 출력해주세요.
x=['apple', 'banana', 'orange']
len(x)

for i in x:
    print(len(i))

[len(i) for i in x]

[문제47] lst1, lst2 변수를 생성한 후 아래화면 처럼 출력해주세요.
lst1=[1, 2, 3]
lst2=[4, 5, 6]
출력결과
[4, 5, 6, 8, 10, 12, 12, 15, 18]

for i in lst1:
    for j in lst2:
        print(i*j)

for i in lst1:
    for j in lst2:
        print(i*j, end=',')

lst3=[]
for i in lst1:
    for j in lst2:
        lst3.append(i*j)
lst3

[표현식 for 변수 in 반복 자료형 for 변수 in 반복 자료형]

[i*j for i in lst1 for j in lst2]

lst3=[7, 8, 9]
[i*j*z for i in lst1 for j in lst2 for z in lst3]

# 구구단도 이렇게 가능

[문제48] 1부터 100까지 짝수만 x 변수에 입력해주세요.

x=[i for i in range(1, 101) if i % 2 == 0]





[문제49] 튜플변수에 사과, 귤, 오렌지, 배, 포도, 바나나, 자몽, 키위, 딸기, 블루베리, 망고를 입력하시고
과일이름중에 세글자 이상인 과일만 fruit_lst변수에 입력해주세요.
fruit=('사과', '귤', '오렌지', '배', '포도', '바나나', '자몽', '키위', '딸기', '블루베리', '망고')
fruit_lst=[i for i in fruit if len(i) >= 3]

[문제50] 변수에 2, -1, 4, -10, 5, -9 가 있습니다.   음수값만 negative변수에 입력해주세요.
x=[2, -1, 4, -10, 5, -9]
negative=[i for i in x if i < 0]


[문제51] x 변수의 있는 값을 y 변수에 아래와 같이 저장하세요.
x=[2, -1, 4, -10, 5, -9]
y=[2, '음수', 4, '음수', 5, '음수']

[i if i >= 0 else '음수' for i in x]  # 이럴 땐 또 if문이 앞으로 나와
y=[]
for i in x:
    if i < 0:
        y.append('음수')
    else:
        y.append(i)

y

[문제52] apple단어를 아래 화면같이 출력해주세요.
 ['a', '*', '*', '*', 'e']

x='apple'
x=','.join(x)
x=x.split(',')
x
[i if i in ['a', 'e'] else "*" for i in x]

답
# 문자열을 리스트 만들 때 이거 굳이 join split 할 필요 없음
[i if i in 'ae' else "*" for i in 'apple']



[문제53] 과일판매 현황을 dictionary 변수로 생성하세요.
과일 이름을 키로 하고 수량은 값으로 표현한 후 과일이름만 대문자로 출력해주세요.
apple  100, banana  300, orange  300
fruit={'apple': 100, 'banana': 300, 'orange': 300}

[i.upper() for i in fruit.keys()]

[문제54] x 변수에 있는 값을 y 변수에 다음과 같이 입력해주세요
x=[[1, 5], [2, 6], [3, 7], [4, 8]]
y=[]
y=[[1, 2, 3, 4], [5, 6, 7, 8]]

temp=[]
for i in x:
    temp.append(i[0])
y.append(temp)



for r in range(2):
    temp=[]
    for i in x:
        temp.append(i[r])
    y.append(temp)
y

[i*j for i in range(2, 10) for j in range(1, 10)]

[i[r] for r in range(2) for i in x]  # 이렇게만 하면 중첩 구분 안되니까
[[i[r] for i in x] for r in range(2)]  # 이렇게 내장객체 안에 내장객체를 넣어서 중첩 구분 가능

[문제55] y 변수에 있는 값을 x 변수에 입력해주세요
y=[[1, 2, 3, 4], [5, 6, 7, 8]]
x=[[1, 5], [2, 6], [3, 7], [4, 8]]

y[0][0]
y[1][0]
-> x[0]

y[0][1]
y[1][1]

x=[]
for r in range(4):
    temp=[]
    for i in y:
        temp.append(i[r])
    x.append(temp)
x

[[i[r] for i in y] for r in range(4)]


■ 함수
- 반복되는 코드를 하나로 묶어서 처리하는 방법
- 기능의 프로그램

def 함수이름(인수, 인수, ...):
    수행할 문장
    ....
    [return 값]  # return은 옵션



함수이름()

def message():
    print("오늘 하루도 행복하자")

message()

def message():
    print("오늘 하루도 행복하자")
    return 'happy'

h=message()
h

def hap(arg1, arg2):
    return arg1+arg2

hap(10, 20)
hap('십', '이십')

[문제 56] 함수에 두개의 숫자를 인수값으로 받아서 값을 비교하는 함수를 생성하세요.
num_compare(10, 5)
10은 5보다 크다

num_compare(10, 10)
10과 10은 같다

def num_compare(arg1, arg2):
    if arg1 > arg2:
        print(f'{arg1}은 {arg2}보다 크다')
    elif arg1 == arg2:
        print(f'{arg1}과 {arg2}은 같다')
    else:
        print(f'{arg1}은 {arg2}보다 작다')

num_compare(5, 7)


def hap(arg1, arg2):
    return arg1+arg2

hap(10, 20)
hap(1, 2, 3, 4, 5)  # 인수 개수가 가변적인 경우

def 함수이름(*가변인수):
    for i in 가변인수:
        수행할 문장

def hap(*arg):
    total=0
    for i in arg:
        total += i
    return total

hap(1, 2, 3, 4, 5)

def 함수이름(인수1, *인수2):
    ..
    수행할 문장

[문제57] cal함수를 생성하세요.

cal('sum', 1, 2, 3, 4, 5)
cal('multiply', 1, 2, 3, 4, 5, 6, 7)

def cal(arg1, *arg2):
    if arg1.lower() == 'sum':
        total=0
        for i in arg2:
            total += i
    elif arg1.lower == 'multiply':
        total=1
        for i in arg2:
            total *= i
    else:
        total=None

    return total


cal('multiply', 1, 2, 3)
cal('sum', 1, 2, 3, 4)

cal('multiply', [1, 2, 3])  # 리스트 값으로 들어오면 안돼.

# 리스트 모양으로 넣고 싶으면 가변이 아니니까

def cal(arg1, arg2):
    if arg1.lower() == 'sum':
        total=0
        for i in arg2:
            total += i

    elif arg1.lower() == 'multiply':
        total=1
        for i in arg2:
            total *= i
    else:
        total=None

    return total

cal('multiply', [1, 2, 3])
cal('sum', [1, 2, 3])

[문제58] 여러 숫자를 인수값으로 받아서 합과 평균을 출력하는 aggF함수를 생성하세요.
aggF(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
합: 55
평균: 5.5

def aggF(*arg1):
    hap=0
    for i in arg1:
        hap += i
    avg=hap / len(arg1)
    print(f'합 : {hap}')
    print(f'평균 : {avg}')

aggF(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
aggF(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

def aggF(*arg):
    result=0
    cn=0
    for i in arg:
        result += i
        cn += 1
    print("합: ", result)
    print("평균: ", result/cn)

aggF(*[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 가변인수에 리스트를 넣고 싶으면 이렇게 해도 돼



# *arg : 여러개의 인수값을 받을 때 사용, 튜플 자료형
def f(*arg):
    print(type(arg))

f(1, 2, 3)
f(*[1, 2, 3])


# **kwargs( keyword arguments) : key - value 형태로 인수값을 받을 때 사용. 딕셔너리 자료형
def dict_f(**args):
    for k, v in args.items():
        print(f'{k} : {v}')

dict_f(firstname='길동', lastname='홍')

info={'fistname': '길동', 'lastname': '홍',
    'email': 'gildong@itwill.com', 'age': 25}
info

dict_f(info)
dict_f(**info)

def f1(arg1, arg2):
    return arg1 + arg2
    return arg2 * arg2    # 첫번째 return 만 수행되고 끝남
 
f1(10,20)

def f1(arg1, arg2):
    return arg1 + arg2, arg1-arg2, arg1 * arg2

f1(10,20)

divmod(11,2)

def f2(arg1,arg2):
    return arg1//arg2, arg1%arg2

def f3(arg1,arg2):
    if arg2 == 0:
        return # 함수에서 값이 없는 return 종료를 의미한다. # 반복문에서는 break
        print("값") # 의미 없는 로직 구현
    else:
        return arg1/arg2

f3(4,0)

def f4(arg1,arg2,arg3):
    print('이름: ',arg1)
    print('나이: ',arg2)
    if arg3 == 'N':
        print('남자')
    else:
        print('여자')
        
f4('홍길동',25,'N')
f4('홍길동',25) # 실제매개변수는 형식매개변수에 위치적으로 대응되게 입력해야 한다.


# arg3='M': 형식매개변수의 기본값을 설정하는 방법
def f4(arg1,arg2,arg3='M'):
    print('이름: ',arg1)
    print('나이: ',arg2)
    if arg3 == 'M':
        print('남자')
    else:
        print('여자')
        
f4('홍길동',25,'M')
f4('홍길동',25)
f4('홍제인',5,'F')

f4(arg1 ='홍제인',arg2=5,arg3='F')
f4(arg2=5,arg1 ='홍제인',arg3='F') # 형식매개변수의 이름을 이용해서 대응하는 방법 위치x

전역변수(global variables) : 프로그램이 종료될때까지 어디서든지 사용할 수 있는 변수
지역변수(local variables) : 함수 안에서만 사용되는 변수

g_x = 10 # 전역변수

def f5(arg1):
    print("변수값 : ", arg1)
    print("변수값 : ", g_x)

f5(g_x)

del g_x

f5(20) # g_x 변수를 삭제한 후 함수를 수행하면 오류발생 g_x 변수를 찾는데 없음

g_x = 10 # 전역변수

def f6(arg1):
    print("변수값 : ", arg1)
    g_x = 100 # 함수 안에서 이거랑, 전역변수 g_x랑 달라
    print("변수값 : ", g_x) # 함수 내에 있는 지역변수 g_x를 찾는다

f6(g_x)

print(g_x)

def f6(arg1):
    print("변수값 : ", arg1)
    l_x = 100 # 함수 안에서만 선언된 로컬변수
    print("변수값 : ", l_x) 

f6(l_x) # 함수안에서만 선언되었기 때문에 사용할 수 없다


g_x = 10 # 전역변수

def f6(arg1):
    print("변수값 : ", arg1)
    global g_x # 함수 내에서 글로벌변수로 선언하고 싶을 때
    print("전역변수 수정 전 g_x: ",g_x)
    g_x = 100 # 전역 변수 수정
    print("전역변수 수정 후 g_x : ", g_x)

f6(20)
g_x

# 함수 내에서 참조가 우선순위인데, 전방참조만 가능하다
def f6(arg1):
    print("변수값 : ", arg1)
    print("지역변수 g_x: ",g_x) # g_x 변수는 지역변수로 찾는다 그런데 내 뒤에 선언되어 있어서 오류
    g_x = 100 # 전역 변수 수정
    print("전역변수 수정 후 g_x : ", g_x)

f6(20)
g_x

[문제59] 입력값을 더하는 함수를 작성하세요.

>>> print(add(2))
2

>>> print(add(8))
10


g_total =0

def add(arg):
    global g_total
    g_total += arg
    return g_total


add(2)
add(8)

스택(stack)
- 데이터를 임시로 저장할 때 사용하는 자료구조
- LIFO(last in first out) : 가장 나중에 입력한 데이터를 가장 먼저 꺼낸다
- push, pop

[문제 60] stack 변수를 선언한 후 push 함수를 이용해서 값을 입력하고 full 함수를 통해 stack 변수를 확인하고
pop변수를 이용해서 stack변수에 입력된 값을 꺼내는 함수를 생성하시오

full()
stack 변수가 비어 있습니다.

push(100)
0 인덱스에 값 100 입력

push(200)
1 인덱스에 값 200 입력

full()
0 인덱스 값 100
1 인덱스 값 200

v_pop = pop()
1 인덱스에 값 200 꺼냄


stack = []
def push(arg):
    stack.append(arg)
    print("{} 인덱스에 값 {} 입력".format(len(stack)-1,arg))
    
push(100)
stack
push(200)
stack

def full():
    if len(stack) == 0:
        print("stack 변수가 비어 있습니다.")
    else:
        v_cnt = 0
        for i in stack:
            print(f'{v_cnt} 인덱스 값 {i}')
            v_cnt += 1
    
full()


# enumerate() : 리스트, 튜플 변수를 반복할 때 인덱스와 값을 같이 리턴하는 함수
def full():
    if len(stack) == 0:
        print("stack 변수가 비어 있습니다.")
    else:
        for idx,value in enumerate(stack):
            print(f'{idx} 인덱스 값 {value}')
            
    
full()


def pop():
    if len(stack) == 0:
        print("stack 변수가 비어 있습니다.")
    else:
        v_cnt = len(stack)-1
        v_pop = stack[v_cnt]
        print(f'{v_cnt} 인덱스에 값 {v_pop} 꺼냄')
        del stack[v_cnt]
        return v_pop
pop()

v_x = pop()


Queue(큐)
- FIFO(First In First Out): 가장 먼저 입력한 데이터를 가장 먼저 꺼내는 작업,
선입선출
- 입력 enqueue, 꺼내는 작업 dequeue

[문제 61] queue 변수를 선언한 후 enqueue 함수를 이용해서 값을 입력하고 full 함수를 통해 queue 변수를 확인하고
dequeue변수를 이용해서 queue변수에 입력된 값을 꺼내는 함수를 생성하시오

queue =[]

def enqueue(arg):
    queue.append(arg)
    print(f'{len(queue)-1} 인덱스에 값 {arg} 입력')

enqueue(100)
enqueue(200)
queue

def full():
    if len(queue)==0:
        print("queue 변수가 비어 있습니다.")
    else:
        for idx, value in enumerate(queue):
            print(f'{idx} 인덱스 값 {value}')

full()

def dequeue():
    if len(queue)==0:
        print('queue 변수가 비어 있습니다.')
    else:
        v_deq = queue[0]
        print(f'{0} 인덱스에 값 {queue[0]} 꺼냄')
        del queue[0]
        return v_deq

dequeue()

queue

[문제62] 함수를 생성하세요.
합 = 관측값의 합
평균 = 관측값의 합 / 관측값의 수
편차 = 관측값 - 평균
편차제곱합 = 편차**2 + 편차**2
분산 = 편차제곱합/관측값의 수-1(자유도)
표준편차 = math.sqrt(분산)

sum(1,2,3,4,5)
mean(1,2,3,4,5)
variance(1,2,3,4,5)
stddev(1,2,3,4,5)

# 내가 구한 건 이전에 만들어놓은 함수를 이용하지 않았어
def sum(*arg):
    total = 0
    for i in arg:
        total += i
    return total

sum(1,2,3,4,5)

def mean(*arg):
    total = 0
    for i in arg:
        total += i
    avg = total / len(arg)
    return avg


mean(1,2,3,4,5)

def variance(*arg):
    v_total = 0
    for j in arg:
        total = 0
        for i in arg:
            total += i
        avg = total / len(arg)
        v_total = v_total + (j - avg)**2
    
    return v_total / (len(arg)-1)
    
    
mean(1,2,3,4,5)
variance(1,2,3,4,5)

import math

def stddev(*arg):
    v_total = 0
    for j in arg:
        total = 0
        for i in arg:
            total += i
        avg = total / len(arg)
        v_total = v_total + (j - avg)**2
    
    return math.sqrt(v_total / (len(arg)-1))

stddev(1,2,3,4,5)


답

def sum(*arg):
    total = 0
    for i in arg:
        total += i
    return total

def mean(*arg):
    return sum(*arg)/len(arg) # sum 가변인수 받았으니까 여기서도 가변인수로

def variance(*arg):
    total = 0
    avg = mean(*arg)
    for i in arg:
        total += (i-avg)**2
    
    return total / (len(arg)-1)

import math

def stddev(*arg):
    return math.sqrt(variance(*arg))

if __name__ == '__main__': # 패키지를 사용할 때 이 밑으로는 실행되지 않도록 하는 구문, 프롬프트에서 실행할 때 쓰기 위해 입력
    print(sum(1,2,3,4,5))
    print(mean(1,2,3,4,5))
    print(variance(1,2,3,4,5))
    print(stddev(1,2,3,4,5))



# 디렉토리 등록하기
import sys
sys.path
sys.path.append('C:\\mypython')
sys.path

sys.path.remove('C:\\mypython') # 디렉토리 삭제

# 내가 저장한 패키지 호출하기
import stats
dir(stats)

stats.sum(1,2,3,4,5)
stats.mean(1,2,3,4,5)
stats.variance(1,2,3,4,5)
stats.stddev(1,2,3,4,5)

del stats
dir(stats)

#stats.mean 이렇게 안하고 mean() 하고 싶다면
from stats import *
dir(stats)
dir(mean)

mean(1,2,3,4,5)
# 그런데, 이렇게 할 경우 기본 내장 method 인지, 패키지를 로드한 것인지 헷갈릴 수 있음


■ feature scaling
서로 다른 변수의 값 범위를 일정한 수준으로 맞추는 작업

1. 표준화(standardization)
- 데이터의 피쳐 각각이 평균 0이고 분산이 1인 정규분포를 가진 값으로 변환
- z score

(관측값 - 관측값의 평균) / (관측값의 표준편차)

[문제63] standardization(표준화) 함수를 생성해주세요.

data =(100,2,4,3,500)

import stats
data
mean1 = stats.mean(100,2,4,3,500)
stddev1 = stats.stddev(100,2,4,3,500)

(data - mean1) / stddev1


def standardization(*arg):
    z = []
    for i in arg:
        z.append((i-stats.mean(*arg)) / stats.stddev(*arg))
    
    return z
    
standardization(100,2,4,3,500)
standardization(*data)

def standardization(*arg):
    z_score = []
    v_mean = mean(*arg) # for 문 돌리기 전에 이 값들 이렇구게 해놓으면 반복할 때 마다 계속 호출하는 비효율 제거
    v_stddev = stddev(*arg)
    for i in arg:
        z_score.append((i - v_mean) / v_stddev)
    return z_score

data_scaler = standardization(*data)
mean(*data_scaler) # 0에 가까움
stddev(*data_scaler) # 1

2. Normalization(정규화)
- 서로 다른 피처의 크기를 동일한 크기로 변환해주는 개녕
- 0 ~1 값으로 변환하는 방법

minmaxscaler = (관측값 - 관측값의 최소값) / (관측값의 최대값 - 관측값 최소값)

[문제64] minmaxscaler 함수를 생성하세요.
1) min_of 함수 생성
2) max_of 함수 생성
3) minmaxscaler 함수 생성

data=(100,2,4,3,500)
data=(1,2,3,4,5)
data=(300,400,500,200,100)


1) # 오류
def min_of(*arg):
    a=[]
    b=[]
    for i in arg:
        for j in arg:
            if i <= j:
                a.append(j)
            if len(a) == len(arg):
                m = i
    return m

min_of(*data)

data=(300,400,500,200,100)
답
1)
def min_of(*arg):
    v_min = arg[0]
    for i in arg[1:]:
        if i < v_min:
            v_min = i
    return v_min

2)
  def max_of(*arg):
      v_max = arg[0]
      for i in arg[1:]:
          if i > v_max:
              v_max = i
      return v_max  

3)
def minmaxscaler(*arg):
    v_max = max_of(*arg)
    v_min = min_of(*arg)
    v_minmax = []
    for i in arg:
        v_minmax.append((i-v_min)/(v_max-v_min))
    return v_minmax
        
■ 날짜
import datetime

datetime
datetime.date.today()
datetime.datetime.now()

datetime.date.today().year
datetime.date.today().month
datetime.date.today().day

datetime.datetime.now().year
datetime.datetime.now().month
datetime.datetime.now().day
datetime.datetime.now().hour
datetime.datetime.now().minute
datetime.datetime.now().second
datetime.datetime.now().microsecond
datetime.datetime.now().date()
datetime.datetime.now().time()
datetime.datetime.now().weekday() # 0:월요일 ~ 6:일요일

[문제65] 오늘 문자 요일을 출력해주세요. toweekday() 함수를 생성해주세요.

datetime.datetime.now().weekday()

def toweekday():
    if datetime.datetime.now().weekday() == 0:
        t = '월요일'
    elif datetime.datetime.now().weekday() == 1:
        t = '화요일'
    elif datetime.datetime.now().weekday() == 2:
        t = '수요일'
    elif datetime.datetime.now().weekday() == 3:
        t = '목요일'
    elif datetime.datetime.now().weekday() == 4:
        t = '금요일'
    elif datetime.datetime.now().weekday() == 5:
        t = '토요일'
    elif datetime.datetime.now().weekday() == 6:
        t = '일요일'
    return t

toweekday()

답
def toweekday():
    day = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
    return day[datetime.datetime.now().weekday()]


■ strftime
- date를 char 로 형변환 하는 method

datetime.datetime.now().strftime('%x')

d =datetime.datetime.now()
d.strftime('%x') # 현재 날짜 월/일/년

d.strftime('%X') # 현재 시:분:초
d.strftime('%Y') # 현재년도 4자리
d.strftime('%y') # 현재년도 2자리
d.strftime('%m') # 현재 달 (숫자지만 문자형)
d.strftime('%m') + 100 # 오류
d.strftime('%d') # 현재 일
d.strftime('%B') # 현재 영문자 달
d.strftime('%b') # 현재 영문자 달(약어)
d.strftime('%H') # 현재 시 24시간
d.strftime('%I') # 현재 시 12시간
d.strftime('%I %P') # AM, PM
d.strftime('%M') # 분
d.strftime('%S') # 초
d.strftime('%A') # 영문자 요일
d.strftime('%a') # 영문자 요일 (약어)
d.strftime('%c')
d.strftime('%j') # 누적날짜
d.strftime('%w') # 요일 0: 일요일 ~ 6: 토요일
int(d.strftime('%w'))
d.strftime('%U') # 누적주(일요일 시작)
d.strftime('%W') # 누적주(월요일 시작)

■ strptime
- char 문자형을 date 형으로 바꿔주는 method

datetime.datetime.strptime('2022-03-10 13:43:30','%Y-%m-%d %H:%M:%S')
datetime.datetime(2022,3,10,13,43,30)

d = datetime.date(2022,3,10)
t = datetime.time(13,43,30)
datetime.datetime.combine(d,t)
datetime.datetime.combine(d,t).strftime('%Y')

datetime.date(2021,12,16) - datetime.date(2022,3,10)
datetime.date(2022,3,10) - datetime.date(2021,12,10)
datetime.date(2022,5,20) - datetime.date(2022,3,10)
(datetime.date(2022,5,20) - datetime.date(2022,3,10)).days

datetime.date(2022,3,10) + datetime.timedelta(days=71)
datetime.date(2022,3,10) - datetime.timedelta(days=84)
datetime.date(2022,3,10) + datetime.timedelta(days=-84)
datetime.datetime(2022,3,10)
datetime.datetime(2022,3,10,13,52,30) + datetime.timedelta(hours=5)
datetime.datetime(2022,3,10,13,52,30) + datetime.timedelta(minutes=300)
datetime.datetime(2022,3,10,13,52,30) + datetime.timedelta(hours=18000)
datetime.datetime(2022,3,10,13,52,30) + datetime.timedelta(weeks=10)

import time

# 1970년 1월 1일 0시 0분0초를 기준으로 지난 시간을 초단위로 리턴해주는 기능
time.time()

time.localtime()
time.localtime().tm_year
time.localtime().tm_mon
time.localtime().tm_hour
time.localtime().tm_min
time.localtime().tm_sec
time.localtime().tm_wday # 요일 0:월 ~ 6:일
time.localtime().tm_yday # 누적일수
time.localtime().tm_isdst # 서머타임일 경우 1, 아닐경우 0, 몰라 -1

time.gmtime() # UTC 기준으로 현재시간
datetime.datetime(2022,3,10,14,2,30) + datetime.timedelta(hours=-9)

time.asctime()
time.ctime()

time -> char
time.strftime('%Y%m%d%H%M%S',time.localtime())

char -> time
t = time.strptime('2022-3-10 14:5:30','%Y-%m-%d %H:%M:%S')
time.mktime(t)

start = time.time()
for i in range(10):
    print(i)
    time.sleep(1)
end = time.time()

print('time elapsed : ', end-start)

import calendar

print(calendar.calendar(2022))
calendar.prcal(2022)
calendar.prmonth(2022,3)
calendar.weekday(2022,3,10) # 요일 0:월 ~ 6:일

'월화수목금토일'[calendar.weekday(2022,3,10)]+'요일'
'월화수목금토일'[time.localtime().tm_wday]+'요일'
'월화수목금토일'[datetime.datetime.now().weekday()]+'요일'

def toweekday():
    return '월화수목금토일'[time.localtime().tm_wday]+'요일'

toweekday()

datetime.date(2022,3,10) + datetime.timedelta(days=365)
datetime.date(2022,3,10) + datetime.timedelta(months=365) # 안됨. 오류

import dateutil

datetime.date(2022,3,10) + dateutil.relativedelta.relativedelta(months=3)
datetime.date(2022,3,10) + dateutil.relativedelta.relativedelta(months=-3)
datetime.date(2022,3,10) - dateutil.relativedelta.relativedelta(months=3)
datetime.date(2022,3,10) + dateutil.relativedelta.relativedelta(years = 1)
datetime.date(2022,3,10) + dateutil.relativedelta.relativedelta(years=10,months=3)

datetime.date(2022,3,10) + datetime.timedelta(days=71)
datetime.date(2022,3,10) + dateutil.relativedelta.relativedelta(days=71)

datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(hours=10)
datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(minutes=300)
datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(seconds=50)
datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(hours=10,minutes=300,seconds=50)
datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(days=71,hours=10,minutes=300,seconds=50)

datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(weeks=2)
datetime.datetime(2022,3,10,14,25,0) + dateutil.relativedelta.relativedelta(weekday=2)


[문제66] 아래와 같은 결과가 출력될수 있도록 프로그램을 생성하세요 # 프로그램이 꼭 함수는 아님

1에서 천만까지 짝수합, 홀수합 구합니다
1에서 천만까지 짝수합: 25000005000000
1에서 천만까지 홀수합: 25000000000000
처리시간 : 0:00:01.950003
처리시간 millisecond(1/1000)  : 1950ms

start=time.time()
hap=0
for i in range(1,10000001,1):
    if i % 2 == 0:
        hap += i
print(hap)
end=time.time()


def t(arg):
    start=time.time()
    e_hap=0
    o_hap=0
    for i in range(1,arg+1,1):
        if i % 2 == 0:
            e_hap += i
        else:
            o_hap += i
    print(f'1에서 {arg}까지 짝수합, 홀수합 구합니다')
    print(f'1에서 {arg}까지 짝수합: {e_hap}')
    print(f'1에서 {arg}까지 홀수합: {o_hap}')
    end=time.time()
    print('처리시간 : ', end - start)
            
t(10000000)

답

start = datetime.datetime.now() # 00:00:00 형식으로 나오려면 이렇게
print('1에서 천만까지 짝수합, 홀수합 구합니다')
e_result = 0
o_result = 0
for i in range(1,10000001):
    if i % 2 == 0:
        e_result += i
    else:
        o_result += i
end = datetime.datetime.now()
delta = end - start
print('1에서 천만까지 짝수합: ',e_result)
print('1에서 천만까지 홀수합: ',o_result)
print('처리시간 : ', delta)
delta.total_seconds()
print('처리시간 millisecond(1/1000) : %dms'%int(delta.total_seconds()*1000))


■ 파일을 읽고, 쓰기

file = open('c:/data/test.txt','w') # 'w' : 쓰기모드로 파일을 열겠다. 기존 파일이 있으면 덮어쓰기(overwrite)
file

for i in range(1,11):
    txt = '%d 오늘 하루도 열심히 하자!!\n'%i
    file.write(txt)

file.close() # open 했으면 close해줘야 돼

file = open('c:/data/test.txt','w') #덮어쓰기 됨

for i in range(11,21):
    txt = '%d 오늘 하루도 열심히 하자!!\n'%i
    file.write(txt)

file.close()


file = open('c:/data/test.txt','a') # 'a' : append 모드로 파일을 열겠다. 기존파일이 있으면 뒤에 이어서 쓰기

for i in range(11,21):
    txt = '%d 오늘 하루도 열심히 하자!!\n'%i
    file.write(txt)

file.close()

file = open("c:/data/test.txt","r") # 'r' : 읽기모드로 파일을 열기
file.readline() #한줄씩 읽어 들인다.
file.readline()
file.close()

file = open('c:/data/test.txt','r')
while True:
    data = file.readline()
    if not data:
        break
    print(data,end='')

file.close()


lst=[]
file = open('c:/data/test.txt','r')
while True:
    data = file.readline()
    if not data:
        break
    lst.append(data.rstrip()) # rstrip 하면 \n도 공백으로 보고 지워줌

file.close()

lst

file = open('c:/data/test.txt','r')
data = file.readlines() # 모든 라인을 한꺼번에 읽어서 리스트에 저장
file.close()
data
data.rstrip() # 리스트에는 rstrip 안먹혀

file = open('c:/data/test.txt','r')
data = file.read() # 파일 전체를 문자열로 리턴한다.
file.close()
data
type(data)

■ with 문:
파일 객체를 자동으로 닫아주는 문

with open('c:/data/test.txt','w') as file:
    for i in range(1,101):
        txt = "%d 오늘 하루도 열심히 하자!!\n"%i
        file.write(txt)

with open('c:/data/test.txt','a') as file:
    for i in range(1,101):
        txt = "%d 오늘 하루도 열심히 하자!!\n"%i
        file.write(txt)

with open('c:/data/test.txt','r') as file:
    data = file.readlines()

data

■ csv
import csv

file = open('c:/data/employees.csv','r')
emp_csv = csv.reader(file)
emp_csv
next(emp_csv) # 한줄(row) 읽기
for i in emp_csv:
    print(i)
file.close()

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        print(i)


with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv) # 한줄(row) 읽기 
    for i in emp_csv:
        print(i[2],i[7])
    
[문제68] employee_id, last_name, salary*12 결과를 출력해주세요. 0 2 7

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) # 텍스트 파일 불러들이면 전부 문자로 불러들인다.
    next(emp_csv) # 컬럼 빼고
    for i in emp_csv:
        print(i[0],i[2],int(i[7])*12)

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) # 텍스트 파일 불러들이면 전부 문자로 불러들인다.
    for i in emp_csv:
        print(i[0],i[2], i[7] if i[7] == 'SALARY' else int(i[7])*12) # 컬럼까지 같이 뽑기


[문제69] last_name, commission_pct를 출력하는데 commission_pct값이 '' 이면 0으로 출력해주세요.

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) 
    next(emp_csv) # 컬럼 이름 빼고
    for i in emp_csv:
        print(i[2],0 if i[8]== '' else i[8])



[문제70] last_name, commission_pct를 출력하는데 commission_pct값이 '' 이면 0으로 ifnull함수를 이용해서 출력해주세요.

def ifnull(arg1, arg2):
    if arg1 == '':
        return arg2
    else:
        return arg1

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) 
    next(emp_csv) # 컬럼 이름 빼고
    for i in emp_csv:
        print(i[2],ifnull(i[8],0))
# 근데 이렇게 하면 관리해야될 함수가 추가되어버리니까 람다로

■ 람다(lambda) 함수
- 이름이 없는 한 줄 짜리 함수
- 가독성을 위해

def f1(x,y):
    return x+y

f1(10,20)

(lambda x,y : x+y)(10,20)

f2 = lambda x,y : x+y
f2(10,20)

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) 
    next(emp_csv) # 컬럼 이름 빼고
    for i in emp_csv:
        print(i[2],(lambda x,y : y if x == '' else x)(i[8],0))

[문제70] last_name, salary * 12 + commission_pct

with open('c:/data/employees.csv','r') as file:
    emp_csv= csv.reader(file) 
    next(emp_csv) # 컬럼 이름 빼고
    for i in emp_csv:
        print(i[2],int(i[7])*12 + float((lambda x,y : y if x == '' else x)(i[8],0))) #int는 정수니까 float으로 해야돼

[문제71] last_name, 입사한 요일(한글)을 출력해주세요.
import csv
import datetime
import time
import calendar



with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        print(i[2],'월화수목금토일'[datetime.datetime.strptime(i[5],'%Y-%m-%d').weekday()]+'요일')

        


[문제72] last_name, 근무 일수를 출력해주세요.

(datetime.datetime.now() - datetime.datetime.strptime(i[5],'%Y-%m-%d')).days

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        print(i[2],(datetime.datetime.now() - datetime.datetime.strptime(i[5],'%Y-%m-%d')).days)

(datetime.date.today() - datetime.datetime.strptime('2021-12-16','%Y-%m-%d').date()).days




[문제73] 2001-01-13일에 입사한 사원의 이름과 입사일을 출력하세요.
with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        if i[5] == '2001-01-13':
            print(i[2],i[5])




[문제74] 2002 년도에 입사한 사원들의 이름과 입사일을 출력하세요.

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        if datetime.datetime.strptime(i[5],'%Y-%m-%d').year == 2002:
            print(i[2],i[5])

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        if i[5][:4] == '2002':
            print(i[2],i[5])

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        if datetime.datetime.strptime(i[5],'%Y-%m-%d').year == datetime.datetime.strptime('2002','%Y').year:
            print(i[2],i[5])

[문제75] job_id가 ST_CLERK인 사원들의 정보를 출력해주세요. 단 가장 최근에 입사한 사원부터 출력해주세요.

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    emp_lst=[]
    for i in emp_csv:
        if i[6] == 'ST_CLERK':
            emp_lst.append(i)

import operator
emp_lst_sorted = sorted(emp_lst,reverse=True,key=operator.itemgetter(5))
for i in emp_lst_sorted:
    print(i)

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    emp_lst = [[i[0],datetime.datetime.strptime(i[5],'%Y-%m-%d').date(),i[6]] for i in emp_csv if i[6] == 'ST_CLERK']

emp_lst_sorted = sorted(emp_lst,reverse=True,key=operator.itemgetter(1))
for i in emp_lst_sorted:
    print(i[0],i[1],i[2])

emp_lst_sorted = sorted(emp_lst,reverse=True,key=lambda arg:arg[1]) # emp_lst가 arg가 되고 arg[1]을 기준으로 한다 이말
for i in emp_lst_sorted:
    print(i[0],i[1],i[2])

[문제76] 년도별 급여의 총액을 구하세요.

year_sum={}

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        y = datetime.datetime.strptime(i[5],'%Y-%m-%d').year
        if y in year_sum.keys():
            year_sum[y]=year_sum[y] + int(i[7])
        else:
            year_sum[y] = int(i[7])


year_sum
year_sum_sorted = sorted(year_sum.items(),reverse=False)

with open('c:/data/q76.txt','w',newline='') as file:
    q76_write = csv.writer(file)
    q76_write.writerows(year_sum_sorted)

with open('c:/data/q76.txt','r') as file:
    q76_csv = csv.reader(file)
    for i in q76_csv:
        print(i)

[문제77] 요일별(한글) 급여의 총액을 구하세요.

wday_sum = {}
with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        y = datetime.datetime.strptime(i[5],'%Y-%m-%d').weekday()
        if y in wday_sum.keys():
            wday_sum[y] += int(i[7])
        else:
            wday_sum[y] = int(i[7])

wday_sum

wday_sum_sorted = sorted(wday_sum.items())

for i in wday_sum_sorted:
    print('월화수목금토일'[i[0]]+'요일',i[1])

wday_sum_kor_lst=[]
for i in wday_sum_sorted:
    wday_sum_kor_lst.append(['월화수목금토일'[i[0]]+'요일',i[1]])

wday_sum_kor_lst = [('월화수목금토일'[i[0]]+'요일',i[1]) for i in wday_sum_sorted]

wday_sum_kor_lst


wday_sum_kor_dict={}
for i in wday_sum_sorted:
    wday_sum_kor_dict['월화수목금토일'[i[0]]+'요일'] = i[1]
wday_sum_kor_dict


# writerows
with open('c:/data/q77.txt','w',newline='') as file:
    q77_write = csv.writer(file)
    q77_write.writerows(wday_sum_kor_lst)

# writerow 한 행씩 바로바로 넣고 싶을 때. 각 줄마다 변화하면서 넣을 때는 이렇게
with open('c:/data/q77.txt','w',newline='') as file:
    q77_write = csv.writer(file)
    for i in wday_sum_sorted:
        q77_write.writerow(['월화수목금토일'[i[0]]+'요일',i[1])

■ pickle
- 변수형태를 그대로 유지해서 파일에 저장시키고 불러올 수 있는 모듈
- 바이너리 형태로 저장

import pickle

lst = ['a','b','c']

file = open('c:/data/lst.txt','wb')
pickle.dump(lst,file)
file.close()

file = open('c:/data/lst.txt','rb')
lst_new = pickle.load(file)
lst_new
file.close()

wday_sum_sorted

file = open('c:/data/wday_sum_sorted.txt','wb')
pickle.dump(wday_sum_sorted,file)
file.close()

file = open('c:/data/wday_sum_sorted.txt','rb')
wday_sum_sorted = pickle.load(file)
wday_sum_sorted
file.close()


[문제78] 부서별 인원수를 출력해주세요. (소속부서가 없는 인원수도 출력)


dept_cnt ={}
with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        y = (lambda arg: 999 if i[10] == '' else int(arg))(i[10]) 
        if y in dept_cnt.keys():
            dept_cnt[y] += 1
        else:
            dept_cnt[y] = 1

dept_cnt 
dept_cnt_sorted=sorted(dept_cnt.items())

for i in dept_cnt_sorted:
    print((lambda arg: '소속부서(X)' if arg ==999 else arg)(i[0]),i[1])

with open('c:/data/q78.txt','w',newline='') as file:
    q78_write = csv.writer(file)
    for i in dept_cnt_sorted:
        q78_write.writerow([(lambda arg: '소속부서(X)' if arg ==999 else arg)(i[0]),i[1]])


with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    dept_lst=[(lambda arg: 999 if i[10] == '' else int(arg))(i[10]) for i in emp_csv]


import collections

collections.Counter(dept_lst)

[문제79] 월별 입사 인원 수를 구하세요.
month_cnt ={}
with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        y = int(datetime.datetime.strptime(i[5],'%Y-%m-%d').month)
        if y in month_cnt.keys():
            month_cnt[y] += 1
        else:
            month_cnt[y] = 1

month_cnt
month_cnt_sorted=sorted(month_cnt.items())


month_cnt_sorted_f = []
for i in month_cnt_sorted:
    month_cnt_sorted_f.append([str(i[0])+'월',i[1]])

file = open('c:/data/month_cnt_sorted_f.txt','wb')
pickle.dump(month_cnt_sorted_f,file)
file.close()

file = open('c:/data/month_cnt_sorted_f.txt','rb')
month_cnt_sorted_f = pickle.load(file)
month_cnt_sorted_f
file.close()

with open('c:/data/q79.txt','w',newline='') as file:
    q79_write = csv.writer(file)
    q79_write.writerows(month_cnt_sorted_f)


fruit_dict={}
p = fruit_dict.get('사과',0)
fruit_dict['사과'] = p + 1
fruit_dict

fruit_dict={}
for i in fruit:
    p = fruit_dict.get(i,0)
    fruit_dict[i] = p + 1
fruit_dict

import collections
fruit_dict = collections.defaultdict(int)

for i in fruit:
    fruit_dict[i] = fruit_dict[i] + 1

fruit_dict

■ pandas
- 데이터분석 기능을 제공하는 라이브러리
- 1차원배열 : Series
- 2차원배열 : DataFrame

from pandas import Series,DataFrame
import pandas as pd

Series
- 1차원배열
- 인덱스(색인) 배열의 데이터에 연관된 이름을 가지고 있다.
- R의 벡터 자료형과 유사
- 단일 데이터 타입만 가능



s1 = Series([10,20,30,40,50])
s1 + 100
type(s1)
s1.astype

s1 = Series(['10','20','30',40,50])
s1 # object : 문자형(character)
s1+100
type(s1)
s1.astype('int32') # 데이터 타입 변경, 미리보기
s1

s1 = s1.astype('int64') # 자료형 수정
s1
s1.index
s1.values
s1.index = ['a','b','c','d','e'] # 인덱스 수정
s1

s1 + 100
s1 - 100
s1 * 10
s1/2
s1//2
s1%2
s1**2

s1['a'] # 인덱스를 이용해서 값을 추출
s1[['a','c']]
s1[0] # 위치를 이용해서 값을 추출
s1[3]
s1[0:3]
s1[-1]

s1 >= 30
s1[s1 >= 30]

'a' in s1
'f' in s1

s1['a'] = 100 # 값 수정
s1['f'] = 500 # 새로운 값 추가
s1['a'] = '' # 빈문자열 수정
s1
del s1['a'] # 요소를 삭제
s1
del s1 # 변수 삭제

lst = [10,20,30]
type(lst)
Series(lst)
lst

t = (10,20,30)
type(t)
Series(t)

dict = {'a':10, 'b':20,'c':30}
dict
Series(dict)

ix = {'a','b'}
type(ix)

Series(dict,index=ix)

ix = {'a','b','f'}
type(ix)

Series(dict,index=ix)
s1
# NaN(Not a Number) : 인덱스 값을 찾을 수 없을 경우 NaN 으로 저장, SQL(NULL), R(NA)


ix = ['a','b','a','f']
s1 = Series(dict,index=ix) # 중복되는 인덱스가 만들어 진다. 주의!

ix = {'a','b','a','f'} # set을 써서 중복되는 인덱스 없앨 수 있다
s1 = Series(dict,index=ix)



ix = ['a','b','f']
Series(dict,index=ix)


# NaN : SQL(NULL), R(NA)
import pandas as pd
pd.isnull(s1) # NaN값을 체크하는 방법
s1[pd.isnull(s1)]

pd.notnull(s1) # NaN값 아닌 것 체크
s1[pd.notnull(s1)]

s1['f'] =''
s1

s1 = Series(dict,index=['a','b','f'])
s1
s1['f'] = ''
pd.isnull(s1)
s1 == '' # 빈문자열은 결측치(NaN)가 아니다

s1['f'] = None # NaN(null)로 수정
s1
pd.isnull(s1)

import numpy as np
s1['f'] = np.NaN #NaN 수정
s1
pd.isnull(s1)
s1.astype('int32') # NaN이 있을 경우 int형 수정이 안된다

s1.astype('float32') # NaN이 있을 경우 float형으로 수정
s1.astype('float64')


d1 = {'서울':500, '부산':300, '경기':700,'제주':200}
s1 = Series(d1)
s1

city = {'서울','경기','제주','대전'}
s2 = Series(d1,index=city)
s2

# 서로 다른 Series를 인덱스를 기준으로 연산작업
s1 + s2 # 없는 인덱스는 NaN으로

s1.name = '인구수'
s1
s1.name = ''
s1.name = None
s1
s1.index.name = '지역명'
s1
s1.index.name = None
s1

DataFrame
-2차원 배열
- 표형식(테이블)의 자료구조
- 각 컬럼은 서로 다른 종류 데이터 타입을 사용할 수 있다.(문자, 숫자, 불린)

df = DataFrame([[1,2,3,],[4,5,6],[7,8,9]])
df
type(df)

data={'도시':['서울','부산','강원','인천'],
      '인구수':[500,400,200,300]}

df = DataFrame(data)
df.info()
df.columns
df.index
df.values

df.columns = ['지역','가구수'] # 컬럼 수정
df

df.지역 # 열선택
type(df.지역)

df.가구수 * 100

df.index = ['one','two','three','four'] #인덱스 수정
df

#행선택
df.iloc[0] # 인덱스 위치를 사용해서 검색

df.iloc['one'] # iloc에는 인덱스 위치가 아닌 인덱스 이름은 사용할 수 없다

df.loc['one'] # 인덱스 이름을 사용하여 검색


data={'도시':['서울','부산','강원','인천'],
      '인구수':[500,400,200,300]}


df.도시
df['도시']

df['부채'] = [1000,300,100,50] #열을 추가
df

del df['부채'] # 열 삭제

data = {'서울':{2001:200,2002:300},
        '부산':{2000:100,2001:50,2002:200}}

df = DataFrame(data)
df.index
df.values

df.T # 행과 열 바꾸기
df.dtypes # 컬럼 별 타입을 확인
df.서울.dtypes
df.info()

obj = Series([10,20,30,40],index=['c','d','a','b'])
obj

# reindex : 새로운 색인에 맞도록 객체를 새로 생성하는 기능
obj1 = obj.reindex(['a','b','c','d'])
obj1

obj2 = obj.reindex(['a','b','c','d','e'])
obj2

obj3 = obj.reindex(['a','b','c'])
obj3

Series(obj,index=['a','b','c'])
Series(obj,index=('a','b','c'))
s = Series(obj,index={'a','b','c'})
s = s.reindex(['a','b','c'])
s


obj.reindex(['a','b','c','d','e'])
obj_new = obj.reindex(['a','b','c','d','e'],fill_value=0) # NaN값 대신 0으로 채우는 방법
obj_new

list(range(4))

np.arange(4).reshape(2,2)
np.arange(9).reshape(3,3)
np.arange(12).reshape(3,4)

df = DataFrame(np.arange(9).reshape(3,3),
          index=['a','b','c'],
          columns=['x','y','z'])

df
df.reindex(['b','c','a'])

df1 = df.reindex(['a','b','c','d']) # reindex로 새로운 인덱스를 추가하면 NaN값으로 채워진다.


df1 = df.reindex(['a','b','c','d'],fill_value=0)
df1

# method = 'ffill', 'pad' NaN값을 앞으 행의 값으로 채운다.
df1 = df.reindex(['a','b','c','d'],method = 'ffill')
df1

df1 = df.reindex(['a','b','c','d'],method = 'pad')
df1

df = DataFrame(np.arange(9).reshape(3,3),
               index=['a','c','d'],
               columns=['x','y','z'])

df.reindex(['a','b','c','d'])

# method = 'bfill','backfill' NaN 값을 뒤의 값으로 채운다
df.reindex(['a','b','c','d'],method='bfill')
df.reindex(['a','b','c','d'],method='backfill')


s = Series(['SQL','R','PYTHON'],index=[0,2,4])
s
s.reindex(range(6))
s.reindex(range(6),fill_value='ML')
s.reindex(range(6),method='ffill')
s.reindex(range(6),method='pad')
s.reindex(range(6),method='bfill')
s.reindex(range(6),method='backfill')

del s[0] # 요소 삭제(행)
s

s.drop(2)
s
s.drop(4) # 인덱스 이름을 기준으로 삭제, 미리보기

df

df.drop('a') # 데이터프레임에서 행삭제, 미리보기
df
df.drop('a',axis=0) # axis=0(기본값)


# 열삭제

df.drop('x',axis=1) # axis=1(열기준), 열삭제

df.drop(['a','d'],axis=0)
df.drop(['x','y'],axis=1)

del df['x']
del df.x # 이건 추출할 때 되는데 여기선 안 돼.

df = DataFrame(np.arange(16).reshape(4,4),
          index=['w','x','y','z'],
          columns=['one','two','three','four'])

df.one
df['one']
df[['one','four']]

df[:]
df[2:]
df[0:2]
df.iloc[0] # 인덱스 위치기반 추출
df.loc['w'] # 이름 기반 추출

df.loc['w','one']
df.loc['w',['one','four']]

df.iloc[0,0]
df.iloc[0,[0,3]]
df.iloc[0,0:3]

df.iloc[-1]
df.iloc[:,0:2]
df.iloc[:,-1]

df[df['one']<5]
df[df['one']<5]['one'] #특정한 열만 추출
df.loc[df['one']<5,'one'] # 특정한 열만 추출
df.iloc[df['one']<5,0] # 이렇게 하면 또 안 됨

df[df['one'] < 5][['one','four']] 특정조건의 여러개 열 추출
df.loc[df['one']<5,['one','four'] # 특정조건의 여러개 열 추출


[문제80] student 데이터 프레임을 생성하세요.
      영어 수학 국어
홍길동  60  80  70
박찬호  50  70  85
손흥민  90  80  95

student = DataFrame({'영어':[60,50,90,],
                     '수학':[80,70,80],
                     '국어':[70,85,95]},
                     index=['홍길동','박찬호','손흥민'])


student = DataFrame([[60,80,70],[50,70,85],[90,80,95]],
                    index=['홍길동','박찬호','손흥민'],
                    columns=['영어','수학','국어'])


# 인덱스 이름, 컬럼이름
student.loc['홍길동','영어']
student.at['홍길동','영어']

# 인덱스 위치, 컬럼 위치
student.iloc[0,0]
student.iat[0,0]

# 새로운 행을 추가
student.loc['제임스','영어'] = 100
student.at['제임스','수학'] = 70
student.iloc[3,2] = 80
student.info()

# 데이터프레임의 모든 컬럼의 타입을 동일하게 수정
student.astype('int32')
student.astype('int64')
student = student.astype('int') # int32
student.info()

# 특정한 열의 데이터 타입 수정
student['영어'] = student['영어'].astype('int64')
student.info()

# 새로운 컬럼 추가
student['과학'] = [50,70,80,60]
student
student['한국사'] = 0
student
student['미술사'] = np.nan # float 형식으로 들어감
student.info()

# 특정한 필드값을 수정하는 방법
student.loc['홍길동','미술사'] = 100
student.at['박찬호','미술사'] = 90
student.iloc[2,5]=90
student.iat[3,5] = 100

# 열 삭제
del student['미술사']
student

student = student.drop('한국사',axis=1)
student

# 행삭제
student = student.drop('제임스',axis=0)
student

# 특정한 인덱스 이름 수정
student = student.rename(index={'홍길동':'제임스'})
student

# 특정한 컬럼 이름 수정
student = student.rename(columns={'수학':'산수'})
student

student.index

# 인덱스를 컬럼으로 이동
student.index

student = student.reset_index()
student = student.rename(columns={'index':'이름'})
student

# 특정 컬럼을 인덱스로 이동
student = student.set_index('이름')
student.index
student.index.name = None
student

import csv

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    for i in emp_csv:
        if i[0] == '100':
            print(i)

emp = pd.read_csv('c:/data/employees.csv')
emp
emp.info()
emp.shape
emp.head()
emp.head(10)
emp.tail(10)

pd.options.display.max_columns # 출력할 수 있는 컬럼의 수 정보 확인
pd.get_option('display.max_columns') # 출력할 수 있는 컬럼의 수 정보 확인
pd.set_option('display.max_columns',11) # 출력할 수 있는 컬럼의 수 설정
pd.reset_option('display.max_columns') # 출력할 수 있는 컬럼의 수를 기본값으로 설정
emp.head()

pd.options.display.max_rows # 출력할 수 있는 행의 수 정보 확인
pd.get_option('display.max_rows') # 출력할 수 있는 행의 수 정보 확인
pd.set_option('display.max_rows',11) # 출력할 수 있는 행의 수 설정
pd.reset_option('display.max_rows') # 출력할 수 있는 행의 수를 기본값으로 설정
emp.head()

emp[emp['EMPLOYEE_ID'] == 100]
emp.loc[emp['EMPLOYEE_ID']==100,] # 행의 조건, 열
emp.loc[emp['EMPLOYEE_ID']==100,'LAST_NAME'] # 행의 조건, 열
emp.loc[emp['EMPLOYEE_ID']==100,['LAST_NAME','SALARY']] # 행의 조건, 열
emp[emp['EMPLOYEE_ID']==100][['LAST_NAME','SALARY']]
emp[['LAST_NAME','SALARY']][emp['EMPLOYEE_ID']==100]

[문제81] JOB_ID가 ST_CLERK인 사원의 LAST_NAME, SALARY를 출력해주세요.
emp.loc[emp['JOB_ID']=='ST_CLERK',['LAST_NAME','SALARY']]

select last_name, salary
from emp
where job_id = 'ST_CLERK'


[문제82] SALARY가 10000이상인 사원들의 LAST_NAME,SALAYR,HIRE_DATE를 출력해주세요.
emp.loc[emp['SALARY']>=10000,['LAST_NAME','SALARY','HIRE_DATE']]

select last_name, salary, hire_date
from emp
where salary >= 10000

정렬
obj = Series([2,7,3,8],index=['d','a','c','b'])
obj
obj.reindex(['a','b','c','d'])
obj.sort_index() #인덱스를 기준으로 오름차순 
obj.sort_index(ascending=True) # 기본값
obj.sort_index(ascending=False) # 인덱스를 기준으로 내림차순 정렬

obj.sort_values() # 값을 기준으로 오름차순
obj.sort_values(ascending=False) # 내림차순

df = DataFrame(np.arange(8).reshape(2,4),
          index=['two','one'],
          columns=['d','a','c','b'])

df.reindex(['one','two'])
df.sort_index() # 인덱스를 기준으로 오름차순
df.sort_index(ascending=False) # 인덱스를 기준으로 내림차순 

df.sort_index(axis=0,ascending=True) # 행기준 오름차순(기본값)
df.sort_index(axis=1) # 열기준 오름차순

df.sort_index(axis=1,ascending=False) # 열기준 내림차순

df.sort_values(by='a',ascending=False,axis=0) # a 열 기준으로 정렬이면 행이바뀌어야 하니까 axis=0 이야.
df.sort_values(by='one',ascending=False,axis=1) # 특정한 행(인덱스)를 기준으로 내림차순


[문제83] salary 10000 이상인 사원들의 last_name, salary, department_id 를 출력하세요. department_id를 기준으로 오름차순 정렬하세요.
emp_sal = emp.loc[emp['SALARY']>=10000,['LAST_NAME','SALARY','DEPARTMENT_ID']]
emp_sal.sort_values(by='DEPARTMENT_ID',axis=0)

# 바로 뒤에 .sort_value 붙이면 되자나
result = emp.loc[emp['SALARY']>=10000,['LAST_NAME','SALARY','DEPARTMENT_ID']].sort_values(by='DEPARTMENT_ID',axis=0)
result.reset_index() # 인덱스를 재설정, 기존 인덱스가 열로 추가
result = result.reset_index(drop=True) # 인덱스를 재설정하되, 기존 인덱스를 없앰
result

emp_sal = emp.loc[emp['SALARY']>=10000,['LAST_NAME','SALARY','DEPARTMENT_ID']]
emp_sal.sort_values(by=['DEPARTMENT_ID','SALARY'],ascending=[True,False],axis=0)


True or False
True | False

True and True
True & True


# .isin : in 연산자의 의미 == or ==
emp[(emp['EMPLOYEE_ID'] == 100) | (emp['EMPLOYEE_ID'] == 101)]
emp[emp['EMPLOYEE_ID'].isin([100,101])]

# ~ .isin : not in 연산자의 의미 != or !=
emp[(emp['EMPLOYEE_ID'] != 100) & (emp['EMPLOYEE_ID'] != 101)]
emp[~emp['EMPLOYEE_ID'].isin([100,101])]


[문제84] job_id가 AD_VP, AD_PRES 인 사원들의 last_name, salary, job_id 출력하세요.
emp = pd.read_csv('c:/data/employees.csv')
from pandas import Series,DataFrame
import pandas as pd


emp.loc[emp['JOB_ID'].isin(['AD_VP','AD_PRES']),['LAST_NAME','SALARY','JOB_ID']]


[문제85] job_id가 AD_VP, AD_PRES 아닌 사원들의 last_name, salary, job_id 출력하세요.

emp.loc[~emp['JOB_ID'].isin(['AD_VP','AD_PRES']),['LAST_NAME','SALARY','JOB_ID']]




[문제86] department_id가 50,60 부서 사원 중에 salary가 5000 이상인 사원들의 last_name, salary, department_id 출력하세요.
emp.loc[emp['DEPARTMENT_ID'].isin([50,60]) & (emp['SALARY']>=5000),['LAST_NAME','SALARY','DEPARTMENT_ID']]




[문제87] department_id가 50,60 부서 아닌 사원 중에 salary가 5000 이상인 사원들의 last_name, salary, department_id출력하세요.
단 department_id는 오름차순, salary는 내림차순으로 정렬하세요.
emp.loc[~emp['DEPARTMENT_ID'].isin([50,60]) & (emp['SALARY']>=5000),['LAST_NAME','SALARY','DEPARTMENT_ID']].sort_values(by=['DEPARTMENT_ID','SALARY'],ascending=[True,False],axis=0)



■ NULL -> NaN

import numpy as np
from numpy import nan as NA

s1 = Series([1,2,3,None,5])
s2 = Series([1,2,3,np.NaN,5])
s3 = Series([1,2,3,np.nan,5])
s4 = Series([1,2,3,NA,5])

# NaN 체크
s1.isnull()
s2.isnull()
s3.isnull()
s4.isnull()
pd.isnull(s1)


s1.notnull()
s2.notnull()
s3.notnull()
s4.notnull()
pd.notnull(s1)


s1[s1.isnull()]
s1[s1.notnull()]

# NaN 값을 채우는 방법
s1.fillna(0) # 미리보기

# NaN 값이 있는 행을 삭제(미리보기)
s2 = s2.dropna()



df = DataFrame([[1,2,3],[1,None,np.NaN],[np.nan,NA,NA],[NA,2,3]])
df
df.fillna(0)
df
df[0].fillna(0)
df[1].fillna(10)
df[2].fillna(20)
df.fillna({0:0,1:10,2:20})

df.dropna()
df.dropna(how='any',axis=0) # 행기준, NaN 하나라도 있으면 그 행 삭제(기본값)
df.dropna(how='all',axis=0) # 행기준, NaN이 전부 있는 행만 삭제

df.dropna(how='any',axis=1) # 열기준
df.dropna(how='all',axis=1)

df = DataFrame([[1,2,3],[None,np.NaN,4],[2,3,NA],[2,NA,3]])
df
df.fillna(0)
df.fillna(method='ffill')
df.fillna(method='pad')
df.fillna(method='bfill')
df.fillna(method='backfill')

[문제88] commission_pct 값이 null 인 사원의 last_name, salary 를 출력해주세요
emp.loc[emp['COMMISSION_PCT'].isnull(),['LAST_NAME','SALARY']]


[문제89] commission_pct 값이 null 아닌 사원의 last_name, salary 를 출력해주세요
emp.loc[emp['COMMISSION_PCT'].notnull(),['LAST_NAME','SALARY']]


[문제90] commission_pct 값이 null이 아닌 사원중에 department_id가 null인 사원의  last_name, salary, commission_pct,department_id 를 출력해주세요
emp.loc[emp['COMMISSION_PCT'].notnull()&(emp['DEPARTMENT_ID'].isnull()),['LAST_NAME','SALARY','COMMISSION_PCT','DEPARTMENT_ID']]


[문제91] commission_pct 값이 null인 사원중에 급여가 5000~10000  사원들의  last_name, department_id, salary를 출력해주세요.
emp.loc[emp['COMMISSION_PCT'].isnull()&((emp['SALARY']>=5000)&(emp['SALARY']<=10000)),['LAST_NAME','SALARY']]


def square(arg):
    return arg ** 2

square(10)

lst = [1,2,3]
square(lst[0])
square(lst[1])
[square(i) for i in lst]

list(map(square,lst))
list(map(lambda arg:arg**2,lst))

s = Series([1,2,3])
square(s)
list(map(square,s))
Series(map(square,s))

s.apply(square)
s.apply(lambda arg:arg**2)

df = DataFrame([[1,2,3],[4,5,6]])
df**2
square(df)
df.apply(square)
df.apply(lambda arg:arg**2)


[문제92] SALARY * 12 + COMMISSION_PCT 결과를 출력해주세요.
단 COMMISSION_PCT null 이면 0으로 처리해 주세요.

def nvl(arg):
    if pd.isnull(arg):
        return 0
    else:
        return arg

nvl(NA)

emp['SALARY']*12 + emp['COMMISSION_PCT'].apply(nvl)
emp['SALARY']*12 + emp['COMMISSION_PCT'].apply(lambda arg: 0 if pd.isnull(arg) else arg)


def nvl(arg):
    if Series(arg).isnull().bool():
        return 0
    else:
        return arg


x = Series([100])
x>50
(x>50).bool()
x.isnull().bool()

[문제93] last_name 첫글자가 S로 시작되는 사원들의 last_name 출력해주세요.
emp['LAST_NAME'][0][0]=='S'

def cap(arg):
    if arg[0] == 'S':
        return arg

emp.loc[emp['LAST_NAME'].apply(cap),'LAST_NAME']
cap('Kteven')


답
emp['LAST_NAME'].startswith('S')

emp[emp['LAST_NAME'].apply(lambda x : x.startswith('S'))]['LAST_NAME']

emp.loc[emp['LAST_NAME'].apply(lambda x : x[0] == 'S'),'LAST_NAME']


obj = [' big','data ',' big data ']
len(obj)
[len(i) for i in obj]
[len(i) for i in obj]
[len(i.strip()) for i in obj]

s = Series(obj)
len(s)
[len(i) for i in s]
[len(i.strip()) for i in s]

s.apply(lambda x : len(x))
s.apply(lambda x : len(x.strip()))

# 문자의 길이
s.str.len()

# 문자의 앞과 뒤 공백을 제거
s.str.strip()
s.str.strip().str.len()

# 문자의 앞의 공백 제거
s.str.lstrip()
s.str.lstrip().str.len()

# 문자의 뒤 공백 제거
s.str.rstrip()
s.str.rstrip().str.len()

# 소문자 함수
s.str.lower()

# 대문자 함수
s.str.upper()



# 문장 첫글자 대문자 뒷글자 소문자
s = s.str.strip()
s.str.capitalize()

# 단어별 첫글자 대문자 뒷글자 소문자
s.str.title()

# 소문자 -> 대문자, 대문자 -> 소문자
s.str.swapcase()

# 문자를 치환하는 함수
s.str.replace('big','BIG')

# 문자를 찾아서 위치를 반환하는 함수
s.str.find('a')
s.str.find('a',0)
s.str.find('a',2)
s.str.find('a').values

# 찾는 문자열이 없으면 오류
Series(s[1]).str.index('a')

# 모든 문자를 찾아 값으로 반환하는 함수
s.str.findall('a')

# 문자열로 시작되는지 체크
s.str.startswith('b')

# 문자열로 끝나는지 체크
s.str.endswith('a')

# 문자열이 포함되어 있는지 체크하는 함수, 대소문자 구분
s.str.contains('a')

s1 = s.str.replace('a','A')
s1
s1.str.contains('a')


s1.str.contains('a',case=True) # 대소문자 구분, 기본값
s1.str.contains('a',case=False) # 대소문자 구분x

# 지정된 위치(인덱스)의 값을 반환하는 함수
emp['LAST_NAME'].str.get(1)

[문제94] LAST_NAME을 KING으로 조회한후 LAST_NAME을 출력하세요.
emp.loc[emp['LAST_NAME'].str.upper() == 'KING','LAST_NAME']



[문제95] a글자가 두번 이상 나온 LAST_NAME을 출력하세요.
emp.loc[emp['LAST_NAME'].str.findall('a').str.len() >= 2,'LAST_NAME'] # 그안에서 또 series 갯수니까 그 뒤에 이어서 .str.len()



[문제96] 소문자 i글자가 포함되어 있는 LAST_NAME을 출력하세요.
emp.loc[emp['LAST_NAME'].str.contains('i',case=True),'LAST_NAME']




[문제97] 소문자 i, g 글자가 모두 포함되어 있는 LAST_NAME을 출력하세요.
emp.loc[emp['LAST_NAME'].str.contains('i',case=True) & emp['LAST_NAME'].str.contains('g',case=True),'LAST_NAME']


[문제98] 두번째 위치에 i글자가 있는 last_name을 출력하세요.
emp.loc[emp['LAST_NAME'].str.find('i')==1,'LAST_NAME'] # 이렇게 하면 제일 첫글자 i 인 경우는 안나오잖아

emp.loc[emp['LAST_NAME'].apply(lambda x : x[1] == 'i'),'LAST_NAME']

# 지정된 위치(인덱스)의 값을 반환하는 함수
emp['LAST_NAME'].str.get(1)

emp.loc[emp['LAST_NAME'].str.get(1) == 'i','LAST_NAME']

[문제 99] 세번째 문자가 'a' 또는 'e'가 있는 LAST_NAME을 출력해주세요
emp.loc[emp['LAST_NAME'].str.get(2).isin(['a','e']),'LAST_NAME']


# 지정된 인덱스 사이 값을 반환하는 함수
emp['LAST_NAME'].str.slice(start=0,stop=2)

emp.loc[emp['LAST_NAME'].str.slice(start=2,stop=3).isin(['a','e']),'LAST_NAME']

obj = Series(['big','big data'])
obj.str.title()

첫번째 위치의 b를 대문자 B로 수정
obj.str.slice(start=0,stop=1) 

'B'+obj.str.slice(start=1)

# 인덱스 사이값을 다른 값으로 수정하는 함수
obj.str.slice_replace(start=0,stop=1,repl='B')

# 지정된 길이 패딩
obj.str.pad(width=20,side='left',fillchar='_')
obj.str.pad(width=20,side='right',fillchar='_')

obj.str.center(width=20,fillchar='_')
obj.str.ljust(width=20,fillchar='_')
obj.str.rjust(width=20,fillchar='_')
obj.str.zfill(width=20) # 지정된 길이 0으로 채움

obj = Series(['itwill@itwill.com','itwill'])

# 문자를 기준으로 분리하는 함수
obj.str.split('@')
obj.str.split('@',expand=True) # DataFrame 모양으로 열 분리할 때

obj.str.partition('@')
obj.str.rpartition('@')

[문제100] salary 값을 1000 당 *하나 출력해주세요
5000 -> *****


'*' * 5
'*' * (5000/1000)
'*' * round(5000/1000)

['*'* int(i/1000) for i in emp.SALARY]

Series('*').str.pad(width=5,side='right',fillchar='*')
x = (emp.SALARY/1000).astype('int')
x.apply(lambda arg:Series('*').str.pad(width=arg,side='right',fillchar='*'))



obj = Series(['1/7','7','seven','SEVEN','Seven','seven7','칠','칠 7',' ','7#'])
obj[obj.str.isalnum()] # 알파벳, 한글, 숫자로만 구성 여부를 체크하는 함수
obj[obj.str.isalpha()] # 알파벳, 한글로만 구성 여부를 체크하는 함수
obj[obj.str.isnumeric()] # 숫자로만 구성 여부를 체크하는 함수
obj[obj.str.isdigit()] # 숫자로만 구성 여부를 체크하는 함수
obj[obj.str.islower()] # 소문자로만 구성 여부를 체크하는 함수 (숫자도 같이 나옴)
obj[obj.str.isupper()] # 대문자로만 구성 여부를 체크하는 함수
obj[obj.str.istitle()] # 첫글자 대문자 뒷글자 소문자 체크하는 함수
obj[obj.str.isspace()] # 공백으로만 구성되어 있는 여부를 체크하는 함수


obj = Series([2,3,5,6,None,4])
obj.sum() # 합
obj.sum(skipna=True) # 기본값
obj.sum(skipna=False)

obj.mean() # 평균
obj.var() # 분산
obj.std() # 표준편차
obj.max() # 최대값
obj.min() # 최소값

obj.max()
obj.idxmax() # 최대값에 대한 인덱스
obj.idxmin()
type(obj.idxmin()) # 최소값의 인덱스

obj.argmax()
obj.argmin()
type(obj.argmin())

obj = Series([2,3,5,6,None,4,6])

obj.idxmax() # 처음으로 나온 최대값 하나만 추출
obj.argmax() # 처음으로 나온 최대값 하나만 추출

obj.max()

obj[obj == obj.max()].index

obj

obj.cumsum() # 누적합
obj.cumprod() # 누적곱
obj.cummin() # 누적최소값
obj.cummax() # 누적 최대값

obj.count() # NaN 제외 건수
len(obj) # NaN 포함 건수

df = DataFrame([[60,80,70],[100,80,90],[60,90,50]],
          index=['홍길동','박찬호','손흥민'],
          columns=['영어','수학','국어'])

df
df.sum()
df.sum(axis=0) # 열의 합 # 기본값
df.sum(axis='rows')

df.sum(axis=1) # 행의 합
df.sum(axis='columns')

df.mean()
df.mean(axis=1)


df.loc['제임스','영어'] = 100
df.loc['제임스','수학'] = None
df.loc['제임스','국어'] = 90

df
df.sum()
df.sum(axis=0,skipna=False)


df.sum(axis=1,skipna=False)

df.영어.sum()
df['영어'].mean()


[문제101] 20번 부서 사원들의 급여 합을 pandas 이용하지 않고 해결하세요.
import csv

with open('c:/data/employees.csv','r') as file:
    emp_csv = csv.reader(file)
    next(emp_csv)
    v_sal = 0
    for i in emp_csv:
        if i[-1] == '20':
            v_sal += int(i[7])
print(v_sal)


[문제102] 20번 부서 사원들의 급여 합을 pandas 이용해서 해결하세요.
emp.loc[emp['DEPARTMENT_ID']==20, 'SALARY'].sum(axis=0)

[문제103] 부서번호를 입력하면 그 부서의 급여 총액을 구하는 함수를 생성하세요.

dept_sum_sal(30)
24900

dept_sum_sal(None)
부서코드를 입력해주세요

dept_sum_sal(120)
부서가 없습니다.

id = Series(list(set(emp['DEPARTMENT_ID'])))
id = id[pd.notnull(id)]
id

def dept_sum_sal(x):
    id = Series(list(set(emp['DEPARTMENT_ID'])))
    id = id[pd.notnull(id)]
    if x in list(id):
        return emp.loc[emp['DEPARTMENT_ID']==x,'SALARY'].sum()
    elif pd.isnull(x):
        print('부서코드를 입력해주세요.')
        return
    else:
        print('부서가 없습니다.')
        return

dept_sum_sal(20)




dept_unique = []
for i in emp.DEPARTMENT_ID:
    if i not in dept_unique:
        dept_unique.append(i)

import collections
collections.Counter(emp.DEPARTMENT_ID).keys()

id = emp.DEPARTMENT_ID.unique()
pd.notnull(id)



# 내가 처음에 했던대로 이렇게 해도돼 난  ==를 해서 오류, in으로 해야해
20 in emp['DEPARTMENT_ID']

[문제104] 부서별로 인원수를 출력해주세요.

import collections
dept_cnt = Series(collections.Counter(emp['DEPARTMENT_ID']))
dept_cnt = dept_cnt.reset_index()
type(dept_cnt.columns[0])
type(dept_cnt.columns[1])

dept_cnt = dept_cnt.rename(columns={'index':'DEPARTMENT_ID',0:'CNT'})
dept_cnt = dept_cnt.sort_values(by='DEPARTMENT_ID')
dept_cnt = dept_cnt.reset_index(drop=True)
dept_cnt

# 빈도수 체크하는 함수
emp.DEPARTMENT_ID.value_counts()
emp.DEPARTMENT_ID.value_counts(dropna=True) # NaN 값 제외 기본값, 빈도수 내림차순 기본값
emp.DEPARTMENT_ID.value_counts(dropna=False,sort=False)

dept_cnt = emp.DEPARTMENT_ID.value_counts(dropna=True)
dept_cnt = dept_cnt.reset_index()
dept_cnt = dept_cnt.rename(columns={'index':'DEPARTMENT_ID','DEPARTMENT_ID':'CNT'})
dept_cnt = dept_cnt.sort_values(by='DEPARTMENT_ID')
dept_cnt = dept_cnt.reset_index(drop=True)
dept_cnt

[문제105] 아래화면과 같이 부서별로 급여의 총액을 구하세요.
10 4400
20 20000
30 24900
40 6500
50 156400
60 28800
70 10000
80 304500
90 58000
100 51608
110 20308
부서(X) 7000

dept_sum=[]
for i in set(emp['DEPARTMENT_ID']):
    dept_sum.append([i,emp.loc[emp['DEPARTMENT_ID']==i,'SALARY'].sum()])

dept_sum

emp.DEPARTMENT_ID -> array(Numpy)

Series(emp.DEPARTMENT_ID.unique()).sort_values()
Series(emp.DEPARTMENT_ID.unique()).sort_values(ascending=False)

# NaN 값의 정렬 위치
Series(emp.DEPARTMENT_ID.unique()).sort_values(na_position='last') # 기본값
Series(emp.DEPARTMENT_ID.unique()).sort_values(ascending=False)

for i in Series(emp.DEPARTMENT_ID.unique()).sort_values():
    if pd.isnull(i):
        print('부서(x)',emp.loc[emp['DEPARTMENT_ID'].isnull(),'SALARY'].sum())
    else:
        print(int(i),emp.loc[emp['DEPARTMENT_ID']==i,'SALARY'].sum())




df = DataFrame()

DataFrame([[int(10),emp.loc[emp['DEPARTMENT_ID']==10,'SALARY'].sum()]])

df = df.append(DataFrame([[int(10),emp.loc[emp['DEPARTMENT_ID']==10,'SALARY'].sum()]]),ignore_index=True)
df = df.append(DataFrame([[int(20),emp.loc[emp['DEPARTMENT_ID']==20,'SALARY'].sum()]]),ignore_index=True)
df
df.


df = DataFrame()
for i in Series(emp.DEPARTMENT_ID.unique()).sort_values():
    if pd.isnull(i):
        df = df.append(DataFrame([['부서(x)',emp.loc[emp['DEPARTMENT_ID'].isnull(),'SALARY'].sum()]]),ignore_index=True)
    else:
        df = df.append(DataFrame([[int(i),emp.loc[emp['DEPARTMENT_ID']==i,'SALARY'].sum()]]),ignore_index=True)

df.columns = ['DEPARTMENT_ID','SUM_SAL']
df


# dictionary 활용하는 법
df = DataFrame()
df = DataFrame(columns=['DEPARTMENT_ID','SUM_SAL'])

for i in Series(emp.DEPARTMENT_ID.unique()).sort_values():
    if pd.isnull(i):
        df = df.append({'DEPARTMENT_ID':'부서(x)','SUM_SAL':emp.loc[emp['DEPARTMENT_ID'].isnull(),'SALARY'].sum()},ignore_index=True)
    else:
        df = df.append({'DEPARTMENT_ID':int(i),'SUM_SAL':emp.loc[emp['DEPARTMENT_ID']==i,'SALARY'].sum()},ignore_index=True)

df

# ignore_index=True 새로운 DataFrame의 index를 무시하고 원래 DataFrame에서 인덱스를 새로 할당

emp.SALARY.sum()
emp['SALARY'].sum()

emp.SALARY.groupby(emp.DEPARTMENT_ID).sum() # NaN 제외

emp.groupby('DEPARTMENT_ID')['SALARY'].sum() # NaN 제외
emp.groupby('DEPARTMENT_ID')['SALARY'].mean() # NaN 제외
emp.groupby('DEPARTMENT_ID')['SALARY'].max() # NaN 제외
emp.groupby('DEPARTMENT_ID')['SALARY'].min() # NaN 제외

emp.groupby('DEPARTMENT_ID')['SALARY'].aggregate(['sum','mean','max','min'])
emp.SALARY.groupby(emp['DEPARTMENT_ID']).aggregate(['sum','mean','max','min'])

emp.groupby('DEPARTMENT_ID').aggregate({'SALARY':'sum','HIRE_DATE':'max'})
emp.groupby('DEPARTMENT_ID').aggregate({'SALARY':'sum','HIRE_DATE':['max','min']})

# DEPARTMENT_ID 가 NaN인 결과도 뽑으려면 fillna
emp.SALARY.groupby(emp['DEPARTMENT_ID'].fillna(999)).aggregate(['sum','mean','max','min'])


emp.SALARY.groupby([emp.DEPARTMENT_ID,emp.JOB_ID]).sum()
emp.SALARY.groupby([emp.DEPARTMENT_ID.fillna(999),emp.JOB_ID]).sum()

emp.groupby(['DEPARTMENT_ID','JOB_ID'])['SALARY'].sum() # 얘로 할 때는 NaN인 경우 뽑을 방법이 없어. 이걸로 하지말자


# 피봇 unstack()
pd.set_option('display.max_columns',20)
emp.SALARY.groupby([emp.DEPARTMENT_ID.fillna(999),emp.JOB_ID]).sum().unstack()
emp.SALARY.groupby([emp.DEPARTMENT_ID.fillna(999),emp.JOB_ID]).sum().unstack().fillna(0)

for name, group in emp.groupby('DEPARTMENT_ID')['EMPLOYEE_ID']:
    print(name)
    print(group)

for name, group in emp.groupby(['EMPLOYEE_ID','LAST_NAME','DEPARTMENT_ID'])['DEPARTMENT_ID']:
    print(name)
    print(group)

for name, group in emp.groupby('DEPARTMENT_ID')['LAST_NAME']:
    print(name)
    print(group)

for name, group in emp[['EMPLOYEE_ID','LAST_NAME','SALARY','DEPARTMENT_ID']].groupby('DEPARTMENT_ID'):
    print(name)
    print(group)

[문제106] 부서별로 급여의 총액을 구하세요. 단, 10000 이상 정보만 출력해주세요.


df = emp.SALARY.groupby(emp.DEPARTMENT_ID.fillna(999)).sum()
df[df>=10000]
df.loc[df>=10000]


[문제107] 부서별로 급여의 총액 데이터프레임으로 구축해주세요.

    부서    총액
0    10    4400
1    20   20000
2    30   24900
3    40    6500
4    50  156400
5    60   28800
6    70   10000
7    80  304500
8    90   58000
9   100   51608
10  110   20308
11  NaN    7000

x = emp.SALARY.groupby(emp.DEPARTMENT_ID.fillna(999)).sum()
x = x.reset_index()
x['DEPARTMENT_ID'] = x['DEPARTMENT_ID'].astype('int') # int로 바꾸고 object로 바꾸면 된다
x['DEPARTMENT_ID'] = x['DEPARTMENT_ID'].astype('object')
x.loc[x['DEPARTMENT_ID'] == 999,'DEPARTMENT_ID'] = None
x

x.columns =['부서','총액']
x


emp = pd.read_csv('c:/data/employees.csv')
dept = pd.read_csv('c:/data/departments.csv')
dept.info()

■ merge
- 관계형 데이터베이스의 JOIN 과 똑같다
- 서로 다른 데이터프레임의 특정 열을 기준으로 연결하는 방법

# inner join, simple join, equi join, 등가조인

select emp.last_name, dept.department_name
from emp, dept
where emp.department_id = dept.department_id;

select emp.last_name, dept.department_name
from emp join dept
on emp.department_id = dept.department_id

select emp.last_name, dept.department_name
from emp natural join dept

select emp.last_name, dept.department_name
from emp join dept
using(department_id)

pd.merge(emp,dept) # natural join. 양 쪽 컬럼의 동일한 모든 컬럼에 대해 조인
pd.merge(emp,dept,on='DEPARTMENT_ID') # join using
pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID')[['EMPLOYY_ID','DEPARTMENT_NAME']] # 값은 같은데 만약 컬럼이름이 다르게 되어 있다면
pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='inner')[['EMPLOYEE_ID','DEPARTMENT_NAME']] # 기본값 how='inner'

emp['DEPARTMENT_ID'] 107개 (M쪽집합)
dept['DEPARTMENT_ID'] 27개 (1쪽집합)

-> 조인 시 결과가 107개 나와야 한다. 더 적게 나왔다면 키 값이 일치되지 않는 데이터가 있다.

# OUTER JOIN
- 키 값이 불일치되는 데이를 출력해야 한다면 outer join을 이용한다

# left outer join

select emp.last_name, dept.department_name
from emp, dept
where emp.department_id = dept.department_id(+);

select emp.last_name, dept.department_name
from emp left outer join dept
on emp.department_id = dept.department_id

pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='left')[['EMPLOYEE_ID','DEPARTMENT_NAME']] # 기본값 how='inner'

# right outer join

select emp.last_name, dept.department_name
from emp, dept
where emp.department_id(+) = dept.department_id;

select emp.last_name, dept.department_name
from emp right outer join dept
on emp.department_id = dept.department_id

pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='right')[['EMPLOYEE_ID','DEPARTMENT_NAME']] # 기본값 how='inner'

# full outer join

select emp.last_name, dept.department_name
from emp, dept
where emp.department_id(+) = dept.department_id;
union
select emp.last_name, dept.department_name
from emp, dept
where emp.department_id = dept.department_id(+);

select emp.last_name, dept.department_name
from emp full outer join dept
on emp.department_id = dept.department_id

pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='outer')[['EMPLOYEE_ID','DEPARTMENT_NAME']] # full outer는 how ='outer'

########## 조인을 해놓고 값을 구하는게 아니라 필요한거 구해놓고 마지막에 조인하는 습관 기르자 - SQL 비효율성 해결 연관


[문제108] JOB_ID가 AD_VP,AD_PRES 인 사원들의 LAST_NAME, SALARY, JOB_ID, DEPARTMENT_ID, DEPARTMENT_NAME을 출력하세요


e =emp.loc[emp['JOB_ID'].isin(['AD_VP','AD_PRES'])]
pd.merge(e,dept,on='DEPARTMENT_ID',how='left')[['LAST_NAME','SALARY','JOB_ID','DEPARTMENT_ID','DEPARTMENT_NAME']]


# dept = dept.set_index('DEPARTMENT_ID')
dept.set_index('DEPARTMENT_ID',inplace=True) # inplace=True 미리보기 없이 즉시 적용시키기
# dept의 department_id는 인덱스가 되어버린 상태
# 컬럼과 인덱스를 연결고리로 수행하는 방법
pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_index=True) 
dept

emp.set_index('DEPARTMENT_ID',inplace=True)
emp

# 컬럼 아닌 인덱스 들을 연결고리로 수행하는 방법
pd.merge(emp,dept,left_index=True,right_index=True)

import pandas as pd

emp = pd.read_csv('c:/data/employees.csv')
dept = pd.read_csv('c:/data/departments.csv')
dept.info()

[문제109] 부서이름별 총액 급여를 출력해주세요.
e = pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='inner')
e.SALARY.groupby(e.DEPARTMENT_NAME).sum()
 
답 # 왜 내꺼랑 다르게 나올까?
dept_sal = emp['SALARY'].groupby(emp['DEPARTMENT_ID']).sum()
pd.merge(dept_sal,dept,left_index=True,right_on='DEPARTMENT_ID',how='inner')[['DEPARTMENT_NAME','SALARY']]




[문제110] 부서이름별 총액 급여를 출력해주세요. 소속부서가 없는 사원들의 급여총액도 출력

e = pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='left')
x = e.SALARY.groupby(e.DEPARTMENT_NAME.fillna(999)).sum()
x = x.reset_index()
x.loc[x['DEPARTMENT_NAME']==999,'DEPARTMENT_NAME'] = '부서X'
x
x.columns = ['부서이름','급여총액']
x

x.reset_index(drop=True,inplace=True) # 이렇게 바로 할 수 있음


[문제111] 50번 부서 사원 중에 급여가 5000 이상인 사원의 LAST_NAME, DEPARTMENT_NAME 을 출력하세요.
x = pd.merge(emp,dept,on='DEPARTMENT_ID')
x.loc[(x['DEPARTMENT_ID']==50)&(x['SALARY']>=5000),['LAST_NAME','DEPARTMENT_NAME']]


[문제112] 사원들의 last_name, department_name, city를 출력하세요.
loc = pd.read_csv('c:/data/locations.csv')
loc
x = pd.merge(emp,dept,on='DEPARTMENT_ID',how='left')
y = pd.merge(x,loc,on='LOCATION_ID',how='left')
y[['LAST_NAME','DEPARTMENT_NAME','CITY']]


[문제113] commission_pct 에 null이 아닌 모든 사원의 last_name, department_name,  city를 출력하세요.
x = pd.merge(emp,dept,on='DEPARTMENT_ID',how='left')
y = pd.merge(x,loc,on='LOCATION_ID',how='left')
y.loc[y['COMMISSION_PCT'].notnull(),['LAST_NAME','DEPARTMENT_NAME','CITY']]



[문제114] 사원들의 last_name,  관리자 사원의 last_name 를 출력해주세요.
x = pd.merge(emp,emp,left_on='MANAGER_ID',right_on='EMPLOYEE_ID',how='left')
pd.set_option('display.max_columns',20)

x.loc[x['EMPLOYEE_ID_x'].isin(x['MANAGER_ID_x'].unique()),'LAST_NAME_x']


답

emp[['EMPLOYEE_ID','LAST_NAME','MANAGER_ID']]

pd.merge(emp,emp,left_on='MANAGER_ID',right_on='EMPLOYEE_ID')[['LAST_NAME_x','LAST_NAME_y']]

# 관리자가 없는 사원도 뽑기
pd.merge(emp,emp,left_on='MANAGER_ID',right_on='EMPLOYEE_ID',how='left')[['LAST_NAME_x','LAST_NAME_y']]




[문제115] city별 근무인원수를 출력하세요.
x = pd.merge(emp,dept,on='DEPARTMENT_ID',how='left')
y = pd.merge(x,loc,on='LOCATION_ID',how='left')
y.CITY.value_counts(dropna=False)

z = y.CITY.value_counts(dropna=False).reset_index()
z.columns = ['CITY','근무인원수']
z
z.loc[z['CITY']==None,'CITY'] 


답

e = emp['EMPLOYEE_ID'].groupby(emp['DEPARTMENT_ID']).count()
d = pd.merge(e,dept,left_index=True,right_on='DEPARTMENT_ID')
z = pd.merge(d,loc,on='LOCATION_ID')[['CITY','EMPLOYEE_ID']]
z = z.rename(columns={'EMPLOYEE_ID':'인원수'})
z['인원수'].groupby(z['CITY']).sum().sort_values()


[문제116] 부서이름,직업별 급여의 총액을 구하세요.

x = emp.groupby(['DEPARTMENT_ID','JOB_ID'])['SALARY'].sum() # 시리즈로 나온다
x.info()
x.index

df = x.reset_index() # 데이터프레임으로 만들기
df
pd.merge(df,dept,on='DEPARTMENT_ID')[['DEPARTMENT_NAME','JOB_ID','SALARY']]



[문제117] 아래화면과 같이 출력해주세요.

      이름     급여 급여등급
0       King  24000    E
1    Kochhar  17000    E
2    De Haan  17000    E
3     Hunold   9000    C
4      Ernst   6000    C
..       ...    ...  ...

job = pd.read_csv('c:/data/job_grades.csv')


import numpy as np

from pandas import Series,DataFrame
import pandas as pd
job

emp['SALARY']

for i in emp['SALARY']:
    print(job.loc[(i >= job['LOWEST_SAL']) & (i <= job['HIGHEST_SAL']),'GRADE_LEVEL'])

# list로 왜 바꿔야 돼? Series를 DataFrame의 컬럼으로 바로 넣으면 안돼?

grade = [list(job.loc[(i >= job['LOWEST_SAL']) & (i <= job['HIGHEST_SAL']),'GRADE_LEVEL']) for i in emp.SALARY]

[['A'],['E']...] -> ['A','E'] # 중첩 for 문을 이용하면 된다

grade[0][0]
grade[100][0]

grade = [j for i in grade for j in i] # [] 안의 []를 풀어낸다
grade[0]
grade[100]

DataFrame({'이름':emp.LAST_NAME,
           '급여':emp.SALARY,
           '급여등급':grade})

# 리스트로 바꾸고 중첩 풀어내는 과정 말고, 처음부터 index를 없애서 뽑아내자

job.loc[(i >= job['LOWEST_SAL']) & (i <= job['HIGHEST_SAL']),'GRADE_LEVEL'].reset_index(drop=True)[0]
emp.SALARY.apply(lambda arg : job.loc[(arg >= job['LOWEST_SAL']) & (arg <= job['HIGHEST_SAL']),'GRADE_LEVEL'].reset_index(drop=True)[0])




[문제118] 소속 사원이 있는 부서정보를 출력해주세요.
dept[dept['DEPARTMENT_ID'].isin(emp['DEPARTMENT_ID'].unique())]



[문제119] 소속 사원이 없는 부서정보를 출력해주세요.
dept[~dept['DEPARTMENT_ID'].isin(emp['DEPARTMENT_ID'].unique())]

pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='inner')
pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='outer')

new = pd.merge(emp,dept,left_on='DEPARTMENT_ID',right_on='DEPARTMENT_ID',how='outer',indicator=True)
new[new['_merge'] == 'both']

new[new['_merge'] == 'left_only']
new[new['_merge'] == 'right_only']
new[new['_merge'] == 'right_only'][['DEPARTMENT_ID','DEPARTMENT_NAME']]

■ rank

obj = Series([78,80,88,60,50,90,79,99,68,80,80])
obj.sort_values()
obj.sort_values(ascending=False)

# 오름차순 순위
obj.rank()

# 내림차순 순위
obj.rank(ascending=False)
DataFrame({'순위':obj.rank(ascending=False).astype(int),
           '점수':obj})



# 기본값 average
DataFrame({'순위':obj.rank(ascending=False,method='average').astype(int),
           '점수':obj})

DataFrame({'순위':obj.rank(ascending=False,method='min').astype(int),
           '점수':obj})

DataFrame({'순위':obj.rank(ascending=False,method='max').astype(int),
           '점수':obj})

DataFrame({'순위':obj.rank(ascending=False,method='first').astype(int),
           '점수':obj})

df = DataFrame({'순위':obj.rank(ascending=False,method='dense').astype(int),
           '점수':obj})


df.sort_values(by='순위')

obj = Series([70,60,80,None,90])
obj.sort_values()
obj.sort_values(ascending=True,na_position='last')
obj.sort_values(ascending=False)
obj.sort_values(ascending=False,na_position='last')


obj.sort_values(ascending=False,na_position='first')

obj.rank()
obj.rank(ascending=False) # NaN 값은 순위 없이 결측치로 나오는게 기본값
obj.rank(ascending=False,na_option='keep') # 기본값
obj.rank(ascending=False,na_option='top') # 결측치 1등
obj.rank(ascending=False,na_option='bottom') # 결측치 꼴등


df = DataFrame({'영어':[60,80,70],'수학':[50,60,86]},
               index=['이문세','윤건','나얼'])

df
df.rank()
df.rank(ascending=True,axis=0) # 기본값
df.rank(ascending=True,axis=1)

[문제120] 급여를 많이 받는 순으로 10위 까지를 구하세요. 	rank, employee_id, last_name, salary를 출력하세요.
emp['rank'] = emp['SALARY'].rank(ascending=False,method='dense').astype(int)
emp.loc[emp['rank']<= 10,['rank','EMPLOYEE_ID','LAST_NAME','SALARY']].sort_values(by='rank')

emp.drop('rank',axis=1) # 미리보기
del emp['rank']

emp.iloc[0:51][['EMPLOYEE_ID','LAST_NAME','SALARY']].to_csv('c:/data/emp_1.csv',index=False)
emp.iloc[51:][['EMPLOYEE_ID','LAST_NAME','SALARY']].to_csv('c:/data/emp_2.csv',index=False)

df = pd.read_csv('c:/data/emp_1.csv',skiprows=[0])
df.info()

df = pd.read_csv('c:/data/emp_1.csv',skiprows=[0],header=None) # 컬럼이름이 없을 때 첫행을 컬럼이름으로 되지 않게 하는법
df.info()
df

df = pd.read_csv('c:/data/emp_1.csv',skiprows=[0],header=None,names=['empid','name','sal'])
df.info()

emp1 = pd.read_csv('c:/data/emp_1.csv',skiprows=[0],header=None,names=['empid','name','sal'])
emp2 = pd.read_csv('c:/data/emp_2.csv',skiprows=[0],header=None,names=['empid','name','sal'])
emp2.head()

df = emp1.append(emp2,ignore_index=True)
df.info()
df

df = DataFrame()
df

for i in range(1,3):
    file = 'c:/data/emp_{}.csv'.format(i)
    temp = pd.read_csv(file,skiprows=[0],header=None,names=['empid','name','sal'])
    df = df.append(temp,ignore_index=True)

df

# 이렇게 하나하나 안하고 한 디렉토리에 있는 파일 한꺼번에 불러오는 법

import glob

file = 'c:/data1/*'
file_lst = glob.glob(file)

df = DataFrame()
for f in file_lst:
    temp = pd.read_csv(f,skiprows=[0],header=None,names=['empid','name','sal'])
    df = df.append(temp,ignore_index=True)

df

[문제121] yob2016.txt 데이터를 이용해서 아기 이름 순위 10위까지 구하세요.
yob2016 = pd.read_csv('c:/data/yob2016.txt',header=None,names=['name','gender','birth'])
yob2016.head()
yob2016['rank'] = yob2016['birth'].rank(ascending=False,method='dense').astype(int)
yob2016[yob2016['rank']<= 10].sort_values('rank')


[문제122] yob2016.txt 데이터를 이용해서  성별 아기 이름 순위 5위까지 구하세요.

yob2016['gender_rank'] = yob2016['birth'].groupby(yob2016.gender).rank(ascending=False,method='dense').astype(int)
yob2016[yob2016['gender_rank']<= 5]



[문제123] yob2010.txt ~ yob2016.txt  년도별 출생수를 출력해주세요.
import glob
file_lst = glob.glob('c:/data/yob*.txt')
file_lst
years = []
y = 2010
for i in file_lst:
    df = pd.read_csv(i,names=['name','gender','birth'])
    years.append([y,df['birth'].sum()])
    y += 1

years

for i,j in years:
    print(i,j)

with open('c:/data/years.txt','w') as file:
    file.write('년도,출생수\n')
    for i,j in years:
        data = '%s,%s\n'%(i,j)
        file.write(data)


DataFrame(years,columns=['년도','출생수']).to_csv('c:/data/years.csv',index=False)

pd.read_csv('c:/data/years.csv')






[문제124] yob2010.txt ~ yob2016.txt  년도별 성별 출생 현황을 year_gender_total.csv 파일로 생성해주세요.
df = pd.read_csv('c:/data/yob2016.txt',names=['name','gender','birth'])
x = df['birth'].groupby(df.gender).sum()

x.loc['F']




import glob
file_lst = glob.glob('c:/data/yob*.txt')
file_lst
years = DataFrame(columns=['년도','여자','남자'])
years
y = 2010
for i in file_lst:
    df = pd.read_csv(i,names=['name','gender','birth'])
    x = df['birth'].groupby(df.gender).sum()
    years = years.append({'년도':y,'여자':x.loc['F'],'남자':x.loc['M']},ignore_index=True)
    y += 1

years

years.to_csv('c:/data/year_gender_total.csv',index=False)


■ pandas 날짜
import datetime
datetime.datetime.now()

import pands as pd
pd.datetime.now()



# 현재 날짜, 시간 정보를 출력하는 함수

pd.Timestamp.now()
pd.Timestamp.today()

pd.Timestamp(year=2022, month=3, day=17, hour=16, minute=43, second=30, microsecond=1,tz='Asia/Seoul')


# char -> timestamp 형변환 함수
pd.to_datetime('2022-3-17')
pd.to_datetime('2022/3/17')
pd.to_datetime('2022317',format='%Y%m%d')
pd.to_datetime('2022317164630',format='%Y%m%d%H%M%S')

pd.Timestamp.now().year
pd.Timestamp.now().month
pd.Timestamp.now().day
pd.Timestamp.now().hour
pd.Timestamp.now().minute
pd.Timestamp.now().second
pd.Timestamp.now().microsecond
pd.Timestamp.now().dayofweek # 0 : 월 ~ 6 : 일
pd.Timestamp.now().day_name() # 얘만 ()
pd.Timestamp.now().quarter

pd.to_datetime('2021-12-16') - pd.Timestamp.now()
pd.Timestamp.now() - pd.to_datetime('2021-12-16')
(pd.to_datetime('2022-5-20') - pd.Timestamp.now()).days
pd.Timestamp.now() + pd.Timedelta('64 days')
pd.Timestamp.now() - pd.Timedelta('64 days')
pd.Timestamp.now() + pd.Timedelta('1 hours')
pd.Timestamp.now() + pd.Timedelta('60 minutes')
pd.Timestamp.now() + pd.Timedelta('60 min')
pd.Timestamp.now() + pd.Timedelta('3600 seconds')
pd.Timestamp.now() + pd.Timedelta('3600 sec')
pd.Timestamp.now() + pd.Timedelta('365 days 10 hours 3600 sec')
pd.Timestamp.now() + pd.Timedelta('365 day 10 hour 3600 sec')
pd.Timestamp.now() + pd.Timedelta('1:30:0')
pd.Timestamp.now() + pd.Timedelta('10 day 1:30:0')

pd.Timestamp.now() + pd.Timedelta('365 days 1:30:0') # Timedelta 는 years,months는 안된다. 일수로 환산해야해

pd.Timestamp.now() + pd.DateOffset(years=10) # 년수를 더하고 싶으면 DateOffset
pd.Timestamp.now() + pd.DateOffset(years=10,months=1) # 년수, 월수를 더하고 싶으면 DateOffset

# 날짜 시간 수정
pd.Timestamp.now() + pd.DateOffset(year=2021,month=1,day=1,hour=0,minute=0,second=0,microsecond=0) # year, month 단수로 하면 수정의 의미

[문제125] 2003년 이전에 입사한 사원들의 정보를 출력하세요.
emp.loc[emp['HIRE_DATE']<='2003-01-01',['EMPLOYEE_ID','HIRE_DATE']]
emp.loc[pd.to_datetime(emp['HIRE_DATE']) < pd.to_datetime('2003-01-01'),['EMPLOYEE_ID','HIRE_DATE']]

pd.Timestamp.now()
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').year # 단일값이 아닌 Series여서 바로 .year 안돼
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d')[100].year

pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.year # 이 경우 Series를 한번에 .year 하기 위해서 .dt.year
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.month
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.day
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.hour
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.minute
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.second
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.microsecond
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.dayofweek
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.weekday
pd.to_datetime(emp['HIRE_DATE'],format='%Y-%m-%d').dt.day_name()
pd.Timestamp.now().weekday() # 여기선 weekday()

emp.loc[pd.to_datetime(emp['HIRE_DATE']).dt.year < 2003,['EMPLOYEE_ID','HIRE_DATE']]


[문제126] 2005년도에 입사한 사원들의 급여의 총액을 구하세요.
emp.loc[pd.to_datetime(emp['HIRE_DATE']).dt.year == 2005,'SALARY'].sum()





[문제127] 년도별 총액급여를 구하세요.
x = emp.SALARY.groupby(pd.to_datetime(emp['HIRE_DATE']).dt.year).sum()
x
x = x.reset_index() # 시리즈를 reset_index()하는 순간 데이터프레임이 되어 버리네?
x.columns = ['년도','총액급여']
x



[문제128] 입사 요일별 인원수를 구하세요.(한글요일로 출력)

# 뽑아가지고 인덱스 이름만 바꿔주면 되는 부분이잖아.
week = emp['EMPLOYEE_ID'].groupby(pd.to_datetime(emp['HIRE_DATE']).dt.weekday).count()
week.index = ['월','화','수','목','금','토','일']
week

[문제129] 년도, 분기별 급여의 총액을 출력하세요.
pd.to_datetime(emp['HIRE_DATE']).dt.year

x = emp['SALARY'].groupby([pd.to_datetime(emp['HIRE_DATE']).dt.year,pd.to_datetime(emp['HIRE_DATE']).dt.quarter]).sum()
x = DataFrame(x)
x.index.names = ['년도','분기'] # name 말고 names로 하니까 된다!!!!
x

result = x.unstack()
result
result.stack()

result.columns = ['1분기','2분기','3분기','4분기']
result
result.index.name = '년도'

result.fillna(0,inplace=True)
result.stack()

pd.pivot_table(data=emp,
               index=pd.to_datetime(emp['HIRE_DATE']).dt.year,
               columns=pd.to_datetime(emp['HIRE_DATE']).dt.quarter,
               values='SALARY',
               aggfunc='sum')

pd.pivot_table(data=emp,
               index=pd.to_datetime(emp['HIRE_DATE']).dt.year,
               columns=pd.to_datetime(emp['HIRE_DATE']).dt.quarter,
               values='SALARY',
               aggfunc=['sum','mean'])


[문제130] 년도, 직무별 입사한 인원수를 출력해주세요.

pt   = pd.pivot_table(data=emp,
                       index=pd.to_datetime(emp['HIRE_DATE']).dt.year,
                       columns='JOB_ID',
                       values='EMPLOYEE_ID',
                       aggfunc='count')
pt.fillna(0,inplace=True)
pt.index.name ='년도'
pt.



x = emp['EMPLOYEE_ID'].groupby([pd.to_datetime(emp['HIRE_DATE']).dt.year,emp['JOB_ID']]).count()
x = x.unstack()
x.index.name = '년도'
x.columns.name = '직무'
x.fillna(0,inplace=True)
x


# 멀티인덱스 해결법
x = emp['EMPLOYEE_ID'].groupby([pd.to_datetime(emp['HIRE_DATE']).dt.year,emp['JOB_ID']]).count()
x.index
x.index.names = ['년도','직무'] # names가 먹히네 이렇게 해도 되고
x

x.reset_index()
x.reset_index(level='HIRE_DATE')

x.index = pd.MultiIndex.from_tuples([(2001,'AD_VP'),(),()]) # 아니면 이렇게 일일이 해야 돼



[문제131] 근무일수가 가장 많은 10위까지 직원들의 EMPLOYEES_ID, LAST_NAME, DEPARTMENT_NAME, 근무일수 출력해주세요.

emp
dept

x = pd.merge(emp,dept,on='DEPARTMENT_ID',how='inner')
x['rank'] = (pd.Timestamp.now() - pd.to_datetime(x['HIRE_DATE'])).dt.days.rank(ascending=False,method='dense').astype(int)
x['rank']


x['days'] =(pd.Timestamp.now() - pd.to_datetime(x['HIRE_DATE'])).dt.days

x.loc[x['rank'] <= 10 , ['EMPLOYEE_ID','LAST_NAME','DEPARTMENT_NAME','days']].sort_values(by='rank') # 이거 왜 오류나는지 다시




답

x = DataFrame({'사번': emp.EMPLOYEE_ID,
           '이름': emp.LAST_NAME,
           '부서코드': emp.DEPARTMENT_ID,
           '근무일수' : (pd.Timestamp.now() - pd.to_datetime(emp['HIRE_DATE'])).dt.days})

x
x['순위'] = x['근무일수'].rank(ascending=False,method='dense').astype(int)
top_10 = x[x['순위']<=10].sort_values(by='순위')
top_10

pd.merge(top_10,dept,left_on='부서코드',right_on='DEPARTMENT_ID')[['사번','이름','근무일수','DEPARTMENT_NAME']]

# 미리 데이터셋 자체를 날짜형으로 바꿔놓고 하는 법

emp.HIRE_DATE = pd.to_datetime(emp.HIRE_DATE)

emp = pd.read_csv('c:/data/employees.csv',parse_dates=['HIRE_DATE']) # parse_dates : 날짜로 바꾸면서 불러들이기. 그런데 만약 2020-01-01, 2020/01/01 이 경우 빼고는 안돼
emp.info()


emp = pd.read_csv('c:/data/employees.csv',parse_dates=['HIRE_DATE'], date_parser=lambda arg:pd.to_datetime(arg,format='%Y-%m-%d')) # 이렇게도 할 수 있는데 너무 복잡해



■ matplotlib

1. pie chart
- 범주형 자료에 대한 그래프를 그릴 때 사용
- 원을 그린 후 각 계급의 상대도수에 대한 면적 또는 부분으로 나눈다


import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/windows/fonts/HMKMMAG.TTF').get_name()
rc('font',family=font_name)


labels = ['좋다','보통','싫다','무응답']
frequency = [45,25,20,10]

survey = DataFrame({'frequency':frequency}, index= labels)
survey.frequency.plot(kind='pie')
survey.frequency.plot(kind='pie',
                      figsize=(7,15),
                      autopct='%.1f%%',
                      startangle=40,
                      colors=['skyblue','red','green','bisque'],
                      title='고객만족도조사',
                      legend=True,
                      fontsize=10) # 그래프 사이즈(가로, 세로) .1f 실수 소수점 1자리까지

survey.frequency.plot.pie()

plt.pie(survey.frequency,
        shadow=True,
        autopct='%.1f%%',
        explode=(0.1,0.1,0,0))

plt.title('고객만족도조사',size=10)
#plt.legend(labels=survey.index,loc='best')
plt.legend(labels=survey.index,loc='lower center',ncol=4)

plt.pie(survey.frequency,
        shadow=True,
        autopct='%.1f%%',
        #explode=(0.1,0.1,0,0),
        wedgeprops={'width':0.7,'linewidth':1,'edgecolor':'white'})

plt.show()

[문제132] blood.csv 파일을 읽어 들여서 도수분포표를 작성하시고, pie chart 생성해주세요.
blood = pd.read_csv('c:/data/blood.csv')
blood
blood_cnt = blood.NAME.groupby(blood.BLOODTYPE).count()
blood_cnt = blood_cnt.reset_index()
blood_cnt.columns = ['혈액형','인원수']
blood_cnt

plt.pie(blood_cnt.인원수,
        shadow=True,
        autopct='%.1f%%')

plt.title('혈액형',size=10)
plt.legend(labels=blood_cnt.혈액형,loc='upper right',ncol=4)


답

x= blood.BLOODTYPE.value_counts()

plt.pie(x,
        shadow=True,
        autopct='%.1f%%',
        #explode=(0.1,0.1,0,0),
        colors=['skyblue','red','green','bisque'],
        textprops={'fontsize':10,'color':'white'},
        wedgeprops={'width':0.7,'linewidth':1,'edgecolor':'white'})
plt.title('혈액형 현황',size=18)
plt.legend(labels=x.index,loc='upper right',ncol=2)

plt.show()


[문제133] 요일별 입사인원수를 pie chart 생성해주세요.


week = emp['EMPLOYEE_ID'].groupby(pd.to_datetime(emp['HIRE_DATE']).dt.weekday).count()
week.index = ['월','화','수','목','금','토','일']
week

plt.pie(week,
        shadow=True,
        autopct='%.1f%%',
        #explode=(0.1,0.1,0,0),
        colors=['red','orange','yellow','green','blue','navy','purple'],
        textprops={'fontsize':18,'color':'black'},
        wedgeprops={'width':0.7,'linewidth':1,'edgecolor':'white'},
        labels=week.index)
plt.title('요일별 입사 인원수',size=18)
plt.legend(labels=week.index,loc='upper right',ncol=7)

plt.show()

2. 막대그래프(bar chart)
- 각 범주에서 도수의 크기를 막대높이로 표현

x = [1,2,3]
y = [90,79,65]
plt.bar(x,y,color=['orange','green','blue'])
plt.title('과목별 점수 현황',size=10)
plt.xlabel('과목', size=7)
plt.ylabel('점수', size=7)
plt.xticks(x,['SQL','R','PYTHON'])

[문제134] 부서별 입사인원수를 막대그래프로 시각화해주세요. 단, 소속부서가 없는 사원의 인원수도 출력해주세요
emp = pd.read_csv('c:/data/employees.csv')
dept = pd.read_csv('c:/data/departments.csv')

emp.EMPLOYEE_ID.groupby(emp.DEPARTMENT_ID).count()

x = emp.DEPARTMENT_ID.value_counts(dropna=False,sort=False)
x.index

x = emp.DEPARTMENT_ID.fillna(999).value_counts()
x.sort_index(inplace=True)
x = x.reset_index()
x.columns = ['부서','도수']
x.부서 = x.부서.astype(int)
x.도수 / x.도수.sum()

x.loc[x.부서==999,'부서'] = '부서X'
x

# 수직 막대그래프

plt.bar(x.index,x.도수) # x 축에 float값만 들어가니까, 일단 index로 넣어놓고 나중에 xticks로 변경
plt.title('부서별 인원수 현황',size=18)
plt.xlabel('부서', size=10)
plt.ylabel('입사인원수', size=10)
plt.xticks(x.index,x.부서) 

x.도수.plot(kind='bar') # 이렇게 바로도 할 수 있어
plt.title('부서별 인원수 현황',size=18)
plt.xlabel('부서', size=10)
plt.ylabel('입사인원수', size=10)
plt.xticks(x.index,x.부서,fontsize=8,color='red',rotation=0)
plt.yticks(range(0,55,5))

# 수평 막대그래프
plt.barh(x.index,x.도수)
plt.title('부서별 인원수 현황',size=18)
plt.ylabel('부서', size=10,rotation=0)
plt.xlabel('입사인원수', size=10)
plt.yticks(x.index,x.부서,fontsize=8,color='red',rotation=0)
plt.xticks(range(0,55,5))

x.도수.plot(kind='barh') # 이렇게 바로도 할 수 있어
plt.title('부서별 인원수 현황',size=18)
plt.ylabel('부서', size=10)
plt.xlabel('입사인원수', size=10)
plt.yticks(x.index,x.부서,fontsize=8,color='red',rotation=0)
plt.xticks(range(0,55,5))

x_cross = pd.crosstab(emp.DEPARTMENT_ID.fillna(999),columns='도수') # 바로 정렬된 결과로 줌
x_cross.plot(kind='bar')
x_cross.plot(kind='barh')


data={'홍길동':[15,13,11],
      '제임스':[13,14,15],
      '하든':[10,9,12]}
data
df = DataFrame(data,index=[2020,2021,2022])
df
df.plot(kind='bar')
df.plot(kind='barh')

df.홍길동.plot(kind='bar')

# 스택형 막대그래프
df.plot(kind='bar',stacked=True)
df.plot(kind='barh',stacked=True)


fruit = pd.read_csv('c:/data/fruits_sales.csv')
fruit

[문제135] fruits_sales.csv 의 데이터를 이용해서 과일의 년도별 수량을 막대그래프로 시각화 해주세요.
fruit
fruit.plot(kind='bar')

fruit.groupby(['year','name'])['qty'].sum().unstack()


fruit.set_index('year',inplace=True)
fruit
df= pd.pivot_table(data=fruit,
               index='year',
               columns='name',
               values='qty')

df.plot(kind='bar',stacked=True)



x=[1,2,3]
y=[90,80,70]

font = {'family':'serif','color':'darkred','size':10} # serif 한글 깨짐
font = {'color':'darkred','size':10}
box = dict(boxstyle='round',edgecolor='black',facecolor='white')

plt.bar(x,y)
plt.text(1,91,90,fontdict=font,bbox=box)
plt.text(3,75,'열심히 공부하자',fontdict=font,bbox=box, rotation=30)

[문제136] 요일별 입사 인원수를 수직형 막대그래프로 시각화, 빈도수도 출력

week = emp.EMPLOYEE_ID.groupby(pd.to_datetime(emp['HIRE_DATE']).dt.weekday).count()
week.index=['월','화','수','목','금','토','일']
week

plt.bar(week.index,week)

font = {'color':'purple','size':12}
box = dict(boxstyle='round',edgecolor='black',facecolor='white')

for i in range(0,len(week)):
    plt.text(i-0.1,week[i]+0.2,week[i],fontdict=font,bbox=box)



[문제137] 분기별 입사 인원수를 원형차트, 막대그래프로 시각화 해주세요.

x = emp.EMPLOYEE_ID.groupby(pd.to_datetime(emp['HIRE_DATE']).dt.quarter).count()

plt.pie(x)
plt.bar(x.index,x)


plt.pie(x,autopct='%1.1f%%')
plt.legend(labels=[str(i)+'분기'for i in x.index],loc='lower center', ncol=4)
plt.title('분기별 입사 현황',fontsize=10)

plt.bar(x.index,x)
plt.xticks(x.index,[str(i) + '분기' for i in x.index])

for i in x.index:
    plt.text(i-0.1,x[i]+0.2,x[i])
    
    
ax = x.plot(kind='bar')
ax.set_xticklabels([str(i) + '분기' for i in x.index],rotation=0)
ax.set_xlabel('분기')
ax.set_ylabel('인원수')
for i in x.index:
    plt.text(i-0.1,x[i]+0.2,x[i])

# 좌표를 확인하는 법

ax.patches
for i in ax.patches:
    print(i)

for i in ax.patches:
    print(i.get_bbox().bounds)



ax = x.plot(kind='bar')
ax.set_xticklabels([str(i) + '분기' for i in x.index],rotation=0)
ax.set_xlabel('분기')
ax.set_ylabel('인원수')
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    plt.text(left,height,height)



# fruit 스택형에 text넣기

fruit
fruit.plot(kind='bar')

fruit.groupby(['year','name'])['qty'].sum().unstack()


fruit.set_index('year',inplace=True)
fruit
df= pd.pivot_table(data=fruit,
               index='year',
               columns='name',
               values='qty')

ax = df.plot(kind='bar',stacked=True)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    
    plt.text(left,bottom+(height//2),int(height))


ax = df.plot(kind='barh',stacked=True)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    
    plt.text(left+(width//2),bottom+0.2,int(width))


[문제138] 2010 ~ 2016년도까지 성별 출생 현황을 막대그래프로 시각화해주세요.

import glob
file_lst = glob.glob('c:/data/yob*.txt')
file_lst
years = DataFrame(columns=['년도','여자','남자'])
years
y = 2010
for i in file_lst:
    df = pd.read_csv(i,names=['name','gender','birth'])
    x = df['birth'].groupby(df.gender).sum()
    years = years.append({'년도':y,'여자':x.loc['F'],'남자':x.loc['M']},ignore_index=True)
    y += 1


years.set_index('년도',inplace=True)

import matplotlib as mpl

ax = years.plot(kind='bar',stacked=True,color=['pink','skyblue'])
ax.set_xticklabels([str(i)+'년' for i in years.index],rotation=0)
ax.xaxis.label.set_visible(False)
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))

for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    plt.text(left,bottom+(height//2),int(height))


3.line plot
- 선을 그리는 그래프
- 시간, 순서 등에 따라 어떻게 변하는지 보여주는 그래프

years.plot()

years['남자'].plot()
years['여자'].plot()

plt.plot(years.index,years.여자,label='여자',color='coral',linestyle=':')
plt.plot(years.index,years.남자,label='남자',color='coral',linestyle='--')
plt.plot(years.index,years.남자,label='남자',color='coral',linestyle='-.')
plt.plot(years.index,years.남자,label='남자',color='coral',linestyle='-')

plt.legend()

[문제139] 년도별 입사 인원수를 bar plot, line plot 을 생성해주세요.

import numpy as np


years = emp['EMPLOYEE_ID'].groupby(pd.to_datetime(emp['HIRE_DATE']).dt.year).count()
years




plt.plot(years.index,years,linestyle='--')


ax = years.plot(kind='bar')
ax.set_xticklabels([str(i) + '년' for i in years.index],rotation=0)
ax.set_xlabel('년도')
ax.set_ylabel('인원수',rotation=0)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    plt.text(left,height,height)


답
cmap = plt.get_cmap('PuRd')
colors = [cmap(i) for i in np.linspace(0,1,8)]
colors
[i for i in np.linspace(0,1,8)]


plt.bar(years.index,years,color=colors)

ax = plt.bar(years.index,years,color=colors)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    plt.text((left_width/2)-0.1,height+0.1,int(height))



ax = plt.bar(years.index,years,color=colors)
plt.annotate('최대값',(2005-0.4,29),color='red')

ax = plt.bar(years.index,years,color=colors)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    plt.annotate(int(height),((left+width/2)-0.1,height+0.1),color='red')


# annotate 화살표로 표현할 때 자주 쓴다
ax = plt.bar(years.index,years,color=colors)
plt.annotate('max',xy=(2005,29),xytext=(2002,20),arrowprops={'arrowstyle':'wedge'})


ax = plt.bar(years.index,years,color=colors)
plt.annotate('max',xy=(2005,29),xytext=(2002,20),arrowprops={'arrowstyle':'->'})



plt.plot(years.index,years,linestyle='--')
plt.annotate('max',xy=(2005,29),xytext=(2002,20),arrowprops={'arrowstyle':'->','facecolor':'red','color':'blue'})


[문제140] 감염병_발생현황.csv 데이터를 이용해서  년도별 감염병 발생현황을 bar plot, line plot 을 생성해주세요.

import pandas as pd
from pandas import Series,DataFrame

pd.read_csv('c:/data/감염병_발생현황.csv',encoding='utf-8') # 이거 안되고, 파일 자체를 다시 UTF-8로 설정해서 저장하니까 그냥 불러들여도됨
pd.read_csv('c:/data/감염병_발생현황.csv',engine='python')

data = pd.read_csv('c:/data/감염병_발생현황.csv')

data = data.drop([0,1])
data
data = data.drop('법정전염병군별(1)',axis=1)
data
data.reset_index(drop=True,inplace=True)
data.set_index('법정전염병군별(2)',inplace=True)
data.index.name = '전염병'
data=data.T
data=data.astype('int')


ax = data.plot(kind='bar',stacked=True)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    
    plt.text(left,bottom+(height//2),int(height))



답
data = pd.read_csv('c:/data/감염병_발생현황.csv')
data = data.iloc[2:,1:].T
infection = data.iloc[1:]
infection.columns = data.iloc[0]
infection
infection.index
infection.columns.name = None
infection.info()
infection = infection.astype(int)
infection.info()

infection.plot(kind='bar')
infection.iloc[:,:-1].plot(kind='bar') # 마지막 열 것만 너무 커서

infection.iloc[:,-1].plot(kind='bar') # 마지막 열 것만 너무 커서 따로



infection.plot()
infection.iloc[:,:-1].plot() # 마지막 열 것만 너무 커서
infection.iloc[:,-1].plot() # 마지막 열 것만 너무 커서 따로



# 두 개를 한 화면에 각각 한꺼번에 표현하는 법

plt.figure(figsize=(10,10))
plt.subplot(2,1,1) # subplot(nrow,ncol,index)
plt.plot(infection.iloc[:,:-1])
plt.legend(labels=infection.columns[:-1])
plt.xticks(infection.index,[str(i) +'년' for i in infection.index])

plt.subplot(2,1,2)
plt.plot(infection.iloc[:,-1])
plt.legend(labels=infection.columns[-1])
plt.xticks(infection.index,[str(i) +'년' for i in infection.index])


# 또 다른 방법.  이걸 보편적으로 많이 씀!
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(infection.iloc[:,:-1],'r*')# marker='o',markerfacecolor='red',markersize=10)
ax1.legend(labels=infection.columns[:-1])
ax1.set_xticklabels([str(i) +'년' for i in infection.index]) # .xtics는 여기선 안돼

ax2.plot(infection.iloc[:,-1],marker='*')
ax2.legend(labels=infection.columns[-1])
ax2.set_xticklabels([str(i) +'년' for i in infection.index])






[문제141] 코로나 바이러스 데이터에서 가장 최근 국가별 확진자, 사망자, 회복자 수를 구한후 확진자 수로 내림차순 정렬하세요. 1,4,5,6,7

covid = pd.read_csv('c:/data/covid_19.csv')

covid = covid.iloc[:,[1,4,5,6,7]]

covid = covid.groupby(['Country/Region'])['Confirmed','Deaths','Recovered'].sum().sort_values(by=['Confirmed'],ascending=False)


답
covid = pd.read_csv('c:/data/covid_19.csv')
covid.head()
covid['Date'] = pd.to_datetime(covid['Date'])

covid['Date'].min()
covid['Date'].max()

lately_covid = covid[covid['Date'] == covid['Date'].max()]
lately_covid[lately_covid['Country/Region'].str.lower().str.contains('korea')]
lately_covid[lately_covid['Country/Region'].str.lower().str.contains('china')]

result = lately_covid.groupby('Country/Region').aggregate({'Confirmed':'sum','Deaths':'sum','Recovered':'sum'})


result
result.sort_values(by='Confirmed',ascending=False)

# 그냥 내가 한대로 이렇게 해도 같음
result = lately_covid.groupby('Country/Region')['Confirmed','Deaths','Recovered'].sum().sort_values(by=['Confirmed'],ascending=False)




[문제142] 가장 최근 국가별 확진자 수가 가장 많은 10개의 국가의 확진자수,사망자수,회복자수를 그룹형 막대그래프  시각화 하세요
top_10 = covid.iloc[:10]


ax = top_10.plot(kind='bar',stacked=True)
for i in ax.patches:
    left,bottom,width,height = i.get_bbox().bounds
    
    plt.text(left,bottom+(height//2),int(height))

답
    
result['rank'] = result.Confirmed.rank(ascending=False,method='dense').astype(int)

top10 = result[result['rank']<=10].sort_values(by='rank')
top10

ax = top10.iloc[:,:-1].plot(kind='bar')
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))



[문제143] 날짜별 확진자수,사망자수,회복자수를 꺽은선 그래프로 시각화 하세요.
covid = pd.read_csv('c:/data/covid_19.csv')

covid = covid.iloc[:,[1,4,5,6,7]]
covid_date = covid.groupby(['Date'])['Confirmed','Deaths','Recovered'].sum()

plt.plot(covid_date)
plt.legend(labels=covid_date)
plt.xticks(covid_date.index,[str(i) for i in covid_date.index],rotation=40)

답
covid = pd.read_csv('c:/data/covid_19.csv')
covid.head()
covid['Date'] = pd.to_datetime(covid['Date'])

result_date = covid.groupby('Date').aggregate({'Confirmed':'sum','Deaths':'sum','Recovered':'sum'})
result_date.plot()


plt.plot(result_date.index,result_date.Confirmed,label='Confirmed')
plt.plot(result_date.index,result_date.Deaths,label='Deaths')
plt.plot(result_date.index,result_date.Recovered,label='Recovered')
plt.legend()
plt.xticks(rotation=70)

import matplotlib.ticker as ticker
from matplotlib.dates import DateFormatter


ax = result_date.Confirmed.plot()
ax.xaxis.set_major_formatter(DateFormatter('%Y%m%d'))
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
plt.xticks(rotation=90)


■ folium
지도 시각화 라이브러리

(base) C:\Users\user>pip install folium

import folium

m = folium.Map(location = [37.49818758750994, 127.02764044946089], zoom_start=13) #tiles='Stamen Terrain'
folium.Marker(location=[37.49818758750994, 127.02764044946089],
              popup='itwill',
              icon=folium.Icon(color='red',icon='star')).add_to(m)

m.save('c:/data/map1.html')


m = folium.Map(location = [37.49818758750994, 127.02764044946089], zoom_start=13) #tiles='Stamen Terrain'
folium.Marker(location=[37.49818758750994, 127.02764044946089],
              color='red',
              radius=100,
              tooltip='학원주변').add_to(m)

m.save('c:/data/map1.html')



lately_covid

m = folium.Map(location = [0, 0], zoom_start=13) #tiles='Stamen Terrain'
for i in lately_covid.index:
    folium.CircleMarker([lately_covid['Lat'][i],lately_covid['Long'][i]],
                        radius=int(lately_covid['Confirmed'][i]/100000),
                        color='red',
                        fill='True',
                        popup=lately_covid['Country/Region'][i],
                        tooltip=int(lately_covid['Confirmed'][i])).add_to(m)
                  

m.save('c:/data/map2.html')






■ 강남구, 구로구의 한식,양식,중식 음식점 비율 비교

data = pd.read_csv('c:/data/소상공인시장진흥공단_상가(상권)정보_서울_202112.csv')



gangnam = data[(data['시군구명']=='강남구')&(data['상권업종중분류명'].isin(['한식','양식','중식']))]
gangnam.reset_index(drop=True,inplace=True)

gooro = data[(data['시군구명']=='구로구')&(data['상권업종중분류명'].isin(['한식','양식','중식']))]
gooro.reset_index(drop=True,inplace=True)

# 비율 분석

n_k = len(gangnam[gangnam['상권업종중분류명']=='한식'])
n_w = len(gangnam[gangnam['상권업종중분류명']=='양식'])
n_c = len(gangnam[gangnam['상권업종중분류명']=='중식'])

round((n_k / (n_k + n_w + n_c)) * 100) # 71%
round((n_w / (n_k + n_w + n_c)) * 100) # 23%
round((n_c / (n_k + n_w + n_c)) * 100) # 6%

r_k = len(gooro[gooro['상권업종중분류명']=='한식'])
r_w = len(gooro[gooro['상권업종중분류명']=='양식'])
r_c = len(gooro[gooro['상권업종중분류명']=='중식'])

round((r_k / (r_k + r_w + r_c)) * 100) # 80%
round((r_w / (r_k + r_w + r_c)) * 100) # 6%
round((r_c / (r_k + r_w + r_c)) * 100) # 14%


# 시각화

m = folium.Map(location = [37.566640, 126.877458], zoom_start=20)

for i in gangnam.index:
    if gangnam.iloc[i]['상권업종중분류명'] =='한식':
        folium.CircleMarker([gangnam['위도'][i],gangnam['경도'][i]],
                            radius=5,
                            color='black',
                            fill='True',
                            popup=gangnam['도로명주소'][i],
                            tooltip=gangnam['상호명'][i]).add_to(m)
    elif gangnam.iloc[i]['상권업종중분류명'] =='양식':
        folium.CircleMarker([gangnam['위도'][i],gangnam['경도'][i]],
                            radius=5,
                            color='blue',
                            fill='True',
                            popup=gangnam['도로명주소'][i],
                            tooltip=gangnam['상호명'][i]).add_to(m)
    elif gangnam.iloc[i]['상권업종중분류명'] =='중식':
        folium.CircleMarker([gangnam['위도'][i],gangnam['경도'][i]],
                            radius=5,
                            color='red',
                            fill='True',
                            popup=gangnam['도로명주소'][i],
                            tooltip=gangnam['상호명'][i]).add_to(m)



for i in gooro.index:
    if gooro.iloc[i]['상권업종중분류명'] =='한식':
        folium.CircleMarker([gooro['위도'][i],gooro['경도'][i]],
                            radius=5,
                            color='black',
                            fill='True',
                            popup=gooro['도로명주소'][i],
                            tooltip=gooro['상호명'][i]).add_to(m)
    elif gooro.iloc[i]['상권업종중분류명'] =='양식':
        folium.CircleMarker([gooro['위도'][i],gooro['경도'][i]],
                            radius=5,
                            color='blue',
                            fill='True',
                            popup=gooro['도로명주소'][i],
                            tooltip=gooro['상호명'][i]).add_to(m)
    elif gooro.iloc[i]['상권업종중분류명'] =='중식':
        folium.CircleMarker([gooro['위도'][i],gooro['경도'][i]],
                            radius=5,
                            color='red',
                            fill='True',
                            popup=gooro['도로명주소'][i],
                            tooltip=gooro['상호명'][i]).add_to(m)
        
m.save('c:/data/S_food2.html')


[문제144] 도수분포표를 생성해주세요.
ages = [21,24,26,27,29,31,37,39,40,42,45,50,51,59,60,69]

------------------------
계급            도수
------------------------
2O(20~29)         5
30(30~39)         3
40(40~49)         3
50(50~59)         3
60(60~)           2

frequency_table = {20:0,30:0,40:0,50:0,60:0}

for i in ages:
    if 20 <= i and i < 30:
        frequency_table[20] += 1
    elif 30 <= i and i < 30:
        frequency_table[30] += 1
    elif 40 <= i and i < 50:
        frequency_table[40] += 1
    elif 50 <= i and i < 60:
        frequency_table[50] += 1
    elif 60 <= i:
        frequency_table[60] += 1



frequency_table = {}

for i in range(20,61,10):
    frequency_table.setdefault(i,0)

for i in ages:
    if 20 <= i and i < 30:
        frequency_table[20] += 1
    elif 30 <= i and i < 30:
        frequency_table[30] += 1
    elif 40 <= i and i < 50:
        frequency_table[40] += 1
    elif 50 <= i and i < 60:
        frequency_table[50] += 1
    elif 60 <= i:
        frequency_table[60] += 1

[문제145] 도수분포표를 생성해주세요. 수치형 자료를 범주형자료로 변환한 후 빈도수를 구하세요.
ages = [21,24,26,27,29,31,37,39,40,42,45,50,51,59,60,69]


21 -> '20대'


------------------------
계급            도수
------------------------
2O대(20~29)         5
30대(30~39)         3
40대(40~49)         3
50대(50~59)         3
60대(60~)           2

ages = [21,24,26,27,29,31,37,39,40,42,45,50,51,59,60,69]
ages_label = []


for i in ages:
    if 20 <= i and i < 30:
        ages_label.append('20대')
    elif 30 <= i and i < 40:
        ages_label.append('30대')

    elif 40 <= i and i < 50:
        ages_label.append('40대')

    elif 50 <= i and i < 60:
        ages_label.append('50대')

    elif 60 <= i:
        ages_label.append('60대')

ages_label

from pandas import Series,DataFrame

Series(ages_label).value_counts()

pd.crosstab(Series(ages_label),columns='freq')

import collections
collections.Counter(ages_label)

import numpy as np

np.unique(Series(ages_label),return_counts=True)

■ cut
연속형 데이터를 범주형 데이터로 변환하는 함수

ages = [21,24,26,27,29,31,37,39,40,42,45,50,51,59,60,69]
bins = [20,30,40,50,60,70]

right = True
20 < ages <= 30

right = False
20 <= ages < 30

pd.cut(ages,bins,right=False).value_counts()

age_cut = pd.cut(ages,bins,right=False)
age_cut.value_counts()
age_cut.codes
age_cut.categories

label = ['20대','30대','40대','50대','60대이상']
pd.cut(ages,bins,right=False,labels=label).value_counts()

4. histogram
자료가 모여있는 위치나 자료의 분포관에 한 대략적인 정보를 한눈에 파악하는 그래프

ages = [21,24,26,27,29,31,37,39,40,42,45,50,51,59,60,69]

import matplotlib.pylab as plt

plt.hist(ages)
plt.hist(ages,bins=5)
plt.hist(ages,bins='auto')


bins = [20,30,40,50,60,70]
plt.hist(ages,bins=bins)

plt.hist(ages,bins=5,density=True,histtype='step')
plt.hist(ages,bins=5,orientation='horizontal')

[문제146] weight.txt 데이터를 도수분포표, 히스토그램을 생성해주세요.

import numpy as np
weight = np.loadtxt('c:/data/weight.txt')
weight.shape
weight= weight.reshape((50,))
weight.shape
weight

weight.max()
weight.min()

bins = list(range(50,101,10))
bins
label = ['50kg이상','60kg이상','70kg이상','80kg이상','90kg이상']
pd.cut(weight,bins=bins,right=False,labels=label).value_counts()

plt.hist(weight,bins=bins)

Series(weight).describe()

np.percentile(weight,[0,25,50,75,100])
np.percentile(weight,[0,30,60,80,100])


weight[weight >= np.percentile(weight,95)] # 상위 5%
weight[weight <= np.percentile(weight,10)] # 하위 10%

5. box plot
- 데이터가 어떤 범위에 걸쳐 존재하는지 분포를 체크할 때 사용되는 그래프
- 다섯 수치 요약을 제공하는 그래프
- 이상치 데이터를 확인할 때 좋은 그래프

plt.boxplot(weight,labels=['몸무게'])
plt.boxplot(weight,labels=['몸무게'],vert=False)


min = np.percentile(weight,0)
q1 = np.percentile(weight,25)
q2 = np.percentile(weight,50)
q3 = np.percentile(weight,75)
max = np.percentile(weight,100)

# 사분위 범위(Inter Quartile Range)
iqr = q3 - q1

# lower fence : 이 값보다 작으면 이상치 데이터
lf = q1 - 1.5 * iqr

# upper fence : 이 값보다 크면 이상치 데이터
uf = q3 + 1.5 * iqr

plt.boxplot(weight,labels=['몸무게'],vert=False)
plt.text(weight[weight < lf][0],1.09,weight[weight < lf][0],color='red')
plt.text(q1,1.09,q1,color='red')
plt.text(q2,1.09,q2,color='red')
plt.text(q3,1.09,q3,color='red')
plt.text(weight[weight >= lf].min(),1.09,weight[weight >= lf].min(),color='red')
plt.text(weight[weight <= uf].max(),1.09,weight[weight <= uf].max(),color='red')
plt.text(lf,0.9,lf,color='blue')
plt.text(uf,0.9,uf,color='blue')

[문제147] noise.txt 데이터를 도수분포표, 히스토그램, boxplot 생성하세요

import numpy as np
noise = np.loadtxt('c:/data/noise.txt')
noise.shape
noise = noise.reshape((50,))
noise

ascending = np.argsort(noise) # array 오름차순 정렬 인덱스
noise[ascending]

descending = np.argsort(noise[::-1]) # array 내림차순 정렬 인덱스

Series(noise).quantile() # 중위수 값을 리턴
Series(noise).quantile([0,0.25,0.5,0.75,1])
np.percentile(noise,[0,25,50,75,100])
np.min(noise)
np.max(noise)
np.mean(noise)


noise.min()
noise.max()
bins = list(range(50,81,5))
label = ['50이상','55이상','60이상','65이상','70이상','75이상']

# 도수분포표
pd.cut(noise,bins=bins,right=False,labels=label).value_counts()

# 히스토그램
plt.hist(noise,bins=bins)

# boxplot
min = np.percentile(noise,0)
q1 = np.percentile(noise,25)
q2 = np.percentile(noise,50)
q3 = np.percentile(noise,75)
max = np.percentile(noise,100)

iqr = q3 - q1
lf = q1 - 1.5 * iqr
uf = q3 + 1.5 * iqr

plt.boxplot(noise,labels=['노이즈'],vert=False)

plt.text(q1,1.09,q1,color='red')
plt.text(q2,1.09,q2,color='red')
plt.text(q3,1.09,q3,color='red')
plt.text(noise[noise >= lf].min(),1.09,noise[noise >= lf].min(),color='red')
plt.text(noise[noise <= uf].max(),1.09,noise[noise <= uf].max(),color='red')
[plt.text(i,1.09,i,color='red') for i in noise[noise > uf]]
plt.text(lf,0.9,lf,color='blue')
plt.text(uf,0.9,uf,color='blue')

height = pd.read_excel('c:/data/height.xlsx')
height.info()
height.describe()

np.percentile(height.남자,[0,25,50,75,100])
np.percentile(height.여자,[0,25,50,75,100])

plt.boxplot(height.남자)
plt.boxplot(height.여자)
plt.boxplot([height.남자,height.여자],labels=['남자','여자']) # 두개 한번에 표현하기

fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
ax1.boxplot([height.남자,height.여자],labels=['남자','여자'])
ax2.boxplot([height.남자,height.여자],vert=False,labels=['남자','여자'])
ax1.set_title('신입생 성별 키 비교(수직)')
ax2.set_title('신입생 성별 키 비교(수평)')

plt.hist(height.남자)
plt.hist(height.여자)

plt.hist([height.남자,height.여자],bins=5,label=['남자','여자'])
plt.legend(loc='upper left')
plt.show()

plt.hist(height.남자,bins=5,alpha=0.7,label=['남자'])
plt.hist(height.여자,bins=5,alpha=0.7,label=['여자'])
plt.legend(loc='upper left')
plt.show()

6. 줄기잎그림( stem and leaf diagram)
(base) C:\Users\USER>pip install stemgraphic

import stemgraphic

stemgraphic.stem_graphic(height.남자)
stemgraphic.stem_graphic(height.여자)

[문제148] add 함수를 생성하세요.
add(10)
add(20)

result
30

g_total =0
def add(arg):
    global g_total
    g_total += arg
    return g_total

add(10)
add(20)

result = 0
def add(arg):
    global result
    result += arg

add(10)
add(20)
result

add(100) # 새로 하고 싶은데, 이전에 했던 거랑 누적 되어 버리잖아 -> 절차적(구조적)으로 되었다는 뜻
add(200)

■ 절차적(구조적) 지향 프로그램(procedural languages)
- C언어
- 물이 위에서 아래로 흐르는 것처럼 순차적인 처리가 중요시되며 프로그램 전체가
유기적으로 연결되도록 만드는 프로그래밍 기법이다.

- 단점
    1) 재사용할 수 없다.
    2) 확장성이 떨어진다.
    3) 유지보수가 어렵다.

■ 객체지향프로그램(object oriented language)
- JAVA, PYTHON, C++, C#
- 구조적 프로그래밍과 다르게 큰 문제를 작은 문제들로 해결할 수 있는 객체들을 만든 뒤
이 객체들을 조합해서 큰 문제를 해결하는 방법

클래스 : 객체를 설명해 놓은 것(객체의 설계도)
인스턴스 : 클래스를 메모리에 만들어서 사용하도록 하는 것

# class 생성
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self,arg):
        self.result += arg
        return self.result

# class를 사용하도록 instance 생성
c1 = Calculator()
c1.add(10)
c1.add(20)
c1.add(30)

c2 = Calculator()
c2.add(100)
c2.add(200)

class Person:
    name='홍길동'
    age = 20
    def myprint(self):
        print('이름은 {}'.format(self.name))
        print('나이는 {}'.format(self.age))

p1 = Person()
p1.myprint()
p1.name

p2 = Person()
p2.myprint()
p2.name = '제임스'
p2.age = 30
p2.myprint()
p2.job = '데이터 분석가'
p2.job

class Person:
    info=''
    def showinfo(self,name,age):
        self.info += '이름: ' +name+' , '+'나이 : '+str(age)+'\n'

man = Person()
man.showinfo('최유진',26)
man.showinfo('구동매',25)
print(man.info)

woman = Person()
woman.showinfo('고애신',20)
woman.showinfo('이양화',21)
print(woman.info)


class Person:
    hobbys = []
    def add_hobby(self,arg):
        self.hobbys.append(arg)

p1 = Person()
p1.add_hobby('요리')
p1.hobbys

p2 = Person()
p2.add_hobby('러닝')
p2.hobbys # 이 경우 누적됨

p3 = Person()
p3.add_hobby('영화보기')
p3.hobbys # 이 경우 누적됨


__init__ : 클래스를 인스턴스화 할 때 자동으로 생성자가 실행되고 자동으로 초기화해주는 메소드
class Person:
    def __init__(self):
        self.hobbys = []
    def add_hobby(self,arg):
        self.hobbys.append(arg)

p1 = Person()
p1.add_hobby('요리')
p1.hobbys

p2 = Person()
p2.add_hobby('러닝')
p2.hobbys 

p3 = Person()
p3.add_hobby('영화보기')
p3.hobbys 

class Happy:
    def __init__(self):
        print('오늘 하루도 행복하자!!')

h1 = Happy()

class Happy:
    def __init__(self,arg):
        print('{} 오늘 하루도 행복하자!!'.format(arg))

h1 = Happy() # init은 무조건 실행하는거니까, arg 입력안하면 오류나옴

h1 = Happy('홍길동')

x=10
x
type(x)

class 클래스명:
    속성(변수)
    메소드(함수)

class ShowInfo:
    #attribute, method
    pass

s1 = ShowInfo()
type(s1)
isinstance(s1,ShowInfo)

class ShowInfo:
    def __init__(self):
        print('initialize method')

s2 = ShowInfo()

class ShowInfo:
    def __init__(self,name): #self.name의 name과 (self,name) 의 name은 다른거야. 그냥 name은 arg라고 봐야대
        self.name = name # name 형식매개변수(입력변수) self.name 인스턴스 변수
        print('initialize method')
        
    def print_info(self):
        print('Name : ',self.name)



s3 = ShowInfo('james')
s3.name

s4 = ShowInfo('hong')
s4.name
s4.print_info()

id(s3)

s3.__dict__ # 네임스페이스 확인하는 방법
s4.__dict__

class Test:
    def test_1():
        print('클래스 함수')
    def test_2(self):
        print('인스턴스 함수')


t1 = Test()

t1.test_1() # 오류발생
t1.test_2()

Test.test_1() # 클래스 메소드는 이렇게 클래스 이름을 같이. 모든 인스턴스에서 동일하게 실행되도록 할 때 사용

class Employee:
    cnt=0
    def __init__(self,arg1,arg2):
        self.name = arg1
        self.age = arg2
        self.cnt += 1  # 인스턴스 변수. 인스턴스마다 초기화된다
    
    def show(self):
        print('이름 : {} 나이 : {}'.format(self.name,self.age))
    
    def showcnt(self):
        print('전체 접속한 인원은 {}명 입니다.'.format(self.cnt))

e1 = Employee('홍길동',20)
e1.show()
e1.showcnt()

e2 = Employee('하든',30)
e2.show()
e2.showcnt()

class Employee:
    cnt=0
    def __init__(self,arg1,arg2):
        self.name = arg1
        self.age = arg2
        Employee.cnt += 1  # 클래스 변수. 인스턴스가 바뀌어도 초기화되지 않음
    
    def __del__(self):
        print('{} 접속 해지 했습니다.'.format(self.name))
        Employee.cnt -= 1
    
    
    def show(self):
        print('이름 : {} 나이 : {}'.format(self.name,self.age))
    
    def showcnt(self):
        print('전체 접속한 인원은 {}명 입니다.'.format(Employee.cnt))

e1 = Employee('홍길동',20)
e1.show()
e1.showcnt()

e2 = Employee('하든',30)
e2.show()
e2.showcnt()

e3 = Employee('손흥민',30)
e3.show()
e3.showcnt()

dir(e3)
del e3
del e2


[문제 149] 생성자에 이름, 핸드폰번호, 메일, 주소 변수를 생성합니다. 
print_info 메소드를 생성한 후  출력하는 Contact 클래스를 생성하세요.

class Contact:
    def __init__(self,name,pn,email,addr):
        self.name=name
        self.pn = pn
        self.email = email
        self.addr
        
    def print_info(self):
        print('이름 : {}'.format(self.name))
        print('전화번호 : {}'.format(self.pn))
        print('이메일 : {}'.format(self.email))
        print('주소 : {}'.format(self.addr))




[문제150] Set 클래스를 생성하세요.
lst1 = [1,3,2,4,5]
lst2 = [1,4,5,9,8]        

s = Set(lst1,lst2)
s.union()
s.union_all()
s.intersect()
s.minus()

def union(x,y):
    x_1 = []
    for i in x:
        if i not in x_1:
            x_1.append(i)
    y_1 = []
    for i in y:
        if i not in y_1:
            y_1.append(i)
            
    result = []
    for i in x_1:
        if i not in y_1:
            result.append(i)
    result = result + y_1
    result.sort()
    
    return result

union(lst1,lst2)

def union_all(x,y):
    result = []
    result = x+y
    result.sort()
    return result

union_all(lst1,lst2)

def intersect(x,y):
    x_1 = []
    for i in x:
        if i not in x_1:
            x_1.append(i)
    y_1 = []
    for i in y:
        if i not in y_1:
            y_1.append(i)
            
    result = []
    for i in x_1:
        if i in y_1:
            result.append(i)
    result.sort()
    
    return result

intersect(lst1,lst2)

def minus(x,y):
    x_1 = []
    for i in x:
        if i not in x_1:
            x_1.append(i)
    y_1 = []
    for i in y:
        if i not in y_1:
            y_1.append(i)
            
    result = []
    for i in x_1:
        if i not in y_1:
            result.append(i)
    result.sort()
    
    return result

minus(lst1,lst2)


s = Set(lst1,lst2)
s.union()
s.union_all()
s.intersect()
s.minus()

class Set:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.result1 = []
        self.result2 = []
        for i in self.x:
            if i not in self.result1:
                self.result1.append(i)
        for i in self.y:
            if i not in self.result2:
                self.result2.append(i)    
                
    def union(self):
        v_union = []
        for i in self.result1:
            if i not in self.result2:
                v_union.append(i)
        v_union = v_union + self.result2
        v_union.sort()
        return v_union
    
    def union_all(self):
        v_union_all = []
        v_union_all = self.x + self.y
        v_union_all.sort()
        return v_union_all

    def intersect(self):
        v_intersect = []
        for i in self.result1:
            if i in self.result2:
                v_intersect.append(i)
        v_intersect.sort()
        return v_intersect
    
    def minus(self):
        v_minus = []
        for i in self.result1:
            if i not in self.result2:
                v_minus.append(i)
        v_minus.sort()
        return v_minus
    
    
    
s = Set(lst1,lst2)
s.union()
s.union_all()
s.intersect()
s.minus()
s.v_minus # self 안붙이고 했기 때문에 로컬변수(함수안)가 되고 이렇게 확인하면 오류가 나온다. self.v_minus로 정의 했었으면, s.minus()를 시행한 후에(인스턴스에서 minus가 정의된 후에) s.v_minus를 실행하면 값이 나온다.

[문제150] Stats 클래스를 생성하세요.
stat = Stats()
stat.sum(1,2,3,4,5)
stat.mean(1,2,3,4,5)
stat.variance(1,2,3,4,5)
round(stat.variance(1,2,3,4,5),2)



def sum(*arg):
    hap = 0
    for i in arg:
        hap += i
    return hap


class Stats:
    def sum(self,*arg):
        self.hap = 0
        for i in arg:
            self.hap += i
        return self.hap
    
    def mean(self,*arg):
        return self.sum(*arg)/len(arg)
    
    def variance(self,*arg):
        self.total = 0
        self.avg = self.mean(*arg)
        for i in arg:
            self.total += (i-self.avg)**2
        return self.total / (len(arg)-1)
    
    def stddev(self,*arg):
        return math.sqrt(self.variance(*arg))
    
    
stat= Stats()    
stat.sum(1,2,3,4,5)
stat.mean(1,2,3,4,5)
stat.variance(1,2,3,4,5)
stat.stddev(1,2,3,4,5)

[문제151] Stats 클래스에 median(중앙값) 함수를 추가해주세요.

Stats.median(3,4,1,2,5)

관측값의 수가 홀수면 : (관측값의 수 +1) / 2
관측값의 수가 짝수면 : x= (관측값의수/2), y=(관측값의수/2) +1, x+y/2

def median(*arg):
    lst = []
    for i in arg:
        lst.append(i)
    lst.sort()
    if len(lst) % 2 == 0:
        return (lst[int(len(lst)/2-1)] + lst[int(len(lst)/2+1-1)])/2
    else:
        return lst[int((len(lst)+1)/2-1)]

median(3,4,1,2,5)

[1,2,3,4,5,6]

class Stats:
    def median(self,*arg):
        self.lst = []
        for i in arg:
            self.lst.append(i) # 튜플은 정렬 안되서 리스트에 넣엇자나 이거 이렇게 하지말고 바로  list(arg)
        self.lst.sort()
        self.len = len(self.lst)
        if self.len % 2 == 0:
            return (self.lst[int(self.len/2-1)] + self.lst[int(self.len/2+1-1)])/2
        else:
            return self.lst[int((self.len+1)/2-1)]

stat = Stats()
stat.median(3,4,1,2,5)



■ 상속 : 부모 클래스에 있는 메소드를 자식클래스에서도 받아서 쓸 수 있게 함
- 클래스의 메소드의 속성을 물려 받는다
- 공통된 내용을 하나로 묶어서 관리할 수 있다

class Parents:
    def __init__(self,name,pn):
        self.name = name
        self.pn =pn
    def show(self):
        print('이름 : {} 전화번호 : {}'.format(self.name,self.pn))

p = Parents('홍길동','010-1000-0001')
p.show()

class Child(Parents):
    def __init__(self,name,pn,addr,sn):
        self.name = name
        self.pn =pn
        self.addr=addr
        self.sn=sn

c = Child('홍하든','010-0001-1004','서울','0000')
c.show()

class Child(Parents):
    def __init__(self,name,pn,addr,sn):
        Parents.__init__(self,name,pn)
        self.addr=addr
        self.sn=sn

c = Child('홍하든','010-0001-1004','서울','0000')
c.show()

class Child(Parents):
    def __init__(self,name,pn,addr,sn):
        Parents.__init__(self,name,pn)
        self.addr=addr
        self.sn=sn
    def show(self): # 실행하고 있는, 자식 클래스에 있는 show(같은이름) 메소드가 우선순위
        Parents.show(self) # 부모에 있는 show도 같이 실행하기
        print('주소 : {} 번호 : {}'.format(self.addr,self.sn))

c = Child('홍하든','010-0001-1004','서울','0000')
c.show()

[문제152] Add 클래스에 두수를 더하는 값을 리턴하는 add 메소드 생성
Multiply 클래스에 두수를 곱한값을 리턴하는 multiply 메소드 생성
Divide 클래스에 두수를 나눈값을 리턴하는 divide메소드 생성
Calculator클래스에는 Add, Multiply, Divide 상속받고 두수를 뺀값을 리턴하는 sub 메소드 생성하세요.

class Add:
    def add(self,x,y):
        return x + y

a= Add()
a.add(1,2)

class Multiply:
    def multiply(self,x,y):
        return x * y

class Divide:
    def divide(self,x,y):
        return x / y

class Calculator(Add,Multiply,Divide):
    def sub(self,x,y):
        return x - y

cal = Calculator()
print(cal.add(10,20))
print(cal.multiply(10,20))
print(cal.divide(10,20))
print(cal.sub(10,20))

# 자주 사용하는 class 파일로 저장해놓고 필요할 때 불러와 쓰기
import sys
sys.path
sys.path.append('c:\\mypython')
sys.path

import stats

dir(stats)

s = stats.Stats()
s.sum(1,2,3,4,5)
s.mean(1,2,3,4,5)

[문제153] stats 클래스 mode(최빈값) 함수를 추가 해주세요.
stat.mode([1,1,1,2,2,3,3,3,4,4,5,5,6])
stat.mode(['a','b','a','a','c'])

lst1 = [1,1,1,2,2,3,3,3,4,4,5,5,6]
lst2 = ['a','b','a','a','c']
a = collections.Counter(lst1)
list(a.items())
len(a)

내 풀이(max 라는 함수를 이용해버렸잖아)
def mode(arg):
    lst_dict = {}
    for i in arg:
        if i in lst_dict.keys():
            lst_dict[i] += 1
        else:
           lst_dict[i] = 1
    lst_max=[]       
    for j in range(0,len(lst_dict)):
        
        if list(lst_dict.items())[j][1] == max(lst_dict.values()):
            lst_max.append(list(lst_dict.items())[j])
    return (lst_dict,lst_max)

mode(lst1)

답

def mode(arg):
    m={}
    for i in arg:
        if i not in m.keys():
            m[i] = 1
        else:
            m[i] += 1
    v_max = 0
    max_key = []
    for i in m.keys():
        if m[i] > v_max:
            v_max = m[i]
            max_key = [i]
        elif m[i] == v_max:
            max_key.append(i)
    cn = []
    for i in max_key:
        cn.append((i,m[i]))
    return(m,cn)

mode(lst1)
mode(lst2)

class Stats:
    def sum(self,*arg):
        self.hap = 0
        for i in arg:
            self.hap += i
        return self.hap
    
    def mean(self,*arg):
        return self.sum(*arg)/len(arg)
    
    def variance(self,*arg):
        self.total = 0
        self.avg = self.mean(*arg)
        for i in arg:
            self.total += (i-self.avg)**2
        return self.total / (len(arg)-1)
    
    def stddev(self,*arg):
        return math.sqrt(self.variance(*arg))
    
    def median(self,*arg):
        self.lst = []
        for i in arg:
            self.lst.append(i)
        self.lst.sort()
        self.len = len(self.lst)
        if self.len % 2 == 0:
            return (self.lst[int(self.len/2-1)] + self.lst[int(self.len/2+1-1)])/2
        else:
            return self.lst[int((self.len+1)/2-1)]
    
    def mode(self,arg):
        self.arg = arg
        self.m={}
        for i in self.arg:
            if i not in self.m.keys():
                self.m[i] = 1
            else:
                self.m[i] += 1
        self.v_max = 0
        self.max_key = []
        for i in self.m.keys():
            if self.m[i] > self.v_max:
                self.v_max = self.m[i]
                self.max_key = [i]
            elif self.m[i] == self.v_max:
                self.max_key.append(i)
        self.cn = []
        for i in self.max_key:
            self.cn.append((i,self.m[i]))
        return(self.m,self.cn)
    
stat = Stats()
stat.mode(lst1)
stat.mode(lst2)

c = collections.Counter(lst1)
c.most_common(1) # 이건 누락이 되는게 생기니까, 못쓰지. 그냥 확인용으로만 쓸 수 있어

from pandas import Series,DataFrame
data = Series(c).reset_index()
data.columns = ['key','value']
data['rank'] = data['value'].rank(ascending=False,method = 'dense').astype(int)
data[data['rank'] == 1]


[문제154] Person 클래스를 생성하세요. 초기 생성자는 이름, 나이, 성별을 만드세요.
Person 클래스 에는 printMe 메소드를 생성하셔서 이름, 나이 성별을 출력합니다.
Employees클래스를 생성한후 Person상속받습니다.
생성자는 이름, 나이, 성별, 주소, 생일입니다.
단 이름, 나이, 성별은 person에서 상속받으세요.
Employees 클래스에 printMe를 재구성하셔서 주소, 생일을 출력하세요.


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age = age
        self.gender = gender

    def printMe(self):
        print('이름 : {}, 나이 : {}, 성별 : {}'.format(self.name,self.age,self.gender))

p = Person('제임스',25,'남')
p.printMe()

class Employees(Person):
    def __init__(self,name,age,gender,addr,birth):
        Person.__init__(self,name,age,gender)
        self.addr = addr
        self.birth = birth
    
    def printMe(self):
        Person.printMe(self)
        print('주소 : {}, 생일 {}'.format(self.addr,self.birth))

e = Employees('하든',20,'남','서울','1월1일')
e.printMe()


# datetime.py

import datetime

datetime.date.today()
datetime.datetime.now()

d = datetime.date # 이렇게 안해도 쓸 수 있는 방법이 있네?
d.today()

class Calc:
    def add_instance_method(self,arg1,arg2):
        return arg1+arg2
    
    @staticmethod
    def add_static_method(arg1,arg2): # 인스턴스를 통할 필요가 없으니까 self도 없지
        return arg1 + arg2

    @classmethod
    def add_class_method(cls,arg1,arg2): # 역할은 static이랑 같아
        return arg1 + arg2

c = Calc()
c.add_instance_method(1,2) 
Calc.add_instace_method(1,2) # 이거는 인스턴스에 클래스를 할당하는 과정이 없으면 오류야

Calc.add_static_method(1,2) # @staticmethod 해줬으니까 인스턴스를 통하지 않아도 가능 datetime처럼
c.add_static_method(1,2) # 이것도 가능하긴 해

Calc.add_class_method(1,2)
c.add_class_method(1,2) # 이것도 가능하긴

class Parent:
    rate = 1.1
    
    @staticmethod
    def static_compute(value):
        return value * Parent.rate
    
    @classmethod
    def class_compute(cls,value):
        return value * Parent.rate

class child(Parent):
    rate  = 1.2
    
Parent.static_compute(1000)
Parent.class_compute(1000)

child.static_compute(1000)
child.class_compute(1000)


class Parent:
    rate = 1.1
    
    @staticmethod
    def static_compute(value):
        return value * Parent.rate
    
    @classmethod
    def class_compute(cls,value):
        return value * cls.rate

class child(Parent):
    rate  = 1.2
    
Parent.static_compute(1000)
Parent.class_compute(1000)

child.static_compute(1000) # 부모클래스의 속성 이용
child.class_compute(1000) # 현재클래스의 속성 이용


■ 예외 사항
실행중에 발생한 오류

def divide(x,y):
    return x/y

divide(10,2)
divide(10,0)
divide(10,'둘')

try:
    print(divide(10,2))
except:
    print('오류가 발생했습니다.')

try:
    print(divide(10,0))
except:
    print('오류가 발생했습니다.')

try:
    print(divide(10,0))
except ZeroDivisionError: # 오류 메시지 이름 복사
    print('0 값으로 나눌 수 없습니다.')
except TypeError as err:
    print('인수값을 숫자로 입력해주세요.',err)

try:
    print(divide(10,'0'))
except ZeroDivisionError:
    print('0 값으로 나눌 수 없습니다.')
except TypeError as err: # 내가 만든 메시지와 실제 오류메시지 같이 출력
    print('인수값을 숫자로 입력해주세요.',err)


try:
    print(divide(10))
except ZeroDivisionError: # 오류 메시지 이름 복사
    print('0 값으로 나눌 수 없습니다.')
except:
    print('오류가 발생했습니다.')

try:
    z = divide(10,2)
except ZeroDivisionError: # 오류 메시지 이름 복사
    print('0 값으로 나눌 수 없습니다.')
except TypeError as err:
    print('인수값을 숫자로 입력해주세요.',err)
except:
    print('오류가 발생했습니다.')
else:
    print('결과 : {}'.format(z))
finally:                              # 오류나 출력 결과와 관계없이 맨 마지막에 수행하고 싶은 것
    print('프로그램 종료')


def fun(arg):
    try:
        if arg < 1 or arg > 10:
            raise Exception('유효하지 않은 숫자입니다.{}'.format(arg)) # 자동으로 류가 뜨는 상황아닌데 내가 오류로 정의하고 싶은 경우
        else:
            print('입력한 수는 {}입니다.'.format(arg))
    except Exception as error:
        print('오류가 발생했습니다.\n{}'.format(error))

fun(1)
fun(11)

[문제155] 양의 정수값만 입력 받아서 나누기를 수행하는 positive_divide 함수를 생성하세요.
positive_divide(10,2)
positive_divide(10,-2)
오류  - 음수로 나눌수 없습니다. -2

def positive_divide(arg1,arg2):
    try:
        if arg2 < 0:
            raise Exception('오류 - 음수로 나눌 수 없습니다.{}'.format(arg2))
        return arg1/arg2
    except TypeError as error:
        print('인수값을 숫자로 입력해주세요.',error)
    except ZeroDivisionError as error:
        print('0으로 나눌 수 없습니다.',error)
    except Exception as error:
        print(error)

positive_divide(10,2)
positive_divide(10,-2)



# 사용자가 명시적으로 예외사항 이름을 생성하는 방법
class NegativeDivisionError(Exception):
    def __init__(self,value):
        self.value = value
        
def positive_divide(arg1,arg2):
    try:
        if arg2 < 0:
            raise NegativeDivisionError(arg2)
        return arg1/arg2
    except TypeError as error:
        print('인수값을 숫자로 입력해주세요.',error)
    except ZeroDivisionError as error:
        print('0으로 나눌 수 없습니다.',error)
    except NegativeDivisionError as error:
        print('오류 - 음수로 나눌 수 없습니다.',error)


positive_divide(10,-2)


def positive_divide(arg1,arg2):
        if arg2 < 0:
            raise NegativeDivisionError(arg2)
        return arg1 /arg2


positive_divide(10,-2)


class NegativeDivisionError(Exception):
    def __init__(self):
        pass

def positive_divide(arg1,arg2):
    if arg2 < 0:
        raise NegativeDivisionError()
    return arg1 /arg2

positive_divide(10,-2)



class NegativeDivisionError(Exception):
    #pass
    def __init__(self):
        super().__init__('음수로 나눌 수 없습니다.')
        
def positive_divide(arg1,arg2):
    if arg2 < 0:
        raise NegativeDivisionError()
    return arg1 /arg2

positive_divide(10,-2)

class happy:
    def __str__(self):
        return '오늘 하루도 행복하자!!'

print(happy())


h = happy()
print(h)

class NegativeDivisionError(Exception):
    #pass
    def __str__(self):
        return '음수로 나눌 수 없습니다.'
        
def positive_divide(arg1,arg2):
    if arg2 < 0:
        raise NegativeDivisionError()
    return arg1 /arg2

positive_divide(10,-2)


■ sqlite
별도의 DB서버가 필요없이 DB파일 기초하여 데이터베이스를 처리하는 엔진

import sqlite3
sqlite3.__file__

conn = sqlite3.connect(':memory:')
conn
c = conn.cursor() # SQL문 실행 메모리 영역
c.execute('create table emp(id integer, name char, sal integer)')
c.execute('insert into emp(id,name,sal) values(1,"홍길동",1000)')
c.execute('select * from emp')
c.fetchone()

c.execute('insert into emp(id,name,sal) values(2,"박찬호",2000)')
c.execute('select * from emp')
c.fetchone()
c.fetchone()

c.execute('select * from emp')
c.fetchall()

# transaction : 논리적으로 DML(insert,update,delete,merge)문을 한꺼번에 처리하는 작업 단위
# transaction이 발생하면 꼭 끝내주는 작업을 수행해야 한다.
# commit, rollback

conn.rollback() # 커서가 아닌 커넥트 기반으로 해야해

c.execute('select * from emp')
c.fetchall()


c.execute('insert into emp(id,name,sal) values(1,"홍길동",1000)')
c.execute('insert into emp(id,name,sal) values(2,"박찬호",2000)')

c.execute('select * from emp')
c.fetchall()
conn.commit()
c.execute('select * from emp')
c.fetchall()

# sqlite 종료
c.close() # cursor 종료
conn.close() # connect 종료

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute('select * from emp')
c.close()
connect.close()

conn = sqlite3.connect('c:/data/insa.db')
c = conn.cursor()
c.execute('create table emp(id integer, name char, sal integer)')
c.execute('insert into emp(id,name,sal) values(1,"홍길동",1000)')
c.execute('insert into emp(id,name,sal) values(2,"박찬호",2000)')
c.execute('select * from emp')
c.fetchall()
conn.commit()
c.close()
conn.close()

conn = sqlite3.connect('c:/data/insa.db')
c = conn.cursor()
c.execute('select * from emp')
c.fetchall()

c.execute('select * from sqlite_master')
c.fetchall()

c.execute('PRAGMA table_info(sqlite_master)')
c.execute('PRAGMA table_info(emp)')

c.fetchall()

c.execute('drop table emp')
c.execute('select * from sqlite_master')
c.fetchall()
c.close()
conn.close()

import pandas as pd

data = pd.read_csv('c:/data/employees.csv')
data.info()
data.head(2)

# pandas dataframe을 sqlite 테이블로 이관작업

conn = sqlite3.connect('c:/data/insa.db')
c = conn.cursor()

data.to_sql('emp',conn,index=False)

c.execute('select * from sqlite_master')
c.fetchall()

c.execute('select * from emp')
c.fetchall()
c.execute('PRAGMA table_info(emp)')
c.fetchall()

c.close()
conn.close()

conn = sqlite3.connect('c:/data/insa.db')
c = conn.cursor()
c.execute('select * from sqlite_master')
c.fetchall()
c.execute('select * from emp')
c.fetchall()
c.execute('PRAGMA table_info(emp)')
c.fetchall()

# sqlite의 테이블을 pandas dataframe으로 이관작업
emp_new = pd.read_sql_query('select * from emp',conn)
emp_new.info()

c.execute('select * from emp where last_name = "King"')
c.fetchall()

c.execute('select * from emp where lower(last_name) = "king"')
c.fetchall()

c.execute('select last_name, substr(last_name,1,1), substr(last_name,2) from emp')
c.fetchall()

c.execute('select last_name, upper(substr(last_name,1,1))||lower(substr(last_name,2)) from emp')
c.fetchall()

c.execute('select last_name, substr(last_name,-2,2) from emp')
c.fetchall()

c.execute('select last_name, length(last_name) from emp')
c.fetchall()

c.execute('select 1+2') # dual 안해도 됨
c.fetchall()

c.execute('select replace("데이터 분석가","분석가","과학자")')
c.fetchall()

c.execute('select trim("   데이터분석가  ")')
c.fetchall()

c.execute('select rtrim("   데이터분석가  ")')
c.fetchall()

c.execute('select trim("데이터 데이터분석가 데이터","데이터")')
c.fetchall()

c.execute('select instr("aaa@itwill.com","@")')
c.fetchall()

c.execute('select 1+2,2-1,2*1,10/3,10%3') # 나누기가 정수 결과(몫)로 나옴
c.fetchall()

c.execute('select 1+2,2-1,2*1,10.0/3,10%3')
c.fetchall()

c.execute('select round(45.926), round(45.926,2), round(45.926,-2)') # (-)같은 경우에는 자리수 의미없어 아쉽지만.
c.fetchall()

c.execute('select last_name, salary, commission_pct from emp')
c.fetchall()

c.execute('select last_name, salary*12+ifnull(commission_pct,0) from emp') # ifnull : nvl을 여기선 쓸 수 없어서 이걸로 해야해
c.fetchall()

c.execute('select last_name, salary*12+coalesce(commission_pct,0) from emp') # coalesce : nvl을 여기선 쓸 수 없어서 이걸로 해야해
c.fetchall()

c.execute('select last_name, length(last_name), nullif(length(last_name),5) from emp') # coalesce : nvl을 여기선 쓸 수 없어서 이걸로 해야해
c.fetchall()

c.execute('select distinct department_id from emp') # coalesce : nvl을 여기선 쓸 수 없어서 이걸로 해야해
c.fetchall()

c.execute('select distinct department_id, job_id from emp') # coalesce : nvl을 여기선 쓸 수 없어서 이걸로 해야해
c.fetchall()

c.execute('select * from emp where last_name like "K%"')
c.fetchall()

c.execute('select * from emp where last_name like "_e%"')
c.fetchall()

c.execute('select * from emp where department_id = 10 or department_id = 20')
c.fetchall()

c.execute('select * from emp where department_id in (10,20)')
c.fetchall()

c.execute('select * from emp where department_id != 10 and department_id != 20')
c.fetchall()

c.execute('select * from emp where salary > 10000')
c.fetchall()

c.execute('select * from emp where salary >= 10000 and salary <=20000')
c.fetchall()

c.execute('select * from emp where salary between 10000 and 20000')
c.fetchall()

[문제 156] 관리자 사원들의 정보를 출력해주세요.
c.execute('select * from emp where employee_id in (select manager_id from emp)')
c.fetchall()

c.execute('''select * 
          from emp e
          where exists ( select 'x'
                        from emp
                        where manager_id = e.employee_id)''')

[문제 157] 관리자가 아닌 사원들의 정보를 출력해주세요.

c.execute('''select * 
          from emp where employee_id not in (select manager_id 
                                             from emp 
                                             where manager_id is not null)''') # null 값이 있으면 수행이 안되니까

c.execute('''select * 
          from emp e
          where not exists ( select 'x'
                        from emp
                        where manager_id = e.employee_id)''') 
c.fetchall()


c.execute('select * from emp where commission_pct is null')
c.fetchall()

c.execute('select date("now"),datetime("now"),datetime("now","localtime")')
c.fetchall()

c.execute('select date("now","52 day")')
c.fetchone()

c.execute('select date("now","-103 day")')
c.fetchone()

c.execute('select date("now","2 month")')
c.fetchone()

c.execute('select date("now","1 year","2 month")')
c.fetchone()

c.execute('select datetime("now","localtime","2 hour","30 minute","30 second")')
c.fetchone()

c.execute('select date("now","weekday 5")') # 0 일 ~ 6 토
c.fetchone()

c.execute('select date("now") - date(hire_date) from emp') # 날짜 - 날짜 = 년수
c.fetchall()

c.execute('select datetime("now","localtime") - datetime(hire_date) from emp') # 날짜 - 날짜 = 년수
c.fetchall()

c.execute('select strftime("%Y %m %d %H %M %S %w", datetime("now","localtime"))')
c.fetchall()

c.execute('select strftime("%s", datetime("now","localtime"))') 
c.fetchall()

c.execute('select strftime("%s", "now")') 
c.fetchall()

c.execute('select (strftime("%s", "now") - strftime("%s", "2022-05-20"))/86400') 
c.fetchall()

c.execute('select (strftime("%s", "now") - strftime("%s", date(hire_date)))/86400 from emp') # 날짜 계산 하고 싶으면 초로 환산해야해. 년수로 나와버리니까
c.fetchall()


[문제158] job_id컬럼의 값이 SA로 시작하고 10000 이상 급여를 받고 2005년도에 입사한모든 사원들의 정보를 출력하세요.
c.execute('select * from emp where job_id like "SA%" and salary >= 10000 and strftime("%Y", datetime(hire_date)) = "2005"')
c.fetchall() # 이렇게 형변하려환 면 0000-00-00 이렇게 되어잇는거 말고는안 돼
c.execute('''select * 
          from emp 
          where job_id like "SA%" 
          and salary >= 10000 
          and hire_date between "2005-01-01" and "2005-12-31"''')
c.fetchall()

[문제159] 2006년도에 홀수달에 입사한 사원들의 정보를 출력해주세요.

c.execute('select * from emp where strftime("%Y",datetime(hire_date)) = "2006" and (strftime("%m",datetime(hire_date)))%2 = 1')
c.fetchall()


c.execute('''select employee_id, salary, department_id
          from emp
          order by department_id asc''')
c.fetchall()

c.execute('''select employee_id, salary, department_id dept_id
          from emp
          order by dept_id asc''')
c.fetchall()

c.execute('''select employee_id, salary, department_id
          from emp
          order by 3 desc, 2 asc''')
c.fetchall()

c.execute('''select last_name, salary, commission_pct,
          case when commission_pct is null then salary * 12
          else (salary*12) + (salary * 12 * commission_pct)
          end
          from emp''')
c.fetchall()

c.execute('select count(*) from emp')
c.fetchall()

[문제160] 2005년, 2006년, 2007년, 2008년도 입사한 인원수를 출력해주세요.
c.execute('''select count(*)
          from emp
          where strftime("%Y",datetime(hire_date)) in ("2005","2006","2007","2008")
          group by strftime("%Y",datetime(hire_date))''')
c.fetchall()

c.execute('''select count(*),
          count(case substr(hire_date,1,4) when '2005' then 1 end),
          count(case substr(hire_date,1,4) when '2006' then 1 end),
          count(case substr(hire_date,1,4) when '2007' then 1 end),
          count(case substr(hire_date,1,4) when '2008' then 1 end)
          from emp''')
c.fetchall()

c.execute('select sum(salary),total(salary),avg(salary),min(salary),max(salary) from emp')
c.fetchall()


c.execute('''select department_id,job_id, sum(salary) 
          from emp
          group by department_id,job_id''')
c.fetchall() 

c.execute('''select department_id,job_id, sum(salary) 
          from emp
          group by department_id,job_id
          having sum(salary) >= 10000''')
c.fetchall() 

[문제161] 년도별 입사한 인원수를 출력해주세요.

c.execute('''select strftime("%Y",datetime(hire_date)), count(*)
          from emp
          group by strftime("%Y",datetime(hire_date))''')
c.fetchall()


[문제162] 요일별 입사한 인원수를 출력해주세요.

c.execute('''select case week
                           when '0' then '일'
                           when '1' then '월'
                           when '2' then '화'
                           when '3' then '수'
                           when '4' then '목'
                           when '5' then '금'
                           when '6' then '토'
                           end ||'요일', cnt
          from (select strftime("%w",datetime(hire_date)) week, count(*) cnt
                from emp
                group by strftime("%w",datetime(hire_date)))''')
          
c.fetchall()

data = pd.read_csv('c:/data/departments.csv')
data.info()
data.head(2)

data.to_sql('dept',conn,index=False)

c.execute('select * from dept')
c.fetchall()

c.execute('PRAGMA table_info(dept)')
c.fetchall()


# catesian product
c.execute('''select employee_id,last_name,department_name
          from emp, dept''')
c.fetchall() 

c.execute('''select employee_id,last_name,department_name
          from emp cross join dept''')
c.fetchall() 

# equi join, simple join, inner join, 등가조인
c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e, dept d
          where e.department_id = d.department_id''')
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e join dept d
          on e.department_id = d.department_id''')
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e inner join dept d
          on e.department_id = d.department_id''')
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e join dept d
          using(department_id)''')
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e natural join dept d''') # 내츄럴 조인은 기준컬럼이 하나면 상관없는데 양쪽에 다 있는 컬럼이 여러개면 그 여러개 컬림이 다 일치하는 경우
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e inner join dept d
          on e.department_id = d.department_id
          and e.manager_id = d.manager_id''') # 이거랑 내츄럴조인이랑 같은 결과가 나와
c.fetchall() 

# outer join

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e left outer join dept d
          on e.department_id = d.department_id''')
c.fetchall() 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from dept d left outer join emp e
          on e.department_id = d.department_id''')
c.fetchall() # right outer는 없으니까 이렇게 left로 하고 위치를 바꿔야해

# full outer join 도 없음 

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e left outer join dept d
          on e.department_id = d.department_id
          union
          select e.employee_id,e.last_name,d.department_name
          from dept d left outer join emp e
          on e.department_id = d.department_id''') # 이렇게 해야해
c.fetchall()

# 교집합

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e left outer join dept d
          on e.department_id = d.department_id
          intersect
          select e.employee_id,e.last_name,d.department_name
          from dept d left outer join emp e
          on e.department_id = d.department_id''') 
c.fetchall()


#차집합

c.execute('''select e.employee_id,e.last_name,d.department_name
          from emp e left outer join dept d
          on e.department_id = d.department_id
          except
          select e.employee_id,e.last_name,d.department_name
          from dept d left outer join emp e
          on e.department_id = d.department_id''') 
c.fetchall()

job_grades = pd.read_csv('c:/data/job_grades.csv')
job_grades.to_sql('job_grades',conn,index=False)

c.execute('select * from job_grades')
c.fetchall()

# non equi join

c.execute('''select e.employee_id, e.salary, j.grade_level
          from emp e, job_grades j
          where e.salary between j.lowest_sal and j.highest_sal''')
c.fetchall()


c.execute('''select e.employee_id, e.salary, j.grade_level
          from emp e join job_grades j
          on e.salary between j.lowest_sal and j.highest_sal''')
c.fetchall()

# self join
c.execute('''select w.employee_id,w.last_name,m.employee_id,m.last_name
          from emp w, emp m
          where w.manager_id = m.employee_id
          ''')
c.fetchall()

c.execute('''select w.employee_id,w.last_name,m.employee_id,m.last_name
          from emp w left outer join emp m
          on w.manager_id = m.employee_id
          ''')
c.fetchall()

[문제163] 부서이름별 총액급여를 구해주세요.

c.execute('''select d.department_name, sum(e.salary)
          from emp e join dept d
          on e.department_id = d.department_id
          group by d.department_name''') # 조회 할 때 마다 조인하는 비효율 발생
c.fetchall() 

# 비효율 해결
c.execute('''select d.department_name, e.sumsal
          from (select department_id, sum(salary) sumsal
                from emp
                group by department_id) e join dept d
                on e.department_id = d.department_id''') # 조회를 해놓고 마지막에 조인
c.fetchall()

[문제164] 자신의 부서 평균 급여보다 더 많이 받는 사원들의 정보를 출력해주세요.
# correlated subquery, 상호관련서브쿼리

c.execute('''select *
          from emp
          where salary >= (select avg(salary)
                           from emp
                           group by department_id) 
          ''') # 계속 avg를 계싼하는 비효율 발생
c.fetchall()

c.execute('''select e.*
          from (select department_id dept_id, avg(salary) avg_sal
                from emp
                group by department_id) dept_avg, emp e
          where e.department_id = dept_avg.dept_id
          and e.salary > dept_avg.avg_sal''') # 인라인 뷰에 넣어서 비효율 해결
c.fetchall()

c.execute('select employee_id,salary,avg(salary) over() from emp')
c.fetchall()

c.execute('''select *
          from (select employee_id,salary,avg(salary) over(partition by department_id), 
                    case when salary > avg(salary) over(partition by department_id) then "ok" end label
                 from emp)
          where label = "ok"''') 
c.fetchall()

[문제165] 부서별 최고 급여자들에 대한 정보를 출력해주세요.
c.execute('''select e2.employee_id, e2.last_name, e2.salary, e2.department_id
          from (select department_id, max(salary) max_sal
                from emp
                group by department_id) e1, emp e2
         where e1.department_id = e2.department_id
         and e1.max_sal = e2.salary
         order by 4''')
c.fetchall()

c.execute('''select *
          from (select employee_id, last_name,salary,department_id,
          case when salary = max(salary) over(partition by department_id) then 1 end sal_case
          from emp)
          where sal_case = 1
          and department_id is not null
          ''')
c.fetchall()


# with도 쓸 수 있지만 같은 테이블 두번 조회함
c.execute('''with
          dept_max as (select department_id, max(salary) max_sal
                       from emp
                       group by department_id)
          select department_id, last_name, salary
          from emp
          where (department_id, salary) in (select department_id, max_sal from dept_max)''')
c.fetchall()



[문제166] 부서별 최소 급여자들에 대한 정보를 출력해주세요.

# 위 문제를 min으로 다시 해보기


c.execute('''select employee_id, last_name, salary, dense_rank() over(order by salary desc) from emp''') 
c.fetchall()



[문제167] 근무일수가 가장 많은 10위까지 직원들의 employee_id, last_name, department_name, 근무일수를 출력해주세요.
단 sqlite 이용하세요.

c.execute('''select e.employee_id, e.last_name, d.department_name, e.days, e.rank
          from (select employee_id, last_name, department_id, (strftime("%s", "now") - strftime("%s", date(hire_date)))/86400 days, dense_rank() over(order by (strftime("%s", "now") - strftime("%s", date(hire_date)))/86400 desc) rank 
                from emp) e join dept d
                on e.department_id = d.department_id
         where e.rank <= 10
         order by e.rank asc''') 
        
c.fetchall()

c.execute('''select e.employee_id, e.last_name, d.department_name, e.working_day, e.rank
          from(select *
          from
          (select employee_id, last_name, salary, department_id, dense_rank() over(order by working_day desc) as rank, working_day
          from(select employee_id, last_name, salary, department_id, 
          (strftime("%s","now") - strftime("%s", date(hire_date)))/86400 working_day
          from emp))
          where rank <= 10) e, dept d
          where e.department_id = d.department_id
          order by 5
          ''')
c.fetchall()



[문제168] 근무일수가 가장 많은 10위까지 직원들의 employee_id, last_name, department_name, 근무일수를 출력해주세요.
단 pandas 이용하세요.

from pandas import DataFrame, Series
import pandas as pd

emp = pd.read_csv('c:/data/employees.csv')
dept = pd.read_csv('c:/data/departments.csv')

x = DataFrame({'사번':emp.EMPLOYEE_ID,
           '이름':emp.LAST_NAME,
           '부서코드':emp.DEPARTMENT_ID,
           '근무일수':(pd.Timestamp.now() - pd.to_datetime(emp['HIRE_DATE'])).dt.days})

x['순위'] = x['근무일수'].rank(ascending=False,method='dense').astype(int)
x
top_10 = x.loc[x['순위'] <= 10,].sort_values(by='순위')
pd.merge(top_10,dept,left_on='부서코드',right_on='DEPARTMENT_ID')[['사번','이름','근무일수','순위','DEPARTMENT_NAME']]


v_id = 1
v_name = 'james'
v_sal = 1000

c.execute('create table insa(id integer,name char, sal integer)')
c.execute('insert into insa(id,name,sal) values(?,?,?)',(1,'james',1000)) # 변수로 넣고 싶을 때 (?)
c.execute('select * from insa')
c.fetchall()
conn.rollback()


c.execute('insert into insa(id,name,sal) values(?,?,?)',(v_id,v_name,v_sal))
c.execute('select * from insa')
c.fetchall()

c.execute('select * from insa where id = ?',(1,))
c.fetchall()

c.execute('select * from insa where id = ?',(v_id,))
c.fetchall()

c.execute('update insa set name = ? where id = ?',('제임스',1))
c.execute('select * from insa')
c.fetchall()
conn.rollback()

v_id=1
v_name = '홍길동'

c.execute('update insa set name = ? where id = ?',(v_name,v_id))
c.execute('select * from insa')
c.fetchone()
conn.rollback()

c.execute('delete from insa where id = ?',(v_id,))
c.execute('select * from insa')
c.fetchone()
conn.rollback()

[문제 169] Contact 클래스 이용해서 입력들어 온 값을 contact 테이블에 저장해주세요.
open, close, search, insert, update, delete, commit, rollback 함수를 구현해주세요.
class Contact:
    def __init__(self,name,pn,email,addr):
        self.name=name
        self.pn = pn
        self.email = email
        self.addr = addr
        
    def print_info(self):
        print('이름 : {}'.format(self.name))
        print('전화번호 : {}'.format(self.pn))
        print('이메일 : {}'.format(self.email))
        print('주소 : {}'.format(self.addr))


c.execute('create table contact(name char,pn char, email char, addr char)')
c.execute('insert into insa(id,name,sal) values(?,?,?)',(1,'james',1000)) # 변수로 넣고 싶을 때 (?)
c.execute('select * from insa')
c.fetchall()

import sqlite3
sqlite3.__file__

conn = sqlite3.connect('c:/data/contact.db')
d = conn.cursor()
d.execute('create table contact(name text,pn text, email text, addr text)')



class Contact:
    def open(self):
        self.conn = sqlite3.connect('c:/data/contact.db')
        self.d = self.conn.cursor()
        print('contact db에 접속했습니다.')
        
    def close(self):
        self.d.close()
        self.conn.close()
        print('contact db 접속 해지했습니다.')
        
    def insert(self,name,pn,email,addr):
        insert_sql = 'insert into contact(name,pn,email,addr) values(?,?,?,?)'
        self.d.execute(insert_sql,(name,pn,email,addr))
    
    def search(self,pn):
        try:
            self.d.execute('select * from contact where pn = ?',(pn,))
            self.lst = self.d.fetchall()
            if len(self.lst) == 0:
                print('데이터가 없습니다.')
            else:
                print(self.lst)
        except:
            print("open 함수를 호출한 후 수행하세요.")
            
    def update(self,pn,email):
        self.d.execute('update contact set email = ? where pn =?',(email,pn))
    
    def delete(self,pn):
        self.d.execute('delete from contact where pn = ?',(pn,))
    
    def commit(self):
        self.conn.commit()
    
    def rollback(self):
        self.conn.rollback()
    
    
    
c = Contact()


c.open()
c.close()
c.insert("김파썬","010-1000-1234","python@aaa.com","서울시 중구 남대문로")
c.search("010-1000-1234")
c.update("010-1000-1234","python1@aaa.com")
c.rollback()
c.delete("010-1000-1234")
c.rollback()
c.commit()

c.close()

■ 정규표현식 (Regular Expression)
특정 패턴과 일치하는 문자열을 검색, 치환, 제거하는 기능을 제공한다.

■ 메타문자(meta characters)
원래 문자가 가진 뜻이 아닌 특별한 용도로 사용되는 문자

[] : [] 사이의 문자들과 매치
[sql1] : s 또는 q 또는 1
[a-z] : [] 안의 두 문자 사이에 -를 사용하면 두 문자사이의 범위를 의미
[a-zA-z]
[가-힣ㄱ-ㅎ]
[!@#$%^&*()]
[0-9]

a.b : . 위치에 모든 문자를 의미(줄바꿈 문자 \n 제외)
a\.b: .을 문자로 인식
a[.]b : .을 문자로 인식

a*b : *바로 앞의 문자가 0번 이상을 찾는다. b, ab, aaab
a+b : +바로 앞의 문자가 1번 이상을 찾는다. ab, aab, aaab
ab?c : ?바로 앞의 문자가 0번, 1번을 찾는다. ac, abc

a{2}b : {n} 바로 앞의 문자가 n번 반복을 찾는다. aab
a{2,3} : {n,m} 바로 앞의 문자가 n번 또는 m번 반복을 찾는다. aab,aaab
a{2,}b : {n,} 바로 앞의 문자가 n번 이상 반복을 찾는다. aab, aaab, aaaab

a|b : a또는 b
[^a] : not을 의미, a는 제외

^ : 시작
$ : 끝

\d : [0-9] 숫자와 매치
\D : [^0-9] 숫자가 아닌 것과 매치
\s : 공백문자
\S : 공백문자가 아닌 것
\w : 문자, 숫자[a-zA-Z0-9가-힣_] 특수문자는 _ 만 포함
\W : 문자, 숫자가 아닌 것[^a-zA-Z0-9가-힣_]

import re

# re.match : 문자열의 처음부터 정규식과 매치되는 지를 찾는 함수
re.match('\w','a')
bool(re.match('\w','a'))

re.match('\w','1')
bool(re.match('\w','1'))

re.match('\w','_')
bool(re.match('\w','_'))

re.match('\w','파이썬')
bool(re.match('\w','파이썬'))

re.match('\w','-파이썬')
bool(re.match('\w','-파이썬'))

re.match('\w','파이-썬')
bool(re.match('\w','파이-썬'))

re.match('c*a','cat')
bool(re.match('c*a','cat'))
re.match('c*a','ccat')
bool(re.match('c*a','ccat'))
re.match('c*a','at')
bool(re.match('c*a','at'))

re.match('c+a','cat')
bool(re.match('c*a','cat'))
re.match('c+a','ccat')
bool(re.match('c+a','ccat'))
re.match('c+a','at')
bool(re.match('c+a','at'))

re.match('c?a','cat')
bool(re.match('c?a','cat'))
re.match('c?a','ccat')
bool(re.match('c?a','ccat'))
re.match('c?a','at')
bool(re.match('c?a','at'))

re.match('c?a','cat')
bool(re.match('c?a','cat'))
re.match('c?a','ccat')
bool(re.match('c?a','ccat'))
re.match('c?a','at')
bool(re.match('c?a','at'))


re.match('c{2}a','cat')
bool(re.match('c{2}a','cat'))
re.match('c{2}a','ccat')
bool(re.match('c{2}a','ccat'))
re.match('c{2}a','at')
bool(re.match('c{2}a','at'))


re.match('c{2,3}a','cat')
bool(re.match('c{2,3}a','cat'))
re.match('c{2,3}a','ccat')
bool(re.match('c{2,3}a','ccat'))
re.match('c{2,3}a','at')
bool(re.match('c{2,3}a','at'))



bool(re.match('c|a','cat'))
bool(re.match('c|a','ccat'))
bool(re.match('c|a','at'))
bool(re.match('c|a','ct'))
bool(re.match('a','cat'))

bool(re.match('[0-9]th','21th'))
bool(re.match('[0-9][0-9]th','21th'))
bool(re.match('[0-9]*th','21th'))
bool(re.match('[0-9]+th','21th'))
bool(re.match('[0-9]?th','21th'))
bool(re.match('[0-9]{2}th','21th'))
bool(re.match('\d\dth','21th'))
bool(re.match('\d{2}th','21th'))

bool(re.match('Da','Data Science'))
bool(re.match('da','Data Science'))
bool(re.match('da','Data Science',re.I)) # re.I 대소문자 무시

m = re.match('Data','Data Science')
m
m.group() # 매치된 문자열을 리턴
m.span() # 매치된 문자열의 (시작,끝)을 리턴
m.start() # m.span()[0] # 매치된 문자열의 시작위치
m.end() # m.span()[1] # 매치된 문자열의 끝 위치

'Data Science'[0:4]
'Data Science'[m.start():m.end()]

'Data Science'.startswith('Data')

re.match('Science','Data Science') # match는 ^를 쓴 것 처럼 그걸로 시작하는지 이다.

'Data Science'.find('Science')
'Data Science'.index('Science')

'Science' in 'Data Science'
'science' in 'Data Science'

from pandas import Series, DataFrame

Series('Data Science').str.contains('Science')
Series('Data Science').str.startswith('Data')
Series('Data Science').str.endswith('Data')
Series('Data Science').str.find('Data')
Series('Data Science').str.index('Data')

re.match('Science','Data Science')


# 패턴에 해당하는 문자열을 어디서든지 찾는다
m=re.search('Science','Data Science')
m.group()
m.span()
m.start()
m.end()

re.search('Science','Data Science Data Science') # 한 번 찾았으면 더 이상 검색안함

re.findall('Science','Data Science Data Science') # 다 찾고 찾은 값만 리턴. 위치정보 x

re.findall('a','Data Science')
re.findall('a*','Data Science')
re.findall('a.*','Data Science')
re.findall('a.+','Data Science')
re.findall('a.?','Data Science')

[문제170] data 변수에서 숫자 패턴을 찾아주세요.
data = '오늘은 2022년 3월31일 입니다.'
re.findall('\d+',data)




[문제171] data 변수에서 문자 패턴을 찾아주세요.
data = '오늘은 2022년 3월31일 입니다.'
re.findall('[^0-9]+',data)
re.findall('\D+',data)


[문제172] 전화번호를 출력해주세요.

message = '''안녕하세요. 전화번호는 02-123-4567 입니다.
문의사항이 있으면 031-1234-0000 으로 연락주시기 바랍니다.
폰 번호는 010-1234-1004 고객센터 전화번호 1588-3600  대표전화 : 031)777-1140'''

re.findall('\d+\)*-*\d+-*\d*',message)
 
 
 
 
[문제173] 이메일 주소를 출력해주세요.

message = '''담당자 이메일주소는 webmaster@itwill.co.kr  
           이메일 주소는 happy.o@gmail.com   
           이메일 주소는 happy123@naver.com 입니다. info_search@joins.com'''


re.findall('[\.\w]*@[\.\w]*',message)

re.findall('([A-z0-9._]+)@([A-z.]+)',message) # () 그룹


mail_compile = re.compile('[A-z0-9._]+@[A-z.]+') # 자주쓰는 패턴을 compile해놓는다
mail_compile.findall(message)


x = '오늘 하루도 우리 힘내서 공부해봐요..\ngo for it!!'
print(x)

# r : raw string escape 문자열을 그냥 문자로 표현한다.
x = r'오늘 하루도 우리 힘내서 공부해봐요..\ngo for it!!'
print(x)

source = 'Data Science'
source.replace('Science','Scientist')
re.sub('Science','Scientist',source)


[문제174] html 변수에서 title tag에 있는 문자열을 추출해주세요.
html = "<head> 안녕하세요 <title> itwill 학원에 오실걸 환영합니다. </title> </head>"

html = re.search('<title.*/title>',html) # 이렇게 하면 간단해. 밑에는 내가 한 것
html = re.search('<title>[\s\w.]*</title>',html) # findall은 다 찾는거니까 리스트, search는 문자열
text = html.group()

re.findall('<.+?>',text)
re.sub('<.+?>','',text)

# 문자열 분리
'python.programming'.split('.')

re.split('\.','python.programming')
re.split('[.]','python.programming')

re.split('\.|:','python.programming:R')
re.split('[:.]','python.programming:R')

re.split('[:. ]','python.programming:R SQL')
re.split('[:.\s]','python.programming:R SQL')

■ web scraping, web crawling
웹사이트에서 원하는 정보를 수집하는 기술

■ urllib
파이썬에서 인터넷 데이터를 받아오는 기능들이 들어있는 패키지

import urllib

url = 'https://www.naver.com/'

urllib.request.Request(url)

response = urllib.request.Request(url)
response.full_url
response.type

# 이렇게도 할 수 있음
from urllib.request import urlopen

url = 'https://www.naver.com/'
html = urlopen(url)
byte_data = html.read()
byte_data
text_data = byte_data.decode()
text_data


■ beautifulsoup
- 데이터를 추출하는 데 필요한 기능이 들어있는 라이브러리
- parsing하는 라이브러리

from bs4 import BeautifulSoup

html = """
<html>
<body>
<h1> 스크래핑 </h1>
<p> 웹페이지 분석하기 </p>
<p> 데이터 정제 작업하기 1 </p>
<p> 데이터 정제 작업하기 2 </p>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
soup
h1 = soup.html.body.h1
h1.string

p1 = soup.html.body.p
p1.text

p2 = p1.next_sibling.next_sibling # 다음 p의 시블링들 뽑기
p2.text

p3 = p2.next_sibling.next_sibling
p3.text

html = """
<html>
<body>
<h1 id = 'title'> 스크래핑 </h1>
<p id = 'subtitle'> 웹페이지 분석하기 </p>
<p> 데이터 정제 작업하기 1 </p>
<p> 데이터 정제 작업하기 2 </p>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
soup.html.body.h1
soup.find('h1')
soup.find(id='title').string
soup.find(id='title').text

soup.html.body.p
soup.find('p')
soup.find(id='subtitle')
soup.find(id='subtitle').string
soup.find(id='subtitle').text

soup.find_all('p') # find_all하면 리스트!
soup.find_all('p').string #오류

for i in soup.find_all('p'):
    print(i.string)

for i in soup.find_all('p'):
    print(i.text)

soup.html.body.string
soup.html.body.text

html = """
<html>
<body>
<h1 id = 'title'> 스크래핑 </h1>
<p id = 'subtitle'> 웹페이지 분석하기 </p>
<p> 데이터 정제 작업하기 1 </p>
<p> 데이터 정제 작업하기 2 </p>
<ul>
<li> <a href='https://www.itwill.co.kr/'> 아이티윌 </a> </li>
<li> <a href='https://www.naver.com'> 네이버 </a> </li>
</ul>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
a1 = soup.html.body.ul.li.a
a1.string
a1.text

ul = soup.html.body.ul 
ul.string # ul 안에 li 태그가 있으니까 string 안먹혀
ul.text # text는 가능

# 속성을 확인하는 방법
'href' in a1.attrs
'id' in a1.attrs

a1['href']
a1.attrs['href']

soup.find('a')
soup.find('a')['href']

soup.find_all('a')
soup.find_all('a')[0]['href']
soup.find_all('a')[1]['href']

for i in soup.find_all('a'):
    print(i.attrs['href'])
    print(i.string)

soup.findAll('a')
soup.findAll('a')[0]['href']
soup.findAll('a')[1]['href']

for i in soup.findAll('a'):
    print(i.attrs['href'])
    print(i.string)

for i in soup.findAll('p'):
    print(i.string)

html = """
<html>
<body>
<h1 id = 'title'> 스크래핑 </h1>
<p id = 'subtitle'> 웹페이지 분석하기 </p>
<p> 데이터 정제 작업하기 1 </p>
<p> 데이터 정제 작업하기 2 </p>
<ul>
<li> <a href='https://www.itwill.co.kr/' class='cafe1' id='link1'> 아이티윌 </a> </li>
<li> <a href='https://www.naver.com' class='cafe2' id='link2'> 네이버 </a> </li>
</ul>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')
soup.find(id='link1')
soup.find(class_='link1') # class_

soup.find(class_='cafe1')

soup.find('a',id = 'link1')

soup.find('a',{'id':'link1'})

soup.find('a',{'class':'cafe1'}) # 'class'

from urllib.request import urlopen

url = 'https://www.donga.com/news/article/all/20220331/112632650/1'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
soup

soup.find('div',{'class':'article_txt'}).text

[문제175] 동아일보 '인공지능' 뉴스기사 검색을 통해 본문기사 내용을 수집하세요.
url = 'https://www.donga.com/news/search?p=1&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
p = soup.findAll('p',{'class':'tit'})

url = []
for i in p:
    url.append(i.find('a')['href'])

html = urlopen(url)[0]
soup = BeautifulSoup(html,'html.parser')
soup.find('div',{'class':'article_txt'}).text

news_url =[]

for i in range(1,32,15):
    url = 'https://www.donga.com/news/search?p='+str(i)+'&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    p = soup.findAll('p',{'class':'tit'})
    for j in p:
        news_url.append(j.find('a')['href'])
    time.sleep(2)
    
import time

news_text = ''

for u in news_url:
    html=urlopen(u)
    soup = BeautifulSoup(html,'html.parser')
    new_text = news_text + soup.find('div',{'class':'article_txt'}).text + '\n'
    time.sleep(2)
    
with open('c:/data/news_20220331.txt', 'w', encoding='utf-8') as file:
    file.wrtie(news_text)


from bs4 import BeautifulSoup

html = """
<ul id = '조선왕'>
<li id = '태조'> '이성계'</li>
<li id = '정종'> '이방과'</li>
<li id = '태종'> '이방원'</li>
<li id = '세종'> '이도'</li>
<li class = '문종'> '이향'</li>
</ul>"""

soup = BeautifulSoup(html,'html.parser')
soup
soup.find(id='세종').text
soup.find('li',id='세종').text
soup.find('li',{'id':'세종'}).text
soup.find(class_='문종').text
soup.find('li',class_='문종').text
soup.find('li',{'class':'문종'}).text

soup.find_all('li')

for i in soup.find_all('li'):
    print(i.string)

# css(cascading style sheets) 선택자
id => #
class => .

soup.select_one('li')
soup.select_one('ul li')
soup.select_one('ul li#세종')
soup.select_one('li#정종')
soup.select_one('li#정종').text
soup.select_one('li[id="세종"]')
soup.select_one('li[class="문종"]')
soup.select_one('li.문종')
soup.select_one('ul#조선왕 li.문종')
soup.select_one('#조선왕 > li.문종')
soup.select_one('#조선왕 > li.문종').text
soup.select_one('#조선왕 > li.문종').get_text()

soup.select_one('ul li:nth-of-type(1)').text
soup.select_one('ul li:nth-of-type(2)').text
soup.select_one('ul li:nth-of-type(3)').text
soup.select_one('ul li:nth-of-type(4)').text
soup.select_one('ul li:nth-of-type(5)').text

html = """
<div class = 'king of choson'>
    <p>'이성계'</p>
    <span>'태조'</span>
    <p>'이방과'</p>
    <span>'정종'</span>
    <p>'이방원'</p>
</div>
"""

soup = BeautifulSoup(html,'html.parser')
soup.select_one('.king of choson')
soup.select_one('div[class="king of choson"]')

soup.select_one('div[class="king of choson"] p')
soup.select_one('div[class="king of choson"] p:nth-of-type(1)').text
soup.select_one('div[class="king of choson"] p:nth-of-type(2)').text
soup.select_one('div[class="king of choson"] p:nth-of-type(3)').text

soup.select_one('div[class="king of choson"] p:nth-child(1)').text
soup.select_one('div[class="king of choson"] p:nth-child(3)').text
soup.select_one('div[class="king of choson"] p:nth-child(5)').text

soup.select_one('div[class="king of choson"] span:nth-child(2)').text
soup.select_one('div[class="king of choson"] span:nth-child(4)').text

soup.select('div[class="king of choson"] p')

for i in soup.select('div[class="king of choson"] p'):
    print(i.text)


[문제176] 동아일보 '4차혁명' 뉴스기사 검색을 통해 본문기사 내용을 수집하세요.
import urllib
from urllib.request import urlopen
import time
from pandas import DataFrame, Series
from bs4 import BeautifulSoup


urllib.parse.quote('4차혁명')
4%EC%B0%A8%ED%98%81%EB%AA%85
urllib.parse.unquote('4%EC%B0%A8%ED%98%81%EB%AA%85')


new_url = []
for i in range(1,17,15):
    url = 'https://www.donga.com/news/search?p='+str(i)+'&query=4%EC%B0%A8%ED%98%81%EB%AA%85&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1'
    html = urlopen(url)
    soup = BeautifulSoup(html,'html.parser')
    p = soup.select('p[class="tit"]')
    
    for u in p:
        new_url.append(u.select_one('a')['href'])
        
    time.sleep(2)

new_url

contents = DataFrame(columns=['title','news'])

for i in new_url:
    html = urlopen(i)
    soup = BeautifulSoup(html,'html.parser')
    title = soup.select_one('h1[class="title"]').string.strip()
    news = soup.select_one('div[class="article_txt"]').text.strip()
    contents = contents.append({'title':title,'news':news},ignore_index=True)
    time.sleep(2)

contents['news'][1]

import re

re.findall('[a-zA-Z0-9._]+@[a-zA-Z.]+',contents['news'][11])

contents['mail'] = contents['news'].apply(lambda x : re.findall('[a-zA-Z0-9._]+@[a-zA-Z.]+',x ))
contents['mail'] = contents['news'].apply(lambda x : ','.join(re.findall('[a-zA-Z0-9._]+@[a-zA-Z.]+',x )))

contents['mail']

contents.to_csv("c:/data/contents.csv",index=False)


# 본문내용 중 필요 없는 거 지우기
new_url[0]
html = urlopen(new_url[0])
soup = BeautifulSoup(html,'html.parser')
news = soup.select_one('div[class="article_txt"]')
news.select('div')
news.select('script')
news.select_one('script').extract() # select로는 안되고, select_one으로 하나지씩 지워야해. 이건 즉시수행이라 바로 적용

for i in news.select('div'):
    i.extract()

news.text

new_url[:3]

from urllib.error import URLError, HTTPError

# 이렇게 url에 오류가 있는 경우 URLError, url은 멀쩡한데 접근이 막힌경우 HTTPError
url = ['https://www.donga.com/news/article/all/20220216/111836516/1',
       'https://finance.daum.net/api/search/ranks?limit=10',
 'https://www.do.com/news/article/all/20210524/107074586/1',
 'https://www.donga.com/news/article/all/20201104/103789830/1']


contents = DataFrame(columns=['title','news'])
failed_url = []
httperror_url = []

for i in url:
    try:
        
        html = urlopen(i)
        soup = BeautifulSoup(html,'html.parser')
        title = soup.select_one('h1[class="title"]').string.strip()
        news = soup.select_one('div[class="article_txt"]').text.strip()
        contents = contents.append({'title':title,'news':news},ignore_index=True)
        time.sleep(2)
    
    except HTTPError as error: # HTTPError를 URLError보다 먼저 수행해야한다. 우선순위.
        print('HTTPError Code : {}'.format(error.code))
        httperror_url.append((i,error.code))
        
    except URLError as error:
        print('url failed')
        print('url error reason', error)
        failed_url.append(i)
    
    else:
        print('http status code : {}'.format(html.getcode()))


(base) C:\Users\USER>pip install fake_useragent

from fake_useragent import UserAgent
from urllib.request import urlopen
import urllib.request as req

ua = UserAgent()
print(ua.ie)
print(ua.msie)
print(ua.chrome)
print(ua.safari)
print(ua.random)

headers = {'User-Agent': ua.ie, 
            'referer' : 'https://finance.daum.net'}

url = 'https://finance.daum.net/api/search/ranks?limit=10'
res = req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')

res

import json
json.loads(res)['data']
top10 = DataFrame(json.loads(res)['data'])
top10
top10.info()

[문제177] 다음사이트에서 코스피200 편입된 종목을 수집하세요.

kospi200= DataFrame()
failed_url = []

headers = {'User-Agent': ua.ie, 
            'referer' : 'https://finance.daum.net/domestic/kospi200'}

for i in range(1,22):
    try:
        url = "https://finance.daum.net/api/trend/included_stocks?page="+str(i)+"&perPage=10&fieldName=changeRate&order=desc&market=KOSPI_200&pagination=true"
        res = req.urlopen(req.Request(url,headers=headers)).read().decode('utf-8')
        kospi200 = kospi200.append(DataFrame(json.loads(res)['data']),ignore_index=True)
        time.sleep(2)

    except URLError as error:
        failed_url.append(url)
        time.sleep(2)
   
kospi200

[문제178] 네이버 영화 리뷰정보를 수집하세요.(평점, 리뷰, 작성자, 작성일)


url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=190991&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
p = soup.select('div[class="score_result"] > ul > li')

score_lst = []
for u in p:
    score_lst.append(u.select_one('div[class="star_score"] em').text)
    time.sleep(2)
comment_lst = []
for u in p:
    comment_lst.append(u.select_one('div[class="score_reple"] p').text)
    time.sleep(2)
c_id_lst = []
for u in p:
    c_id_lst.append(u.select_one('dl a').text)
    time.sleep(2)
date_lst = []
for u in p:
    date_lst.append(u.select_one('dl em').text)
    time.sleep(2)

답

movie=DataFrame()
for i in range(1,11):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=190695&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='+str(i)
    html =  urlopen(url)
    soup = BeautifulSoup(html)
    
    review = []
    for i in soup.select('div.score_reple > p'):
        if i.select_one('span.ico_viewer') == None:
            review.append(i.text.strip())
        else:
            i.select_one('span.ico_viewer').extract()
            review.append(i.text.strip())
    
    point = []
    for i in soup.select('div.star_score > em'):
        point.append(i.text)
        
    id = []
    for i in soup.select('div.score_reple > dl > dt > em > a > span'):
        id.append(i.text)
    
    day = []
    for i in soup.select('div.score_reple > dl > dt > em:nth-of-type(2)'):
        day.append(i.text)
    
    movie = movie.append(DataFrame({'day':day,'id':id,'review':review,'point':point}))
    time.sleep(2)

movie.to_csv('c:/data/movies.csv',index=False)

[문제179] 네이버 뉴스에서 언론사별 랭킹 5위까지 데이터를 수집하세요

# 하나를 [0] 인덱스해서 해보고, 반복문에 차근차근 넣자
# 보면 [0] 인덱스 해놓는게 3번있잖아. 그러면 반복문 3개 중첩해야한다는 거.

import urllib
from urllib.request import urlopen
import time
from pandas import DataFrame, Series
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
div_rank = soup.select('div.rankingnews_box')
len(div_rank)

# 하나 확인하기. 인덱스
div_rank[0].select_one('strong.rankingnews_name').text
div_rank[0].select('ul > li > div > a')[0].string
div_rank[0].select('ul > li > div > a')[0]['href']
html = urlopen(div_rank[0].select('ul > li > div > a')[0]['href'])
soup = BeautifulSoup(html,'html.parser')
soup.select_one('div#newsct_article > div#dic_area').text


news_ranking_df = DataFrame(columns=['언론사','랭킹URL','title','news'])

url = 'https://news.naver.com/main/ranking/popularDay.naver?mid=etc&sid1=111'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')

for i in soup.select('div.rankingnews_box')[:2]:
    press = i.select_one('strong.rankingnews_name').text
    news_ranking=[]
    news_ranking_url =[]
    news =[]
    
    for j in i.select('ul > li > div > a'):
        news_ranking.append(j.string)
        news_ranking_url.append(j['href'])
        html = urlopen(j['href'])
        soup = BeautifulSoup(html,'html.parser')
        news.append(soup.select_one('div#newsct_article > div#dic_area').text.strip())
        time.sleep(2)
    news_ranking_df = news_ranking_df.append(DataFrame({'언론사':press, '랭킹URL':news_ranking_url,'title':news_ranking,'news':news}),ignore_index=True)
    print('수집 언론사 : ',press)
    time.sleep(2)
    
news_ranking_df.to_csv('c:/data/news_ranking.csv',index=False)

[문제180] 수집한 뉴스기사 내용에서 [내용..] 출력해주세요.
import re
re.findall('\[.+?\]',news_ranking_df.news[4])
news_ranking_df.news.apply(lambda x : re.findall('\[.+?\]',x))

[문제181] 수집한 뉴스기사 내용에서 <내용..> 출력해주세요.
news_ranking_df.news.apply(lambda x : re.findall('\<.+?\>',x))


[문제182] 수집한 뉴스기사 내용에서 (내용..) 출력해주세요.
news_ranking_df.news.apply(lambda x : re.findall('\(.+?\)',x))

[문제183] 네이버 웹툰 랭킹을 딕셔너리 자료형으로 수집하세요.
import urllib
from urllib.request import urlopen
import time
from pandas import DataFrame, Series
from bs4 import BeautifulSoup

comic_dict = {}

url = 'https://comic.naver.com/index'
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
li = soup.select('ol#realTimeRankFavorite > li')
comic_dict[li[0]['class']] = li[0].select_one('a').text

li[0]['class'] -> str 변환
li[0]['class'][0]
''.join(li[0]['class'])

for i in li:
    comic_dict[''.join(i['class'])] = i.select_one('a').text

comic_dict

dict([(key.replace('rank',''),value) for key, value in comic_dict.items()])


https://www.lfd.uci.edu/~gohlke/pythonlibs/#wordcloud

(base) C:\Users\USER\anaconda3\Lib>dir *.whl
 C 드라이브의 볼륨에는 이름이 없습니다.
 볼륨 일련 번호: F4C5-D847
(base) C:\Users\USER>cd C:\Users\user\anaconda3\Lib

 C:\Users\USER\anaconda3\Lib 디렉터리

2022-04-04  오후 02:18           609,919 ad3-2.2.1-cp39-cp39-win_amd64.whl
2022-04-04  오후 02:21           161,093 wordcloud-1.8.1-cp39-cp39-win_amd64.whl
               2개 파일             771,012 바이트
               0개 디렉터리  18,690,437,120 바이트 남음
(base) C:\Users\USER\anaconda3\Lib>pip install wordcloud-1.8.1-cp39-cp39-win_amd64.whl



import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/windows/fonts/HMKMMAG.TTF').get_name()
rc('font',family=font_name)
from wordcloud import WordCloud
word = {'떡볶이':100,'감자탕':50,'순대국밥':10,'치즈':70,'볶음밥':80,'김밥':20,'자장면':300,'치킨':100,
        '핫도그':90,'호두':60,'알감자':50,'짬뽕':200,'탕수육':150}

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(word)
plt.imshow(w)
plt.axis('off')

txt = ' '.join(news_ranking_df.news)
txt

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate(txt) # generate만 하면 알아서 빈도수 계산해서 그려줌
plt.imshow(w)
plt.axis('off')


import pandas as pd
movies = pd.read_csv('c:/data/movies.csv')
movies.columns
movies.review
movies[pd.notnull(movies.review)]

reviews = ' '.join(movies.review[pd.notnull(movies.review)])
w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate(reviews) 
plt.imshow(w)
plt.axis('off')

[문제184] winter.txt 텍스트를 이용해서 워드클라우드 생성해주세요.
import numpy as np
from PIL import Image
alice_mask = np.array(Image.open('c:/data/alice_mask.png'))

import numpy as np
winter = np.loadtxt('c:/data/winter.txt') # 이거는 숫자로 된 것만 불어올 수 있어

with open('c:/data/winter.txt', 'r') as file:
    text=file.read()

text
len(text)
w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500,
              colormap='PuRd',
              mask=alice_mask).generate(text) 
plt.imshow(w)
plt.axis('off')

■ selenium
웹브라우저를 컨트롤하여 웹을 자동화하는 도구

(base) C:\Users\USER>pip install selenium

from selenium import webdriver
url = "https://www.naver.com"
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.save_screenshot('c:/data/naver.png')
driver.quit()


import urllib
from urllib.request import urlopen
import time
from pandas import DataFrame, Series
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/index'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
html = driver.page_source
driver.quit()

comic_dict = {}

soup = BeautifulSoup(html, 'html.parser')
li = soup.select('ol#realTimeRankFavorite > li')

for i in li:
    comic_dict[''.join(i['class'])] = i.select_one('a').text


from selenium.webdriver.common.by import By
url = "https://www.naver.com"
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.implicitly_wait(2)
driver.find_element(By.CLASS_NAME,'id_finance').click()
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
soup.select('p')
driver.quit()

url = 'https://search.naver.com/search.naver?where=image'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.implicitly_wait(2)
element = driver.find_element(By.CLASS_NAME,'box_window')
element.clear()
element.send_keys('강아지')
driver.implicitly_wait(1)
element.submit()

import time
from selenium.webdriver.common.keys import Keys

driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_UP)

for i in range(5):
    driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
    time.sleep(1)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html,'html.parser')
soup
img_url = []
for i in soup.select('img._image'):
    img_url.append(i.attrs['src'])

len(img_url)
img_url[0]

import urllib.request as req
# 이거 반복문 어떻게?
req.urlretrieve(img_url[0],'c:/image/1.jpg')

for i in range(len(img_url)):    
    req.urlretrieve(img_url[i],'c:/image/naverdog'+str(i)+'.jpg')

# 다음에서 강아지 사진 찾기

url = 'https://search.daum.net/search?nil_suggest=btn&w=img'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.implicitly_wait(2)
element = driver.find_element(By.CLASS_NAME,'tf_keyword')
element = driver.find_element(By.XPATH,'')
element = driver.find_element(By.CSS_SELECTOR,'div.inner_searcher > input')

element.clear()
element.send_keys('강아지')
driver.implicitly_wait(1)
element.submit()
element.send_keys(Keys.ENTER)

while True:
    
    for i in range(4):
        driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
        time.sleep(1)
        
    driver.find_element(By.CLASS_NAME,'open').click()
    time.sleep(1)
    cnt += 1
    if cnt ==5:
        break

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html,'html.parser')
soup
img_url = []
for i in soup.select('img.thumb_img'):
    img_url.append(i.attrs['src'])
    
for i in range(len(img_url)):    
    req.urlretrieve(img_url[i],'c:/image/daumdog'+str(i)+'.jpg')
    
■ pickle
-변수형태를 그대로 유지해서 파일에 저장시키고 불러올 수 있는 모듈
- 바이너리 형태로 저장

import pickle    

with open('c:/data/dog_img_url.txt','wb') as file:
    pickle.dump(img_url,file)    

with open('c:/data/dog_img_url.txt','rb') as file:
    dog_img_url = pickle.load(file)

dog_img_url


j=1
httperror_url =[]
urlerror_url = []
for i in dog_img_url[:10]:
    try:
        req.urlretrieve(i,'c:/image/dog_'+str(j)+'.jpg')
        j+=1
        time.sleep(1)
    except HTTPError as error:
        print('HTTPError Code : {}'.format(error.code))
        httperror_url.append((i,error.code))
    except URLError as error:
        print('URL error reason', error)
        urlerror_url.append(i)

url = 'https://search.daum.net/search?nil_suggest=btn&w=img'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.implicitly_wait(2)
element = driver.find_element(By.CLASS_NAME,'tf_keyword')
element = driver.find_element(By.XPATH,'')
element = driver.find_element(By.CSS_SELECTOR,'div.inner_searcher > input')

element.clear()
element.send_keys('강아지')
driver.implicitly_wait(1)
element.submit()
element.send_keys(Keys.ENTER)

# 현재 스크롤 좌표 추출
diver.execute_script('return window.pageYOffset')

# 지정 좌표로 스크롤 이동
diver.execute_script('window.scrollBy(0,3000)')

# 현재 스크롤 좌표 추출
diver.execute_script('return window.pageYOffset')

# 현재 스크롤 전체 길이
driver.execute_script('return document.body.scrollHeight')

diver.execute_script('window.scrollBy(0,document.body.scrollHeight)')


driver.execute_script('return document.body.scrollHeight')
diver.execute_script('window.scrollBy(0,document.body.scrollHeight)')


last = driver.execute_script('return document.body.scrollHeight')
while True:
    diver.execute_script('window.scrollBy(0,document.body.scrollHeight)')
    time.sleep(3)
    
    current = driver.execute_script('return document.body.scrollHeight')
    if current == last:
        try:
            driver.find_element(By.CLASS_NAME,'open').click()
            current = diver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

            time.sleep(1)
    
        except:
            break
    last = current

[문제185] 중앙일보 인공지능 기사 검색을 통해 데이터 수집해 주세요.
import pandas as pd
답

# 알림(팝업창) 제어하는 법

from selenium.webdriver.chrome.options import Options
opt = Options()
opt.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':1})

url = 'https://www.joongang.co.kr'
driver = webdriver.Chrome('c:/data/chromedriver.exe',options=opt)
driver.get(url)
driver.find_element(By.CLASS_NAME,'btn_search').click()

input = driver.find_element(By.CLASS_NAME,'form_control')
input.clear()
input.send_keys('인공지능')
input.send_keys(Keys.ENTER)

# 창의 크기 확인
previous = driver.get_window_size()
previous['width']
previous['height']

# 창 크기 최대화 최소화
driver.maximize_window()
driver.minimize_window()
driver.set_window_size(1500,1000)
driver.set_window_size(previous['width'],previous['height'])

# 해당 태그가 있는 위치까지 커서 이동시키기(스크롤)
from selenium.webdriver import ActionChains

# 전체보기
btn = driver.find_element(By.CLASS_NAME, 'btn.btn_full')
action = ActionChains(driver)
action.move_to_element(btn).perform()
driver.find_element(By.CLASS_NAME,'btn.btn_full').click()

# 더보기
btn = driver.find_element(By.CLASS_NAME, 'btn.btn_outline_gray')
action = ActionChains(driver)
action.move_to_element(btn).perform()
driver.find_element(By.CLASS_NAME, 'btn.btn_outline_gray').click()

for i in range(4):
    btn = driver.find_element(By.CLASS_NAME, 'btn.btn_outline_gray')
    action = ActionChains(driver)
    action.move_to_element(btn).perform()
    driver.find_element(By.CLASS_NAME, 'btn.btn_outline_gray').click()
    time.sleep(1)

html = driver.page_source
driver.close()

ai_url = []
soup = BeautifulSoup(html,'html.parser')
for i in soup.select('ul.story_list > li.card > div.card_body > h2.headline'):
    ai_url.append(i.select_one('a')['href'])

contents = DataFrame(columns={'day','title','news','reporter'})
day =[]
title =[]
news = []
reporter =[]
error_url =[]
for i in ai_url:
    try:
        html = req.urlopen(i)
        soup =BeautifulSoup(html,'html.parser')
        day = soup.select_one('div.time_bx > p.date').text.replace('입력','').strip()
        title = soup.select_one('h1.headline').text.strip()
        reporter= soup.select_one('div.ab_byline').text.strip()
        soup.select_one('div.ab_byline').extract() # 이렇게 뽑을거 뽑고 본문에 필요없는 애들을 전체에서 날리는 식으로 하자
        for j in soup.select('div.ab_photo.photo_center'):
            j.extract()
        news= soup.select_one('div#article_body').text
        contents = contents.append({'day':day,'title':title,'news':news,'reporter':reporter},ignore_index=True)
        time.sleep(1)
    except:
        error_url.append(i)
        print('오류가 발생했습니다.')
    
ai_url[0]
contents
len(contents.reporter)
contents.reporter[5]
contents.to_csv('c:/data/contents.csv')
contents.news[1]
[문제186] 중앙일보 인공지능 기사 검색을 통해 이메일 정보를 수집해주세요.
import re

contents.email = contents.reporter.apply(lambda x: ''.join(re.findall('[a-zA-Z0-9._]+@[a-zA-Z.]+',x)))







[문제187] 중앙일보 인공지능 기사 검색을 통해 (내용),[내용],<내용> 정보를 수집해주세요.
contents.news.apply(lambda x : re.findall('\(.+?\)',x))
contents.news.apply(lambda x : re.findall('\[.+?\]',x))
contents.news.apply(lambda x : re.findall('\<.+?\>',x))






[문제188] 중앙일보 인공지능 기사 정보를 전처리 하기 전과 후에 워드클라우드를 생성해주세요.

import matplotlib.pylab as plt

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/windows/fonts/HMKMMAG.TTF').get_name()
rc('font',family=font_name)

from wordcloud import WordCloud


news_join = ' '.join(contents.news)

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate(news_join) 
plt.imshow(w)
plt.axis('off')


# 전처리 후
# 전처리 공백, 특수문자, 등등

lst =['있다','등','통해','및','을','이','를','했다','밝혔다','함께','예정이다','위한','있는','위해','수','같은','는','전']
for i in lst:
    news_join = news_join.replace(i,'')

# 이렇게 전처리 공부 좀만 더하자 
p = re.compile('[\[\(][\w\s=.]+[\]\)]')
contents.clean_news = contents.news.apply(lambda x: p.sub(' ',x))

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate(news_join) 
plt.imshow(w)
plt.axis('off')

# 워드클라우드 파일로 떨어뜨리기
w.to_file('c:/data/clean_news.jpg')


[문제189] 다나와사이트에서 가격정보를 수집하세요.
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

# 1,2,3 페이지를 수집해야하는데, 1,1,2 로 수집함..
url = 'http://prod.danawa.com/list/?cate=112758'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()
driver.find_element(By.XPATH,'//*[@id="searchMaker1452"]').click()

laptop = DataFrame(columns ={'name','spec','price'})

for i in range(1,4):
    if i in (1,2):
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productListArea"]/div[5]/div/div/a['+str(i)+']'))).click()
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
   
        soup.select_one('div.main_prodlist >ul > li.prod_item.prod_layer.product-pot').extract()
        try:
            for i in soup.select('div.main_prodlist >ul > li.prod_item.prod_layer > div.prod_main_info'):
                name= i.select_one('div.prod_info > p > a').text.strip()
                spec_add=[]
                for j in i.select('div.prod_info > dl > dd > div > a'):
                    spec_add.append(j.text.strip())
                spec = ' / '.join(spec_add)
                price_add=[]
                for j in i.select('div.prod_pricelist > ul > li'):
                    price_add.append(' : '.join([j.select_one('div > p').text.strip(),j.select_one('p.price_sect > a > strong').text.strip()]))
                price = ' / '.join(price_add)
                laptop = laptop.append({'name':name,'spec':spec,'price':price},ignore_index=True)
    
        except:
            print('오류 발생')    
    else:
        wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="productListArea"]/div[4]/div/div/a['+str(i)+']'))).click()
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        
        soup.select_one('div.main_prodlist >ul > li.prod_item.prod_layer.product-pot').extract()
        try:
            for i in soup.select('div.main_prodlist >ul > li.prod_item.prod_layer > div.prod_main_info'):
                name= i.select_one('div.prod_info > p > a').text.strip()
                spec_add=[]
                for j in i.select('div.prod_info > dl > dd > div > a'):
                    spec_add.append(j.text.strip())
                spec = ' / '.join(spec_add)
                price_add=[]
                for j in i.select('div.prod_pricelist > ul > li'):
                    price_add.append(' : '.join([j.select_one('div > p').text.strip(),j.select_one('p.price_sect > a > strong').text.strip()]))
                price = ' / '.join(price_add)
                laptop = laptop.append({'name':name,'spec':spec,'price':price},ignore_index=True)
        except:
            print('오류 발생')

       
len(laptop.name)
len(laptop.spec)
len(laptop.price)

답 # for 문에 넣기!

url = 'http://prod.danawa.com/list/?cate=112758'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()
driver.find_element(By.XPATH,'//*[@id="searchMaker1452"]').click()

html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
li = soup.select('div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer')
prod_name = li[0].select_one('p.prod_name > a').text.strip()

prod_info = ''
for i in li[0].select('div.spec_list > a'):
    prod_info += i.text + ','

//*[@id="productInfoDetail_12660491"]/p[2]/span/button
//*[@id="productInfoDetail_14766710"]/p[2]/span/button
'//*[@id="productInfoDetail_{}"]/p[2]/span/button'.format()

input = li[0].select('div.prod_pricelist > ul > li')
id_value = []
for i in input:
    id_value.append(i.find('input',{"name":"compareValue"})['value'])

prod_dic = {}

driver.find_element(By.XPATH,'//*[@id="productInfoDetail_{}"]/p[2]/span/button'.format(id_value[0])).click()
html_2 = driver.page_source
soup_2 = BeautifulSoup(html_2,'html.parser')

tag1 = 'span#layer_price_more_{} > span.lpm_wrap'.format(id_value[0])
info = ''
for i in soup_2.select(tag1):
    info += i.select_one('a > img')['alt'] + '/'+ i.select_one('a.lpm_price').text.strip() + ' '

tag2 = 'li#productInfoDetail_{} > div > p.memory_sect'.format(id_value[0])
prod_dic[soup_2.select_one(tag2).text.strip()] = info


driver.find_element(By.XPATH,'//*[@id="productInfoDetail_{}"]/p[2]/span/button'.format(id_value[1])).click()
html_2 = driver.page_source
soup_2 = BeautifulSoup(html_2,'html.parser')

tag1 = 'span#layer_price_more_{} > span.lpm_wrap'.format(id_value[1])
info = ''
for i in soup_2.select(tag1):
    info += i.select_one('a > img')['alt'] + '/'+ i.select_one('a.lpm_price').text.strip() + ' '

tag2 = 'li#productInfoDetail_{} > div > p.memory_sect'.format(id_value[1])
prod_dic[soup_2.select_one(tag2).text.strip()] = info

df = DataFrame(columns = ['제품명','제품정보','제품가격'])
df = df.append({'제품명':prod_name,'제품정보':prod_info,'제품가격':prod_dic},ignore_index=True)
df

# 페이지 정보
//*[@id="productListArea"]/div[5]/div/div/a[2]
//*[@id="productListArea"]/div[5]/div/div/a[3]
//*[@id="productListArea"]/div[5]/div/div/a[4]

# 태그가 계속 바뀌니까 XPATH 안돼.
driver.find_element(By.CSS_SELECTOR,'div.number_wrap > a:nth-of-type(2)').click()
driver.find_element(By.CSS_SELECTOR,'div.number_wrap > a:nth-of-type(3)').click()

■ 형태소 분석
from konlpy.tag import Kkma

kkma = Kkma()

text = "통찰력은 사물이나 현상의 원인과 결과를 이해하고 간파하는 능력이다. 통찰력을 얻는 좋은 방법은 독서다."

kkma.sentences(text)

# 문장을 분석
kkma.sentences(text)

# 명사 분석
kkma.nouns(text)

# 형태소 분석(품사태깅)
kkma.pos(text)

# 형태소 추출
kkma.morphs(text)

from konlpy.tag import Komoran
komoran = Komoran()

# 명사분석
komoran.nouns(text)

# 형태소 분석(품사태깅)
komoran.pos(text)

# 형태소 추출
komoran.morphs(text)



from konlpy.tag import Hannanum
hannanum = Hannanum()

# 명사분석
hannanum.nouns(text)

# 형태소 분석(품사태깅)
hannanum.pos(text)

# 형태소 추출
hannanum.morphs(text)

from konlpy.tag import Okt
okt = Okt()

# 명사분석
okt.nouns(text)

# 형태소 분석(품사태깅)
okt.pos(text)

# 형태소 추출
okt.morphs(text)

[문제190] 중아일보 인공지능 기사 검색을 통해서 받아 놓은 뉴스기사를 명사만 추출해서 워드클라우드 생성해주세요.
import pandas as pd
from konlpy.tag import Kkma
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/windows/fonts/HMKMMAG.TTF').get_name()
rc('font',family=font_name)
from wordcloud import WordCloud

contents['nouns'] = contents['news'].apply(lambda x : okt.nouns(x))
contents_noun = [j for i in contents['nouns'] for j in i if len(j) >= 2]
contents_noun[0]

import operator
from collections import Counter
contents_noun_freq = Counter(contents_noun)
contents_noun_freq
contents_noun_freq_sorted = sorted(contents_noun_freq.items(),key = operator.itemgetter(1),reverse=True)
contents_noun_freq_sorted
contents_noun_freq.most_common(50)

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(contents_noun_freq) 
plt.imshow(w)
plt.axis('off')
w.to_file('c:/data/contetns_noun_freq.jpg')

stop_words = ['분야','지난해','국내','지원','제공','대표','올해','진행','출시']

news_nouns = [word for word in contents_noun if word not in stop_words]

news_nouns_freq = Counter(news_nouns)
news_nouns_freq.most_common(50)

news_nouns_freq

# dictionary를 dataframe로 표현하기
# document_term_matrix 형태가 됨
pd.DataFrame.from_dict([news_nouns_freq])
pd.DataFrame.from_records([news_nouns_freq])


pd.DataFrame.from_dict([news_nouns_freq]).T
news_freq_df = pd.DataFrame.from_records([news_nouns_freq]).T
news_freq_df.reset_index(inplace=True)
news_freq_df
news_freq_df.columns = ['word','freq']
news_freq_df

top_50 = news_freq_df[news_freq_df['freq']>=50]
top_50
top_50.set_index('word')
top_50.set_index('word').to_dict()

# dataframe을 dictionary로 변환하는 법
top_50_freq = top_50.set_index('word').to_dict()['freq']

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(top_50_freq) 
plt.imshow(w)
plt.axis('off')
w.to_file('c:/data/top50_noun_freq.jpg')

[문제191] okt 형태소 분석기를 이용해서 중앙일보 인공지능 뉴스 기사에서 명사, 형용사를 추출해서 워드클라우드를 생성하세요.
from konlpy.tag import Okt
okt = Okt()


def okt_pos(arg):
    token = []
    for i in okt.pos(arg):
        if i[1] in ['Noun','Adjective']:
            token.append(i[0])
    return token

okt_pos(contents.news[0])

# 두 결과 비교
contents_token = [okt_pos(i) for i in contents.news]
contents_token = contents.news.apply(lambda x : okt_pos(x))

# 리스트 풀기
[word2 for word in contents_token for word2 in word]

# 불용어 처리, 2글자 이상 뽑기
news_token = [word2 for word in contents_token for word2 in word if word2 not in stop_words and len(word2) >= 2]

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(Counter(news_token)) 
plt.imshow(w)
plt.axis('off')

[문제192] 네이버, 다음에서 같은 영화의 날짜, 작성자, 평점, 리뷰글을 수집해주세요.
import pandas as pd
import numpy as np

n_movie=DataFrame()
for i in range(1,11):
    url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=167613&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page='+str(i)
    html =  urlopen(url)
    soup = BeautifulSoup(html)
    
    review = []
    for i in soup.select('div.score_reple > p'):
        if i.select_one('span.ico_viewer') == None:
            review.append(i.text.strip())
        else:
            i.select_one('span.ico_viewer').extract()
            review.append(i.text.strip())
    
    point = []
    for i in soup.select('div.star_score > em'):
        point.append(i.text)
        
    id = []
    for i in soup.select('div.score_reple > dl > dt > em > a > span'):
        id.append(i.text)
    
    day = []
    for i in soup.select('div.score_reple > dl > dt > em:nth-of-type(2)'):
        day.append(i.text)
    
    n_movie = n_movie.append(DataFrame({'day':day,'id':id,'point':point,'review':review}),ignore_index=True)
    time.sleep(2)
n_movie.point

from selenium import webdriver
import urllib
from urllib.request import urlopen
import time
from pandas import DataFrame, Series
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import matplotlib.pylab as plt
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname='c:/windows/fonts/HMKMMAG.TTF').get_name()
rc('font',family=font_name)
from wordcloud import WordCloud
from collections import Counter

url = 'https://movie.daum.net/moviedb/grade?movieId=125080'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)

for i in range(1,4):
    btn = driver.find_element(By.XPATH, '//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button')
    action = ActionChains(driver)
    action.move_to_element(btn).perform()
    driver.find_element(By.XPATH, '//*[@id="alex-area"]/div/div/div/div[3]/div[1]/button').click()
    time.sleep(1)
    
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')

d_movie = DataFrame()
try:
    for i in soup.select('ul.list_comment > li'):
        day = i.select_one('span.info_author > span.txt_date').text.strip()
        id = i.select_one('span.info_author > a > span:nth-of-type(2)').text.strip()
        point = i.select_one('div.cmt_info > div:nth-of-type(1)').text.strip()
        try:
            review = i.select_one('p.desc_txt').text.strip()
        except:
            print('리뷰없음 ')
            review = ''
        d_movie = d_movie.append(DataFrame({'day':day,'id':id,'point':point,'review':review},index=[0]),ignore_index=True)
        time.sleep(1)
except:
    print('오류')

n_movie.point
d_movie.point

from konlpy.tag import Okt
okt = Okt()


def okt_pos(arg):
    token = []
    for i in okt.pos(arg):
        if i[1] in ['Noun','Adjective']:
            token.append(i[0])
    return token

n_movie_token = [okt_pos(i) for i in n_movie.review]
d_movie_token = [okt_pos(i) for i in d_movie.review]

# 리스트 풀기
n_movie_word = [word2 for word in n_movie_token for word2 in word]
d_movie_word = [word2 for word in d_movie_token for word2 in word]


# 워드클라우드 1차확인

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(Counter(n_movie_word)) 
plt.imshow(w)
plt.axis('off')

w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(Counter(d_movie_word)) 
plt.imshow(w)
plt.axis('off')

n_word_df = pd.DataFrame.from_dict([Counter(n_movie_word)]).T
d_word_df = pd.DataFrame.from_dict([Counter(d_movie_word)]).T

Counter(n_movie_word).most_common(50)

n_word_df.reset_index(inplace=True)
n_word_df
n_word_df.columns = ['word','freq']

d_word_df.reset_index(inplace=True)
d_word_df.columns = ['word','freq']


n_top = n_word_df[n_word_df['freq']>=5]
n_top

d_top = d_word_df[d_word_df['freq']>=5]
d_top
n_top.set_index('word',inplace=True)
d_top.set_index('word',inplace=True)


# 워드 클라우드 (5번 이상 등장한 단어)
w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(n_top.to_dict()['freq']) 
plt.imshow(w)
plt.axis('off')

w.to_file('c:/data/n_movie_word.jpg')


w = WordCloud(font_path='c:/windows/fonts/HMKMMAG.TTF',
              background_color='white',
              width=900,height=500).generate_from_frequencies(d_top.to_dict()['freq']) 
plt.imshow(w)
plt.axis('off')

w.to_file('c:/data/d_movie_word.jpg')
n_movie.point = n_movie.point.astype('int')
d_movie.point = d_movie.point.astype('int')

n_point = n_movie.point.value_counts().reset_index()
d_point = d_movie.point.value_counts().reset_index()

n_point.columns = ['평점','빈도수']
d_point.columns = ['평점','빈도수']

n_point = n_point.append({'평점':7,'빈도수':0},ignore_index=True)

n_point = n_point.sort_values(by='평점')
d_point = d_point.sort_values(by='평점')

# 두 사이트 평점 빈도 막대그래프
plt.bar(n_point['평점'],n_point['빈도수'],
        width=0.2) 
plt.xticks(n_point['평점'],rotation=45)

plt.bar(d_point['평점']+0.2,d_point['빈도수'],
        width=0.2) 
plt.xticks(d_point['평점'],rotation=45)

plt.title('사이트별 평점 현황',size=20)
plt.xlabel('평점', size=10)
plt.ylabel('빈도수', size=10,rotation=90)
plt.legend(labels=['네이버','다음'],loc='upper center',ncol=4)


# 평점 평균 비교
np.array([int(i) for i in n_movie.point]).mean() # 9.79
np.array([int(i) for i in d_movie.point]).mean() # 9.38




# 작성자 아이디를 통해 장르 취향 파악
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

url = 'https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=167613&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page=1'
driver = webdriver.Chrome('c:/data/chromedriver.exe')
driver.get(url)

genre_final = []
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
id = []
for i in soup.select('div.score_reple > dl > dt > em > a > span'):
    id.append(i.text.strip())
for i in range(1,4):
    btn = driver.find_element(By.XPATH, '/html/body/div/div/div[5]/ul/li['+str(i)+']/div[2]/dl/dt/em[1]/a')
    action = ActionChains(driver)
    action.move_to_element(btn).perform()
    driver.find_element(By.XPATH, '/html/body/div/div/div[5]/ul/li['+str(i)+']/div[2]/dl/dt/em[1]/a').click()
    
    genre = []
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    for i in soup.select('div.score_reple > dl > dt > em > a > span'):
        id.append(i.text.strip())
    for i in range(1,len(soup.select('div#old_content > table > tbody > tr'))+1):
        btn = driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr['+str(i)+']/td[2]/a[1]')
        action = ActionChains(driver)
        action.move_to_element(btn).perform()
        driver.find_element(By.XPATH, '//*[@id="old_content"]/table/tbody/tr['+str(i)+']/td[2]/a[1]').click()
    
        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        soup1 = soup.select('div.choice_movie_info > table > tbody > tr:nth-of-type(1) > td > a')
        
        for i in soup1[0:len(soup1)-2]:
            genre.append(i.text.strip())
        time.sleep(1)
        driver.back()
    genre_final.append(genre)   
    driver.back()
    time.sleep(1)



#id
/html/body/div/div/div[5]/ul/li[1]/div[2]/dl/dt/em[1]/a
/html/body/div/div/div[5]/ul/li[2]/div[2]/dl/dt/em[1]/a
/html/body/div/div/div[5]/ul/li[1]/div[2]/dl/dt/em[1]/a/span
# movie
//*[@id="old_content"]/table/tbody/tr[1]/td[2]/a[1]
//*[@id="old_content"]/table/tbody/tr[2]/td[2]/a[1]
# genre
//*[@id="old_content"]/div[1]/div[1]/table/tbody/tr[1]/td


# 뒤로가기
driver.back()
driver.forward()






