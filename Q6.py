arr = []


def cal_KhayyamPascal(n):
    for row in range(n):
        arr.append([])
        arr[row].append(1)
        for column in range(1, row):
            arr[row].append(arr[row - 1][column - 1] + arr[row - 1][column])
        if(n != 0):
            arr[row].append(1)


def show_KhayyamPascal(n):
   for row in range(n):
        for column in range(row + 1):
            print(arr[row][column], end = " ")
        print("\n", end = "")


n = int(input("n = "))
cal_KhayyamPascal(n)
show_KhayyamPascal(n)
