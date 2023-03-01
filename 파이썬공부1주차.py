print("Hello World")
print('안녕하세요')
print("True")

value=300
print(value)
num = float(3)
print(num)

word = "꿀꽈배기"
print('2'+word)
print(str(2)+word)

print(5%2)
print(5//2)

print(5>=2)
print(5<4)
print(not 6>7)

a = 100
b = 10
if a > b and b == a**2:
    print("Yes")
else:
    print("No")
    
print(bool())

print("안녕하세요")
# 상대방이 인사를 받아준 후
print("저는 손재우라고 합니다.")

lang = 'numercial'
print(lang[0:])
print(lang[:-1])
print(lang[:8])
print(lang[2:9])

num=100
num/=2
print(int(num))

sentence = "파이선을 배워봅시다."
print(len(sentence))

letter = 'Numercial methods with PYTHON'
print(letter.upper())
print(letter.swapcase())
print(letter.split())
print(letter.lower())
print(letter.title())
print(letter.capitalize())
print(letter.count('with'))

w = '정보통신대대'
print(w.replace('통신대대','대대'))
print(w.strip('대대'))
print(w.startswith('정보'))
print(w.endswith('ㅌ어'))
print(w.find('통신'))
print(w.center(8,'*'))
print(w.center(7,'*'))

print('오늘은 {}, {} 등을 공부해보고 {}로 저장해보는 실습을 하였다'.format(
    '문자열 메소드','여러 연산자','파일'))
    
print('오늘은 {2}, {0} 등을 공부해보고 {1}로 저장해보는 실습을 하였다'.format(
    '문자열 메소드','여러 연산자','파일'))

print("나는 오늘 '파이썬을 쉽게 배울 수 있나?...'하고 생각을 했다.")    
print('과연 그게 맞는지...\'라고 생각을 했으나 나중에 \"이게 맞아\"라고 확신을 했다.' )

snack = '과자는 \n 늘 \n 맛있습니다.'
print(snack)

slist = ['초코파이', '파이', '파이', '빵', '초코파이']
print(slist)
if slist[0] == slist[2]:
    print('문자가 똑같습니다.')
else:
    print(slist[0],slist[2])

print('몽쉘' in slist)

slist.append('몽쉘')
print(slist)

slist.remove('빵')
print(slist)

nlist = [1,100,0,50]
nlist.reverse()
print(nlist)

nlist.sort()
print(nlist)

nlist.pop(2)
print(nlist)

ituple = ('파이썬','자바','c')
print(ituple[1])
