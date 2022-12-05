def fibonacci(n):
    result = [0,1]
    for i in range(1, n-1):
        result.append(result[i]+result[i-1])
    return result
def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
def calc(num1,num2,operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        print("Неизвестная операция")
        return 0
