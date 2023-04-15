'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

print("Hello World")

A={'돈까스','초밥','우동','피자'}
B={'초밥','우동','국밥'}
print(A.intersection(B))
print(A.union(B))
print(A.difference(B))

# 세트는 중복 불가능
# 세트는 순서 지정 불가
# 튜플은 수정 불가
# copy(), discard(), isdisjoint(), issubset(), issuperset(), update() 등이 있음

animal={'종류': '토끼', '나이': 7, '몸무게': 20}
print(animal['종류'])
print(animal.get('별명'))
animal['별명']='토순이'
print(animal['별명'])

animal['몸무게']=30

print(animal['몸무게'])

animal.update({'키': 8, '몸무게':45})
print(animal['키'])

animal.pop('몸무게')
print(animal.keys())
print(animal.values())
print(animal.items())

# fromkeys: 제공된 keys를 통해 새로운 딕셔너리를 생성 및 변환 
# popitem: 마지막으로 추가된 데이터 삭제
# setdefault: key에 해당하는 value 반환 / key가 없다면 새로 만들고 default value 설정 및 반환

# 리스트는 순서 보장,중복 허용, 수정, 추가, 삭제 가능
# 튜플은 순서 보장, 중복 허용, 수정 불가, 추가 불가, 삭제 불가
# 세트는 순서x, 중복 불가, 수정 불가, 추가 및 삭제는 가능
# 딕셔너리는 순서 보장, 중복 불가, 수정 가능, 추가 및 삭제도 가능

my_tuple=('오리온','오리온','롯데','롯데')
my_list=list(my_tuple)
my_list.append('초코파이')
my_tuple=tuple(my_list)
print(my_tuple)


my_list=['오리온','오리온','초코파이','초코파이']
my_set=set(my_list)
my_list=list(my_set)
print(my_list)

my_list=['초코파이','초코파이','오예스','초코송이']
my_dic=dict.fromkeys(my_list)
print(my_dic)
my_list=list(my_dic)
print(my_list)

today='토요일'
if today=='토요일':
    print('잠시 쉰후')
print('공부 시작')

yesterday='월요일'
if yesterday=='금요일':
    print('오늘은 쉬고 나중에')
else:
    print('바로')
print('공부하자')

성적=76
if 성적>=80:
    print('성적은 A입니다.')
elif 성적>=75 and 성적<80:
    print('성적은 B입니다.')
elif 성적==75:
    print('성적은 C입니다.')
else:
    print('성적은 D입니다. 재수강하시길 바랍니다.')

성적=80
if 성적>=80:
    print('성적은 A입니다.')
elif 성적>=75 and 성적<80:
    print('성적은 B입니다.')
elif 성적==75:
    print('성적은 C입니다.')
else:
    print('성적은 D입니다. 재수강하시길 바랍니다.')

성적=60
if 성적>=80:
    print('성적은 A입니다.')
elif 성적>=75 and 성적<80:
    print('성적은 B입니다.')
elif 성적==75:
    print('성적은 C입니다.')
else:
    print('성적은 D입니다. 재수강하시길 바랍니다.')

yellow_card=0
foul= True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적으로 퇴장')
    else:
        print('다음부터 조심해야지')

yellow_card = 1
foul= True
if foul:
    yellow_card += 1
    if yellow_card == 2:
        print('경고 누적으로 퇴장')
    else:
        print('다음부터 조심해야지')

n=5
total=1
for i in range(1,(n+1)):
    total=total*i
print(total)

for i in range(10):
    print(f'윗몸일으키기 {i}회 완료')

n=5
total=1
for i in range(1,(n+1),2):
    total=total*i
print(total)

    
