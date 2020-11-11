
arr=[ ['Ф','А','В','О','Р','И','Т'],
      ['Ә','Б','Г','Ғ','Д','Е','Ё'],
      ['Ж','З','Й','К','Қ','Л','М'],
      ['Н','Ң','Ө','П','С','У','Ұ'],
      ['Ү','Х','Һ','Ц','Ч','Ш','Щ'],
      ['Ъ','Ы','І','Ь','Э','Ю','Я']
]

def Encript(arr):
    s=''
    for i in arr:
        for j in i:
            print('\t',j,end="")
        print()
    encrypt_w=input(" Шифрлау керек сөзді енгіз : ")
    for item in encrypt_w.upper():
        if item=='Ф':
            s+='Ә'
        elif item=='А':
            s+='Б'
        elif item=='В':
            s+='Г'
        elif item=='О':
            s+='Ғ'
        elif item=='Р':
            s+='Д'
        elif item=='И':
            s+='Е'
        elif item=='Т':
            s+='Ё'
        elif item=='Ә':
            s+='Ж'
        elif item=='Б':
            s+='З'
        elif item=='Г':
            s+='Й'
        elif item=='Ғ':
            s+='К'
        elif item=='Д':
            s+='Қ'
        elif item=='Е':
            s+='Л'
        elif item=='Ё':
            s+='М'
        elif item=='Ж':
            s+='Н'
        elif item=='З':
            s+='Ң'
        elif item=='Й':
            s+='Ө'
        elif item=='К':
            s+='П'
        elif item=='Қ':
            s+='С'
        elif item=='Л':
            s+='У'
        elif item=='М':
            s+='Ұ'
        elif item=='Н':
            s+='Ү'
        elif item=='Ң':
            s+='Х'
        elif item=='Ө':
            s+='Һ'
        elif item=='П':
            s+='Ц'
        elif item=='С':
            s+='Ч'
        elif item=='У':
            s+='Ш'
        elif item=='Ұ':
            s+='Щ'
        elif item=='Ү':
            s+='Ъ'
        elif item=='Х':
            s+='Ы'
        elif item=='Һ':
            s+='І'
        elif item=='Ц':
            s+='Ь'
        elif item=='Ч':
            s+='Э'
        elif item=='Ш':
            s+='Ю'
        elif item=='Щ':
            s+='Я'
        elif item=='Ъ':
            s+='Ф'
        elif item=='Ы':
            s+='А'
        elif item=='І':
            s+='В'
        elif item=='Ь':
            s+='О'
        elif item=='Э':
            s+='Р'
        elif item=='Ю':
            s+='И'
        elif item=='Я':
            s+='Т'
        else:
            s+=item
    print(' Шифрланған мәтін \t\t\t', s)

Encript(arr)
