# Written By: Hannah Lormenyo
# 8th Ocotber 2018 

import re

def question(instring):
    if instring.count("?") < 3:
        return False
    else:
        pos = re.findall(r"\d", instring)
        pair = [(i,pos[pos.index(i)+1]) for i in pos[0:len(pos)-1] if int(i) + int(pos[pos.index(i)+1]) == 10 ]
        for i in range(len(pair)):
            if instring[instring.index(pair[i][0]): instring.index(pair[i][1])].count("?") == 3:
                return True
            else:
                return False

print(question("arrb6???4xxb15???eee5"))
print(question("acc?7??sss?3rr1??????5"))
print(question("5??aaaaaaaaaaaa?5?5"))
print(question("9???1???9???1???9"))
print(question("aa6?9")) 
