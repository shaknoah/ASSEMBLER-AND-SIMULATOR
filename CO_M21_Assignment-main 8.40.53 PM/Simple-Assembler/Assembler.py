reg_dict = {'R0': '000', 'R1': '001', 'R2': '010', 'R3': '011', 'R4': '100', 'R5': '101', 'R6': '110', 'FLAGS': '111'}
isa_dictA = {"add": "00000", "sub": "00001", "mul": "00110", "xor": "01010", "or": "01011", "and": "01100"}
isa_dictB = {"mov": "00010", "rs": "01000", "ls": "01001"}
isa_dictC = {"mov": "00011", "div": "00111", "not": "01101", "cmp": "01110"}
isa_dictD = {"ld": "00100", "st": "00101"}
isa_dictE = {"jmp": "01111", "jlt": "10000", "jgt": "10001", "je": "10010"}
isa_dictF = {"hlt": "10011"}
head_dict = {"A": isa_dictA, "B": isa_dictB, "C": isa_dictC, "D": isa_dictD, "E": isa_dictE, "F": isa_dictF}
cmd = ["add", "sub", "mov", "mov", "ld", "st", "mul", "div", "rs", "ls", "xor", "or", "and", "not", "cmp", "jmp", "jlt","jgt", "je", "hlt"]

allins=[]

while True:
    try:
        inp = input()

        if(inp==""):
            allins.append(inp)
            break
        t=inp.split(" ")

        if t[len(t)-1]=="hlt":
            allins.append(inp)
            break
        allins.append(inp)



    except EOFError:
        break

check=False
for i in allins:
    if "hlt" in i:
        check=True





def fw(lcount):
    for i in range(0,len(lcount)):
        lcount[i]+=1
lcount=[]
lcount.append(2)


linecount = 1

count=0

finalans=[]

while (count<=len(allins)-1):

    if(check==False):
        break


  

    userinput = allins[count]
    count+=1

   






    arr = userinput.split(" ")
    if ":" in str(arr[0]):
        arr.pop(0)

    arr1 = []
    if "var" in str(arr):
        continue

    if (len(arr) == 4):
        for key in isa_dictA:
            if arr[0] == key:
                arr1.append(isa_dictA[key]);

        arr1.append("00")

        for i in range(1, len(arr)):
            for key, value in reg_dict.items():
                if (arr[i] == key):
                    arr1.append(value)

        ans = ""
        for ele in arr1:
            ans += ele
        finalans.append(ans)

    #
    if (len(arr) == 3):
        
        if "$" in str(arr[2]):
            for key in isa_dictB:
                if arr[0] == key:
                    arr1.append(isa_dictB[key]);

            for i in range(1, len(arr)):
                for key, value in reg_dict.items():
                    if (arr[i] == key):
                        arr1.append(value)

            a = arr[2][1:]  
            if(a.isnumeric()):

                c = bin(int(a))[2:]
                z = c.zfill(8)
                arr1.append(z)
            ans = ""
            for ele in arr1:
                ans += ele
            finalans.append(ans)


  

           
    if (len(arr) == 3):
        if "$" not in str(arr[2]):
            arrel = arr[len(arr) - 1]
            if (
                    arrel == "R0" or arrel == "R1" or arrel == "R1" or arrel == "R2" or arrel == "R3" or arrel == "R4" or arrel == "R5" or arrel == "R6" or arrel == "FLAGS"):
                for key, value in isa_dictC.items():
                    if (key == arr[0]):
                        arr1.append(value)

                arr1.append("00000")

                for i in range(1, len(arr)):
                    for key, value in reg_dict.items():
                        if (arr[i] == key):
                            arr1.append(value)

                ans = ""
                for ele in arr1:
                    ans += ele
                
                finalans.append(ans)


            else:

                for key in isa_dictD:
                    if arr[0] == key:
                        arr1.append(isa_dictD[key])

                for i in range(1, len(arr)):
                    for key, value in reg_dict.items():
                        if (arr[i] == key):
                            arr1.append(value)


                a = lcount[0]+1
                c = bin(int(a))[2:]
                z = c.zfill(8)
                arr1.append(z)
                ans = ""
                for ele in arr1:
                    ans += ele

                finalans.append(ans)

                    


    if (len(arr) == 2):


        if(arr[0]=='var'):
           
            lcount.append(2)
        

        for key, value in isa_dictE.items():
            if (arr[0] == key):
                arr1.append(value)

        arr1.append("000")
        
        a = arr[1]
        c = bin(int(linecount))[2:]
        z = c.zfill(8)
        arr1.append(z)
        ans = ""
        for ele in arr1:
            ans += ele
        # print(ans)
        finalans.append(ans)

    map(fw,lcount)
    linecount += 1

    # print(count)

    if arr[len(arr)-1] == "hlt":
        
        r="1001100000000000"
        finalans.append(r)



if "hlt" not in allins[len(allins)-1]:
    print("General Syntax Error")

else:


    t=True
    for i in range(0,len(finalans)):
        if (len(finalans[i]) < 16):
            print("General Syntax Error")
            t=False
            break


    for i in range(0,len(finalans)):
        if(t):
            print(finalans[i])