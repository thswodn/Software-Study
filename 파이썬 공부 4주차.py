# 가변인자
def visit(today, *customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2022-03-01','영희','철수')

def schedule(date,subject,*objects):
    print(date,subject)
    for object in objects:
        print(object)

schedule('2023-09-07','mathematics','나잘남','이순경')
schedule('2023-08-01','societies','이경석','이난도')

# 지역 변수: 함수 내에서 정의된 변수 / 외부에서 접근,수정 불가

# 전역변수: 어디서든 사용 가능

# 함수내에서 전역변수 값을 사용할 때는 상관 무 / 값을 직접 수정시 global 사용

def my_secret():
    message = '이건 나의 비밀이지'
    print(message)

my_secret()

message='나는 전역변수임'
print(message)

def nosecret():
    message = '이러면 또 지역변수'
    print(message)
nosecret()

def nosecret():
    global message # 전역변수 사용하겠음. 없으면 여기서 만들겠다는 의미
    message = '오 진짜 전역변수'
    print(message)
nosecret()
print(message)

# 사용자 입력 -> input사용
question = input('성함이 어떻게 되시나요??')
print(question)

count = input('혹시 몇분이신가요?')
print(count)

# 자판기
sum = int(input('동전을 넣어주세요'))
if sum < 500:
    print('금액이 모자랍니다.')
    sum1 = int(input(f'동전 최소 {500 - sum}원 더 넣어주시겠어요?'))
    if sum1 < (500-sum):
        print('나중에 다시 오시기 바랍니다.')
    elif sum1 == 500-sum:
        print('콜라 선택하셨습니다.')
        print('이용해주셔서 감사합니다.')
    elif sum1 >= 500 and sum1 + sum < 1000 :
        print(f'거스름돈은 {sum1 - 500 + sum}원 입니다. 환타 선택하셨습니다.')
        print('이용해주셔서 감사합니다.')
    else:
        print(f'거스름돈은 {sum1 + sum - 1000}원입니다. 몬스터 캔 음료 선택하셨습니다.')
        print('이용해주셔서 감사합니다.')
elif sum == 500:
    print('콜라 선택하셨습니다.')
    print('이용해주셔서 감사합니다.')
elif sum > 500 and sum < 1000:
    print(f'거스름돈은 {sum - 750}원입니다. 환타 선택하셨습니다.')
    print('이용해주셔서 감사합니다.')
else:
    print(f'거스름돈은 {sum - 1000}원입니다. 몬스터 캔 음료 선택하셨습니다.')
    print('이용해주셔서 감사합니다.')

# 파일 입출력

# open(파일명, 열기 모드,  encoding='인코딩')
# 열기 모드
# r(read) / a(append) / w(Write)

f = open('list.txt', 'w', encoding='utf8') # 쓰기 모드 / 한글 사용
f.write('김xx\n') # 문장 입력하기
f.write('정xx\n') # 문장 입력하기
f.write('어xx\n') # 문장 입력하기
f.close() # 파일 닫기

f = open('list.txt', 'r', encoding='utf8') # 읽기모드로 열기
contents = f.read() # 파일 내용 다 읽어오기
print(contents)
f.close()

f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')
f.close()

