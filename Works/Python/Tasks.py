#str daxilində neçə hərf olduğunu ekrana yazdırın
a='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
spaceCounter=0
lst=a.split()
for c in lst:
    spaceCounter+=len(c)     
    
#print(spaceCounter)



#str daxilində neçə sait və neçə samit olduğunu ekrana çap edin
st='Proqramalaşdırma nə qədər çox şey bildiyinizlə yox, bildiyinizlə ortaya çıxardığınız işlərlə maraqlanır'
sait='aouie'
samit='bcdrtfsdwklp'
saitSayi=0
samitSayi=0

for herf in st:
    for h in sait:
        if herf==h:
            saitSayi+=1
    for n in samit:
        if(herf==n):
            samitSayi+=1

#print(saitSayi)
#print(samitSayi)
            
#str daxilində son iki sözü silən metod yazın
def removeLastTwoLetters():
    lst=st.split()
    newStr=''
    for s in range(2):
        lst.pop(len(lst)-1)
    for i in lst:
        newStr+=i+' '        
        
    return newStr


#print(removeLastTwoLetters())

##str ni vergülə görə ayırıb iki string halına gətirin

spl=st.split(',')
firstString=spl[0]
secondString=spl[1]

##stringSearch(word) adında bir metod yazın. daxil edilən sözün mətnin içində olub olmadığını ekrana çap edən metod yazın

def stringSearch(word):
    flag=0;
    spl=st.split()
    for s in spl:
        if word==s:
            flag=1
            
    if flag==1:
          print(f'"{word}" sozu metnin daxilinda var')
    else: print(f'"{word}" sozu metnin daxilinda yoxdur')

    
#stringSearch('ortaya')
    
#Ədədlər arasında rəqəmlərinin cəmi ən böyük olan ədədi tapın
nums=[1,22,33,567,34,221]
sumNum=[]
max=nums[0]

for num in nums:
    sum=0
    for h in str(num):
        sum+=int(h)
    sumNum.append(sum)


for n in sumNum:
    if n>max:
      max=n
    
#print(sumNum)
#print(max)
      
### Ədədlərin kvadratlarının olduğu yeni bir massiv yaradan metod yazın
      
newList=[]
for n in nums:
    newList.append(n**2)
        
#print(newList)
    
### Tək ədədlərin cəmini tapan metod yazın ###
    
def sumEvens(lst):
    sum=0
    for l in lst:
        if l%2==1:
            sum+=l
    
    return sum
    
    
#sumEvens(nums)

###Daxilində 3 rəqəmi olan neçə ədəd olduğunu ekrana çap edən metod yazın

def printThreeNum(arr):
    sum=0
    for num in arr:
        if num>99 and num <1001:
            sum+=1    
    
    print(sum)
        
#printThreeNum(nums)
    
    
### Tək ədədləri ayıraraq ayrıca bir massivə yığan metod yazın ###
    
newLst=[]
for l in nums:
    if l%2==1:
        newLst.append(l)
    
#print(newLst)








    







