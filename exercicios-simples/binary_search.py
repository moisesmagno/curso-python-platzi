import random

def binary_search(data, target, low, high):
    if low > high:
        return False

    mid = (low + high) // 2

    if target == data[mid]:
        return True
    elif (target < data[mid]):
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    data = [random.randint(0,100) for i in range(10)]

    data.sort()

    print(data)

    target = int(input('Digite o número a ser buscado: '))

    found = binary_search(data, target, 0, len(data)-1)

    if(found == True):
        print('O número {} se encontra no random'.format(target))
    else:
        print('O número {} não se encontra no random'.format(target))