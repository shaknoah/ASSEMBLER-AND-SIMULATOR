import  matplotlib.pyplot as plt


isdict = {"00000": "A", "00001": "A", "00110": "A", "01010": "A", "01011": "A", "01100": "A", "00010": "B",
          "01000": "B", "01001": "B", "00011": "C", "00111": "C", "01101": "C", "01110": "C", "00100": "D",
          "00101": "D", "01111": "E", "10000": "E", "10001": "E", "10010": "E", "10011": "F"}
reg_dict = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}
isdict = {"00000": 'A', "00001": "A", "00110": "A", "01010": "A", "01011": "A", "01100": "A", "00010": "B",
          "01000": "B", "01001": "B", "00011": "C", "00111": "C", "01101": "C", "01110": "C", "00100": "D",
          "00101": "D", "01111": "E", "10000": "E", "10001": "E", "10010": "E", "10011": "F"}

regval = {'000': '0000000000000000', '001': '0000000000000000', '010': '0000000000000000', '011': '0000000000000000',
          '100': '0000000000000000', '101': '0000000000000000', '110': '0000000000000000', '111': '0000000000000000'}


def converter(R):
    for k in regval:
        if R == k:
            a = int((regval[k]), 2)
    return a


A = []
B = []
C = []
D = []
E = []
F = []

inparr = []
output = []
giraffe = []
# print(gir)
memadd=[]
kp=0

f = True
while (f):
    inp = input();

    inparr.append(inp)
    output.append(inp)
    if (str(inp[0:5]) == "10011"):
        break

e = len(output)
# gir=[]
# gir=[i for i in range(0,len(inparr))]
# print(gir)
while e + 1 <= 256:
    output.append("0000000000000000")
    e += 1

pc = 0
pcbi = ""
i = 0
aziz = ""
lastflag = ""

