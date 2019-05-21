import re
import sys

def main():
    clauses = []
    with open('demo.in.txt', errors = 'ignore') as input_file:
        for i, line in enumerate(input_file):
            line = re.sub(r'\n', '', line)
            line = re.sub(r'[ \t]+$', '', line)
            #print(line)
            cl = []
            for c in line.split(" "):
                cl.append(c)
            clauses.append(cl)

    toProve = clauses[-1]
    del clauses[-1]

    for c in range(len(toProve)):
        if '~' in toProve[c]:
            toProve[c] = re.sub(r'~', '', toProve[c])
        else:
            toProve[c] = '~' + toProve[c]


    for c in toProve:
        clauses.append([c])
    
    # print(clauses[3], clauses[1])
    # print(resolve(clauses[3], clauses[1]))
    count = 0
    #print("L",len(clauses))

    cli = 0
    endFlag1 = False
    while endFlag1 == False:
        if cli == len(clauses):
            endFlag1 = True
            break
        cli = count
        endFlag2 = False
        count += 1
        #print("Cli", cli)
        i = 0
        #print(count)
        while endFlag2 == False:
            if i == cli or cli == 0:
                endFlag2 = True
                break
            clj = i
            #print("Clj", clj)
            if cli == 9 or clj == 8:
                print("Hello========================== Cli", cli, clj)
            i += 1
            result = resolve(clauses[cli], clauses[clj], clauses)
            if result is False:
                #print(clauses)
                print("Contrdiction", '{',cli+1, clj+1,'}')
                #print(clauses[cli])
                #print(clauses[clj])
                sys.exit(0)
            elif result is True:
                continue
            else:
                print(result,'{',cli+1, clj+1,'}')
                clauses.append(result)

    
def resolve(c1, c2, clauses):
    resolved2 = c1 + c2
    resolved = None
    hashmap = {}
    for r1 in resolved2:
        if r1 not in hashmap.keys():
            hashmap[r1] = 0

    resolved = list(hashmap.keys())
    ors = list(hashmap.keys())
    for l1 in c1:
        for l2 in c2:
            if neg(l1, l2):
                resolved.remove(l1)
                resolved.remove(l2)
                if len(resolved) is 0:
                    return False
                elif impTrue(resolved):
                    #print("True", c1, c2)
                    return True
                else:
                    for cl in clauses:
                        if Diff(resolved, cl) == []:
                            #print(resolved, c1)
                            return True
                    return resolved

    if resolved == ors:
        return True
    

def neg(l1, l2):
    if l1 == ('~' + l2) or l2 == ('~' + l1):
        return True
    else:
        return False

def impTrue(resolved):
    for r1 in resolved:
        for r2 in resolved:
            if neg(r1, r2):
                return True
    return False

def Diff(li1, li2): 
    li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2] 
    return li_dif 

if __name__ == "__main__":
    main()