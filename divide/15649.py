n, m = map(int, input().split())
arr = []
def main():
    
    if m == len(arr):
        print(' '.join(map(str, arr)))
        return

    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            main()
            arr.pop()
            
main()