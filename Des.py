from pyzt import *
my_array=[[7,3,5],
          [6,8,1],
          [2,4,9]
]

for i in my_array:
        for j in i:
          print(j,end='  ')
        print()

def Encrypt(my_array):
  print('ENCRYPT'.center(50,'='))
  encrypted_text=''
  while True:
    encrypt_message=input("Шифрлау керек сөзді енгіз : ")
    if len(encrypt_message)>9 and len(encrypt_message)<9 :
      print(" Қайта енгіз  !!! ")
    elif len(encrypt_message)==9:
      for i in my_array:
        for j in i:
          encrypted_text+=encrypt_message[j-1]
          print(str(j)+' '+encrypt_message[j-1],end='    ')
        print()
      print("Жабық мәтін".center(50,'='))
      print("Жабық мәтін : ", encrypted_text)
      break
def Decrypt(my_array):
  print('DECRYPT'.center(50,'='))
  my_dict={}
  decrypted_text=''
  while True:
    decrypt_message=input("Дешифрлау керек сөзді енгіз : ")
    if len(decrypt_message)>9 and len(decrypt_message)<9 :
      print(" Қайта енгіз !!! ")
    elif len(decrypt_message)==9:
      c=0
      for i in my_array:
        for j in i:
          my_dict[j]=decrypt_message[c]
          print(str(j)+' '+decrypt_message[c],end='    ')
          c+=1
        print()
      for item in range(1,len(my_dict)+1):
          decrypted_text+=my_dict[item]
      print("Ашық мәтін".center(50,'='))
      print("Ашық мәтін : ", decrypted_text)
      break
def tanda():
    t=inputi("Мәтінді шифрлау үшін {1}-ді бас , дешифрлау үшін {2}-ні бас :  ")
    if t is 1:
        Encrypt(my_array)
    else:
        Decrypt(my_array)
tanda()
