# en_al=str('abcdefghijklmnopqrstuvxyzabcdefghijklmnopqrstuvxyz')
# words=input('Шифрлау керек сөзді енгіз : ')
# key=input('Кілтті енгіз : ')
# count=0
# s=''
# for i in range(len(words)):
#     for j in range(len(en_al)):
#         count+=1
#         if words[i]==en_al[j]:
#             print(f"{count}='Yess'")
#             s+=en_al[j+int(key)]
# print(s)

def tanda():
    t=int(input(f"Шифрлау үшін '1' санын бас. Дешифрлау үшін '2' санын бас : Таңдауың = "))
    if t==1:
        Encrypt()
    else :
        Decrypt()

def Encrypt():
    en_al=str('аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюяаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя')
    encrypt=input('Шифрлау керек сөзді енгіз : ')
    key=int(input('Кілтті енгіз : '))
    s=""
    for i in encrypt.lower():
        num_al=en_al.find(i)
        print(i ,' = ',num_al)
        kadam=num_al+key
        if i in en_al:
            s+=en_al[kadam]
        else:
            s+=i
    print(f"Шифрланғын сөз(сөйлем) 😎 : {s} ")




def Decrypt():
    en_al=str('аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюяаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщъыіьэюя')
    decrypt=input('Дешифрлау керек сөзді енгіз : ')
    key=int(input('Кілтті енгіз : '))
    s=""
    for i in decrypt.lower():
        num_al=en_al.find(i)
        kadam=num_al-key
        if i in en_al:
            s+=en_al[kadam]
        else:
            s+=i
    print(f"Дешифрланғын сөз(сөйлем) 😉 : {s} ")

tanda()












































