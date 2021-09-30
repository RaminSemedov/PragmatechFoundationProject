##Hər hansı bir natural n ədədini götürək. Onu növbəti şəkildə dəyişdirəcəyik:
##Əgər ədəd cütdürsə, onda onu 2-ə bölək, əgər təkdirsə ona 1 əlavə edək.
##Bir neçə belə dəyişmədən sonra həmişə 1 alacağıq. Məsələn, 11 ədədindən 12 ədədi alınır, sonra 6, 3, 4, 2 və sonda 1.
##Beləliklə, 11-dən 1 almaq üçün 6 dəyişiklik etmək lazımdır.
##Verilmiş natural ədədə görə 1 alınana qədər onun dəyişmələrinin sayını tapın.

def changeNumber(n):
    counter=0
    while(n!=1):
        if(n%2==0):
            n/=2
            counter+=1
        else:
            counter+=1
            n-=1        
    return counter
#print(changeNumber(4))

#============================================================================================================================

##n natural ədədi verilmişdir. Əgər n ədədi hər hansı bir m natural ədədinin kvadratıdırsa,
##onda m ədədini çap edin, əks halda No çap edin.
##Məsələn: User 25 daxil etsə ekrana 5 verilsin 27 daxil etsə, NO yazılsın
def checkNumber(n):
    
    for i in range(0,int(n/2)+1):
        if(i**2==n):
            return i
        
    return 'NO'                
        
          
       
        
#print(checkNumber(49))

#===========================================================================================================================

###User bir ədəd daxil etsin həmin ədədə qədər bütün ədədləri çapa verin.

def printAllNumbers(n):
    for i in range(n):
        print(i,end=' ')
        
#printAllNumbers(7)

#===========================================================================================================================
        
### İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin.
    
stng='İnternetdən bir mətni bir dəyişkəndə saxlayın. Həmin mətnin cüt indexlərində olan simvolları bir sətirdə çapa verin.'
def printEvens(a):
    

    for i in range(len(a)):
        if(i%2==0):
            print(a[i],end='')

#printEvens(stng)
            
#===========================================================================================================================
            
### Random bir rəqəm götürsün proqram 1-4 aralığında. İstifadəçidən həmin rəqəmi təxmin etməyi istəyin.
### Hər doğru təxmin etdikcə istifadəçi bir xal qazansın.
### 5 xala çatanda istifadəçinin 5 xala çatması üçün etdiyi cəhdlərin sayını çapa verin.
import random
attempts=0
points=0

def findNumber(a,p):
    while(p!=5):
        rand=random.randrange(0,5)
        num=int(input('Enter number 1-4: '))
        if(num>0 and num<5):
            a+=1
            if(num==rand):
                p+=1
                print('You win 1 point')
        else:
            print('Wrong number')
            return None
        
    print(f'You win game with {a} attempts')

#findNumber(attempts,points)
    
#==========================================================================================================================

###Userdən daxil etmısini tələb edin. 1-dən sonra gələn ən kiçik bölünəni çapa verin.
def theSmallestDevider():
    n=int(input("Enter a number:  "))
    for i in range(2,n):
        if(n%i==0):
            return i
                
        

#print(theSmallestDevider())
        
#==========================================================================================================================
### Masa üzərində n sikkə var. Onların bəzilərinin reşka (1) üzü, bəzilərinin isə gerb( 0) üzü yuxarıdır.
### Bütün sikkələrin eyni üzlərinin yuxarı olması üçün çevriləcək sikkələrin minimal sayını tapın.
### İstifadəçi birinci inputda sikkələrin sayını daxil edir.
### O daxil etdiyi sayda siz userdən sikkələrin hansı üzdə düşdüyünü soruşmalısız.
### Bütün üzləri daxil etdikdən sora siz bütün sikkələri eyni üzə çevirmək üçün ən minumum sayı tapmalısız.
### Məsələn birinci inputda sikkələrin sayını user 5 daxil edib.
### Ardınca 5 sikkənin hər birinin üzünü daxil edir. 1, 0, 0, 1, 0.
### Bu sikkələrin üzünü bir etmək üçün iki yolumuz var: ya hamısını 0 ya da hamısını 1 etməliyik.
### 1-ləri 0 etmək daha qısa yoldur, çünki onların sayı azdır.
### Bu səbəbdən edəcəyimiz minimal hərəkət sayı ikidir. Əgər 0 və 1 eyni sayda olarsa, EQUAL çapa verin.

def invertCoin():
    upSide=0
    downSide=0
    coins=[]
    try:
        coinSize=int(input(f'Enter coin size:  '))
        for i in range(coinSize):
            coinSide=input(f'Enter coin side 1 or 0:  ')
            if(coinSide=='0' or coinSide=='1'):
                coins.append(coinSide)
            else:
                print('You entered a wrong data')
                return None
            if(coinSide=='1'):
                upSide+=1
            elif(coinSide=='0') :
                downSide+=1
                
                
        if(upSide>downSide):
            for i in range(coinSize):
                if(coins[i]=='0'):
                    coins[i]='1'
                                 
                
               
                    
        elif(upSide<downSide):
            for i in range(coinSize):
                if(coins[i]=='1'):
                    coins[i]=='0'
            
                    
        else:
            print('Equal')
    
   
    
   
    
    except ValueError:
        print('You entered a wrong data')
    
    if(len(coins)!=0):
        print(coins)
        
    
    
    

#invertCoin()
    

        
    
    
    
        
    
#==============================================================================================================
        
### Userdən bir ədəd daxil etməsini tələb edin. Ekrana həmin ədəddəki ədədlərin hasilini çapa verin.

def multiNum():
    num=int(input("Enter a number: "))
    mul=1
    for i in range(1,num):
        num*=i
    
    return num
    
        
            
#print(multiNum())

#=======================================================================================================================

###Kvadrat tənliyin əmsallarını daxil etsin user. Həmin əmsallara görə tənliyin köklərini daxil edin.
import math

def tenlikKokuTap():
    a=int(input('a emsalini daxil ele: '))
    b=int(input('b emsalini daxil ele: '))
    c=int(input('c emsali daxil ele: '))
    x1=0
    x2=0
    
    D=b**2-4*a*c
    print(f"D= {D}")
    
    if(D>0):
        x1=(-b+math.sqrt(b**2-4*a*c))/2*a
        x2=(-b-math.sqrt(b**2-4*a*c))/2*a
    elif(D==0):
        x1=-b/2*a
        x2=x1
    print(x1)
    print(x2)
    

#tenlikKokuTap()
    
#=========================================================================================================================

## 1-50 arasında ədədlərdən 3-ə bölünən ədədlərə three, 5-ə bölünən ədədlərə five,
## həm 3 və həm də 5-ə bölünənlərə isə ThreeFive print edin.
## Əgər heç birinə bölünməsə sadəcə ədədin özünü çapa verin.
    
def getNumber(n):
    listThree=[]
    listFive=[]
    listThreeFive=[]
    listNone=[]
    for i in range(n):
        if(i%3==0):
            listThree.append(i)
        if(i%5==0):
            listFive.append(i)
        if(i%3==0 and i%5==0):
            listThreeFive.append(i)
        if(i%3!=0 and i%5!=0):
            listNone.append(i)

    print(f'Three {listThree}')
    print(f'Five {listFive}')
    print(f'ThreeFive {listThreeFive}')
    print(f'None {listNone}')



#getNumber(100)
            
        
        
        
    
            
        


      
    

    
            
    
















