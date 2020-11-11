from pyzt import *
kaz_al='аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыіъэюя'
my_dict={}
for i in range(len(kaz_al)):
    my_dict[kaz_al[i]]=i
print(my_dict)
def Encrypt(message,key):
    j=0
    encrypt=''
    for i in message:
        if j>len(key)-1:
            j=0
            number=my_dict[i]+my_dict[key[j]]
            if number>42:
                number-=42
                encrypt+=kaz_al[number]
            else:
                encrypt+=kaz_al[number]
        else:
            number=my_dict[i]+my_dict[key[j]]
            if number>42:
                number-=42
                encrypt+=kaz_al[number]
            else:
                encrypt+=kaz_al[number]
        j+=1
    return encrypt
def Decrypt(encrypted_text,key):
    j=0
    decrypt=''
    for i in encrypted_text:
        if j>len(key)-1:
            j=0
            number=my_dict[i]-my_dict[key[j]]
            if number<0:
                number=my_dict[i]+42-my_dict[key[j]]
                decrypt+=kaz_al[number]
            else:
                decrypt+=kaz_al[number]
        else:
            number=my_dict[i]-my_dict[key[j]]
            if number<0:
                number=my_dict[i]+42-my_dict[key[j]]
                decrypt+=kaz_al[number]
            else:
                decrypt+=kaz_al[number]
        j+=1
    return decrypt
def foo():
    message=inputs(' Хатыңды жаз : ').lower()
    key=inputs(' Кілт сөзді енгіз : ').lower()
    encrypted_text=Encrypt(message,key)
    decrypted_text=Decrypt(encrypted_text,key)
    print(' Хат :\t\t\t\t  '+message+'\n'+' Шифрланған мәтін :   '+encrypted_text+'\n'+' Дешифрланған мәтін : '+decrypted_text)
foo()

