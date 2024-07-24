if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    SortedUniqueScore = sorted(set(arr), reverse=True)
    RunnerUp = SortedUniqueScore[1]
    print(RunnerUp)

