my_list = [1,2,3]
for x in my_list:
  print(x)

my_tuple = [1,2,3]
for x in my_tuple:
  print(x)

animal={'종류': '호랑이', '나이': 10, '몸무게': 15}
for i in animal.values():
  print(i)

for i in animal.keys():
  print(i)

for k, v in animal.items():
  print(k, v)

beverage = 'coke'
for x in beverage:
  print(x)

# for은 정해진 범위 또는 데이터를 순회하면서 반복 반면 while은 조건이 참인 동안 반복

max=10 # 최대 허용 개수
count=0 # 현재 개수
item=2 # 각 봉지당 개수

while count + item <= max: # 몇 봉지를 더 가져갈 수 있는 지 확인
  count += item
  print(f'{max/item - count/item}봉지 추가할 수 있습니다')

drama=['시즌1','시즌2','시즌3']
for x in drama:
  if x == '시즌2':
    print('재미없으니 그만 보자')
    break
  print(f'{x}시청')

# 어떤 동작 건너뛰고 싶을대 사용하는 것이 continue

drama=['시즌1','시즌2','시즌3']
for x in drama:
  if x == '시즌2':
    print('재미없으니 그만 보자')
    continue
  print(f'{x}시청')

# 짝수 판별기
for x in range(1,15):
  if x%2 == 1:
    continue
  print(x)

# 홀수 판별기
for x in range(1,15):
  if x%2 == 0:
    continue
  print(x)

# 7의 배수만??
for x in range(1,50):
  if x%7==0:
    print(x)

# 파이썬에서 들여쓰기는 중요!!

machines = ['A-100','A-501','B-715','B-805'] # 라인 별 기계번호들
fix =[] # 수리대상 기계 목록
for m in machines:
  if m.startswith('B'):
    fix.append(m)
print(fix)
# 그렇다면 이 긴거를 어떻게 간단하게??

# List Comprehension 사용

fix = [m for m in machines if m.startswith('B')]
print(fix)

# 동일 코드들을 매번 찾아서 수정하기 힘들고 시간이 많이 소요 / 번거로움 -> 함수 사용

# 함수 정의
def show_price():
  print('이발 가격은 15000원 입니다.')

# 함수 호출
show_price()

customer1 = '나이름'
print(f'{customer1}고객님')
show_price()

customer2 = '나예쁨'
print(f'{customer2}고객님')
show_price()

# 함수 정의
def show_price(customer):
  print(f'{customer}고객님')
  print('이발 가격은 15000원 입니다.')

customer1 = '나이름'
show_price(customer1)

customer2 = '나예쁨'
show_price(customer2)

# 전달값 여러개 사용가능(콤마로 구분)
# 함수 내에서만 사용가능!!

# def 함수명(전달값):
#    수행할 문장
#    return 반환값

# 단골은 11000원만 받고 나머지 다른 손님은 15000원 받도록 설정해보자.

def get_price(is_vip): # True: 단골손님, False: 일반 손님
  if is_vip == True:
    return 11000
  else:
    return 15000

price = get_price(True)
print(f'이발 가격은 {price}입니다.')

# 반환되는 즉시 함수 탈출
# 기본값은 전달값에 기본으로 사용되는 값

# def 함수명(전달값=기본값):
#    수행할 문장

def show_money(is_vip=True): # True: 단골손님, False: 일반 손님
  if is_vip == True:
    return 5000
  else:
    return 10000

money = show_money(False)
print(f'주문하신 음식의 가격은 {money}입니다.')
mone = show_money()
print(f'주문하신 음식의 가격은 {mone}입니다.')

# 전달값이 다양할때??
# 키워드값 사용 / 전달값의 대상 정해둔다.

def order(shot=1, size='Tall', takeout=False): # 커피 주문
  print(f'아메리카노 {size} 사이즈 {shot} 샷')
  if takeout:
    print('포장주문이 완료되었습니다.')
  else:
    print('주문이 완료되었습니다.')

order(size='Regular')

# 손님관리하여 재방문 유도하자
# 가변인자: 개수가 바뀔 수 있는 인자 -> 전달값 앞에 *붙이기

def visit(today,*customers):
  print(today)
  for customer in customers:
    print(customer)

# 가변인자는 마지막에 딱 한번만 사용가능
visit('2023-03-01','stella')
visit('2023-03-01','stella,venia')
visit('2023-03-01','stella,venia,dellis')
