import re
import sys


def main():
    clauseNumber = 1
    clauses = []
    with open(sys.argv[1], errors='ignore') as input_file:
        for i, line in enumerate(input_file):
            line = re.sub(r'\n', '', line)
            line = re.sub(r'[ \t]+$', '', line)
            cl = []
            for c in line.split(" "):
                cl.append(c)
            clauses.append(cl)

    toProve = clauses[-1]
    del clauses[-1]

    for cl in clauses:
        print(clauseNumber, ". ", ' '.join(cl), " { }", sep='')
        clauseNumber += 1

    for c in range(len(toProve)):
        if '~' in toProve[c]:
            toProve[c] = re.sub(r'~', '', toProve[c])
        else:
            toProve[c] = '~' + toProve[c]

    for c in toProve:
        clauses.append([c])
        print(clauseNumber, ". ", ' '.join([c]), " { }", sep='')
        clauseNumber += 1


    cli = 1
    while cli < clauseNumber - 1:
        clj = 0
        while clj < cli:
            #print("testing",cli, clj)
            result = resolve(clauses[cli], clauses[clj], clauses)
            if result is False:
                print(clauseNumber, ". ","Contradiction", ' {', cli + 1, ", ", clj + 1, '}', sep='')
                clauseNumber += 1
                print("Valid")
                sys.exit(0)
            elif result is True:
                clj += 1
                continue
            else:
                print(clauseNumber, ". ",' '.join(result), ' {', cli + 1, ", ", clj + 1, '}', sep='')
                clauseNumber += 1
                clauses.append(result)
            clj += 1
        cli += 1
    print('Not Valid')


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
                    return True
                else:
                    for cl in clauses:
                        if Diff(resolved, cl) == []:
                            # print(resolved, c1)
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

def printFunc(cl, i1, i2):
    for c in cl:
        print()


if __name__ == "__main__":
    main()

