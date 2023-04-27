f = open('list.txt','w',encoding='utf8')
f.write('나는 코딩 공부를 해봤다.\n')
f.write('나는 대학생이다.\n')
f.write('나는 지금도 공부중이다.\n')
f.close()

f = open('list.txt','r',encoding='utf8')
contents = f.read()
print(contents)
f.close()

# 파일 열고 닫아야 하는데 깜빡할 수도 있음 -> 이걸 자동으로 해주는게 with이다.
# with 블럭 벗어나면 자동으로 파일 닫음

with open('sentence.txt','w',encoding='utf8') as file:
    file.write('나는 코딩 공부를 해봤다.\n')
    file.write('나는 대학생이다.\n')
    file.write('나는 지금도 공부중이다.\n')
    
with open('sentence.txt','r',encoding='utf8') as file:
    contents = file.read()
    print(contents)

# 클래스

# 블랙박스 모델 하나 더 관리?? -> 효율적으로 관리??
# 별도로 관리하는 기능?
# ---> 클래스 사용
# 클래스는 여러 변수들을 모아서 한 번에 관리 가능 / 어떤 기능을 하도록 함수도 만들 수 있음
# 클래스는 한번 만들면 그 클래스를 가지고 여러 많은 것을 만들 수 있음
# 그 많은 것들을 object(객체)라고 함 / 각 개체는 이 클래스의 인스턴스임
# 대문자들의 조합으로 클래스명 만들기

class 클래스명:
    정의

class BlackBox:
    pass

b1 = BlackBox() # b1객체 생성 완료
b1.name='검둥이' # 변수선언
print(b1.name)
print(isinstance(b1,BlackBox))

b2=BlackBox()
print(b2.name) # -> 오류발생

# __init__
# __init__함수는 객체가 생성될때 자동으로 실행
# 일반 함수와 다르게 (self,...) self가 들어간다는 점 기억!!

class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
b1=BlackBox('흰둥이',15000)
print(b1.name,b1.price)

# 멤버변수: 위의 예시에서는 self.name, self.price
# 클래스 객체마다 서로 다른 값 가질 수 있음
# 두 개체는 완전히 독립

class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        
b1=BlackBox('흰둥이',15000)
b1.nickname = '1호'
print(b1.name,b1.price,b1.nickname)
print(b2.name,b2.price,b2.nickname) # -> 오류 발생

# 메소드: 클래스 내에서 선언되는 함수

class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def set_travel_mode(self):
        print('여행모드 on')
b1=BlackBox('흰둥이',15000)
b1.set_travel_mode() # 결과 -> 여행모드 on

class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(str(min) + '분동안 여행모드 on')
b1=BlackBox('흰둥이',15000)
b1.set_travel_mode(20) # 결과 -> 20분동안 여행모드 on

# 메소드는 self를 제외한 전달값들을 일반 함수와 같은 방식으로 호출하면 됨

# self에 대해서 -> 객체 자기 자신을 의미
class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

b1=BlackBox('흰둥이',15000)
b2=BlackBox('검둥이',20000)

b1.set_travel_mode(20) # 결과: 흰둥이20분동안 여행모드 on
b2.set_travel_mode(50) # 결과: 검둥이50분동안 여행모드 on

BlackBox.set_travel_mode(b1,20) # 결과: 흰둥이20분동안 여행모드 on

#1. 메소드를 정의할 때 처음 전달값은 반드시 self
#2. 메소드 내에서는 self.name과 같은 형태로 멤버변수 사용

# 상속: 새로운 코드 만들때마다 중복되는 코드 생김 -> 이럴 때 사용

class BlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
        

class TravelBlackBox():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

class TravelBlackBox(BlackBox):
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')
# 여기서 Blackbox가 부모클래스, TravelBlackbox가 자식클래스


# super : 부모클래스를 의미
class TravelBlackBox():
    def __init__(self,name,price,sd):
        self.name = name
        self.price = price
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')


b2=TravelBlackBox('검둥이',20000, '256')
print(b2.name,b2.price,b2.sd)

# 결과: 검둥이 20000 256

=======================================================
class TravelBlackBox(BlackBox):
    def __init__(self,name,price,sd):
        BlackBox.__init__(self,name,price)
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

b2=TravelBlackBox('검둥이',20000, '256')
print(b2.name,b2.price,b2.sd)

# 결과: 검둥이 20000 256

=======================================================

class TravelBlackBox(BlackBox):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

