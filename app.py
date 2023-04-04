"""
INTERPRETERANDE SPRÅK = ingen kompilering i förtid
"script"
"""

while True:
    namn = input("Vad heter du?")
    # strlen
    l = len(namn)
    if l > 1:
        break
    print("Skriv in lite längre tack")

i = i  + 1 

namn = namn.upper()
namn = namn.replace("läxa", "****")
namn = namn.replace("grönsaker", "****")

# if namn.find("läxa") != -1:
#     print("Fult ord")

print(f"Ditt namn börjar på {namn[0]}")

print("ccc")    



n = "S"
n += "tefan"

n = n * 10
print(n)

y = 0.1   #0.0999999998
y = 12.12343
y = y + 12




if y + y + y == 0.3:
    print("Hej")

#pr
# 
# x =int("Vad heter du?")
# 'citat "r3wr4"  dwsad'
namn = input('Vad heter du')
age = input("Hur gammal är du?")
age = int(age)
age = age + 1
namn = 1234
print(f"Hej {namn} kul att du är {age} år")





namn = "Stefan"
namn = namn + " Holmberg"
age = 12
age = age + 1

# Hej Stefan Holmberg kul att du är 13 år

print("Hej " + namn + " kul att du är " + str(age) + " år")
print(f"Hej {namn} kul att du är {age} år")






