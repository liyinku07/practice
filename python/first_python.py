import random as rd
x = rd.randint(1,10)
for i in range(3):              
  s = int(input('猜數字1-10:'))
  if x == s:
    print('猜中')
    break
  elif x > s:
    print('大一點')
  elif x < s:
    print('小一點')
print('遊戲結束!')


#使用內定索引
print(sc[1])
sc[1] = 100
print(sc[1])

#使用自定索引
print(sc['英文'])
sc['英文'] = 80
print(sc['英文'])