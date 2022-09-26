inputa = input('Write Text want to encrypt: ')
inputa = inputa.lower()
output = []

abclist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
codelist = ['000000' , '000001', 
'000010', '000011',
 '000100', '000101', '000110', '000111',
 '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111',
 '010000', '010001', '010010', '010011', '010100', '010101', '010110', '010111', '011000', '011001']

for character in inputa:
        inds = abclist.index(character)
        enout = codelist[inds]
        output.append(enout)



    
print ("Encrypted code is: " , output) 
decrpt = []

inputabc = input('Do you want to decrypt this? Y/N')
if (inputabc=="y"):
        for item in output:
                itemindex = codelist.index(item)
                des = abclist[itemindex]
                decrpt.append(des)
        print("Text after decryptin is: " , str(decrpt))
