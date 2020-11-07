
'''
num=4567
Alafim=4
Meot=5
Asarot=6
Ahadot=7
'''
######This is my solution######
num=4567

print("My num is:" + str(num))

Alafim=num//1000

print("Alafim is: " +str(Alafim))

Meot=(num-(Alafim*1000))//100

print("Meot is: " +str(Meot))

Asarot=((num-(Alafim*1000))-Meot*100)//10
print("Asarot is: " +str(Asarot))

Ahadot=((num-(Alafim*1000))-Meot*100)%10
print("Ahadot is: " +str(Ahadot))


#######This is Idan's solution ! ########


num1=4567

print("Alafimm " + str(num1//1000))

print("Meoott " +str((num1%1000)//100))

print("Asarott " +str((num1%100)//10))

print("Ahadott " +str(num1%10))

##### input ###

num1=int(input("Enter a number with 4 digits: "))

print("Alafimm " + str(num1//1000))

print("Meoott " +str((num1%1000)//100))

print("Asarott " +str((num1%100)//10))

print("Ahadott " +str(num1%10))

