if __name__ == '__main__':
    N = int(input())
    l1 = []
    for i in range(N):
        command = input().split()
        if command[0] == 'insert':
            l1.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(l1)
        elif command[0] == 'remove':
            l1.remove(int(command[1]))
        elif command[0] == 'append':
            l1.append(int(command[1]))
        elif command[0] == 'sort':
            l1.sort()
        elif command[0] == 'pop':
            l1.pop()
        elif command[0] == 'reverse':
            l1.reverse()
