import random
msg = 482868688225475437892578967863786783786541679678
msg = "J'adore manger des pommes"
seed = random.randrange(1<<15, (1<<16)-1)

seed1 = random.randrange(1<<24, (1<<25)-1)

seed2 = random.randrange(1<<30, (1<<31)-1)

seed3 = random.randrange(1<<32, (1<<33)-1)

seed4 = random.randrange(1<<38, (1<<39)-1)


def lsfrb(msg):
    global seed
    sl = seed.bit_length()
    for n in range(msg.bit_length()):
        if n >= sl:
            seed = (seed << 1) | ((seed ^ (seed >> sl-5) ^ (seed >> sl-6) ^ (seed >> sl-15) ^ (seed >> sl-16)) & 1)
    return msg ^ (seed >> (seed.bit_length()+1 - msg.bit_length()))

def lsfrb4(msg):
    global seed1,seed2,seed3,seed4
    sl1,sl2,sl3,sl4 = seed1.bit_length(), seed2.bit_length(), seed3.bit_length(), seed4.bit_length()
    for n in range(msg.bit_length()):
        if n >= sl1:
            seed1 = (seed1 << 1) | ((seed1 ^ (seed1 >> sl1-5) ^ (seed1 >> sl1-13) ^ (seed1 >> sl1-17) ^ (seed1 >> sl1-25)) & 1)
        if n >= sl2:
            seed2 = (seed2 << 1) | ((seed2 ^ (seed2 >> sl2-7) ^ (seed2 >> sl2-15) ^ (seed2 >> sl2-19) ^ (seed2 >> sl2-31)) & 1)
        if n >= sl3:
            seed3 = (seed3 << 1) | ((seed3 ^ (seed3 >> sl3-5) ^ (seed3 >> sl3-9) ^ (seed3 >> sl3-29) ^ (seed3 >> sl3-33)) & 1)
        if n >= sl4:
            seed4 = (seed4 << 1) | ((seed4 ^ (seed4 >> sl4-3) ^ (seed4 >> sl4-11) ^ (seed4 >> sl4-35) ^ (seed4 >> sl4-39)) & 1)
    return (msg ^ 
            (seed1 >> (seed1.bit_length()+1 - msg.bit_length())) ^ 
            (seed2 >> (seed2.bit_length()+1 - msg.bit_length())) ^
            (seed3 >> (seed3.bit_length()+1 - msg.bit_length())) ^ 
            (seed4 >> (seed4.bit_length()+1 - msg.bit_length())))

def text2binary(text):
    return int.from_bytes(text.encode(), "big")

def binary2text(integ):
    return integ.to_bytes(integ.bit_length(), "big").decode()



print('message :', msg, " code : ", text2binary(msg))
msg = text2binary(msg)
newmsg = lsfrb4(msg)
print("cryptage : ",newmsg)
print("decryptage : ",binary2text(lsfrb4(newmsg)))



