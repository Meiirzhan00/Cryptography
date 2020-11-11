arr=[ [4,9,2],
      [3,5,7],
      [8,1,6]
]
def Encript(arr):
    s=''
    for i in arr:
        for j in i:
            print('\t',j,end="")
        print()
Encript(arr)
