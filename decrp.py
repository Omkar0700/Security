x=input("please enter string for decryption: ")
def decrypt(x,v):
    result=""
    for i in x:
        if (i.isupper()):
            result+=chr((ord(i)-v-65)%26+65)
        elif(i.islower()):
            result+=chr((ord(i)-v-97)%26+97)
        else:
            result+=chr((ord(i)-v-48)%10+48)

    return print(f"Decrypted text:{result}")

for i in range (1,27):
    decrypt(x,i)