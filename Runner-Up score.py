if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    lista = sorted(set(arr))
    print(lista[-2])