
'''
num=4567
Alafim=4
Meot=5
Asarot=6
Ahadot=7
'''

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
