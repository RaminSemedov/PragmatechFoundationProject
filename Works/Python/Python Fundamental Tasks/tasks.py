# 1.Kvadrat yaratmaq olarsa daxil edilən 4 ədəddən, ekrana kvadratın sahəsini, olmazsa, həmin ədədlərin cəmini verin.

# def getArea(side1, side2, side3, side4):
#     if(side1 == side2 and side2 == side3 and side3 == side4):
#         return side1*side2
#     else:
#         return side1+side2+side3+side4


# side1 = int(input("Enter side1: "))
# side2 = int(input("Enter side2: "))
# side3 = int(input("Enter side3: "))
# side4 = int(input("Enter side4: "))

# print(getArea(side1, side2, side3, side4))
# ==========================================================================================================================

# 2. Dörd ədəd daxil edin. Onlardan ən böyüyünü çapa verin.

# def getGraeterNumber(*params):
#     num = params[0]
#     for i in params:
#         if i > num:
#             num = i
#     return num


# num1 = int(input("Enter side1: "))
# num2 = int(input("Enter side2: "))
# num3 = int(input("Enter side3: "))
# num4 = int(input("Enter side4: "))

# print(getGraeterNumber(num1, num2, num3, num4))
# ====================================================================================================================


# 3.Proqram run olunanda, istifadəçiyə meyvələr menyusu təqdim olunsun.
# Userdən menyunuzdakı meyvələrdən birinin adını daxil etməsini tələb edin və ekrana meyvənin qiymətini yazdırın.
#  (İstədiyiniz qiyməti yazdırın).
# Əgər menyuda olmayan meyvə daxil edilsə, ekrana error mesajı verin.

# fruits = {
#     'alma': '1 azn',
#     'armud': '2azn',
#     'nar': '3azn',
#     'banan': '1.5 azn'
# }


# def showFruitPrice(fruit):
#     return fruits.get(fruit.lower(), 'There is no shuch as fruit')


# print('''
# 1.Alma
# 2.Armud
# 3.Nar
# 4.Banan
# ''')

# f = input("Enter your fruit name: ")

# print(showFruitPrice(f))

# =====================================================================================================================

# 4. Qeydiyyat formu düzəldin. İstifadəçi adını daxil etsin. Adın uzunlu 3-dən kiçik 11-dən böyük ola bilməz.
# Əgər adını düzgün daxil edərsə, soyadının daxil etməsini istəyin. Soyad 5 hərfdən kiçik, 15 hərfdən uzun olmasın.
# Əgər soyad düzgün daxil edilsə, Daha sonra doğulduğu ili daxil etsin. Doğum ilinin uzunluğu 4 simvoldan ibarət olmalıdır.
# Sonra email daxil etməsini tələb edin. Emailin uzunluğu 10 hərifdən qısa 22 hərfdən uzzun olmasın, tərkibində @gmail.com olsun
# və bu hissə daxil etdiyi emailin sonunda olsun. Ardınca parol axil etsin. Parol 6-13 simvol aralığında olmalıdır.
# Sonra parolu təsdiqləməyini tələb edin. Təsdiqlədiyi parol birinci yazdığı parol ilə eyni olmalıdır.
# Bütün bunlar düzgün daxil edilərsə, Qeydiyyat tamamlandı mesajı verilsin və istifadəçidən qeydiyyatın detallarına baxmaq
# istəyib-istəməməsi soruşulsun. Əgər hə desə, aşağıdakı görüntü çapa verilsin:
# (Qeyd: Yuxarıda sizin verdiyiniz şərtlərə uyğun istifadəçi input daxil etmsəsə, hər verdiyibiz şərtə uyğun error tipli
# mesaj verin. Məsələn doğum ilini 5 simvoldan ibarət daxil etsə, mesaj verilsin ki 4 simvol daxil edin.
# Yəni hər şərti müvafiq mesajlar ilə userə izah edin.
# ================ Ad: Murad Soyad: Əliyev Yaş: 22 Email: muradaliyev1996@gmail.com Parol: 123456789 ===================
# Əgər yox desə, Murad Əliyev, Uğurlar! Yazılsın.


# while(True):
#     print('''1.Register
# 2.Exit''')

