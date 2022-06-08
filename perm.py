import os, shutil

def mode2value(perm:int)->int:
    octal = str(perm)
    digits = [
        int(octal[0]),
        int(octal[1]),
        int(octal[2])
    ]
    mode = 0
    index = 256

    for digit in digits:
        temp = str(bin(digit))
        tempy = []
        dindex = 0
        for i in temp:
            tempy.append(temp[dindex])
            dindex = dindex+1
        
        tempy = tempy[2:]
        
        while len(tempy)<3:
            tempy = ['0'] + tempy

        for i in tempy:
            if i == '1':
                mode = mode + index
            index = index / 2
    
    return int(mode)

def chmod(path, perm):
    os.chmod(path, mode2value(perm))