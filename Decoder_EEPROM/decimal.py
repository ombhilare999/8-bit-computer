import binascii
f = open("TEST","r")

byte = [0x7E, 0x30, 0x6D, 0x79, 0x33, 0x5B, 0x5F, 0x71, 0x7F, 0x7B]
counter = 0 

for i in range(256):
    print("%x%x%x\t" % (byte[((i//100) % 10)] , byte[((i//10) % 10)] , byte[i%10]), end = "")
    counter += 1
    if counter == 8:
        print("\n", end = "")
        counter = 0 

print(f.read())