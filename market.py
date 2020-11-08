
print("Now we will calculate your marketing!!\n----------------\nTomatos : 3 NIS/kg" + "\nCucmbers: 2 NIS/kg" + "\nCola : 5 NIS " + "\nChicken  : 20 NIS/kg\n---------------- \n")

Tomatos=input("Enter how many Tomatos : ")
Cucmbers=input("Enter how many  Cucmbers : ")
Cola=input("Enter how many colas : ")
Chicken=input("Enter how many Chickens : ")

print("You have to pay : " + str(int(Tomatos)*3+int(Cucmbers)*2+int(Cola)*5+int(Chicken)*20) +" NIS without tax")
###### כולל מע"מ מספר שלם בלי שאירית#####
print(ג"You have to pay : " + str(int((int(Tomatos)*3+int(Cucmbers)*2+int(Cola)*5+int(Chicken)*20)*1.17))+ " NIS with tax")
###### דוגמה לשתי ספרות אחרי הנקודה #####
print("You have to pay : " + str("%.2f" % ((int(Tomatos)*3+int(Cucmbers)*2+int(Cola)*5+int(Chicken)*20)*1.17))+ " NIS with tax.2field ")
####### דוגמה לשלוש ספרות אחרי הנקודה #####
print("You have to pay : " + str("%.3f" % ((int(Tomatos)*3+int(Cucmbers)*2+int(Cola)*5+int(Chicken)*20)*1.17))+ " NIS with tax.2field ")