graphcounter = 0
while (i < len(inparr)):
    giraffe.append(graphcounter)
    graphcounter=graphcounter+1
    rty = []

    # memadd.append(i)

    re = bin(pc)[2:]
    rt = re.zfill(8)
    pcbi = rt

    for key, value in isdict.items():

        str1 = inparr[i][0:5]
        if (str1 == key):
            if (value == "A"):
                A.append(inparr[i][7:10])
                A.append(inparr[i][10:13])
                A.append(inparr[i][13:16])

            if (value == "B"):
                B.append(inparr[i][5:8])
                B.append(inparr[i][8:16])

            if (value == "C"):
                C.append(inparr[i][10:13])
                C.append(inparr[i][13:16])

            if (value == "D"):
                D.append(inparr[i][5:8])
                D.append(inparr[i][8:16])
            if (value == "E"):
                E.append(inparr[i][8:16])

    opcode = inparr[i][0:5]

    run = ""
    for u in isdict:
        if u == opcode:
            run = isdict[u]

    if run == 'E':
        if opcode == '01111':
            mem = inparr[i][8:]
            me = int((mem), 2)
            memadd.append([i])

            i = me

            continue
        if opcode == '10000':
            if regval['111'][13] == '1':
                mem = inparr[i][8:]
                me = int((mem), 2)
                memadd.append([i])

                i = me

                continue
        if opcode == '10001':
            if regval['111'][14] == '1':
                mem = inparr[i][8:]
                me = int((mem), 2)
                memadd.append([i])

                i = me
                continue
        if opcode == '10010':
            if regval['111'][15] == '1':
                mem = inparr[i][8:]
                me = int((mem), 2)
                memadd.append([i])

                i = me
                continue

    if run == 'A':
        RA = A[0]
        RB = A[1]
        RC = A[2]

        a = converter(RB)
        b = converter(RC)

        ans = 0

        if opcode == '00000':
            ans = a + b
        if opcode == '00001':
            ans = a - b
        if opcode == '00110':
            ans = a * b
        if opcode == '01010':
            ans = a ^ b
        if opcode == '01011':
            ans = (a or b)
        if opcode == '01100':
            ans = (a and b)
        c = bin(int(ans))[2:]
        if len(c) > 16:
            it = ""
            for t in range(0, 16):
                if i != 12:
                    it += regval['111'][t]
                else:
                    it += '1'
            regval['111'] = it
        t = len(c) - 16
        c = c[t:]
        z = c.zfill(16)

        for k in regval:
            if RA == k:
                regval[k] = z

    if run == 'B':
        RA = B[0]  # mov RA
        imm = B[1]  # 00000111
        for k in regval:
            if RA == k:
                ans = regval[k]

        if opcode == '00010':
            z = imm.zfill(16)
        # ls
        if opcode == '01001':
            z1 = int((imm), 2)
            z1 = int((ans), 2) << z1
            c = bin(int(z1))[2:]
            z = c.zfill(16)

        if opcode == '01000':
            z1 = int((imm), 2)

            z1 = int((ans), 2) >> z1

            c = bin(int(z1))[2:]
            z = c.zfill(16)

        for k in regval:
            if RA == k:
                regval[k] = z

    if run == 'C':
        RA = C[0]
        RB = C[1]

        if opcode == '00011':
            for we in regval:
                if RB == '111':
                    ans = lastflag

                elif RB == we:
                    ans = regval[we]
            for wr in regval:
                if RA == wr:
                    regval[wr] = ans

        if opcode == '00111':
            a = converter(RA)
            b = converter(RB)
            z1 = int(a / b)
            c = bin(int(z1))[2:]
            z = c.zfill(16)

            for ty in regval:
                if RA in ty:
                    regval[ty] = z

        if opcode == '01110':
            a = converter(RA)
            b = converter(RB)
            if a > b:
                it = ""
                for q in range(0, 16):
                    if q != 14:
                        it += regval['111'][q]
                    else:
                        it += '1'
                regval['111'] = it
            if a < b:
                it = ""
                for q in range(0, 16):
                    if q != 13:
                        it += regval['111'][q]
                    else:
                        it += '1'
                regval['111'] = it
            if a == b:
                it = ""
                for q in range(0, 16):
                    if q != 15:
                        it += regval['111'][q]
                    else:
                        it += '1'
                regval['111'] = it

        if opcode == '01101':
            for k in regval:
                if RB == k:
                    ans = regval[k]
            c = [char for char in ans]

            for er in range(0, len(c)):
                if (c[er] == "0"):
                    c[er] = "1"
                else:
                    c[er] = "0"

            str = ""
            for y in c:
                str += y

            for gh in regval:
                if RA == gh:
                    regval[gh] = str

    if run == 'D':
        RA = D[0]
        madd = D[1]
        for k in regval:
            if RA == k:
                ans = regval[k]

        # print(ans,'lol')
        if (opcode == '00101'):
            output[int((madd), 2)] = ans


            rty.append(i)
            rty.append(int((madd), 2))




        if (opcode == '00100'):



            for z in regval:
                if RA in z:
                    regval[z] = output[int((madd), 2)]


            rty.append(i)
            rty.append(int((madd), 2))


    aziz += pcbi + " "
    aziz += regval['000'] + " "
    aziz += regval['001'] + " "
    aziz += regval['010'] + " "
    aziz += regval['011'] + " "
    aziz += regval['100'] + " "
    aziz += regval['101'] + " "
    aziz += regval['110'] + " "
    aziz += regval['111'] + " "
    aziz += "\n"
    pc += 1

    lastflag = regval['111']

    regval['111'] = "0000000000000000"
    A.clear()
    B.clear()
    C.clear()
    D.clear()
    E.clear()



    if len(rty)==0:

        memadd.append([i])
        # kp+=1
    else:
        memadd.append(rty)
    i+=1

for sd in range(0, len(output)):
    aziz += output[sd] + "\n"


for xe, ye in zip(giraffe, memadd):
        
        plt.scatter([xe] * len(ye), ye)


print(aziz)
plt.xlabel("cycle")
plt.ylabel("memmoryadd")

plt.show()