# 코딩스타 5번
a,b,c = map(int,input().split())
who = input()
win = int(input())

game = []
next = ''

if who == 'A':
    if b>c:
        next = 'AB'
    else:
        next = 'AC'
        
    for i in range(win):
        if next == 'AB':
            a -= 1
            b -= 1
            game.append(next)
            next = 'AC'
            
        elif next == 'AC':
            a -= 1
            c -= 1
            game.append(next)
            next = 'AB'
    
    next='BC'
    while a>0 or b>0 or c>0:
            if next == 'AB' and a>0 and b>0:
                a -= 1
                b -= 1
                game.append(next)
                if a>b:
                    next = 'AC'
                else:
                    next = 'BC'
            
            if next == 'BC' and b>0 and c>0:
                b -= 1
                c -= 1
                game.append(next)
                if b>c:
                    next = 'AB'
                else:
                    next = 'AC'
            
            if next == 'AC' and a>0 and c>0:
                a -= 1
                c -= 1
                game.append(next)
                if c>a:
                    next = 'BC'
                else:
                    next = 'AB'

if who == 'B':
    if a>c:
        next = 'AB'
    else:
        next = 'BC'
        
    for i in range(win):
        if next == 'AB':
            a -= 1
            b -= 1
            game.append(next)
            next = 'BC'
            
        elif next == 'BC':
            b -= 1
            c -= 1
            game.append(next)
            next = 'AB'
    
    next='AC'
    while a>0 or b>0 or c>0:
            if next == 'AB' and a>0 and b>0:
                a -= 1
                b -= 1
                game.append(next)
                if a>b:
                    next = 'AC'
                else:
                    next = 'BC'
            
            if next == 'BC' and b>0 and c>0:
                b -= 1
                c -= 1
                game.append(next)
                if b>c:
                    next = 'AB'
                else:
                    next = 'AC'
            
            if next == 'AC' and a>0 and c>0:
                a -= 1
                c -= 1
                game.append(next)
                if c>a:
                    next = 'BC'
                else:
                    next = 'AB'

if who == 'C':
    if a>b:
        next = 'AC'
    else:
        next = 'BC'
        
    for i in range(win):
        if next == 'AC':
            a -= 1
            c -= 1
            game.append(next)
            next = 'BC'
            
        elif next == 'BC':
            b -= 1
            c -= 1
            game.append(next)
            next = 'AC'
    
    next='BC'
    while a>0 or b>0 or c>0:
            if next == 'AB' and a>0 and b>0:
                a -= 1
                b -= 1
                game.append(next)
                if a>b:
                    next = 'AC'
                else:
                    next = 'BC'
            
            if next == 'BC' and b>0 and c>0:
                b -= 1
                c -= 1
                game.append(next)
                if b>c:
                    next = 'AB'
                else:
                    next = 'AC'
            
            if next == 'AC' and a>0 and c>0:
                a -= 1
                c -= 1
                game.append(next)
                if c>a:
                    next = 'BC'
                else:
                    next = 'AB'
                    
for i in range(len(game)-1,-1,-1):
    print(game[i],end=' ')