p = int(input('p = '))
q = int(input('q = '))
n = p*q
ph_n= (p-1)*(q-1)

e = int(input('e = '))

d1 = 0
while True:
  d1 += 1
  if (e*d1)%ph_n == 1:
    d = d1
    break

m = int(input('Enter m = '))
print(f'Жабық кілт: {d, n}')
print(f'Ашық кілт: {e, n}')

s = (m**d)%n
print(f'Цифрлы қолтаңба : {m, s}')

m_ = (s**e)%n

print(f'Дешифрланған мәтін : {m_}')
