
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr1 = list(arr)
    arr1.sort()
    x = len(arr1)
    runner_up = 0
    for i in range(x):
        if(arr1[x-i-1]==arr1[x-1]):
            continue
        else:
            runner_up = arr1[x-i-1]
            break
    
    print(runner_up)
