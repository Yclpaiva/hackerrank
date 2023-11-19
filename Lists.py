if __name__ == '__main__':
    arr = []
    N = int(input())
    i = 0
    try:
        while i <= N:
            command = input().strip().split()
            if command[0] == 'insert':
                position = int(command[1])
                value = int(command[2])
                arr.insert(position, value)
                i+=1
            elif command[0] == 'print':
                print(arr)
                i+=1
            elif command[0] == 'remove':
                value = int(command[1])
                arr.remove(value)
                i+=1
            elif command[0] == 'append':
                value = int(command[1])
                arr.append(value)
                i+=1
            elif command[0] == 'sort':
                arr.sort()
                i+=1
            elif command[0] == 'pop':
                arr.pop()
                i+=1
            elif command[0] == 'reverse':
                arr.reverse()
                i+=1
    except EOFError:
        pass  # Chegou ao final do arquivo

