if __name__ == "__main__":
    # arr = []

    # for i in range(6):
    #     arr.append(list(map(int, input().split())))
    arr = [
        [1, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    
    subSum = sum(arr[0][0:3]) + arr[1][1] + sum(arr[1][0:3])
    for i in range(4):
        for j in range(4):
            currentSum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            if currentSum > subSum:
                subSum = currentSum
    
    print(subSum)


# Sample:

# 7