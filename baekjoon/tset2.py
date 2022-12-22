a,b,c = map(int,input().split())
who = input()
win = int(input())

listA = ['A' for i in range(a)]
listB = ['B' for i in range(b)]
listC = ['C' for i in range(c)]

next = ''

if len(listA)>=len(listB) and len(listA)>=len(listC):
    if len(listB)>len(listC):
        next = 'AB'
    else:
        next = 'AC'

if len(listB)>=len(listA) and len(listB)>=len(listC):
    if len(listA)>len(listC):
        next = 'AB'
    else:
        next = 'BC'

if len(listC)>=len(listA) and len(listC)>=len(listB):
    if len(listA)>len(listB):
        next = 'AC'
    else:
        next = 'BC'

if who == 'A':
    while True:
        if len(listA) == win:
            break
        if next == 'AB':
            print(listA.pop(0)+listB.pop(0),end=' ')
            if len(listA)-win>len(listB):
                next = 'AC'
            else:
                next = 'BC'
            
        elif next == 'BC':
            print(listB.pop(0)+listC.pop(0),end=' ')
            if len(listB)>len(listC):
                next = 'AB'
            else:
                next = 'AC'
        
        elif next == 'AC':
            print(listA.pop(0)+listC.pop(0),end=' ')
            if len(listC)>len(listA)-win:
                next = 'BC'
            else:
                next = 'AB'
    
    if len(listA) != len(listB)+len(listC):
        print(listB.pop(0)+listC.pop(0),end=' ')
        
    if len(listB)>len(listC):
        next = 'AB'
    else:
        next = 'AC'
              
    while len(listA)>0 or len(listB)>0 or len(listC)>0:
        try:
            if next == 'AB':
                print(listA.pop(0)+listB.pop(0),end=' ')
                next = 'AC'

            elif next == 'AC':
                print(listA.pop(0)+listC.pop(0),end=' ')
                next = 'AB'
        except:
            break

if who == 'B':
    while True:
        if len(listB) == win:
            break
        if next == 'AB':
            print(listA.pop(0)+listB.pop(0),end=' ')
            if len(listA)>len(listB)-win:
                next = 'AC'
            else:
                next = 'BC'
            
        elif next == 'BC':
            print(listB.pop(0)+listC.pop(0),end=' ')
            if len(listB)-win>len(listC):
                next = 'AB'
            else:
                next = 'AC'
        
        elif next == 'AC':
            print(listA.pop(0)+listC.pop(0),end=' ')
            if len(listC)>len(listA):
                next = 'BC'
            else:
                next = 'AB'
    
    if len(listB) != len(listA)+len(listC):
        print(listA.pop(0)+listC.pop(0),end=' ')
        
    if len(listA)>len(listC):
        next = 'AB'
    else:
        next = 'BC'
              
    while len(listA)>0 or len(listB)>0 or len(listC)>0:
        try:
            if next == 'AB':
                print(listA.pop(0)+listB.pop(0),end=' ')
                next = 'BC'

            elif next == 'BC':
                print(listB.pop(0)+listC.pop(0),end=' ')
                next = 'AB'
        except:
            break
        
if who == 'C':
    while True:
        if len(listC) == win:
            break
        if next == 'AB':
            print(listA.pop(0)+listB.pop(0),end=' ')
            if len(listA)>len(listB):
                next = 'AC'
            else:
                next = 'BC'
            
        elif next == 'BC':
            print(listB.pop(0)+listC.pop(0),end=' ')
            if len(listB)>len(listC)-win:
                next = 'AB'
            else:
                next = 'AC'
        
        elif next == 'AC':
            print(listA.pop(0)+listC.pop(0),end=' ')
            if len(listC)-win>len(listA):
                next = 'BC'
            else:
                next = 'AB'
    
    if len(listC) != len(listA)+len(listB):
        print(listA.pop(0)+listB.pop(0),end=' ')
        
    if len(listA)>len(listB):
        next = 'AC'
    else:
        next = 'BC'
              
    while len(listA)>0 or len(listB)>0 or len(listC)>0:
        try:
            if next == 'AC':
                print(listA.pop(0)+listC.pop(0),end=' ')
                next = 'BC'

            elif next == 'BC':
                print(listB.pop(0)+listC.pop(0),end=' ')
                next = 'AC'
        except:
            break