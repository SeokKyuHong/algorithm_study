import sys
sys.stdin = open("/Users/seokkyuhong/dev/python/algorithm/input.txt","r")

sys.setrecursionlimit(10**6)

def append_star(LEN):
    if LEN == 1:
        return ['*']
    
    Stars = append_star(LEN//3) 
    L = []  
    
    for S in Stars:
        L.append(S*3)
    for S in Stars:
        L.append(S+' '*(LEN//3)+S)
    for S in Stars:
        L.append(S*3)

    return L

n = int(sys.stdin.readline())

print('\n'.join(append_star(n)))

