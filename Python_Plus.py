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