#     choice=input("Enter your choice! : ")
#     if choice=='1':
#         name=input("Enter your name: ")
#         if(len(name)>3 and len(name)<11):
#             surname=input("Enter your surname: ")
#             if len(surname)>5 and len(surname)<15:
#                 date=input("Enter date of birth: ")
#                 if(int(date)>1900 and int(date)<2020):
#                     email=input('Enter your e-mail: ')
#                     if(len(email)>10 and len(email)<22 and email.find('@gmail.com')!=-1):
#                         password=input('Enter password: ')
#                         if(len(password)>6 and len(password)<13):
#                             c=input("Confirm your password: ")
#                             if(c==password):
#                                 while(True):
#                                     s=input('''Registration is complited.  1.Show information  2. Exit : ''')
#                                     if(s=='1'):
#                                         age=2021-int(date)
#                                         print('===========Name {} , Surname {}, age {}, email {} ==========='.format(name,surname,age,email))

#                                     elif s=='2':
#                                         print("Good luck: {} {}".format(name, surname))
#                                         break
#                                     else:
#                                         print('Enter right number ')
#                             else:
#                                 print("Confirmed password must be the same with the main password")

#                         else:
#                             print("Password length must be between 6 and 13")
#                     else:
#                         print('Email length must be between 10 and 22  and it must has @gmail.com')
#                 else:
#                     print("Date of bith must be between 1900 and 2020")
#             else:
#                 print('Surname length must be between 5 and 15')

#         else:
#             print("Name length must be between 3 and 11")


#     elif choice=='2':
#         print("Good luck")
#         break
#     else:
#         print("Enter right choice")


# =====================================================================================================================

# 5.Listin elementlerini toplayan alqoritm yazin. Sum funksiyasindan istifade etmeyin.

# def sumListElelements(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum


# l = [1, 2, 3, 4, 5]

# print(sumListElelements(l))

# ====================================================================================================================


# 6.Listin en boyuk elementini max funksiyasini istifade etmededen tapan alqoritm yazin.

# def getMaxListNum(list):
#     max = list[0]
#     for l in list:
#         if l > max:
#             max = l
#     return max


# l = [1, 32, 3, -4, 5]

# print(getMaxListNum(l))

# ====================================================================================================================

# 7.Listin en kicik elementini min funksiyasini istifade etmededen tapan alqoritm yazin.
# def getMinListNum(list):
#     min = list[0]
#     for l in list:
#         if l < min:
#             min = l
#     return min


# l = [1, -32, 3, -4, 5]

# print(getMinListNum(l))

# ====================================================================================================================

# 8. Write a Python program to count the number of strings where the string length is 2 or more and
#  the first and last character are same from a given list of strings.
#  Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

# def stringCounter(stringList):
#     counter = 0
#     if(len(stringList) >= 2):
#         for s in stringList:
#             if(s[0] == s[len(s)-1]):
#                 counter += 1
#     return counter


# sList = ['aba', 'se', '1221', 'djkhhkjhd', '12ds1']
# print(stringCounter(sList))

# ====================================================================================================================

# 9.Write a Python program to check a list is empty or not.

# def chechList(list):
#     if len(list) == 0:
#         print("List is empty")
#     else:
#         print("list is nor empty")


# chechList([1, 2, 3])

# ====================================================================================================================

# 10. #my_text = “Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of strings.”
# my_text stringindeki sozler
# elifba sirasi ile duzub string formatinda ekrana yazdirin.

# text='Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.'


# def changeString(text):
#     textLower=text.lower()
#     textList=textLower.split(' ')
#     textList.sort()
#     for  s  in textList:
#         print(s,end=' ')

# changeString(text)

# ====================================================================================================================

# 11. Write a Python program to select the odd items of a list.

# def selectOddNum(list):
#     newList = []
#     for l in list:
#         if l % 2 == 0:
#             newList.append(l)
#     return newList


# print(selectOddNum([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))

# ====================================================================================================================

# 12. Write a Python function to sum all the numbers in a list.

# def sumListNumbers(list):
#     num = 0
#     for i in list:
#         num += i
#     return num


# print(sumListNumbers([1, 2, 3, 54, 8, 5]))

# ====================================================================================================================

# 13. Write a Python function to multiply all the numbers in a list.

# def mulListNumbers(list):
#     num = 1
#     for i in list:
#         num *= i
#     return num


# print(mulListNumbers([8, 2, 3, -1, 7]))

# ====================================================================================================================

# 14.Write a function called returnDay. This function takes in one parameter ( a number from 1-7) and
#  returns the day of the week ( 1 is Sunday, 2 is Monday etc.).
# If the number is less than 1 or greater than 7, the function should return None.

# days = {
#     1: 'Sunday',
#     2: 'Monday',
#     3: 'Tuesday',
#     4: 'Wednesday',
#     5: 'Thursday',
#     6: 'Fryday',
#     7: 'Saturday'
# }


# def showDay(day):
#     print(days.get(day, None))


# showDay(1)
