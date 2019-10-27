#code
numcases = int(input());

for i in range(0, numcases):
    arrLen = int(input());
    arr = [int(ch) for ch in input().strip().split(" ")];
    arr.sort();
    
    tripletCount = 0;
    
    for n in range(arrLen-1, 0, -1):
        start = 0;
        end = n-1;
        while(start < end):
            if((arr[start] + arr[end]) < arr[n]):
                start += 1;
            elif((arr[start] + arr[end]) == arr[n]):
                tripletCount += 1;
                start += 1;
                end -= 1;
            else:
                end -= 1;
    
    if(tripletCount):
        print(tripletCount);
    else:
        print(-1);