b2=TravelBlackBox('검둥이',20000, '256')
print(b2.name,b2.price,b2.sd)

# 결과: 검둥이 20000 256

=======================================================
# 다중상속: 여러클래스로부터 상속을 받음 -> 상속받을 클래스명을 콤마로 구분해서 적음

# 추억용 영상 제작 기능 구현 클래스
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')
        
# 여행지원용 블랙박스
class TravelBlackBox(BlackBox):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

==============================================================
# 새로 만든 블랙박스
class TravelBlackBox(BlackBox,VideoMaker):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

b1=TravelBlackBox('흰둥이',20000, '32')
b1.make() # 결과: 추억용 여행 영상 제작

===============================================================
# 메일 발송 기능 구현 클래스
class MailSender:
    def send(self):
        print('메일발송')

================================================================
# 새로 만든 블랙박스 2
class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd # sd카드(64 or 256)
        
    def set_travel_mode(self,min): # 여행모드 시간(분)
        print(f'{self.name}{min}분동안 여행모드 on')

b2=TravelBlackBox('보람',200000, '64')
b2.make() # 결과: 추억용 여행 영상 제작
b2.send() # 결과: 메일발송
==================================================================
# 메소드 오버라이딩: 부모클래스의 메소드를 새로 정의하는 것
class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd
        
    def set_travel_mode(self,min):
        print(str(min) + '분동안 여행모드 on')

# 개선된 여행모드 지원 블랙박스(AdvancedTravelBlackBox)
class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self,min):
        print(str(min) + '분동안 여행모드 on')
        self.make()
        self.send()
b2.set_travel_mode(100) # 결과: 100분동안 여행모드 on / 추억용 여행 영상 제작 / 메일 발송

# 자식 클래스에서 같은 메소드를 새로 정의하지 X -> 부모클래스의 메소드를 새로 정의하면 자식 클래스의 메소드를 사용
===================================================================
# pass: '나중에 할게 일단 내버려둬'라는 의미로 사용 -> 완성되지 않았어도 에러 발생 X
# for, if, while, 함수 등에서 사용 가능

class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd=sd
        
    def set_travel_mode(self,min):
        pass
b2=TravelBlackBox('보람',200000, '64')
b2.set_travel_mode(100)

# 결과: 에러 발생 X
===================================================================
# 예외처리: 에러를 만나도 프로그램이 작동되도록 해주는 것

# 유형 1
try:
    수행문장
except:
    에러 발생시 수행문장

# 유형 2
try:
    수행문장
finally:
    마지막으로 수행할 문장 # 에러 여부 상관없이 작동

# 유형 3
try:
    수행문장
except:
    에러 발생시 수행문장
else:
    정상 작동 시 수행문장

# 유형 4
try:
    수행문장
except:
    에러 발생시 수행문장
else:
    정상 작동 시 수행문장
finally:
    마지막으로 수행할 문장 # 에러 여부 상관없이 작동
===================================================================
# 예시1
num1 = 154
num2 = 0
try:
    result = num1 / num2
    print(f'연산결과는 {result}입니다.')
except:
    print('0으로 나눌 수 없으니 계산을 실행할 수 없습니다.')
else:
    print('정상 작동 했습니다.')
finally:
    print('수행종료')

# 결과: 0으로 나눌 수 없으니 계산을 실행할 수 없습니다. / 수행종료
=====================================================================

# 예시2
num1 = 154
num2 = 2
try:
    result = num1 / num2
    print(f'연산결과는 {result}입니다.')
except:
    print('0으로 나눌 수 없으니 계산을 실행할 수 없습니다.')
else:
    print('정상 작동 했습니다.')
finally:
    print('수행종료')

# 결과: 연산결과는 77.0입니다. / 정상 작동 했습니다. / 수행종료

========================================================================
# 에러
num1 = 154
num2 = 0
try:
    result = num1 / num2
    print(f'연산결과는 {result}입니다.')
except Exception as err:
    print('계산을 실행할 수 없습니다.:', err)
# 결과: 계산을 실행할 수 없습니다.: division by zero
==========================================================================
# 여러 에러 다르게 처리하기 위해서는 except구문 여러개 사용
num1 = 154
num2 = 0
try:
    result = num1 / num2
    print(f'연산결과는 {result}입니다.')
except ZeroDivisionError:
    print('0으로 나눌 수 없어요')
except Exception as err:
    print('계산을 실행할 수 없습니다.:', err)
# 결과: 0으로 나눌 수 없어요

