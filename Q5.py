arr = []

print("Enter your array then enter the symbol \".\" to end:")
while(True):
    temp = input()
    if(temp == '.'):
        break
    else:
        arr.append(int(temp))

for i in range(len(arr) // 2):
    if(arr[i] == arr[len(arr) - 1 - i]):
        continue
    else:
        print("This array is NOT symmetric!")
        exit()
print("This array is symmetric.")