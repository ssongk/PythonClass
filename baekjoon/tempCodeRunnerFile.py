                if len(listB)>len(listC):
                    next = 'AB'
        except:
            if len(listC)==0:
                next = 'AB'
            elif len(listB)==0:
                next = 'AC'
        
        try:
            if next == 'AB':
                print(f'{listA.pop(0)}{listB.pop(0)}',end=' ')
                next = 'AC'
        except:
            if len(listA)==0:
                next = 'BC'
            elif len(listB)==0:
                next = 'AC'
            
        try:       
            if next == 'AC':
                print(f'{listA.pop(0)}{listC.pop(0)}',end=' ')
                next = 'BC'
        except:
            if len(listA)==0:
                next = 'BC'
            elif len(listC)==0:
                next = 'AB' 