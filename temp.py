kaz_alp={
    'А':['І','^'],'Б':['И','@'],'В':['О',')'],'Г':['А','+'],'Д':['Щ','>'],
    'Е':['П','<'],'Ж':['К','இ'],'З':['Б','♦'], 'И':['Ъ','*'],'К':['Ұ','♥'],
    'Л':['Р','♠'],'М':['Ң','№'],'Н':['Ә','#'],'О':['Ё','-'],'П':['Ж','='],
    'Р':['Ғ','('],'С':['Л','?'],'Т':['Х','%'],'У':['С','☺'],'Ф':['Ь','!'],
    'Х':['Ч','©'],'Ц':['З','®'],'Ч':['М','♞'],'Ш':['У','♬'],'Щ':['Д','☯'],
    'Ъ':['Э','▲'],'Ы':['Н','§'],'Ь':['Ю','¤'],'Э':['Ы','€'],'Ю':['Г','Ŋ'],
    'Я':['Қ','♀'],'Ё':['Ф','☺'],'Й':['Я','♣'],'Ә':['Ц','♂'],'Ғ':['Ш','㋛'],
    'Қ':['Е','⌚'],'Ң':['Ү','✔'],'Ө':['Й','✿'],'Ұ':['Ө','ق'],'Ү':['Т','√'],
    'Һ':['В','&'],'І':['Һ','$'],' ':[' ',' ']
}

def Encrypt(kaz_alp):
    sh1=''
    sh2=''
    encrypt=input("Шифрлау керек сөзді енгіз : ")
    for i in encrypt.upper():
        if i in kaz_alp:
            sh1+=kaz_alp[i][0]
            sh2+=kaz_alp[i][1]
            print(i,' = ',kaz_alp[i])
        else:
            sh1+=i
            sh2+=i
    nn='\tАшық мәтін'
    print(f"{'♥'.center(64,'♥')}",f"\n {nn.expandtabs(23)} : {encrypt}",
          f"\n Шифр 1 көмегімен шифрланған мәтін : {sh1}",
          f"\n Шифр 2 көмегімен шифрланған мәтін : {sh2}",
          f"\n{'♥'.center(64,'♥')}")
    print("\n   Шифр 1      Шифр 2   Ашық мәтін")
    for x ,y in kaz_alp.items():
        for item in y:
            print('\t',item,end="\t\t")
        print('\t',x)

Encrypt(kaz_alp)
