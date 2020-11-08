
a='''

my name is: adham
age :30
i live in beit jann

'''

print(a)

##format

print("p1={},p2={},p3={},p4={red}" .format(1,1.0,"adham",red="bbfd"))
#true/false
print("adham" in "adham sweid")

a="adham sweid"
print("adham" in a)

#תדפיס לי את תו מסםר 0
s1="ABCDEFG"
print((s1)[0])
print((s1)[-1])
#לא כולל ה -1
print((s1)[1:-1])
#תביא לי עד הסוף
print((s1)[1:])
# תביא לי הכל
print((s1)[:])
#קפיצות של 2
print((s1)[::2])
print((s1)[2::2])
#מדפיס מילה בסדר הפוך שלה
print((s1)[::-1])
