if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    SortedUniqueScore = sorted(set(arr))
    RunnerUp = SortedUniqueScore[-2]
    print(RunnerUp)

