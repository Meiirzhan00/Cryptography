from pyzt import *
kaz_al='аәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыіъэюяаәбвгғдеёжзийкқлмнңоөпрстуұүфхһцчшщьыіъэюя'
def tanda():
    while True:
        t=inputi(' Гронсфельд шифрын таңдағың келсе "1"-ді бас. Вижинер шифрын таңдасаң "2"-ні бас : ')
        if t==1:
            Gronsfeld(kaz_al)
        elif t==2:
            Vizhiner(kaz_al)
        else:
            print(" Қате енгіздіңіз. Қайта енгізіңіз !!! ")

def Gronsfeld(kaz_al):
    myDict={}
    sh=''
    encrypt=input(' Хабарламаны енгіз : ')
    print(" ЕСКЕРТУ: КІЛТ СӨЗ 26-дан АСПАУЫ ҚАЖЕТ.  КІЛТ СӨЗ ҚАТАРЫ: 191786 ")
    for i in encrypt.lower():
        myDict[i]=int(input(f" Кілт сандарын енгіз (бір-бірлеп) : {i} =  "))
    for i in encrypt.lower():
      if i in myDict:
        d=kaz_al.find(i)
        if i in " ":
            sh+=i
        else:
            sh+=kaz_al[d+myDict[i]]
    print("-".center(50,"-"))
    print(" Шифрлау керек сөз : %s "%encrypt)
    print(" Шифрланған сөз  :   %s"%sh.title())
    print("-".center(50,"-"))


def Vizhiner(kaz_al):
    myDict1={}
    sh1=''
    encrypt1=input(' хабарламаны енгіз : ')
    print(" КІЛТ СӨЗ: ПРОГРАММИСТ ")
    for i in encrypt1.lower():
        myDict1[i]=input(f" Кілт сөзді енгіз (бір-бірлеп) : {i} =  ")
    for i in encrypt1.lower():
        if i in myDict1:
            if i in " ":
                sh1+=i
            else:
                d=kaz_al.find(i)
                dk=kaz_al.find(myDict1[i])
                res=d+dk
                if res>26:
                    res1=res-26
                    sh1+=kaz_al[res1]
                else:
                    sh1+=kaz_al[res]

    print("-".center(50,"-"))
    print(" Шифрлау керек сөз : %s "%encrypt1)
    print(" Шифрланған сөз  :   %s"%sh1.title())
    print("-".center(50,"-"))
tanda()
