t = int(input())
for _ in range(t):
    keyboard = input().strip()
    word = input().strip()
    char2Index = {char: idx for idx, char in enumerate(keyboard)}
    time = 0
    for i in range(1, len(word)):
        time += abs(char2Index[word[i]] - char2Index[word[i-1]])   
    print(time)
